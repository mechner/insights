
# Questions and Inferences
This document contains questions and inferences made by the AI agent when generating or evaluating features in the feature catalog. These inferences are your "working hypothesis" based on the information available in the various resources, and may include reconciliations of conflicting information, assumptions made to fill in gaps, and any other insights that the AI agent has generated. Questions should call out ambiguous or conflicting information that the AI agend it unsure how to resolve, and that should be clarified by a human expert. 

When generating or evaluating features, or analyzing resources for such purposes, the AI agent should capture any relevant inferences here, along with the reasoning behind them and any relevant context. This will help ensure consistent interpretation of source materials across sessions, and that any assumptions or reconciliations are transparent and can be reviewed by human experts.

When capturing questions or inferences, use the following format: 
* {summary} - a brief summary of the inference, question, or assumption
  * {Reasoning}: the reasoning process that led to this inference, including any relevant information from the resources or general background knowledge.

## Questions

*All questions from the previous session have been resolved — see Resolved Questions below.*

## Resolved Questions
* **Countering** — confirmed as an optional sub-workflow within the Live response state: client proposes a less favorable price to a dealer. 3-step flow: hit Counter button → populate level field → submit counter. Shown inline in the Direct (HT) "Post-Submit: Live" design. *(Confirmed in knowledge.md)*
* **Direct (HT)** — a High Touch flow where the client targets a single pre-selected dealer, initiated from Market Depth by clicking a specific dealer's quote. Has its own complete lifecycle: Market Depth → Direct Modal → Bin (Awaiting Response) → Live (with optional Countering) → Done. *(Confirmed in knowledge.md)*
* **Targeted (HT)** — implemented as a "Targeted" toggle in the Inquiry Parameters form; when ON, a dealer selection widget appears. The AC order row shows a Targeted indicator tag. Not a separate submission flow — it is a variant within the standard parameters form. *(Confirmed in knowledge.md)*
* **Spot Negotiation** — in scope. The Figma file "Spot Negotiation" is actually titled "Amend, Spotting, Spot Negotiation" covering three related post-submission workflows. Ready for Dev page is empty; designs are in High Fidelity pages. *(Confirmed in knowledge.md)*
* **Trace/TRAX** — in scope. Figma subtitle is "Global RFQ" suggesting it covers last-print/pre-trade data display in the RFQ context. Design V2 (node 4:21) is the current design. *(Confirmed in knowledge.md)*
* **Summary Ribbon vs List Analytics Panel** — List Analytics Ribbon design shows a persistent summary bar (the Ribbon) with an expandable "List Analytics" section below it, confirming knowledge.md note that the Panel is likely a tab/expandable within the Ribbon context. *(Partially confirmed — further exploration needed to finalize feature boundary)*
* **Parameters page xp1 content** — all content in node 0:1 of RFQ Micro-frontends MVP is xp2. *(Confirmed in knowledge.md)*

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

#### Other files (Features project and project 488812420)
* **Trade Manager** — order takeover/reassignment workflow for the Trade Manager role. [web](https://www.figma.com/design/0cvRqbb7fVqoM5bs0HSLEJ/Trade-Manager)
* **Loading States** — component-level loading state designs. [web](https://www.figma.com/design/LkCk1f2EOgKC0NH89kVSHy)
* **Open Trading Errors** — error state designs for Open Trading flows. [web](https://www.figma.com/design/2i2fmG1E226mvkolADhrhn)
* **Direct (HT)** — High Touch Direct RFQ lifecycle (pre-submit via Market Depth → Direct Modal → bin → live → done). Ready for Dev page is authoritative (node 3:8); High Fidelity → Q2 Release (node 4:20). Contains Countering sub-flow inline. [web](https://www.figma.com/design/uLEut9g8NJEyB6tEuBB2jN/Direct-(HT)?node-id=3-8)
* **Countering** — Counter-quote workflow. Ready for Dev page (node 3:8) is empty; use High Fidelity → Version 1 (node 4:20, popover) and Version 2 (node 4523:106571, inline). [web](https://www.figma.com/design/LgGqkaz17hRBiyCwOMLDun/Countering)
* **Targeted (HT)** — Targeted RFQ toggle and dealer selection in Inquiry Parameters. Ready for Dev (node 3:8) has designs; also High Fidelity Version 1 (node 4:20) and Version 2 (node 6212:94296). WIP. [web](https://www.figma.com/design/RYefL603oPOdeldqcAaWlv/Targeted-(HT)?node-id=3-8)
* **Spot Negotiation** ("Amend, Spotting, Spot Negotiation") — covers three related post-submission workflows: Amend inquiry, Spotting (Awaiting Spot state), and Spot Negotiation (FX rate agreement). Ready for Dev page (node 3:8) is empty; use High Fidelity Version 1 (node 4:20) and Version 2 (node 4:21). [web](https://www.figma.com/design/EWt91nQV6zncWrO9PNmsQe/Spot-Negotiation)
* **Trace/TRAX** ("Global RFQ") — pre-trade last print / recent trade data display in the RFQ context. Design V2 (node 4:21) is current. [web](https://www.figma.com/design/dpD5uLu4D22Pc1xTNjchLr/Trace-TRAX?node-id=4-21)
* **List Analytics Ribbon** ("Summary of Key Metrics") — persistent summary bar above AC grid; "List Analytics" appears as an expandable section/tab below it. WIP (no date). Ready for Dev Version 1 (node 3:8) and Version 2 (node 8220:52453). [web](https://www.figma.com/design/vQYE6xznZXiYBeDQFGWLlI/List-Analytics-Ribbon?node-id=3-8)
* **Auto-X** — ADX panel dedicated design file. [web](https://www.figma.com/design/tovFPT7H78xZ0SShVM02ux/Auto-X)
* **Process Trade Single Updates** — process trade workflow updates. [web](https://www.figma.com/design/veQkHiIYQdSvlguduea8UR/Process-Trade-Single-Updates)
* **RFQ Statuses** — inquiry status badge designs. [web](https://www.figma.com/design/HQAq0qmgWefd8b9JfgkxMk/RFQ-Statuses)

