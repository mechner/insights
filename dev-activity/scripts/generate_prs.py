#!/usr/bin/env python3
"""
generate_prs.py

Generates prs-{{project}}.csv files from local git repos and commits data.

Strategy per project:
  xp2     — squash-PR commits (message starts "Merged PR NN:") in commits CSV
  pano    — commits with "(#NNNN)" in message (one commit ≈ one PR)
  xp1     — 2-parent "Pull request #N:" merge commits (via git log --merges)
  nucleus — no PR markers in git; file is written with header only + a note

Columns: date, repo, author, pr-id, jira-link, file-count,
         +lines, -lines, message, file-types, %test

Usage:
    python3 generate_prs.py
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
DATE_MIN   = "2026-01-01"
DATE_MAX   = "2026-02-28"

FIELDNAMES = [
    "date", "repo", "author", "pr-id", "jira-link",
    "file-count", "+lines", "-lines", "message", "file-types", "%test",
]

# ── Test-file detection (same rules as generate_commits.py) ───────────────────

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


def file_stats_from_numstat(numstat_lines):
    """
    Parse numstat lines (list of 'added\tremoved\tpath' strings).
    Returns (file_count, added, removed, file_types_str, pct_test).
    """
    files = []
    for line in numstat_lines:
        parts = line.strip().split("\t")
        if len(parts) == 3:
            added_s, removed_s, path = parts
            added   = int(added_s)   if added_s.isdigit()   else 0
            removed = int(removed_s) if removed_s.isdigit() else 0
            ext     = path.rsplit(".", 1)[-1] if "." in path.rsplit("/", 1)[-1] else ""
            files.append({"path": path, "added": added, "removed": removed,
                          "test": is_test_file(path), "ext": ext})

    total_lines = sum(f["added"] + f["removed"] for f in files)
    test_lines  = sum(f["added"] + f["removed"] for f in files if f["test"])
    pct_test    = round(100 * test_lines / total_lines) if total_lines > 0 else 0

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

    return (
        len(files),
        sum(f["added"]   for f in files),
        sum(f["removed"] for f in files),
        file_types,
        pct_test,
    )


# ── xp2: squash-PR commits from commits CSV ───────────────────────────────────

def prs_xp2():
    rows = []
    path = os.path.join(DATA_DIR, "xp2-commits.csv")
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("commit-type") != "squash-pr":
                continue
            if not (DATE_MIN <= r.get("date", "") <= DATE_MAX):
                continue
            m = re.match(r"Merged PR (\d+):\s*(.*)", r.get("message", ""))
            if not m:
                continue
            pr_id   = m.group(1)
            title   = m.group(2).strip()
            jira    = " ".join(re.findall(r"[A-Z]+-\d+", title))
            rows.append({
                "date":       r["date"],
                "repo":       r["repo"],
                "author":     r["author"],
                "pr-id":      pr_id,
                "jira-link":  jira,
                "file-count": r["file-count"],
                "+lines":     r["added-lines"],
                "-lines":     r["removed-lines"],
                "message":    title,
                "file-types": r["file-types"],
                "%test":      r["%test"],
            })
    return rows


# ── pano: commits with (#N) reference ─────────────────────────────────────────

def prs_pano():
    rows = []
    path = os.path.join(DATA_DIR, "pano-commits.csv")
    seen = set()
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            msg  = r.get("message", "")
            m    = re.search(r"\(#(\d+)\)", msg)
            if not m:
                continue
            if not (DATE_MIN <= r.get("date", "") <= DATE_MAX):
                continue
            pr_id = m.group(1)
            if pr_id in seen:
                continue  # skip duplicate (rare)
            seen.add(pr_id)
            title = re.sub(r"\s*\(#\d+\)\s*$", "", msg).strip()
            jira  = " ".join(re.findall(r"[A-Z]+-\d+", title))
            rows.append({
                "date":       r["date"],
                "repo":       r["repo"],
                "author":     r["author"],
                "pr-id":      pr_id,
                "jira-link":  jira,
                "file-count": r["file-count"],
                "+lines":     r["added-lines"],
                "-lines":     r["removed-lines"],
                "message":    title,
                "file-types": r["file-types"],
                "%test":      r["%test"],
            })
    return rows


# ── xp1: Pull request #N: merge commits ───────────────────────────────────────

def xp1_pr_merges(repo_name):
    repo_path = os.path.join(REPOS_DIR, repo_name)
    cmd = [
        "git", "-C", repo_path, "log",
        "--merges",
        f"--after={DATE_START}",
        f"--before={DATE_END}",
        "--format=COMMIT|%H|%ad|%an|%s",
        "--date=short",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    commits = []
    for line in result.stdout.strip().split("\n"):
        if not line.startswith("COMMIT|"):
            continue
        _, hash_, date_, author_, *msg_parts = line.split("|")
        msg = "|".join(msg_parts).strip()
        m = re.match(r"Pull request #(\d+):\s*(.*)", msg)
        if not m:
            continue
        commits.append({"hash": hash_, "date": date_, "author": author_,
                         "pr_id": m.group(1), "title": m.group(2).strip()})
    return commits


def prs_xp1():
    repos = [
        "bondlinkbridge-deployment", "hulk-api-srv", "hulk-commons",
        "kauai-vips", "maom-action-svc", "maom-commons",
        "maom-ui", "maom-ui-iac", "maom-subview-svc",
    ]
    rows = []
    for repo_name in repos:
        for pr in xp1_pr_merges(repo_name):
            repo_path = os.path.join(REPOS_DIR, repo_name)
            result = subprocess.run(
                ["git", "-C", repo_path, "diff", "--numstat",
                 f"{pr['hash']}^1", pr["hash"]],
                capture_output=True, text=True,
            )
            numstat_lines = [l for l in result.stdout.split("\n") if "\t" in l]
            fc, added, removed, file_types, pct_test = file_stats_from_numstat(numstat_lines)
            jira = " ".join(re.findall(r"[A-Z]+-\d+", pr["title"]))
            rows.append({
                "date":       pr["date"],
                "repo":       repo_name,
                "author":     pr["author"],
                "pr-id":      pr["pr_id"],
                "jira-link":  jira,
                "file-count": fc,
                "+lines":     added,
                "-lines":     removed,
                "message":    pr["title"],
                "file-types": file_types,
                "%test":      pct_test,
            })
    return rows


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    tasks = [
        ("xp2",     prs_xp2,     "squash-PR commits"),
        ("pano",    prs_pano,    "(#N) commits"),
        ("xp1",     prs_xp1,     "Pull request #N: merge commits"),
    ]

    for project, fn, strategy in tasks:
        print(f"  {project} ({strategy}) ...", end=" ", flush=True)
        rows = fn()
        out  = os.path.join(DATA_DIR, f"prs-{project}.csv")
        with open(out, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(rows)
        print(f"{len(rows)} PRs → {out}")

    # nucleus: no PR markers — write header-only with comment row
    nuc_path = os.path.join(DATA_DIR, "prs-nucleus.csv")
    with open(nuc_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
    print(f"  nucleus: no PR markers in git history — {nuc_path} written (empty)")


if __name__ == "__main__":
    main()
