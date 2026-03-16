
# Questions and Inferences
This document contains questions and inferences made by the AI agent when generating or evaluating features in the feature catalog. These inferences are your "working hypothesis" based on the information available in the various resources, and may include reconciliations of conflicting information, assumptions made to fill in gaps, and any other insights that the AI agent has generated. Questions should call out ambiguous or conflicting information that the AI agend it unsure how to resolve, and that should be clarified by a human expert. 

When generating or evaluating features, or analyzing resources for such purposes, the AI agent should capture any relevant inferences here, along with the reasoning behind them and any relevant context. This will help ensure consistent interpretation of source materials across sessions, and that any assumptions or reconciliations are transparent and can be reviewed by human experts.

When capturing questions or inferences, use the following format: 
* {summary} - a brief summary of the inference, question, or assumption
  * {Reasoning}: the reasoning process that led to this inference, including any relevant information from the resources or general background knowledge.

## Questions
* **Is "Countering" a separate feature from Trade Ticket responses?** A dedicated Figma file "Countering" exists in project 488812420. Is this a distinct workflow (trader counter-quoting a dealer response) that should be its own index entry, or is it a sub-feature of Trade Ticket: Responses?
* **What are "Direct (HT)" and "Targeted (HT)"?** Two Figma files in project 488812420 suggest High Touch variants of Direct and Targeted RFQ. Are these distinct features from the current "Direct RFQ" entry, or design variants of the same feature?
* **Is "Spot Negotiation" in scope?** A Figma file exists for Spot Negotiation (project 488812420) and the AC has a "Spotting" tab. Is the spot negotiation workflow (agreeing on the FX spot rate) in scope for the feature catalog?
* **Is "Trace/TRAX" in scope?** A Figma file "Trace/TRAX" exists in project 488812420. Is trade reporting/TRACE display in scope?
* **Summary Ribbon vs List Analytics Panel — are these one feature or two?** The Figma file has separate pages for "Summary Ribbon" and "List Analytics" and a dedicated "List Analytics Ribbon" file exists in project 488812420. Should these be two separate index entries?
* **Parameters page xp1 content** — The Parameters page in RFQ Micro-frontends contains xp1 reference screenshots alongside xp2 designs. The sub-pages (Open Trading, Disclosed CPs, etc.) appear to be the authoritative xp2 content. Needs UX team confirmation on which sections are target state.

## Inferences

### Figma Design References
The following Figma files and frames have been identified as likely authoritative sources for xp2 feature designs, based on exploring the MarketAxess Figma team. **Pending review and confirmation by the UX team.**

