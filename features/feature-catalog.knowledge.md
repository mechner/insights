
# Background and Resources

When generating or evaluating features, you should incorporate the following background information and resources.

# Systems
We will refer to several systems in this prompt:
- **xp2** 
  - Description: React-based web UI we are building to replace xp1 and integrate with bl via canonical api over kafka. 
  - Aliases: x-pro, xpro
  - Repositories: @xpro-monorepo
- **xp1** 
  - Description: A deprecated but in-production react-based web UI that integrates with bl via its native JMS messages. It was poorly architected and implemented, and we are replacing xp1 with xp2.
  - Aliases: X-Pro 1
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
  - Description: Our primary backend trading system. It is a monolith with a thick client **workstation** that xp2 will eventually replace.   
  - Aliases: BondLink
  - Repositories: @bondlink
- **nuc**
  - Description: Our new sequencer-based trading platform and system. Currently only supports the MOC Auction, but will be extended over time to take over more of bl and other systems' responsibilities.  
- **canon** (also **CanAPI**) is the "Canonical API," a set of schemas and kafka topics that we are defining to decouple xp2 from bl idiosyncrasies and implementation details.

## Figma Designs


## Reconciliation across Systems

There is much valuable information


Content from bl should be used with care; while it reflects the ground truth of our RFQ trading product, it contains many naming, concept, and implementation idiosyncrasies that we do not want to propagate into xp2.

We are building canon to decouple xp2 from bl's idiosyncrasies and implementation details, and to enable us to eventually replace bl if we want to.

## Source Code
The above systems' source code lives in the following git repositories:
- xp2: @xpro-monorepo
- bl: @bondlink
- canon: @
