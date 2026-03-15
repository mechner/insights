#!/usr/bin/env python3
"""
report_activity.py

Generates dev-activity.md:
  - per-project summary table
  - per-team summary table
  - per-team-member detail tables

Usage:
    python3 report_activity.py
"""

import csv
import datetime
import os
from collections import defaultdict
from report_commits import load_data, PROJECTS

SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR  = os.path.dirname(SCRIPT_DIR)          # dev-activity/
DATA_DIR     = os.path.join(PROJECT_DIR, "data")
REPORTS_DIR  = os.path.join(PROJECT_DIR, "reports")
REPOS_DIR    = os.path.dirname(os.path.dirname(SCRIPT_DIR))  # IdeaProjects/
OUT_FILE     = os.path.join(REPORTS_DIR, "dev-activity.md")

# Working days in the analysis date range (Mon–Fri, no holiday exclusions)
_D0 = datetime.date(2026, 1, 1)
_D1 = datetime.date(2026, 2, 28)
WORKING_DAYS = sum(
    1 for n in range((_D1 - _D0).days + 1)
    if (_D0 + datetime.timedelta(n)).weekday() < 5
)

TEAM_LABELS = {
    "xp-us":       "xp-us (Rivera, Enmanuel)",
    "xp-eu":       "xp-eu (Jaen, Rodrigo)",
    "xp-match":    "xp-match (Desai, Keshal)",
    "xp-pt":       "xp-pt (Bobbala, Ramakrishna)",
    "xp-platform": "xp-platform (Richard, Michel)",
    "nucleus":     "nucleus (Fishler, Eran)",
    "pano":        "pano (Hakim, Jawaid)",
}


# ── Data helpers ──────────────────────────────────────────────────────────────

def load_prs(project):
    """Return list of row-dicts from prs-{project}.csv (may be empty)."""
    path = os.path.join(DATA_DIR, f"prs-{project}.csv")
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _int(val):
    try:
        return int(val or 0)
    except (ValueError, TypeError):
        return 0


def _float(val):
    try:
        return float(val or 0)
    except (ValueError, TypeError):
        return 0.0


def primary_area(rows):
    """Return the file extension with the most changed lines across rows."""
    ext_lines = defaultdict(int)
    for r in rows:
        ft = r.get("file-types", "") or ""
        added   = _int(r.get("added-lines",   r.get("+lines", 0)))
        removed = _int(r.get("removed-lines", r.get("-lines", 0)))
        loc     = added + removed
        exts    = ft.split()
        if exts and loc > 0:
            # distribute evenly across listed types (already filtered to >=10%)
            per = loc / len(exts)
            for e in exts:
                ext_lines[e] += per
    if not ext_lines:
        return "—"
    return max(ext_lines, key=ext_lines.__getitem__)


# ── Per-project / per-team aggregation ────────────────────────────────────────

def summarise(commit_rows, pr_rows, alias_to_person):
    """
    Return a dict of summary stats for a set of commit rows and pr rows.
    Both sets have already been filtered to the relevant project/team/person.
    """
    authors  = set()
    added    = 0
    removed  = 0
    pct_sum  = 0.0
    n        = len(commit_rows)

    for r in commit_rows:
        name, _, _ = alias_to_person.get(r.get("author", ""), (r.get("author", ""), "", ""))
        authors.add(name)
        added   += _int(r.get("added-lines", 0))
        removed += _int(r.get("removed-lines", 0))
        pct_sum += _float(r.get("%test", 0))

    na       = len(authors)
    area     = primary_area(commit_rows)
    pct_test = round(pct_sum / n) if n > 0 else 0

    # PR stats
    total_pr_lines = sum(_int(r.get("+lines", 0)) + _int(r.get("-lines", 0)) for r in pr_rows)
    np = len(pr_rows)

    return {
        "commits":      n,
        "authors":      na,
        "added":        added,
        "removed":      removed,
        "added_author": round(added   / na) if na else 0,
        "removed_author": round(removed / na) if na else 0,
        "area":         area,
        "pct_test":     pct_test,
        "prs":          np,
        "prs_author":   f"{np/na:.1f}" if na and np else "—",
        "lines_pr":     str(round(total_pr_lines / np)) if np else "—",
    }


def fmt(val):
    if isinstance(val, int):
        return f"{val:,}"
    return str(val)


# ── Team grouping ─────────────────────────────────────────────────────────────

