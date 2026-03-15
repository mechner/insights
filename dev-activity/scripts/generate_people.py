#!/usr/bin/env python3
"""
generate_people.py

Generates people.csv by matching git author identities from all *-commits.csv
files to OrgChart.csv entries, then computing team membership.

Usage:
    python3 generate_people.py
"""

import csv
import os
import re
import unicodedata
from collections import defaultdict

SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR  = os.path.dirname(SCRIPT_DIR)          # dev-activity/
DATA_DIR     = os.path.join(PROJECT_DIR, "data")
REPORTS_DIR  = os.path.join(PROJECT_DIR, "reports")
REPOS_DIR    = os.path.dirname(os.path.dirname(SCRIPT_DIR))  # IdeaProjects/
PROJECTS = ["xp2", "nucleus", "pano", "xp1"]

# Team manager → team name mapping (using OrgChart canonical names)
TEAM_MANAGERS = {
    "Rivera, Enmanuel": "xp-us",
    "Jaen, Rodrigo":    "xp-eu",
    "Desai, Keshal":    "xp-match",
    "Bobbala, Ramakrishna": "xp-pt",
    "Richard, Michel":  "xp-platform",
    "Fishler, Eran":    "nucleus",
    "Hakim, Jawaid":    "pano",
}

# Hard-coded overrides for identities that algorithms can't resolve
# (nicknames, unusual username patterns, alternate names, etc.)
KNOWN_MATCHES = {
    "Andy Smith":       "Smith, Andrew",
    "Jim Higson":       "Higson, James",
    "Ram Bobbala":      "Bobbala, Ramakrishna",
    "Tim Kang":         "Kang, Timothy",
    "shjain":           "Jain, Shreshthha",
    "rahukumar":        "Kumar, Rahul",
    "Evan Yu":          "Yu, Yiwen",
    "Dimitar Christoff":"Kodjabashev, Dimitar",
}

# Unmatched identities that belong to the same (non-OrgChart) person.
# Each inner list merges those aliases into one people.csv row.
MERGE_UNMATCHED = [
    ["Satraj Sehmi", "sat sehmi"],
]

