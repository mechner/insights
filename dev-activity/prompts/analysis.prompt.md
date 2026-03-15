# Goals

My goals are to understand:
- What is the productivity of the org?
- What is the quality of the work the org is doing?
- What is the safety and maintainability of the code being produced?
- Are the developers doing enough automated testing?
- For all the above, does it vary
  - by project?
  - by team?
  - by individual?
- Are any of the developers particularly strong (productive) or weak (unproductive).
- Are any of the managers particularly strong or weak?
- How are these metrics evolving over time?

This is for private use by management only. Goodhart's law "When a measure becomes a target, it ceases to be a good 
measure" applies here, so productivity measures are only to flag places where managers might want to spend time 
to take a closer look (false positives are OK) - not to be made public or used for evaluation.

We will be working interactively and iteratively generating reports based on several local data 
files described below. If the "raw data files" are not present, your first job in a 
session will be to create them by retrieving and caching the data from git (for the referenced repos).

# Date Range

The date range for this analysis is 2026-01-01 to 2026-02-28. 
Only commits and PRs with a date in this range should be retrieved in the raw data files or analysis.

# Projects, Repositories, and Teams

Mapping of projects to repositories:
- xp2: @monorepo
- nucleus: @Nucleus
- pano: @pano2
- xp1: 
  - @bondlinkbridge-deployment
  - @hulk-api-srv 
  - @hulk-commons 
  - @kauai-vips
  - @maom-action-svc 
  - @maom-commons 
  - @maom-ui
  - @maom-ui-iac
  - @maom-subview-svc
These repositories should all exist locally in the parent directory of this project; report as an error if they don't.

Mapping of team name to manager:
 - xp-us: Mendez, Enmanuel
 - xp-eu: Jaen, Rodrigo
 - xp-match: Desai, Keshal
 - xp-pt: Bobbala, Ramakrishna
 - xp-platform: Richard, Michel
 - nucleus: Fishler, Eran
 - pano: Hakim, Jawaid

# Raw Data Files

@OrgChart.csv - defines my org (this must be given; don't try to generate it if missing. However this may be updated from time to time; if you notice middle initials or suffixes (Jr./Ph.D.) in the names, or if you find git identities that don't match any names in the org chart, report these to me so I can update the org chart and re-generate the derived files)

@commits=-{{project}}.csv - one file for each project listed above, with one row per commit from the git repos associated with that project above, and columns:
- date (yyyy-mm-dd)
- repo
- author
- git-hash (to uniquely identify the commit)
- jira-link (if found in commit message, pattern "[A-Z]+-\d+", multiple space-delimited if more than one found)
- file-count
- added-lines
- removed-lines
- message (the commit message)
- file-types (file suffixes of changed files, space delimited; omit types where the changed lines represent less than 10% of the total changed lines in that commit)
- %test: percentage of changed lines (added + removed) that are in test files,
  rounded to the nearest integer (0–100). Compute per-file using --numstat output.
  A file is a test file if ANY of the following match:
  Path-based (applies uniformly across all repos):
  - path contains /src/test/            (Maven/Gradle unit test source root — all Java repos)
  - path contains /src/testFixtures/    (Gradle test fixtures — Nucleus)
  - path contains /src/integrationTest/ (integration tests — Nucleus, pano)
  - path contains /__tests__/           (Jest test dirs — pano frontend, maom-ui)
  - path contains /e2e/                 (E2E tests — monorepo, pano)
  - path contains /test/playwright/     (Playwright — pano)
  - path contains /test/protractor/     (Protractor — pano)
  - path contains /smoke-test/          (smoke tests — monorepo)

  Filename-based:
  - filename ends with Test.java or Tests.java  (Java unit tests)
  - filename matches *.test.ts, *.test.tsx      (TS unit tests)
  - filename matches *.spec.ts, *.spec.tsx      (TS e2e / Playwright)

  Extension-based:
  - extension is bek                    (Nucleus Beaker integration tests)
  - extension is feature                (Gherkin/Cucumber — monorepo)

- commit-type: `squash-pr` if this is a single-parent Azure DevOps squash-merge commit
  (message starts with `"Merged PR "`); otherwise `direct`.

**Merge strategy and double-counting rules** (apply when generating each commits CSV):

- All repos: use `git log --no-merges` — this excludes traditional 2-parent merge commits
  whose code is already captured in the individual commits that landed via that merge.
- **xp2 (monorepo)** — Azure DevOps, mixed strategy:
  - Most PRs are squash-merged → a single-parent `"Merged PR NNNNN: …"` commit lands on main.
    No individual feature-branch commits appear on main for that PR. These are `commit-type=squash-pr`
    and ARE the correct unit of work; include them.
  - Some PRs use traditional merge → 2-parent merge commit (excluded by `--no-merges`); the
    individual feature-branch commits DO land on main and are counted as `commit-type=direct`.
  - Interpretation: xp2 `squash-pr` commits represent a full PR's worth of work; do not compare
    raw commit counts between xp2 and other projects without noting this distinction.
