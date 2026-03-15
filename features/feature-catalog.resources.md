
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
Figma designs for xp2 are located in the MarketAxess Figma workspace
**TODO**: fill in references for the primary figma designs 

## Test Cases
JSON files containing test cases for xp1 and xp2 can be found in @xpro-monorepo/ui/tools/testrail-fix-extractor.output. The summary file is in summary.json; it points to test case content in project subdirectories. 

## Jira
Access jira using MCP. The primary project for xp2 work is **XRFQ**.

## Confluence
Access confluence using MCP. 

The primary space for xp2 feature documentation is
https://marketaxess.atlassian.net/wiki/spaces/XE/folder/5007343617?atlOrigin=eyJpIjoiZDlmNTg2ZGIxZTYxNDQ0OTkxYzVhZjk0NzI0ZWNhNTQiLCJwIjoiYyJ9 

A glossary of terms can be found here:
https://marketaxess.atlassian.net/wiki/x/dYACMwE