# Service/bot accounts to exclude entirely
SKIP_IDENTITIES = {
    "Azure DevOps Build Service",
    "svc-azure_devops",
    "svc-ui-azure-pipelines",
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def normalize(s):
    """Lowercase, strip accents, keep only letters/digits/spaces."""
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()


def strip_suffix(name):
    """Remove trailing middle initial (e.g. 'Pfeiffer, Karl C.' → 'Pfeiffer, Karl')."""
    parts = name.rsplit(" ", 1)
    if len(parts) == 2 and re.match(r"^[A-Z]\.$", parts[1]):
        return parts[0]
    return name


# ── OrgChart loading ──────────────────────────────────────────────────────────

def load_orgchart():
    """Return {org_name: {manager, title}} from OrgChart.csv."""
    path = os.path.join(DATA_DIR, "OrgChart.csv")
    people = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            name = row.get("Name", "").strip()
            if name:
                people[name] = {
                    "manager": row.get("Manager", "").strip(),
                    "title":   row.get("Title", "").strip(),
                }
    return people


def compute_teams(orgchart):
    """
    BFS from each team manager to assign every org member a team name.
    Returns {org_name: team_name}.
    """
    children = defaultdict(list)
    for name, info in orgchart.items():
        mgr = strip_suffix(info["manager"])
        children[mgr].append(name)

    # Pre-seed each team manager into their own team first, so higher-level BFS
    # (e.g. Fishler's nuc-platform) won't overwrite sub-team managers (e.g. Leykin → nuc-match).
    person_to_team = {mgr: team for mgr, team in TEAM_MANAGERS.items()}

    for team_mgr, team_name in TEAM_MANAGERS.items():
        queue = list(children.get(team_mgr, []))   # direct reports only; manager already seeded
        while queue:
            person = queue.pop(0)
            if person in person_to_team:
                continue   # already assigned (another sub-team manager or duplicate); skip subtree
            person_to_team[person] = team_name
            queue.extend(children.get(person, []))
    return person_to_team


# ── Git author loading ────────────────────────────────────────────────────────

def load_all_git_authors():
    """Return set of all author strings from all *-commits.csv files."""
    authors = set()
    for project in PROJECTS:
        path = os.path.join(DATA_DIR, f"{project}-commits.csv")
        if not os.path.exists(path):
            continue
        with open(path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                a = row.get("author", "").strip()
                if a:
                    authors.add(a)
    return authors - SKIP_IDENTITIES


# ── Matching ──────────────────────────────────────────────────────────────────

def build_name_maps(orgchart):
    """
    Build lookup dicts for matching git author strings to org names.
    Returns:
      norm_fl_map: {normalized "First Last" → org_name}
      username_map: {username_pattern → [org_name, ...]}  (list for ambiguity detection)
    """
    norm_fl_map = {}
    username_map = defaultdict(list)

    for org_name in orgchart:
        parts = org_name.split(",", 1)
        if len(parts) != 2:
            continue
        last  = parts[0].strip()
        first = parts[1].strip()

        # Strategy 1 keys: normalized "First Last" and "Last First"
        norm_fl_map[normalize(f"{first} {last}")] = org_name
        norm_fl_map[normalize(f"{last} {first}")] = org_name

        # Strategy 3 username patterns
        f_norm = normalize(first)
        l_norm = normalize(last).replace(" ", "")
        if f_norm and l_norm:
            fi = f_norm[0]
            username_map[fi + l_norm].append(org_name)             # first-initial + last
            username_map[f_norm.replace(" ", "") + l_norm].append(org_name)  # first+last

    return norm_fl_map, username_map


def match_author(author, orgchart, norm_fl_map, username_map):
    """
    Try all strategies to match a git author string to an OrgChart entry.
    Returns org_name or None.
    """
    # Hard-coded override
    if author in KNOWN_MATCHES:
        return KNOWN_MATCHES[author]

    author_lower = author.lower()

    # Strategy 1: exact normalized name match ("First Last" or "Last First")
    key = normalize(author)
    if key in norm_fl_map:
        return norm_fl_map[key]

    # Strategy 2: email prefix
    if "@" in author:
        prefix = author.split("@")[0].lower()
        matches = username_map.get(prefix, [])
        if len(matches) == 1:
            return matches[0]
        return None  # ambiguous or not found

    # Strategy 3: username pattern (no spaces — single-token identity)
    if " " not in author:
        matches = username_map.get(author_lower, [])
        if len(matches) == 1:
            return matches[0]
        if len(matches) > 1:
            return None  # ambiguous
        return None

    # Strategy 4: token subset match (handles middle names, compound last names)
    author_tokens = set(normalize(author).split())
    candidates = []
    for org_name in orgchart:
        parts = org_name.split(",", 1)
        if len(parts) != 2:
            continue
        last  = parts[0].strip()
        first = parts[1].strip()
        org_tokens = set(normalize(f"{first} {last}").split())
        # Author tokens are a subset of org tokens (extra middle names in org)
        if author_tokens and author_tokens <= org_tokens:
            candidates.append(org_name)
            continue
        # Org core (first word of each name part) is subset of author tokens
        core = {normalize(first.split()[0]), normalize(last.split()[0])}
        if core and core <= author_tokens:
            candidates.append(org_name)

    if len(candidates) == 1:
        return candidates[0]
    return None  # zero or ambiguous


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    orgchart   = load_orgchart()
    person_to_team = compute_teams(orgchart)
    authors    = load_all_git_authors()
    norm_fl_map, username_map = build_name_maps(orgchart)

    org_to_aliases = defaultdict(list)
    unmatched = []

    for author in sorted(authors):
        match = match_author(author, orgchart, norm_fl_map, username_map)
        if match:
            org_to_aliases[match].append(author)
        else:
            unmatched.append(author)

    # Write people.csv
    out_path = os.path.join(DATA_DIR, "people.csv")
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "manager", "team", "aliases"])
        writer.writeheader()
        for org_name in sorted(orgchart.keys()):
            aliases = org_to_aliases.get(org_name, [])
            if not aliases:
                continue
            writer.writerow({
                "name":    org_name,
                "manager": orgchart[org_name]["manager"],
                "team":    person_to_team.get(org_name, ""),
                "aliases": " ".join(sorted(aliases)),
            })
        # Merge known-same unmatched identities into single rows
        merge_groups = []
        remaining = set(unmatched)
        for group in MERGE_UNMATCHED:
            group_set = set(group) & remaining
            if group_set:
                merge_groups.append(sorted(group_set))
                remaining -= group_set
        for author in sorted(remaining):
            merge_groups.append([author])

        for group in sorted(merge_groups, key=lambda g: g[0]):
            writer.writerow({"name": "", "manager": "", "team": "", "aliases": " ".join(group)})

    print(f"Written: {out_path}")
    print(f"Matched: {len(org_to_aliases)} people with git activity")
    print(f"Unmatched git identities: {len(unmatched)}")
    if unmatched:
        print("\nUnmatched identities (update OrgChart and re-run if these are org members):")
        for u in unmatched:
            print(f"  {u}")


if __name__ == "__main__":
    main()
