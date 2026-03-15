#!/usr/bin/env python3
"""
report_commits.py

Loads raw and derived data files into indexed in-memory dicts and prints
a per-project commit summary table broken down by author and committer,
resolving git identities to OrgChart names via people.csv aliases.

Usage:
    python3 report_commits.py
"""

import csv
import os
import sys
from collections import defaultdict

SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR  = os.path.dirname(SCRIPT_DIR)          # dev-activity/
DATA_DIR     = os.path.join(PROJECT_DIR, "data")
REPORTS_DIR  = os.path.join(PROJECT_DIR, "reports")
REPOS_DIR    = os.path.dirname(os.path.dirname(SCRIPT_DIR))  # IdeaProjects/
PROJECTS = ["xp2", "nucleus", "pano", "xp1"]


# ── Data Loading ───────────────────────────────────────────────────────────────

def load_orgchart():
    """Return {org_name: {title, level, manager}} from OrgChart.csv."""
    path = os.path.join(DATA_DIR, "OrgChart.csv")
    people = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            name = row.get("Name", "").strip()
            if name:
                people[name] = {
                    "title":   row.get("Title", "").strip(),
                    "level":   row.get("Level", "").strip(),
                    "manager": row.get("Manager", "").strip(),
                }
    return people


BOT_AUTHORS = {"svc-azure_devops"}

# Commit whose message starts with this prefix is an Azure DevOps squash-merge (one commit = one PR).
_SQUASH_PREFIX = "Merged PR "


def commit_type(row):
    """Return 'squash-pr' or 'direct' based on commit message."""
    return "squash-pr" if row.get("message", "").startswith(_SQUASH_PREFIX) else "direct"


def load_commits(project):
    """Return list of row-dicts from {project}-commits.csv, excluding bot authors."""
    path = os.path.join(DATA_DIR, f"{project}-commits.csv")
    if not os.path.exists(path):
        print(f"ERROR: {project}-commits.csv not found.", file=sys.stderr)
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if r.get("author", "") not in BOT_AUTHORS]


def load_all_commits():
    """Return {project: [row, ...]} for all projects."""
    return {p: load_commits(p) for p in PROJECTS}


def build_alias_lookup(all_identities):
    """
    Parse people.csv and build {git_identity: (org_name, manager, team)}.

    The aliases field in people.csv is a space-joined string of git identity
    strings (which may themselves contain spaces, e.g. "Evan Yu").  We resolve
    ambiguity by testing each *known* git identity as a contiguous substring
    bounded by spaces or string edges.
    """
    path = os.path.join(DATA_DIR, "people.csv")
    alias_to_person = {}

    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    for row in rows:
        name    = row.get("name", "").strip()
        manager = row.get("manager", "").strip()
        team    = row.get("team", "").strip()
        aliases_str = row.get("aliases", "").strip()
        if not aliases_str:
            continue
        padded = f" {aliases_str} "
        for identity in all_identities:
            if f" {identity} " in padded:
                alias_to_person[identity] = (name if name else identity, manager, team)

    # Identities with no people.csv entry keep their raw git string.
    for identity in all_identities:
        alias_to_person.setdefault(identity, (identity, "", ""))

    return alias_to_person


def load_data():
    """
    Load all source files and return an indexed data dict:
      data["orgchart"]        -> {org_name: {title, level, manager}}
      data["commits"]         -> {project: [commit_row, ...]}
      data["alias_to_person"] -> {git_identity: (display_name, manager)}
    """
    orgchart = load_orgchart()
    commits  = load_all_commits()

    all_identities = set()
    for rows in commits.values():
        for row in rows:
            if row.get("author"):
                all_identities.add(row["author"])
            if row.get("committer"):
                all_identities.add(row["committer"])

    alias_to_person = build_alias_lookup(all_identities)

    return {
        "orgchart":        orgchart,
        "commits":         commits,
        "alias_to_person": alias_to_person,
    }


# ── Report: commits by author/committer ───────────────────────────────────────

def resolve(identity, alias_to_person):
    """Resolve a git identity to (display_name, manager, team)."""
    return alias_to_person.get(identity, (identity, "", ""))


def _int(val):
    try:
        return int(val or 0)
    except (ValueError, TypeError):
        return 0


def build_project_table(project, rows, alias_to_person):
    """
    Aggregate commits by (resolved_author, resolved_committer).
    Returns (headers, data_rows, totals_row).
    """
    Agg = lambda: {"commits": 0, "files": 0, "added": 0, "removed": 0, "manager": ""}
    stats = defaultdict(Agg)

    for row in rows:
        author_name, author_mgr, _  = resolve(row.get("author",    ""), alias_to_person)
        committer_name, _, _        = resolve(row.get("committer", ""), alias_to_person)
        key = (author_name, committer_name)
        s = stats[key]
        s["commits"]  += 1
        s["files"]    += _int(row.get("file-count"))
        s["added"]    += _int(row.get("added-lines"))
        s["removed"]  += _int(row.get("removed-lines"))
        s["manager"]   = author_mgr

    # Sort: descending commit count, then author name, then committer name
    keys = sorted(stats, key=lambda k: (-stats[k]["commits"], k[0], k[1]))

    headers = ["Author", "Manager", "Commits", "Files Changed",
               "Lines Added", "Lines Removed"]

    data_rows = []
    for author, committer in keys:
        s = stats[(author, committer)]
        data_rows.append([
            author,
            s["manager"],
            s["commits"],
            s["files"],
            s["added"],
            s["removed"],
        ])

    totals = [
        "TOTAL", "", "",
        sum(s["commits"]  for s in stats.values()),
        sum(s["files"]    for s in stats.values()),
        sum(s["added"]    for s in stats.values()),
        sum(s["removed"]  for s in stats.values()),
    ]

    return headers, data_rows, totals


# ── Formatting ────────────────────────────────────────────────────────────────

NUMERIC_COLS = {3, 4, 5, 6}   # column indices that should be right-aligned


def print_table(headers, data_rows, totals, title, file=sys.stdout):
    all_rows = data_rows + [totals]

    # Column widths
    widths = [len(h) for h in headers]
    for row in all_rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(f"{cell:,}" if isinstance(cell, int) else str(cell)))

    SEP = "  "

    def fmt(val, col):
        text = f"{val:,}" if isinstance(val, int) else str(val)
        return text.rjust(widths[col]) if col in NUMERIC_COLS else text.ljust(widths[col])

    header_line  = SEP.join(
        h.rjust(widths[i]) if i in NUMERIC_COLS else h.ljust(widths[i])
        for i, h in enumerate(headers)
    )
    divider = SEP.join("─" * w for w in widths)
    thick   = SEP.join("═" * w for w in widths)

    p = lambda *args, **kwargs: print(*args, file=file, **kwargs)

    p(f"\n{thick}")
    p(f"  Project: {title.upper()}")
    p(thick)
    p(header_line)
    p(divider)
    for row in data_rows:
        p(SEP.join(fmt(cell, i) for i, cell in enumerate(row)))
    p(divider)
    p(SEP.join(fmt(cell, i) for i, cell in enumerate(totals)))
    p(thick)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    data = load_data()

    for project in PROJECTS:
        rows = data["commits"][project]
        headers, data_rows, totals = build_project_table(
            project, rows, data["alias_to_person"]
        )
        print_table(headers, data_rows, totals, project)

    print()


if __name__ == "__main__":
    main()