def group_by_team(commit_rows, pr_rows_all, alias_to_person):
    """
    Returns {team_label: (commit_rows, pr_rows)} for each team.
    pr_rows_all is a flat list of all PR rows across all projects.
    PRs are matched to a team by resolving the PR author.
    """
    team_commits = defaultdict(list)
    team_prs     = defaultdict(list)

    for r in commit_rows:
        _, _, team = alias_to_person.get(r.get("author", ""), (r.get("author", ""), "", ""))
        label = TEAM_LABELS.get(team)
        if label:
            team_commits[label].append(r)

    for r in pr_rows_all:
        _, _, team = alias_to_person.get(r.get("author", ""), (r.get("author", ""), "", ""))
        label = TEAM_LABELS.get(team)
        if label:
            team_prs[label].append(r)

    return team_commits, team_prs


def group_by_author(commit_rows, pr_rows, alias_to_person):
    """
    Returns {display_name: (commit_rows, pr_rows)}.
    """
    author_commits = defaultdict(list)
    author_prs     = defaultdict(list)

    for r in commit_rows:
        name, _, _ = alias_to_person.get(r.get("author", ""), (r.get("author", ""), "", ""))
        author_commits[name].append(r)

    for r in pr_rows:
        name, _, _ = alias_to_person.get(r.get("author", ""), (r.get("author", ""), "", ""))
        author_prs[name].append(r)

    return author_commits, author_prs


# ── Markdown table builders ───────────────────────────────────────────────────

