
## git rules
* Never commit without my explicit instruction - I want to be able to review your changes and commit them only if I like them, otherwise to revert them. If you commit to git I lose that option. 

## Project structure knowledge
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

## Figma API Access

Credentials are stored in `~/.copilot/figma.env`:
FIGMA_TOKEN=<personal_access_token>

**API access rules:**
- Prefer MCP tools (figma-*) for screenshots, design context, metadata, and variable definitions
- Fall back to REST API via `curl` for operations MCP doesn't support (e.g., listing files in a project, listing pages in a file)
- When using curl: `source ~/.copilot/figma.env && curl -s -H "X-Figma-Token: $FIGMA_TOKEN" <url>`
- REST API rate-limits aggressively (429s) — prefer MCP tools where possible
- Node IDs in URLs use `-` (e.g. `118-4905`) but MCP tools require `:` format (`118:4905`)

## Jira / Confluence API Access

Credentials are stored in `~/.copilot/atlassian.env`:
ATLASSIAN_EMAIL=dmechner@marketaxess.com
ATLASSIAN_TOKEN=<api_token>

If the token is expired (you'll get 401), direct the user to https://id.atlassian.com/manage-profile/security/api-tokens to regenerate it and overwrite the file.

**Cloud ID**: `2bf67ec3-0d65-4824-b963-7308181bfea7` (marketaxess.atlassian.net)

**API access rules:**
- Prefer MCP tools (atlassian-*) for Jira and Confluence access. Fall back to `curl` only when MCP tools don't support the needed operation.
- When using curl, use `-u "$ATLASSIAN_EMAIL:$ATLASSIAN_TOKEN"` for auth; always `source ~/.copilot/atlassian.env` first
- Python's `urllib` fails due to a corporate SSL CA cert issue — use curl for HTTP fallbacks, not Python
- The old `GET /rest/api/3/search` is **deprecated (410)**; use `POST /rest/api/3/search/jql` instead
- The new search endpoint uses **cursor-based pagination** (`nextPageToken`) and does **not** return a `total` count; paginate until `isLast == true`
- Fetch individual issues via: `GET /rest/api/3/issue/{KEY}?fields=...`

**Useful JQL fields** (request by name): `summary`, `issuetype`, `status`, `priority`, `assignee`, `reporter`, `created`, `updated`, `description`, `comment`, `parent`, `resolution`, `resolutiondate`, `labels`, `fixVersions`, `issuelinks`, `subtasks`, `customfield_10014` (Epic Link), `customfield_10016` (Story point estimate), `customfield_10021` (Sprint), `customfield_10026` (Story Points)

## TestRail API Access

Credentials are stored in `~/.copilot/testrail.env`:
TESTRAIL_EMAIL=dmechner@marketaxess.com
TESTRAIL_TOKEN=<api_token>

**Base URL**: `http://crpashtr01/testrail/index.php?/api/v2/`

**API access rules:**
- Use `curl` with `--user "$TESTRAIL_EMAIL:$TESTRAIL_TOKEN"` for auth; always `source ~/.copilot/testrail.env` first
- Add `-H "Content-Type: application/json"` to all requests
