
# Questions and Inferences
This document contains questions and inferences made by the AI agent when generating or evaluating features in the feature catalog. These inferences are based on the information available in the various resources, and may include reconciliations of conflicting information, assumptions made to fill in gaps, and any other insights that the AI agent has generated. Questions should call out ambiguous or conflicting information that the AI agend it unsure how to resolve, and that should be clarified by a human expert. 

When generating or evaluating features, or analyzing resources for such purposes, the AI agent should capture any relevant inferences here, along with the reasoning behind them and any relevant context. This will help ensure consistent interpretation of source materials across sessions, and that any assumptions or reconciliations are transparent and can be reviewed by human experts.

When capturing questions or inferences, use the following format: 
* {summary} - a brief summary of the inference, question, or assumption
  * {Reasoning}: the reasoning process that led to this inference, including any relevant information from the resources or general background knowledge.

## Questions
* {start here}

## Inferences

### Figma Design References
The following Figma files and frames have been identified as likely authoritative sources for xp2 feature designs, based on exploring the MarketAxess Figma team. **Pending review and confirmation by the UX team.**

All designs explored are in the **MarketAxess** Figma team, under the **Activity Console 2.0** project: [web](https://www.figma.com/files/1279115914045676988/project/344298335)

#### Likely authoritative files

* **Activity Console Microfrontend** — AC left-hand panel: tabs, grids, row states, filters, context menus, empty states, summary tiles. [web](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend)
  * Pages to ignore: `Archive`, `Errors WIP`, `Components - Misc (To delete?)`
  * Key tab frames:
    * `All Orders` — all statuses mixed. [web](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=723-273460)
    * `Staged` — Staging status only. [web](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=824-248907)
    * `In Progress` — Ready (Buy Best/Sell Best) and Bin rows; single bonds have no inline response view. [web](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=830-285408)
    * `Spotting` — Awaiting Spot rows with Spot Now action. [web](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=917-65927)
    * `Done`. [web](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=917-67758)
    * `Auction Eligible`. [web](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=917-69864)
    * `EM` — Emerging Markets variant. [web](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=2329-150966)

* **Activity Console Prototype** — full-screen layouts showing left + right panels together in multiple states. Page 1 is primary. Note: some frames use xp1 workstation screenshots as background reference — not xp2 designs. [web](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype)
  * Key frames:
    * `Activity Console` — AC left panel, Staged tab; all order statuses; workflow status banner; Opportunities column; all Trade Types and action buttons. [web](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=1-91259)
    * `RFQ List` — US RFQ List in Quoting state; right panel is RFQ List Negotiation (progress, timer, Cancel). [web](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=5-221094)
    * `EU List` — EU List in Staging state; right panel is Trading Options (Protocol, Timer, Auto-X, Visibility, Counterparty Selection, Submit/Cancel). [web](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=18-32065)
    * `PT` — Portfolio List in Staging state; right panel is Submission (Trade type, Pricing, Timing, Protocol, Cross, Counterparty Selection, Submit). [web](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=1-146072)
    * `ADX` — Adaptive Auto-X panel; Summary by list + Parent bond grid; TAKE and SEEK actions. [web](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=19-29554)
    * `Details Panel//US RFQ` — Trade Ticket, Traded state; tabs: Details / Responses / Activity Log; collapsible sections: Pricing, Trade Proceeds, Instrument Details, Identifiers. [web](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=73-46108)
    * `Market Depth` — single bond pre-trade Market Depth / My History inline panel; Bid and Offer grids. [web](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=5-280945)
    * `List Analytics overlay` — floating List Analytics panel with analytics summary grid and distribution charts. [web](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=5-288880)
  * **Architectural inference — single-bond RFQ quoting state**: There appears to be no separate right-panel for a single bond during quoting. The order sits in In Progress (Bin → Ready); the trader uses Buy Best / Sell Best inline, or opens the Trade Ticket → Responses tab. Inferred from exhaustive exploration of all named frames in this file — none showed a single-bond live response grid.

#### Other files (Features project)
* **Trade Manager** — order takeover/reassignment workflow for the Trade Manager role. [web](https://www.figma.com/design/0cvRqbb7fVqoM5bs0HSLEJ/Trade-Manager)
* **Loading States** — component-level loading state designs. [web](https://www.figma.com/design/LkCk1f2EOgKC0NH89kVSHy)
* **Open Trading Errors** — error state designs for Open Trading flows. [web](https://www.figma.com/design/2i2fmG1E226mvkolADhrhn)

#### Files inferred as exploratory / lower priority
* **Activity Console Archive** (`DkzBNwEpm6iG1mORjVEOBr`) — archived/superseded designs.
* **Activity Console Microfrontend (Copy)** (`ojjH4kBpHTXnzqpcgzFtWR`) — working copy, not authoritative.
* **Dev Copy (25th July)** (`c2DUjtGFPA9IIpzAQcQL7c`) — dated dev copy, not authoritative.
* **Q1 release** (`hr0lbYZQxivu0qWY0vQzE2`) — release-scoped planning/notes; mixed with xp1 reference screenshots, not authoritative xp2 designs.