def md_table(headers, data_rows, total_row=None, right_cols=None):
    """
    Build a markdown table. right_cols: set of column indices to right-align.
    Returns list of lines.
    """
    if right_cols is None:
        right_cols = set(range(1, len(headers)))  # right-align everything except col 0

    all_rows = data_rows + ([total_row] if total_row else [])
    widths   = [len(h) for h in headers]
    for row in all_rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))

    def fmt_cell(val, i):
        s = str(val)
        return s.rjust(widths[i]) if i in right_cols else s.ljust(widths[i])

    def md_row(cells):
        return "| " + " | ".join(fmt_cell(c, i) for i, c in enumerate(cells)) + " |"

    sep = "| " + " | ".join(
        ("-" * (widths[i] - 1) + ":") if i in right_cols else ("-" * widths[i])
        for i in range(len(headers))
    ) + " |"

    lines = [md_row(headers), sep]
    for row in data_rows:
        lines.append(md_row(row))
    if total_row:
        lines.append(sep)
        lines.append(md_row(total_row))
    return lines


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    data            = load_data()
    alias_to_person = data["alias_to_person"]

    all_prs_by_project = {p: load_prs(p) for p in PROJECTS}
    all_prs_flat       = [r for rows in all_prs_by_project.values() for r in rows]
    all_commits_flat   = [r for p in PROJECTS for r in data["commits"][p]]

    lines = [
        "# Developer Activity Summary",
        "",
        "Date range: 2026-01-01 to 2026-02-28",
        f"_(%Test = mean across commits. "
        f"Lines/Day denominator = {WORKING_DAYS} working days. "
        f"PRs/Author and Lines/PR from prs-*.csv; nucleus has no git PR markers.)_",
        "",
        "## Activity by Project",
        "",
    ]

    # ── Project table ─────────────────────────────────────────────────────────
    proj_headers = [
        "Project", "Commits", "Authors",
        "+Lines/Author", "-Lines/Author", "Area",
        "%Test", "PRs/Author", "Lines/PR",
    ]
    proj_rows = []
    totals_added = totals_removed = totals_prs = 0
    totals_authors = set()

    for project in PROJECTS:
        c_rows = data["commits"][project]
        p_rows = all_prs_by_project[project]
        s      = summarise(c_rows, p_rows, alias_to_person)
        proj_rows.append([
            project.upper(),
            fmt(s["commits"]),
            fmt(s["authors"]),
            fmt(s["added_author"]),
            fmt(s["removed_author"]),
            s["area"],
            f"{s['pct_test']}%",
            s["prs_author"],
            s["lines_pr"],
        ])
        totals_added   += s["added"]
        totals_removed += s["removed"]
        totals_prs     += s["prs"]
        for r in c_rows:
            name, _, _ = alias_to_person.get(r.get("author", ""), (r.get("author", ""), "", ""))
            totals_authors.add(name)

    na_total = len(totals_authors)
    total_pct = round(
        sum(_float(r.get("%test", 0)) for p in PROJECTS for r in data["commits"][p])
        / sum(len(data["commits"][p]) for p in PROJECTS)
    ) if all_commits_flat else 0
    total_pr_lines = sum(_int(r.get("+lines", 0)) + _int(r.get("-lines", 0)) for r in all_prs_flat)

    proj_total = [
        "**TOTAL**",
        fmt(len(all_commits_flat)),
        fmt(na_total),
        fmt(round(totals_added   / na_total)) if na_total else "—",
        fmt(round(totals_removed / na_total)) if na_total else "—",
        primary_area(all_commits_flat),
        f"{total_pct}%",
        f"{totals_prs/na_total:.1f}" if na_total and totals_prs else "—",
        str(round(total_pr_lines / totals_prs)) if totals_prs else "—",
    ]

    lines += md_table(proj_headers, proj_rows, proj_total)

    # ── Team table ─────────────────────────────────────────────────────────────
    lines += ["", "## Activity by Team", ""]

    team_commit_map, team_pr_map = group_by_team(all_commits_flat, all_prs_flat, alias_to_person)

    team_headers = [
        "Team (Manager)", "Commits", "Authors",
        "+Lines/Author", "-Lines/Author", "Area",
        "%Test", "PRs/Author", "Lines/PR",
    ]
    team_rows = []
    team_data = []
    for label in TEAM_LABELS.values():
        c = team_commit_map.get(label, [])
        p = team_pr_map.get(label, [])
        if not c:
            continue
        s = summarise(c, p, alias_to_person)
        team_data.append((label, s, c, p))
        team_rows.append([
            label,
            fmt(s["commits"]),
            fmt(s["authors"]),
            fmt(s["added_author"]),
            fmt(s["removed_author"]),
            s["area"],
            f"{s['pct_test']}%",
            s["prs_author"],
            s["lines_pr"],
        ])

    team_rows.sort(key=lambda r: -int(r[1].replace(",", "")))

    all_team_commits = [r for c, _ in [(td[2], td[3]) for td in team_data] for r in c]
    all_team_prs     = [r for _, p in [(td[2], td[3]) for td in team_data] for r in p]
    s_all = summarise(all_commits_flat, all_prs_flat, alias_to_person)
    team_total = [
        "**TOTAL**",
        fmt(s_all["commits"]),
        fmt(s_all["authors"]),
        fmt(s_all["added_author"]),
        fmt(s_all["removed_author"]),
        primary_area(all_commits_flat),
        f"{s_all['pct_test']}%",
        s_all["prs_author"],
        s_all["lines_pr"],
    ]

    lines += md_table(team_headers, team_rows, team_total)

    # ── Per-team member tables ─────────────────────────────────────────────────
    lines += ["", "## Activity by Team Member", "",
              f"_(%Test = mean across commits. "
              f"+Lines/Day = added-lines ÷ {WORKING_DAYS} working days.)_"]

    member_headers = [
        "Author", "+Lines", "-Lines", "Area",
        "+Lines/Day", "%Test", "PRs", "Lines/PR",
    ]

    for label in TEAM_LABELS.values():
        c_rows = team_commit_map.get(label, [])
        p_rows = team_pr_map.get(label, [])
        if not c_rows:
            continue

        author_commits, author_prs = group_by_author(c_rows, p_rows, alias_to_person)

        member_rows = []
        for author, a_commits in author_commits.items():
            a_prs = author_prs.get(author, [])
            added   = sum(_int(r.get("added-lines", 0))   for r in a_commits)
            removed = sum(_int(r.get("removed-lines", 0)) for r in a_commits)
            n       = len(a_commits)
            pct     = round(sum(_float(r.get("%test", 0)) for r in a_commits) / n) if n else 0
            area    = primary_area(a_commits)
            np      = len(a_prs)
            pr_lines = sum(_int(r.get("+lines", 0)) + _int(r.get("-lines", 0)) for r in a_prs)
            lines_pr = str(round(pr_lines / np)) if np else "—"

            member_rows.append([
                author,
                fmt(added),
                fmt(removed),
                area,
                f"{added / WORKING_DAYS:.1f}",
                f"{pct}%",
                str(np) if np else "—",
                lines_pr,
            ])

        # sort by +lines descending
        member_rows.sort(key=lambda r: -int(r[1].replace(",", "")))

        lines += ["", f"### {label}", ""]
        lines += md_table(member_headers, member_rows, right_cols={1, 2, 4, 5, 6, 7})

    lines.append("")

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Written: {OUT_FILE}")


if __name__ == "__main__":
    main()
