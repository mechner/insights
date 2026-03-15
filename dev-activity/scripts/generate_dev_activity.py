#!/usr/bin/env python3
"""Generates dev-activity.md: activity tables + Jira analysis."""

import csv, json, os, re, math, datetime, statistics
from collections import defaultdict

SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR  = os.path.dirname(SCRIPT_DIR)          # dev-activity/
DATA_DIR     = os.path.join(PROJECT_DIR, "data")
REPORTS_DIR  = os.path.join(PROJECT_DIR, "reports")
REPOS_DIR    = os.path.dirname(os.path.dirname(SCRIPT_DIR))  # IdeaProjects/
OUT_FILE     = os.path.join(REPORTS_DIR, "dev-activity.md")

DATE_START   = datetime.date(2026, 1, 1)
DATE_END     = datetime.date(2026, 2, 28)
WORKING_DAYS = sum(1 for n in range((DATE_END - DATE_START).days + 1)
                   if (DATE_START + datetime.timedelta(n)).weekday() < 5)

PROJECTS      = ["xp2", "nucleus", "pano", "xp1"]
JIRA_PROJECTS = ["CODE", "NUMA", "PAN", "XPMI", "XRFQ", "MAUI"]
BOT_AUTHORS   = {"svc-azure_devops"}

TEAM_MANAGER = {
    "xp-us":       "Rivera, Enmanuel",
    "xp-eu":       "Jaen, Rodrigo",
    "xp-match":    "Desai, Keshal",
    "xp-pt":       "Bobbala, Ramakrishna",
    "xp-platform": "Richard, Michel",
    "nucleus":     "Fishler, Eran",
    "pano":        "Hakim, Jawaid",
}
TEAM_ORDER  = ["xp-us","xp-eu","xp-match","xp-pt","xp-platform","nucleus","pano"]
TEAM_LABELS = {t: f"{t} ({m})" for t, m in TEAM_MANAGER.items()}

# ── Loaders ───────────────────────────────────────────────────────────────────

def _int(v):
    try: return int(v or 0)
    except: return 0

def _float(v):
    try: return float(v or 0)
    except: return 0.0

def load_orgchart():
    path = os.path.join(DATA_DIR, "OrgChart.csv")
    oc = {}
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            n = r.get("Name","").strip()
            if n:
                raw_title = r.get("Title","").strip()
                # Abbreviate: take part before comma, remove suffix like ", Pragma", ", XP", etc.
                short = raw_title.split(",")[0].strip()
                oc[n] = {"title": short or "—", "full_title": raw_title, "manager": r.get("Manager","").strip()}
    return oc

