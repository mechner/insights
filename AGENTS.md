

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

## TestRail API Access

Credentials are stored in `~/.copilot/testrail.env`:
TESTRAIL_EMAIL=dmechner@marketaxess.com
TESTRAIL_TOKEN=<api_token>

**Base URL**: `http://crpashtr01/testrail/index.php?/api/v2/`

**API access rules:**
- Use `curl` with `--user "$TESTRAIL_EMAIL:$TESTRAIL_TOKEN"` for auth; always `source ~/.copilot/testrail.env` first
- Add `-H "Content-Type: application/json"` to all requests
