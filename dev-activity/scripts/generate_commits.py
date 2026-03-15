#!/usr/bin/env python3
"""
generate_commits.py

Regenerates all *-commits.csv files from local git repos.
Columns: date, repo, author, git-hash, jira-link, file-count,
         added-lines, removed-lines, message, file-types, %test, commit-type

Usage:
    python3 generate_commits.py
"""

import csv
import os
import re
import subprocess
import sys

SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR  = os.path.dirname(SCRIPT_DIR)          # dev-activity/
DATA_DIR     = os.path.join(PROJECT_DIR, "data")
REPORTS_DIR  = os.path.join(PROJECT_DIR, "reports")
REPOS_DIR    = os.path.dirname(os.path.dirname(SCRIPT_DIR))  # IdeaProjects/

DATE_START = "2025-12-31"   # --after (exclusive, for git)
DATE_END   = "2026-03-01"   # --before (exclusive, for git)
# Hard date bounds applied in Python to filter by author date
DATE_MIN = "2026-01-01"
DATE_MAX = "2026-02-28"

BOT_AUTHORS = {"svc-azure_devops"}

PROJECTS = {
    "xp2":     ["monorepo"],
    "nucleus": ["Nucleus"],
    "pano":    ["pano2"],
    "xp1":     [
        "bondlinkbridge-deployment", "hulk-api-srv", "hulk-commons",
        "kauai-vips", "maom-action-svc", "maom-commons",
        "maom-ui", "maom-ui-iac", "maom-subview-svc",
    ],
}

FIELDNAMES = [
    "date", "repo", "author", "git-hash", "jira-link",
    "file-count", "added-lines", "removed-lines",
    "message", "file-types", "%test", "commit-type",
]

# ── Test-file detection ────────────────────────────────────────────────────────

TEST_PATHS = [
    "/src/test/",
    "/src/testFixtures/",
    "/src/integrationTest/",
    "/__tests__/",
    "/e2e/",
    "/test/playwright/",
    "/test/protractor/",
    "/smoke-test/",
]


def is_test_file(path):
    norm = "/" + path
    for tp in TEST_PATHS:
        if tp in norm:
            return True
    fname = path.rsplit("/", 1)[-1]
    if re.search(r"Tests?\.java$", fname):
        return True
    if re.search(r"\.(test|spec)\.(tsx?)$", fname):
        return True
    ext = fname.rsplit(".", 1)[-1] if "." in fname else ""
    if ext in ("bek", "feature"):
        return True
    return False


# ── Git log parsing ────────────────────────────────────────────────────────────

def git_commits(repo_name):
    """
    Yield raw commit dicts from a single repo using git log --numstat.
    Each dict has: date, author, hash, message, files[]
    """
    repo_path = os.path.join(REPOS_DIR, repo_name)
    if not os.path.isdir(repo_path):
        print(f"  ERROR: repo not found: {repo_path}", file=sys.stderr)
        return

    cmd = [
        "git", "-C", repo_path, "log",
        "--no-merges",
        f"--after={DATE_START}",
        f"--before={DATE_END}",
        "--format=COMMIT|%H|%ad|%an|%s",
        "--date=short",
        "--numstat",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ERROR running git log in {repo_name}: {result.stderr[:200]}", file=sys.stderr)
        return

    current = None
    for raw_line in result.stdout.split("\n"):
        line = raw_line.rstrip()

        if line.startswith("COMMIT|"):
            if current is not None:
                yield current
            _, hash_, date_, author_, *msg_parts = line.split("|")
            current = {
                "date":    date_,
                "author":  author_,
                "hash":    hash_,
                "message": "|".join(msg_parts).strip(),
                "files":   [],
            }
        elif current is not None and "\t" in line:
            parts = line.strip().split("\t")
            if len(parts) == 3:
                added_s, removed_s, path = parts
                added   = int(added_s)   if added_s.isdigit()   else 0
                removed = int(removed_s) if removed_s.isdigit() else 0
                ext     = path.rsplit(".", 1)[-1] if "." in path.rsplit("/", 1)[-1] else ""
                current["files"].append({
                    "path":    path,
                    "added":   added,
                    "removed": removed,
                    "test":    is_test_file(path),
                    "ext":     ext,
                })

    if current is not None:
        yield current


def in_range(date_str):
    return DATE_MIN <= date_str <= DATE_MAX


# ── Row construction ───────────────────────────────────────────────────────────

def build_row(c, repo_name):
    files       = c["files"]
    total_lines = sum(f["added"] + f["removed"] for f in files)
    test_lines  = sum(f["added"] + f["removed"] for f in files if f["test"])

    pct_test = round(100 * test_lines / total_lines) if total_lines > 0 else 0

    # file-types: extensions covering >= 10% of total lines
    ext_lines = {}
    for f in files:
        if f["ext"]:
            ext_lines[f["ext"]] = ext_lines.get(f["ext"], 0) + f["added"] + f["removed"]
    if total_lines > 0:
        file_types = " ".join(
            ext for ext, lines in sorted(ext_lines.items(), key=lambda x: -x[1])
            if lines / total_lines >= 0.10
        )
    else:
        file_types = ""

    jira_link   = " ".join(re.findall(r"[A-Z]+-\d+", c["message"]))
    commit_type = "squash-pr" if c["message"].startswith("Merged PR ") else "direct"

    return {
        "date":          c["date"],
        "repo":          repo_name,
        "author":        c["author"],
        "git-hash":      c["hash"],
        "jira-link":     jira_link,
        "file-count":    len(files),
        "added-lines":   sum(f["added"]   for f in files),
        "removed-lines": sum(f["removed"] for f in files),
        "message":       c["message"],
        "file-types":    file_types,
        "%test":         pct_test,
        "commit-type":   commit_type,
    }


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    for project, repos in PROJECTS.items():
        out_path = os.path.join(DATA_DIR, f"{project}-commits.csv")
        rows = []
        for repo_name in repos:
            print(f"  {project}/{repo_name} ...", end=" ", flush=True)
            count = 0
            for c in git_commits(repo_name):
                if c["author"] in BOT_AUTHORS:
                    continue
                if not in_range(c["date"]):
                    continue
                rows.append(build_row(c, repo_name))
                count += 1
            print(f"{count} commits")

        with open(out_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(rows)

        print(f"  → wrote {len(rows)} rows to {out_path}")


if __name__ == "__main__":
    main()