def load_people():
    """Returns (alias_to_person, unmatched_aliases).
    alias_to_person: {alias_str: (canonical_name, manager, team)}
    """
    path = os.path.join(DATA_DIR, "people.csv")
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    # Collect all aliases first
    all_aliases = []
    for row in rows:
        als = row.get("aliases","").strip()
        if als:
            all_aliases.append((row, als))

    # For each alias string in a row, we need to find which substrings are valid identities
    # Strategy: build set of known git identities from commits first, then match
    # We'll do this in two passes
    alias_to_person = {}
    unmatched = []

    # Build set of all git identities from commits files
    all_git_ids = set()
    for proj in PROJECTS:
        path2 = os.path.join(DATA_DIR, f"{proj}-commits.csv")
        if not os.path.exists(path2): continue
        with open(path2, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                a = r.get("author","").strip()
                if a and a not in BOT_AUTHORS:
                    all_git_ids.add(a)
    # Also from PR files
    for proj in PROJECTS:
        path2 = os.path.join(DATA_DIR, f"prs-{proj}.csv")
        if not os.path.exists(path2): continue
        with open(path2, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                a = r.get("author","").strip()
                if a and a not in BOT_AUTHORS:
                    all_git_ids.add(a)

    for row, als_str in all_aliases:
        name    = row.get("name","").strip()
        manager = row.get("manager","").strip()
        team    = row.get("team","").strip()
        padded  = f" {als_str} "
        for identity in all_git_ids:
            if f" {identity} " in padded:
                alias_to_person[identity] = (name if name else identity, manager, team)
        if not name:
            # collect unmatched identities from this row
            for identity in all_git_ids:
                if f" {identity} " in padded:
                    unmatched.append(identity)

    # Any git identity not in people.csv → unresolved
    for identity in all_git_ids:
        if identity not in alias_to_person:
            alias_to_person[identity] = (identity, "", "")
            unmatched.append(identity)

    return alias_to_person, sorted(set(unmatched))

def load_commits(project):
    path = os.path.join(DATA_DIR, f"{project}-commits.csv")
    if not os.path.exists(path): return []
    with open(path, newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if r.get("author","") not in BOT_AUTHORS]

def load_prs(project):
    path = os.path.join(DATA_DIR, f"prs-{project}.csv")
    if not os.path.exists(path): return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def load_jira(project):
    path = os.path.join(DATA_DIR, f"jira-{project}.json")
    if not os.path.exists(path): return []
    with open(path) as f:
        return json.load(f)

# ── Helpers ───────────────────────────────────────────────────────────────────

def primary_area(rows, lines_key_add="added-lines", lines_key_rem="removed-lines"):
    ext_lines = defaultdict(float)
    for r in rows:
        ft   = (r.get("file-types","") or "").split()
        add  = _int(r.get(lines_key_add, r.get("+lines", 0)))
        rem  = _int(r.get(lines_key_rem, r.get("-lines", 0)))
        loc  = add + rem
        if ft and loc > 0:
            per = loc / len(ft)
            for e in ft:
                ext_lines[e] += per
    return max(ext_lines, key=ext_lines.__getitem__) if ext_lines else "—"

def fmt_num(v):
    if isinstance(v, int):    return f"{v:,}"
    if isinstance(v, float):  return f"{v:,.1f}"
    return str(v)

def pearson(xs, ys):
    n = len(xs)
    if n < 3: return None
    mx, my = statistics.mean(xs), statistics.mean(ys)
    num    = sum((x-mx)*(y-my) for x,y in zip(xs,ys))
    denom  = math.sqrt(sum((x-mx)**2 for x in xs) * sum((y-my)**2 for y in ys))
    return num/denom if denom else None

# ── Markdown helpers ──────────────────────────────────────────────────────────

def md_table(headers, data_rows, total_row=None, right_cols=None):
    if right_cols is None:
        right_cols = set(range(1, len(headers)))
    all_rows = list(data_rows) + ([total_row] if total_row else [])
    widths   = [len(str(h)) for h in headers]
    for row in all_rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))

    def fc(val, i):
        s = str(val)
        return s.rjust(widths[i]) if i in right_cols else s.ljust(widths[i])

    sep = "| " + " | ".join(
        ("-"*(widths[i]-1)+":") if i in right_cols else "-"*widths[i]
        for i in range(len(headers))
    ) + " |"
    def mrow(cells): return "| " + " | ".join(fc(c,i) for i,c in enumerate(cells)) + " |"

    lines = [mrow(headers), sep]
    for row in data_rows:
        lines.append(mrow(row))
    if total_row:
        lines.append(sep)
        lines.append(mrow(total_row))
    return lines

# ── Activity section ──────────────────────────────────────────────────────────

def summarise(commit_rows, pr_rows, alias_to_person):
    authors = set()
    added = removed = 0
    pct_sum = 0.0
    n = len(commit_rows)
    for r in commit_rows:
        name = alias_to_person.get(r.get("author",""), (r.get("author",""),"",""))[0]
        authors.add(name)
        added   += _int(r.get("added-lines",0))
        removed += _int(r.get("removed-lines",0))
        pct_sum += _float(r.get("%test",0))
    na = len(authors)
    pct_test = round(pct_sum / n) if n > 0 else 0
    np = len(pr_rows)
    pr_lines = sum(_int(r.get("+lines",0)) + _int(r.get("-lines",0)) for r in pr_rows)
    return {
        "commits": n, "authors": na,
        "added": added, "removed": removed,
        "added_author":   round(added   / na) if na else 0,
        "removed_author": round(removed / na) if na else 0,
        "area":     primary_area(commit_rows),
        "pct_test": pct_test,
        "prs": np,
        "prs_author": f"{np/na:.1f}" if na and np else "—",
        "lines_pr":   str(round(pr_lines / np)) if np else "—",
    }

