
# Feature Catalog Resources

When generating or evaluating features, make use of the following background information and resources.

WARNING: these resources include a mixture of correct "target state" and non-target-state information. See the prompt for principles on how to reconcile conflicting information, and ask for clarification if you are unsure about which information to prioritize or how to reconcile conflicts.

## Systems
The following systems are relevant to xp2 development and testing:
- **xp2**
    - Description: React-based web UI we are building to replace xp1 and integrate with bl via canonical api over kafka. **This is the system we are building, and that the feature catalog documents.**
    - Aliases: x-pro, xpro, RFQ ASAP, EU ASAP.
    - Repositories: @xpro-monorepo
- **xp1**
    - Description: A deprecated but in-production react-based web UI that integrates with bl using bl's JMS messages. It was poorly architected and implemented, and we are replacing xp1 with xp2.
    - Aliases: X-Pro 1, Kauai (xp1 rfq), Hawaii (xp1 PT), Maui. Note, in old documents, jiras, code, etc. xp1 may be called simply "xpro" or "x-pro" - but going forward we will call it xp1 to avoid confusion with xp2)
    - Repositories:
        - @bondlinkbridge-deployment
        - @hulk-api-srv
        - @hulk-commons
        - @kauai-vips
        - @maom-action-svc
        - @maom-commons
        - @maom-ui
        - @maom-ui-iac
        - @maom-subview-svc
- **bl**
    - Description: Our primary backend fixed income RFQ trading system. It is a monolith with a thick client **workstation** that xp2 will eventually replace.
    - Aliases: BondLink
    - Repositories: @bondlink
- **canon** (also **CanAPI**) is the "Canonical API," an API implemented as a set of schemas and kafka topics meant to decouple xp2 from bl idiosyncrasies and implementation details.
- **nuc**
    - Description: Our new sequencer-based trading system and platform. Currently only supports the MOC Auction, but will be extended over time to take over more of bl and other backend trading systems' responsibilities.
    - Aliases: Nulceus
    - Repositories: @Nucleus

The referenced code repositories can be found in the parent directory from the root of this project; you have permission to read them freely. 

## Figma Designs
Figma designs for xp2 are located in the MarketAxess Figma workspace across three projects:
* RFQ Panel: https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=118-4905
* Activity Console: https://www.figma.com/files/1279115914045676988/team/1613317744861427514
* XP2 Features: https://www.figma.com/files/1279115914045676988/project/488812420

## Legacy Resources
* CI Client Workflows: https://marketaxess.atlassian.net/wiki/spaces/CI/pages/1082032221/Client+Workflows

### Project: Activity Console 2.0
https://www.figma.com/files/1279115914045676988/project/344298335
* Activity Console Microfrontend (`Q4keHW9QtaM3adu9y6Nsjq`)
* Activity Console Prototype (`2q1qq3C53E0sqnqmgChTgw`)
* Activity Console Functionality (`CcpJ6jo6jiq1ascqoBfn4N`)
* Loading States (`LkCk1f2EOgKC0NH89kVSHy`)
* Open Trading Errors (`2i2fmG1E226mvkolADhrhn`)
* Non-authoritative (ignore): Activity Console Archive, Activity Console Microfrontend (Copy), Dev Copy (25th July), Q1 release

### Project: Features
https://www.figma.com/files/1279115914045676988/project/405813627
* **RFQ Micro-frontends - MVP** (`1BASLVXWRKMUzvPU23o3am`) — primary detailed design reference
* Market Depth (`3QWBnnFsZ8hmp2QHJrRbPb`)
* Desktop Components (`GRNFTbZpvkhIQdmaipUsEX`)
* Bulk Action Bar Updates (`CouTz2fR9nCGcmek7cUebd`)
* Notifications & Alerts 2.0 (`4MgZjcHNNywWXOtQwAoQ1h`)

### Project: (unnamed / project 488812420)
https://www.figma.com/files/1279115914045676988/project/488812420
* Auto-X (`tovFPT7H78xZ0SShVM02ux`)
* Countering (`LgGqkaz17hRBiyCwOMLDun`)
* Direct (HT) (`uLEut9g8NJEyB6tEuBB2jN`)
* List Analytics Ribbon (`vQYE6xznZXiYBeDQFGWLlI`)
* Process Trade Single Updates (`veQkHiIYQdSvlguduea8UR`)
* RFQ Statuses (`HQAq0qmgWefd8b9JfgkxMk`)
* Spot Negotiation (`EWt91nQV6zncWrO9PNmsQe`)
* Targeted (HT) (`RYefL603oPOdeldqcAaWlv`)
* Trace/TRAX (`dpD5uLu4D22Pc1xTNjchLr`)
* Trade Ticket (`HOUfJChNoOTWgahm3jezFO`)

See @inferences.md for detailed page-level descriptions and node IDs for each file.

## Test Cases
JSON files containing test cases for xp1 and xp2 can be found in @xpro-monorepo/ui/tools/testrail-fix-extractor.output. The summary file is in summary.json; it points to test case content in project subdirectories. 

## Jira
Access jira using MCP. The primary project for xp2 work is **XRFQ**.

## Confluence
Access confluence using MCP. 
Some key "source" pages that contain important information and documentation about xp2 include:
* A hand-written doc describing workflows supported in xp2: https://marketaxess.atlassian.net/wiki/spaces/XE/pages/4022075525/XPro+2.0+Supported+Workflows
* A glossary of terms: https://marketaxess.atlassian.net/wiki/x/dYACMwE

Some "Legacy" resources with background information: 
* CI Client Workflows (general BondLink/FIX and xp1, not specific to xp2): https://marketaxess.atlassian.net/wiki/spaces/CI/pages/1082032221/Client+Workflows