- **nucleus** — rebase / fast-forward only; no merge commits. All commits are `direct`.
- **pano** — GitHub-style: individual commits land via 2-parent merge commit. `--no-merges`
  correctly excludes the merge commit. PR reference appears as `(#NNNN)` suffix in message.
  All commits are `commit-type=direct`.
- **xp1 repos** — Bitbucket-style: individual commits land via 2-parent `"Pull request #N:"`
  merge commit (excluded by `--no-merges`). Cascading release merges also excluded. All `direct`.

**Bot exclusion:** Exclude any commit authored by `svc-azure_devops` from all analysis.
These are automated version-bump and tagging commits (primarily in xp2).

@prs-{{project}}.md - one file for each project, with columns:
- date (yyyy-mm-dd)
- repo
- author
- pr-id (to uniquely identify the PR)
- jira-link (if found in PR or commit title or description, pattern "[A-Z]+-\d+", multiple space-delimited if more than one found)
- file-count
- +lines
- -lines
- message (the PR title)
- file-types (file suffixes of changed files, space delimited; omit types where the added lines represent less than 5% of the total added lines in that PR)
- %test (defined the same as for commits, but computed across all commits in the PR)

Retrieve PR metadata directly from github/azure-devops APIs where possible, matching PRs to commits by author and date range if PR metadata is not available (e.g. for nucleus).

@jira-{{project}}.json - one file for each jira project that appears in any commit (CODE, NUMA, PAN, XPMI, XRFQ, 
MAUI), with one JSON object per ticket. Retrieve using `POST /rest/api/3/search/jql` (see AGENTS.md for API access 
details). Filter by `project=X AND updated >= "2026-01-01" AND updated <= "2026-02-28 23:59"`. Paginate via 
`nextPageToken` until `isLast == true` (the endpoint does not return a total count). Request these fields: `summary`,
`issuetype`, `status`, `priority`, `assignee`, `reporter`, `created`, `updated`, `resolution`, `resolutiondate`, 
`description`, `parent`, `labels`, `fixVersions`, `issuelinks`, `customfield_10014`, `customfield_10016`, 
`customfield_10021`, `customfield_10026`.

Each record in the JSON array should contain:
- `key` — ticket key (e.g. "XRFQ-4836")
- `summary` — ticket title (plain string)
- `issue_type` — issue type name: "Story", "Bug", "Task", "Sub-task", "Epic", etc.
- `status` — current status name (e.g. "In Progress", "Completed")
- `status_category` — normalized to one of: `"to-do"`, `"in-progress"`, `"done"` (from `status.statusCategory.key`: "new"→"to-do", "indeterminate"→"in-progress", "done"→"done")
- `priority` — priority name (e.g. "Medium", "High")
- `assignee` — display name of assignee, or null
- `reporter` — display name of reporter
- `created` — ISO timestamp
- `updated` — ISO timestamp
- `resolved` — ISO timestamp from `resolutiondate`, or null
- `resolution` — resolution name (e.g. "Done", "Won't Do"), or null
- `epic_key` — parent epic key: use `customfield_10014` if present, else use `parent.key` when `parent` exists and issue type is not "Sub-task" (for sub-tasks, use `parent.key` as `parent_key` instead)
- `parent_key` — direct parent key from `parent.key` (for sub-tasks and stories-under-epics), or null
- `story_points` — from `customfield_10026` (Story Points), falling back to `customfield_10016` (Story point estimate), or null
- `sprint` — sprint name from `customfield_10021[last].name` (take the last sprint if multiple), or null
- `fix_versions` — list of version names from `fixVersions`, or empty list
- `labels` — list of label strings
- `linked_issues` — list of `{"key": "...", "type": "...", "direction": "inward|outward"}` from `issuelinks`
- `description_text` — plain text extracted from the ADF `description` field (recursively concatenate all `text` nodes; skip if null)

Normalization and interpretation:
- Only include the six main projects (CODE, NUMA, PAN, XPMI, XRFQ, MAUI); skip the minor one-off project keys (AD, APPSRE, MAUI, MAUL, MAIU, XPCD, MDS, XSRE) found in some commits.
- Labels vary by project: CODE/NUCLEUS use them for release-version tracking (e.g. "matching/15.22.0"); PAN uses sprint labels (e.g. "sprint-1.89") and team labels; MAUI uses team/PCF labels. Treat labels as opaque tags unless specifically analyzed.
- `fix_versions` is populated for PAN, XPMI, and XRFQ; absent for CODE and NUMA — do not use for cross-project release comparisons without noting this gap.
- Bug count vs. total ticket count is a useful quality proxy: a high bug ratio in a project or sprint suggests quality problems.
- Cycle time (resolved − created) for Stories and Bugs can be used as a productivity/throughput metric; filter to `status_category == "done"` before computing.
- `story_points` is sparsely populated across all projects; do not use as a primary metric unless specifically analyzing a project known to use it consistently.