def group_by_team(commit_rows, pr_rows, alias_to_person):
    tc, tp = defaultdict(list), defaultdict(list)
    for r in commit_rows:
        _, _, team = alias_to_person.get(r.get("author",""), ("","",""))
        if team in TEAM_LABELS:
            tc[TEAM_LABELS[team]].append(r)
    for r in pr_rows:
        _, _, team = alias_to_person.get(r.get("author",""), ("","",""))
        if team in TEAM_LABELS:
            tp[TEAM_LABELS[team]].append(r)
    return tc, tp

def group_by_author(commit_rows, pr_rows, alias_to_person):
    ac, ap = defaultdict(list), defaultdict(list)
    for r in commit_rows:
        name = alias_to_person.get(r.get("author",""), (r.get("author",""),"",""))[0]
        ac[name].append(r)
    for r in pr_rows:
        name = alias_to_person.get(r.get("author",""), (r.get("author",""),"",""))[0]
        ap[name].append(r)
    return ac, ap

def build_activity_section(alias_to_person, unmatched, orgchart):
    all_commits = {p: load_commits(p) for p in PROJECTS}
    all_prs     = {p: load_prs(p)     for p in PROJECTS}
    commits_flat = [r for rows in all_commits.values() for r in rows]
    prs_flat     = [r for rows in all_prs.values()     for r in rows]

    lines = [
        "# Developer Activity Summary",
        "",
        f"Date range: {DATE_START} to {DATE_END}",
        f"_(%Test = mean across commits. Lines/Day denominator = {WORKING_DAYS} working days. "
        "PRs/Author and Lines/PR from prs-*.csv; nucleus has no git PR markers.)_",
        "",
        "## Activity by Project",
        "",
    ]

    # Project table
    ph = ["Project","Commits","Authors","+Lines/Author","-Lines/Author","Area","%Test","PRs/Author","Lines/PR"]
    proj_rows = []
    for proj in PROJECTS:
        s = summarise(all_commits[proj], all_prs[proj], alias_to_person)
        proj_rows.append([proj.upper(), fmt_num(s["commits"]), fmt_num(s["authors"]),
                          fmt_num(s["added_author"]), fmt_num(s["removed_author"]),
                          s["area"], f"{s['pct_test']}%", s["prs_author"], s["lines_pr"]])
    s_all = summarise(commits_flat, prs_flat, alias_to_person)
    proj_total = ["**TOTAL**", fmt_num(s_all["commits"]), fmt_num(s_all["authors"]),
                  fmt_num(s_all["added_author"]), fmt_num(s_all["removed_author"]),
                  primary_area(commits_flat), f"{s_all['pct_test']}%", s_all["prs_author"], s_all["lines_pr"]]
    lines += md_table(ph, proj_rows, proj_total)

    # Team table
    lines += ["", "## Activity by Team", ""]
    tc, tp = group_by_team(commits_flat, prs_flat, alias_to_person)
    th = ["Team (Manager)","Commits","Authors","+Lines/Author","-Lines/Author","Area","%Test","PRs/Author","Lines/PR"]
    team_rows = []
    for team in TEAM_ORDER:
        label = TEAM_LABELS[team]
        if label not in tc: continue
        s = summarise(tc[label], tp.get(label,[]), alias_to_person)
        team_rows.append([label, fmt_num(s["commits"]), fmt_num(s["authors"]),
                          fmt_num(s["added_author"]), fmt_num(s["removed_author"]),
                          s["area"], f"{s['pct_test']}%", s["prs_author"], s["lines_pr"]])
    team_rows.sort(key=lambda r: -int(r[1].replace(",","")))
    lines += md_table(th, team_rows, proj_total)  # reuse same totals row

    # Per-team member tables
    lines += ["", "## Activity by Team Member", "",
              f"_(%Test = mean across commits. +Lines/Day = added-lines ÷ {WORKING_DAYS} working days.)_"]
    mh = ["Author","Title","+Lines","-Lines","Area","+Lines/Day","%Test","PRs","Lines/PR"]

    for team in TEAM_ORDER:
        label   = TEAM_LABELS[team]
        c_rows  = tc.get(label, [])
        p_rows  = tp.get(label, [])
        if not c_rows: continue

        manager = TEAM_MANAGER[team]
        ac, ap  = group_by_author(c_rows, p_rows, alias_to_person)

        member_rows = []
        for author, a_commits in ac.items():
            a_prs   = ap.get(author, [])
            added   = sum(_int(r.get("added-lines",0))   for r in a_commits)
            removed = sum(_int(r.get("removed-lines",0)) for r in a_commits)
            n       = len(a_commits)
            pct     = round(sum(_float(r.get("%test",0)) for r in a_commits) / n) if n else 0
            area    = primary_area(a_commits)
            np      = len(a_prs)
            pr_lines= sum(_int(r.get("+lines",0))+_int(r.get("-lines",0)) for r in a_prs)
            lines_pr= str(round(pr_lines/np)) if np else "—"
            title   = orgchart.get(author, {}).get("title", "—")

            display = f"**{author}**" if author == manager else author
            member_rows.append([display, title, fmt_num(added), fmt_num(removed),
                                 area, f"{added/WORKING_DAYS:.1f}", f"{pct}%",
                                 str(np) if np else "—", lines_pr,
                                 added])  # sort key

        member_rows.sort(key=lambda r: -r[-1])
        member_rows = [r[:-1] for r in member_rows]  # strip sort key

        lines += ["", f"### {label}", ""]
        lines += md_table(mh, member_rows, right_cols={2,3,5,6,7,8})

    # Unmatched Authors
    unmatched_commits = defaultdict(list)
    unmatched_prs     = defaultdict(list)
    for r in commits_flat:
        a = r.get("author","")
        if a in unmatched:
            unmatched_commits[a].append(r)
    for r in prs_flat:
        a = r.get("author","")
        if a in unmatched:
            unmatched_prs[a].append(r)

    if unmatched_commits:
        lines += ["", "### Unmatched Authors", "",
                  "_Authors not found in OrgChart.csv. Provide aliases to merge these into team tables._", ""]
        um_rows = []
        for author, a_commits in unmatched_commits.items():
            a_prs   = unmatched_prs.get(author,[])
            added   = sum(_int(r.get("added-lines",0))   for r in a_commits)
            removed = sum(_int(r.get("removed-lines",0)) for r in a_commits)
            n       = len(a_commits)
            pct     = round(sum(_float(r.get("%test",0)) for r in a_commits)/n) if n else 0
            np      = len(a_prs)
            pr_lines= sum(_int(r.get("+lines",0))+_int(r.get("-lines",0)) for r in a_prs)
            um_rows.append([author, "—", fmt_num(added), fmt_num(removed),
                            primary_area(a_commits), f"{added/WORKING_DAYS:.1f}",
                            f"{pct}%", str(np) if np else "—",
                            str(round(pr_lines/np)) if np else "—",
                            added])
        um_rows.sort(key=lambda r: -r[-1])
        um_rows = [r[:-1] for r in um_rows]
        lines += md_table(mh, um_rows, right_cols={2,3,5,6,7,8})

    return lines