All designs explored are in the **MarketAxess** Figma team, under the **Activity Console 2.0** project: [web](https://www.figma.com/files/1279115914045676988/project/344298335)

#### Primary authoritative file — RFQ micro-frontend

* **RFQ Micro-frontends - MVP** — the primary detailed design reference for the RFQ right-hand panel and related components. Located in the **Features** project (405813627). [web](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP)
  * **RFQ Panel** (node 118:4905) — List and Single bond panel states with Filters section; multiple workflow states. [web](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=118-4905)
  * **Parameters** (node 0:1) — Inquiry parameter form variants (List, List+single-selected, Single, Error states); counterparty picker; date controls; EU RFQ variant. **Note: contains xp1 reference screenshots — treat as background only; use sub-pages for authoritative detail.** [web](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=0-1)
    * **Open Trading** (659:88942) — Open Trading variant of parameters
    * **Disclosed OT** (1853:529776) — Disclosed Open Trading counterparty selection
    * **Disclosed Counterparties** (5:5540) — Disclosed CP selection widget
    * **Auto-X (WIP)** (1994:143667) — Auto-X parameter variant
  * **Responses** (node 111:11298) — Full response grid with many state variants: empty, live bids/offers, expired timer, with Buy/Counter/Pass buttons, Open Trading variants. [web](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=111-11298)
  * **Trade Ticket** (node 161:27675) — Trade Ticket detail panel: Default and EM variants; sections: Overview, Instrument Details, Pricing, Trade Proceeds. [web](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=161-27675)
  * **Activity Log** (node 161:38809) — Timestamped free-text audit trail entries (bond details, price, counterparty accepted). [web](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=161-38809)
  * **Market Depth** (node 113:12963) — Bid/Offer depth grid with: pre-trade summary header bar (Tradability, best pre-trade levels with Axe badges, axed size Buyers/Sellers, pre-trade depth, CP+, last print); grid columns: Direct, Source, Type, Cpty, Qty(M), Yield, Spread; type filter (Axe/Algo/MKT/QTE/CP+); Focus on toggle. [web](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=113-12963)
  * **My History** (node 925:70063) — User's own trade/inquiry history for this security; columns: My Action, Formatted Size, Trade Level, Best Level, Price, Cpty, Depth, Status, Trader, Company, Date; same pre-trade summary header bar as Market Depth. [web](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=925-70063)
  * **Summary Ribbon** (node 1283:31123) — Compact horizontal analytics bar embedded above the AC grid (distinct from the floating List Analytics panel). [web](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=1283-31123)
  * **List Analytics** (node 401:43176) — Floating List Analytics panel with summary grid and distribution charts; also shows the Summary Ribbon context. [web](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=401-43176)
  * **Context Menus** (node 2858:628994) — Column settings menu + order-level context menus for Single bond, Staged, and In Progress row states; options include: Edit, Cancel, Pass, New ADQ, Open in new tab, Copy ISIN/identifiers, Column settings, Export to Excel, Counter, Orders sub-menu. [web](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=2858-628994)
  * **Modals** (node 820:53018) — Full modal dialog inventory: Rename list, Add items to list, Remove items, Trade confirmation (with partials warning), Buy partial order, Amend order, Choose spot time, Update limit levels; validation warning modals: Limit worse than Limit, Not the best level, Negative Spread/Yield, 2 Warnings combined, Error example. [web](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=820-53018)
  * **Tooltips (Errors + Warnings)** (node 1703:136075) — Inline validation tooltip designs: warning (yellow) for minimum increment and amount outstanding; error (red) for required fields and non-standard settlement date. [web](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=1703-136075)
  * **Headers** (node 41:14118) — Panel header component designs.
  * **EM** (node 2471:16551) — Emerging Markets variants (out of scope per prompt).

#### Likely authoritative files — Activity Console

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
    * `ADX` — Adaptive Auto-X panel; Summary section with view tabs (List / Product / Side / Liq Score) + Parent bond grid with filter tabs (All / Eligible / Take Eligible); TAKE and SEEK actions. [web](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=19-29554)
    * `Details Panel//US RFQ` — Trade Ticket, Traded state; tabs: Details / Responses / Activity Log; collapsible sections: Pricing, Trade Proceeds, Instrument Details, Identifiers. [web](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=73-46108)
    * `Market Depth` — single bond pre-trade Market Depth / My History inline panel; tabs: Market Depth (Bid/Offer depth grid with Axe/Algo/CP+ source types, Focus on Price/Spread/Yield filter, Show All/Axe/+ filter) and My History. [web](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=5-288880) *(corrected — was 5-280945 in prior session)*
    * `List Analytics overlay` — floating List Analytics panel; analytics summary grid (YTW, VWAP, DWAS, Duration, DV01, Tradability) with pricing mode selector tabs (CP+ / CP+ Close / Ref Limit / Near-touch / Mid / Far-touch) plus distribution histograms. [web](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=5-280945) *(corrected — was 5-288880 in prior session)*
  * **Architectural inference — single-bond RFQ quoting state**: There appears to be no separate right-panel for a single bond during quoting. The order sits in In Progress (Bin → Ready); the trader uses Buy Best / Sell Best inline, or opens the Trade Ticket → Responses tab. Inferred from exhaustive exploration of all named frames in this file — none showed a single-bond live response grid.
  * **Trade Manager tab structure**: The Trade Manager design (node 2082:38879 in file 0cvRqbb7fVqoM5bs0HSLEJ) uses the same Activity Console tabstrip as the standard AC — no additional TM-specific tabs. TM adds a "Traders: Mine / Desk" quick-filter toggle and extra columns (Counterparty, Best Level, Auction Eligible, Trader) to the AC grid.

#### Other files (Features project)
* **Trade Manager** — order takeover/reassignment workflow for the Trade Manager role. [web](https://www.figma.com/design/0cvRqbb7fVqoM5bs0HSLEJ/Trade-Manager)
* **Loading States** — component-level loading state designs. [web](https://www.figma.com/design/LkCk1f2EOgKC0NH89kVSHy)
* **Open Trading Errors** — error state designs for Open Trading flows. [web](https://www.figma.com/design/2i2fmG1E226mvkolADhrhn)