# Generated Files
@people.csv - one row per person who appears in any of the commits files with columns for:
- name (linking to OrgChart.csv)
- manager (linking to OrgChart.csv)
- team (the team name, derived from manager and the above mapping of team name to manager. Each team includes its manager as a member, so the manager's commits are included in the team totals and averages)
- aliases (space-delimited list of every git author identity associated with this person)
  - For each git identity found across all commits files, attempt to match it to an OrgChart person using these strategies in order:
    1. Exact normalized name match ("Rodrigo Jaen" → "Jaen, Rodrigo", case-insensitive)
    2. Reversed "Last First" form
    3. Derived username patterns from the OrgChart name: first-initial+last (e.g. "rjaen"), first-initial+middle-initial+last, first name only (if unambiguous), last name only (if unambiguous), email-prefix (strip domain and apply above rules)
    4. Known variations: strip punctuation/accents, handle Jr./Ph.D./initials suffixes
  - Collect ALL matched identities for a person as their aliases; unmatched identities appear as rows with empty name/manager
  - In all analysis scripts, load people.csv once at startup into a dict keyed by alias for O(1) identity resolution; never do per-row name matching in analysis code
  - The following are **known overrides** that cannot be resolved algorithmically — always apply these when generating people.csv:
    - "Evan Yu" → "Yu, Yiwen" (goes by English name Evan)
    - "Dimitar Christoff" → "Kodjabashev, Dimitar" (commits under different last name)
    - "Andy Smith" → "Smith, Andrew" (nickname)
    - "Jim Higson" → "Higson, James" (nickname)
    - "Ram Bobbala" → "Bobbala, Ramakrishna" (nickname)
    - "Tim Kang" → "Kang, Timothy" (nickname)
    - "shjain" → "Jain, Shreshthha" (username: first-2-chars + last)
    - "rahukumar" → "Kumar, Rahul" (username: first-name-truncated + last)
  - The following unmatched identities are confirmed to be the **same person** (not in OrgChart); merge into one aliases row:
    - "Satraj Sehmi" and "sat sehmi"

# Prep

Ensure the above raw data files exist, generating them by using git commands on the referenced repositories if they do not.
Report on whether they exist, summarizing the number of commits (i.e. the number of lines) in each file, and the date range covered.
If they don't exist, briefly summarize the process you will use to generate them, and then generate them.

Generate derived files if they don't exist. 
Re-generate any derived files whose dependencies have changed (e.g. if any of the commits files have changed, re-generate people.csv).

# Overview of Activity

To dev-activity.md generate:

- a table to show the activity of each project: 
  - prs
  - authors
  - prs/author (from prs files, matching by author and date range)
  - lines/pr (from prs files, matching by author and date range)
  - +lines/author
  - -lines/author
  - %test (average across commits)

- a table to show the activity of teams (grouping authors by team based on the manager/team mapping above):
  - prs
  - authors
  - prs/author
  - lines/pr (from prs files, matching by author and date range)
  - +lines/author
  - -lines/author
  - area (primary file type)
  - %test (average across commits)

- a table for each team (and a virtual team of unmatched authors) to show the activity if its members, sorted by +lines with columns:
  - author
  - title (derived from the OrgChart manager column)
  - +lines
  - -lines
  - area (primary file type)
  - +lines/day
  - %test (average across commits)
  - prs
  - lines/pr (from prs files, matching by author and date range)
Bold the name of the manager in each team table.

Using the cached jira content, create a section for "Jira Analysis" to dev-activity.md:
- a summary of the jira content by project, including number of defects, cycle time, and story points completed, grouping by sprint if that data is available.
- Summarize the length of the description by jira reporter to see if some reporters are writing more detailed descriptions than others.
- Summarize the complexity of the epics by the number of linked issues to see if some epics are more complex than others, and see how that varies by project.
- Summarize the reltionship between PR size and 
  - Jira story points if possible by matching PRs to jira tickets via the jira-link field and plotting PR size vs. story points for all matched PRs.
  - Description length (including description of the parent epic if applicable) by plotting PR size vs. description length for all matched PRs to qualify the relationship between ticket description detail and the size of the resulting code change. 
- Any other interesting observations or patterns about the jira by project and correlations between jira and PRs that might be relevant for management to understand the state of the projects and teams.