# ── Jira Analysis section ─────────────────────────────────────────────────────

def parse_dt(s):
    if not s: return None
    try: return datetime.datetime.fromisoformat(s[:19])
    except: return None

def cycle_days(ticket):
    c = parse_dt(ticket.get("created"))
    r = parse_dt(ticket.get("resolved"))
    if not c or not r: return None
    return max(0, (r - c).days)

def build_jira_section(alias_to_person):
    jira = {}
    for proj in JIRA_PROJECTS:
        for t in load_jira(proj):
            jira[t["key"]] = t

    lines = ["", "---", "", "## Jira Analysis", ""]

    # ── 1. Summary by project ────────────────────────────────────────────────
    lines += ["### Summary by Project", ""]
    sh = ["Project","Total","Stories","Bugs","Tasks","Bug %","Done","Done %","Avg Cycle (days)","Sprints?"]
    s_rows = []
    for proj in JIRA_PROJECTS:
        tickets = [t for t in jira.values() if t["key"].startswith(proj+"-")]
        if not tickets: continue
        stories  = [t for t in tickets if t["issue_type"] == "Story"]
        bugs     = [t for t in tickets if t["issue_type"] in ("Bug","Bug Sub-task")]
        tasks    = [t for t in tickets if t["issue_type"] == "Task"]
        done     = [t for t in tickets if t["status_category"] == "done"]
        bug_pct  = f"{100*len(bugs)//(len(stories)+len(bugs)) if (stories or bugs) else 0}%"
        done_pct = f"{100*len(done)//len(tickets) if tickets else 0}%"
        cycles   = [d for t in done if t["issue_type"] in ("Story","Bug") for d in [cycle_days(t)] if d is not None]
        avg_cyc  = str(round(statistics.mean(cycles))) if cycles else "—"
        has_sprint = "✓" if any(t.get("sprint") for t in tickets) else "—"
        s_rows.append([proj, len(tickets), len(stories), len(bugs), len(tasks),
                       bug_pct, len(done), done_pct, avg_cyc, has_sprint])
    lines += md_table(sh, s_rows, right_cols={1,2,3,4,5,6,7,8})

    # ── 2. Sprint breakdown for structured projects ──────────────────────────
    lines += ["", "### Sprint Breakdown (Jan–Feb 2026)", "",
              "_Shows sprints active in Jan–Feb 2026 for projects with structured sprint cadences._", ""]

    for proj, sprint_filter in [("XRFQ", lambda s: s and "P26." in s and any(x in s for x in ["P26.5","P26.6"])),
                                  ("PAN",  lambda s: s and float(s) >= 1.85 if s and s.replace(".","").isdigit() else False),
                                  ("MAUI", lambda s: s and "PI-26." in s)]:
        proj_tickets = [t for t in jira.values() if t["key"].startswith(proj+"-")]
        sprint_data  = defaultdict(lambda: {"total":0,"done":0,"bugs":0,"stories":0})
        for t in proj_tickets:
            s = t.get("sprint","")
            if sprint_filter(s):
                sprint_data[s]["total"]   += 1
                sprint_data[s]["done"]    += (t["status_category"] == "done")
                sprint_data[s]["bugs"]    += (t["issue_type"] in ("Bug","Bug Sub-task"))
                sprint_data[s]["stories"] += (t["issue_type"] == "Story")

        if not sprint_data: continue
        lines += [f"**{proj}**", ""]
        sp_h = ["Sprint","Total","Done","Done %","Stories","Bugs","Bug %"]
        sp_rows = []
        for sprint in sorted(sprint_data.keys()):
            d = sprint_data[sprint]
            sp_rows.append([sprint, d["total"], d["done"],
                            f"{100*d['done']//d['total'] if d['total'] else 0}%",
                            d["stories"], d["bugs"],
                            f"{100*d['bugs']//(d['stories']+d['bugs']) if (d['stories']+d['bugs']) else 0}%"])
        lines += md_table(sp_h, sp_rows, right_cols={1,2,3,4,5,6})
        lines.append("")

    # ── 3. Description quality by reporter ──────────────────────────────────
    lines += ["### Description Quality by Reporter", "",
              "_Length of ticket description (chars). Reporters listed if they filed ≥5 tickets._", ""]
    reporter_stats = defaultdict(lambda: {"count":0,"total_len":0,"empty":0})
    for t in jira.values():
        r   = t.get("reporter") or "Unknown"
        dl  = len(t.get("description_text") or "")
        reporter_stats[r]["count"]    += 1
        reporter_stats[r]["total_len"]+= dl
        reporter_stats[r]["empty"]    += (dl == 0)

    rq_rows = []
    for reporter, s in reporter_stats.items():
        if s["count"] < 5: continue
        avg = s["total_len"] // s["count"]
        empty_pct = 100 * s["empty"] // s["count"]
        rq_rows.append([reporter, s["count"], avg, f"{empty_pct}%"])
    rq_rows.sort(key=lambda r: -r[2])
    rq_h = ["Reporter","Tickets","Avg Desc (chars)","% Empty"]
    lines += md_table(rq_h, rq_rows[:20], right_cols={1,2,3})

    # ── 4. Epic complexity ───────────────────────────────────────────────────
    lines += ["", "### Epic Complexity", "",
              "_Number of child tickets per epic. Top 10 epics per project with ≥5 children._", ""]
    child_counts = defaultdict(int)
    for t in jira.values():
        ek = t.get("epic_key")
        if ek and t["issue_type"] not in ("Epic",):
            child_counts[ek] += 1

    for proj in JIRA_PROJECTS:
        proj_epics = [(k, v) for k,v in child_counts.items() if k.startswith(proj+"-") and v >= 5]
        if not proj_epics: continue
        proj_epics.sort(key=lambda x: -x[1])
        lines += [f"**{proj}**", ""]
        ec_h = ["Epic","Summary","Children","Linked Issues"]
        ec_rows = []
        for ek, cnt in proj_epics[:10]:
            t = jira.get(ek, {})
            summary = (t.get("summary") or "")[:55]
            linked  = len(t.get("linked_issues") or [])
            ec_rows.append([ek, summary, cnt, linked])
        lines += md_table(ec_h, ec_rows, right_cols={2,3})
        lines.append("")

    # ── 5 & 6. PR size vs story points and description length ────────────────
    # Build combined jira-link index from prs files
    pr_jira_pairs = []  # (pr_added_lines, story_points, desc_length)
    for proj in PROJECTS:
        for pr in load_prs(proj):
            jira_links_raw = pr.get("jira-link","") or ""
            keys = re.findall(r'[A-Z][A-Z0-9]+-\d+', jira_links_raw)
            for key in keys:
                t = jira.get(key)
                if not t: continue
                pr_lines = _int(pr.get("+lines",0))
                sp       = t.get("story_points")
                # description length: ticket + parent epic
                desc_len = len(t.get("description_text") or "")
                ek = t.get("epic_key")
                if ek and ek in jira:
                    desc_len += len(jira[ek].get("description_text") or "")
                if pr_lines > 0:
                    pr_jira_pairs.append((pr_lines, sp, desc_len, key))
                break  # one match per PR is enough

    lines += ["### PR Size vs Story Points", ""]
    sp_pairs = [(lines_count, sp) for lines_count, sp, _, _ in pr_jira_pairs if sp is not None]
    if len(sp_pairs) >= 5:
        buckets = [(0,100),(100,500),(500,2000),(2000,999999)]
        bucket_labels = ["<100",  "100–500", "500–2K", ">2K"]
        b_h = ["PR Size (+lines)","# Matched PRs","Avg Story Points","Median Story Points"]
        b_rows = []
        for (lo, hi), label in zip(buckets, bucket_labels):
            group = [sp for sz, sp in sp_pairs if lo <= sz < hi]
            if group:
                b_rows.append([label, len(group), f"{statistics.mean(group):.1f}", f"{statistics.median(group):.1f}"])
        if b_rows:
            lines += md_table(b_h, b_rows, right_cols={1,2,3})
        xs, ys = zip(*sp_pairs)
        r = pearson(list(xs), list(ys))
        lines.append(f"\n_Pearson r = {r:.2f} (n={len(sp_pairs)}). {'Weak' if abs(r)<0.3 else 'Moderate' if abs(r)<0.6 else 'Strong'} correlation between PR size and story points._")
    else:
        lines.append(f"_Only {len(sp_pairs)} matched PRs have story point data — insufficient for reliable correlation analysis._")

    lines += ["", "### PR Size vs Description Length", "",
              "_Description length = ticket description + parent epic description (chars)._", ""]
    dl_pairs = [(sz, dl) for sz, _, dl, _ in pr_jira_pairs if dl > 0]
    if len(dl_pairs) >= 10:
        buckets = [(0,100),(100,500),(500,2000),(2000,999999)]
        bucket_labels = ["<100", "100–500", "500–2K", ">2K"]
        b_h = ["PR Size (+lines)","# Matched PRs","Avg Desc Len (chars)","Median Desc Len"]
        b_rows = []
        for (lo, hi), label in zip(buckets, bucket_labels):
            group = [dl for sz, dl in dl_pairs if lo <= sz < hi]
            if group:
                b_rows.append([label, len(group), f"{statistics.mean(group):.0f}", f"{statistics.median(group):.0f}"])
        lines += md_table(b_h, b_rows, right_cols={1,2,3})
        xs, ys = zip(*dl_pairs)
        r = pearson(list(xs), list(ys))
        lines.append(f"\n_Pearson r = {r:.2f} (n={len(dl_pairs)}). "
                     f"{'Weak' if abs(r)<0.3 else 'Moderate' if abs(r)<0.6 else 'Strong'} correlation between PR size and description length._")
    else:
        lines.append(f"_Only {len(dl_pairs)} matched PRs with non-empty descriptions._")

    # ── 7. Notable Observations ──────────────────────────────────────────────
    lines += ["", "### Notable Observations", ""]

    # Bug ratios
    bug_ratios = {}
    for proj in JIRA_PROJECTS:
        tickets = [t for t in jira.values() if t["key"].startswith(proj+"-")]
        bugs    = sum(1 for t in tickets if t["issue_type"] in ("Bug","Bug Sub-task"))
        stories = sum(1 for t in tickets if t["issue_type"] == "Story")
        if stories + bugs > 0:
            bug_ratios[proj] = (bugs, stories, 100*bugs//(bugs+stories))

    high_bug = [(p, *v) for p, v in sorted(bug_ratios.items(), key=lambda x: -x[1][2]) if v[2] >= 20]
    if high_bug:
        lines.append("**High bug ratios** (bugs as % of stories+bugs, Jan–Feb period):")
        for proj, bugs, stories, pct in high_bug:
            lines.append(f"- **{proj}**: {pct}% ({bugs} bugs vs {stories} stories)")

    # Cycle time comparison
    lines.append("")
    lines.append("**Cycle time** (avg days from ticket created → resolved, for completed stories/bugs):")
    for proj in JIRA_PROJECTS:
        tickets = [t for t in jira.values() if t["key"].startswith(proj+"-")]
        cycles  = [d for t in tickets
                   if t["status_category"] == "done" and t["issue_type"] in ("Story","Bug")
                   for d in [cycle_days(t)] if d is not None]
        if cycles:
            lines.append(f"- **{proj}**: {round(statistics.mean(cycles))} days avg, "
                         f"{round(statistics.median(cycles))} days median (n={len(cycles)})")

    # In-flight work
    lines.append("")
    lines.append("**In-flight work** (tickets in 'in-progress' status at end of period):")
    for proj in JIRA_PROJECTS:
        tickets = [t for t in jira.values() if t["key"].startswith(proj+"-")]
        in_prog = sum(1 for t in tickets if t["status_category"] == "in-progress")
        total   = len(tickets)
        if in_prog:
            lines.append(f"- **{proj}**: {in_prog} in-progress of {total} total ({100*in_prog//total}%)")

    # Nucleus has no sprints — call out separately
    lines += ["",
              "**Sprint discipline**: XRFQ and PAN show structured sprint cadences (2-week sprints); MAUI uses PI sprints. "
              "CODE and NUCLEUS have minimal sprint tracking — work is tracked via labels (release version tags) rather "
              "than sprints. XPMI uses a mix of sprints and evergreen backlogs.",
              "",
              "**Nucleus PR coverage**: `prs-nucleus.csv` is empty — Nucleus uses direct-push/rebase workflow "
              "with no PR metadata available from the git log. PR/author metrics for the nucleus team are unavailable.",
    ]

    # Top contributors to linked jira work
    matched = len(pr_jira_pairs)
    total_prs = sum(len(load_prs(p)) for p in PROJECTS)
    lines.append(f"\n**Jira ↔ PR link coverage**: {matched} of {total_prs} PRs ({100*matched//total_prs if total_prs else 0}%) "
                 "were matched to a Jira ticket. Unlinked PRs are either infrastructure/ops work, or commits "
                 "that use issue keys not in the six main Jira projects tracked here.")

    return lines

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("Loading data...", flush=True)
    orgchart = load_orgchart()
    alias_to_person, unmatched = load_people()
    print(f"  {len(alias_to_person)} aliases, {len(unmatched)} unmatched", flush=True)

    print("Building activity section...", flush=True)
    lines = build_activity_section(alias_to_person, unmatched, orgchart)

    print("Building Jira analysis section...", flush=True)
    lines += build_jira_section(alias_to_person)

    lines.append("")
    output = "\n".join(lines)

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"Written: {OUT_FILE} ({len(output):,} chars, {len(lines)} lines)", flush=True)

if __name__ == "__main__":
    main()
