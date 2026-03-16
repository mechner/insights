
# Questions and Inferences

## Questions

* **RFQ List section** — the old index had "RFQ List: Submission / Trading Options", "Negotiation Panel", and "Items Grid" as subfeatures. In the new scope-based structure, List submission uses the same RFQ Parameters Panel and Dealer Selection Panel as singles. Should there still be a separate "RFQ List" section for list-specific panel behaviors (e.g., Negotiation Panel during quoting, Items Grid), or are they subsumed?
* **Spreadsheet Upload** — Jira epic XRFQ-2381 ("Unsolicited RFQ") covers creating orders from a spreadsheet upload. Is "Spreadsheet Upload" the right feature name, or is there a better term?
* **My History placement** — should My History be a tab within Market Depth Panel (as in the AI-generated index) or a separate top-level feature under Single Order Scoped (as in the manual index)?
* **Disclosed Open Trading scope** — the Confluence page (5160665141, created 2026-03-16) describes a "Day 1" scope with several permissions deferred. Is this feature in scope for July, or later?

## Resolved Questions

*7 questions resolved in prior sessions (Countering, Direct HT, Targeted HT, Spot Negotiation, Trace/TRAX, Summary Ribbon vs List Analytics Panel, Parameters page xp1 content). All answers confirmed and recorded in knowledge.md.*

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
* **List Analytics Ribbon** ("Summary of Key Metrics") — the **Summary Ribbon** (compact single-row analytics bar above the AC grid) and the **List Analytics Panel** (separate grid with grouping/aggregation by side and other groupings) are two distinct features. The Ribbon file designs the persistent bar; the RFQ Micro-frontends MVP node 401:43176 designs the full Panel (out of scope for July). [web](https://www.figma.com/design/vQYE6xznZXiYBeDQFGWLlI/List-Analytics-Ribbon?node-id=3-8)
* **Auto-X** — ADX panel dedicated design file. [web](https://www.figma.com/design/tovFPT7H78xZ0SShVM02ux/Auto-X)
* **Process Trade Single Updates** — process trade workflow updates. [web](https://www.figma.com/design/veQkHiIYQdSvlguduea8UR/Process-Trade-Single-Updates)
* **RFQ Statuses** — inquiry status badge designs. [web](https://www.figma.com/design/HQAq0qmgWefd8b9JfgkxMk/RFQ-Statuses)

#### Additional Figma Files Explored (session 2)
* **Activity Console Functionality** (`CcpJ6jo6jiq1ascqoBfn4N`) — contains Global Search workflow (search collapsed → expanded → type → enter) and Empty States (no results, no results with filter). Enriches Filter Bar and adds Empty States as a common pattern.
* **Desktop Components** (`GRNFTbZpvkhIQdmaipUsEX`) — tab design system: three levels of tabs (Page/DockTabs with pop-out, Panel/DockTabs with reorder, Default/Mantine Tabs). Panel Container and Group Container components. Enriches Common Panel Tab Behavior.
* **Notifications & Alerts 2.0** (`4MgZjcHNNywWXOtQwAoQ1h`) — toast notification system with 5 types (Success, Error, Warning, Informative, User) in Default/Hover states. Actionable notifications with CTA buttons. Also has a Notification Center panel design. NEW feature added to index.
* **Open Trading Errors** (`2i2fmG1E226mvkolADhrhn`) — extensive error state designs for OT in list context ("All Orders - List with Error"). Cross-cutting concern for Activity Console and Open Trading features.
* **Loading States** (`LkCk1f2EOgKC0NH89kVSHy`) — empty file (no designs).
* **Bulk Action Bar Updates** (`CouTz2fR9nCGcmek7cUebd`) — cover page only (no designs).
* **Trade Ticket** standalone (`HOUfJChNoOTWgahm3jezFO`) — cover page only; real Trade Ticket designs are in RFQ MVP node 161:27675.
* **Market Depth** standalone (`3QWBnnFsZ8hmp2QHJrRbPb`) — cover page only; real Market Depth designs are in RFQ MVP node 113:12963.

### Confluence / Jira Cross-Check (2026-03-16)

**Supported Workflows page** (4022075525, v65): Rich authoritative source covering EU Price protocol workflows. Key topics with feature-index implications:
* **Dealer Selection complexity** — Filter on Inventory, line-by-line dealer selection, dealer inclusions/exclusions via FIX, dealer groups, Smart Select. All these are now part of the Dealer Selection Panel feature.
* **EU-specific response behaviors** — Trying to Trade (Subject → TRADE → 25s counterparty response), Tied Levels (sorting and multiple trade buttons), Partials. These belong in the Responses Panel feature.
* **Create List / Delist** — full workflow described; max 40 items; delist returns items as singles. Now under List Structure Operations.
* **Cancel / Pass** — detailed rules: cancel only pre-submission or live-without-levels; pass only submitted. These are Context Menu actions with business rules.
* **RTS on DNT** — auto-recreate RTS order when inquiry DNTs (requires LINX property). This is a system behavior, not a panel feature; belongs in process documentation.
* **Targeted RFQ** — EU default from "Default to Targeted RFQ (EU)" permission; EM from "Disable Targeted RFQ (EM)" permission. Enriches the Bilateral Counterparties sub-feature.
* **Smart Select** — AI-driven dealer selection, shown as dealer group option; uses BondLink Smart Select preferences. Added as sub-feature of Dealer Selection Panel.

**Disclosed Open Trading** — new Confluence page (5160665141, created 2026-03-16 by Omer Naseer). Describes Disclosed OT as a distinct workflow: disclosed inquiry to a dealer without a bilateral relationship, settling through MKTX. Has its own LINX permissions (AllowDisclosedOT, per-market-segment relationships). Jira epic XRFQ-2389 (PI27, At Risk). Figma node 233:41438 in RFQ MVP.

**Field Specifications & Validation Rules** — Confluence page (5065638683), child of Editable Inquiry Fields. Contains detailed per-field validation rules, LINX property mappings, and formatter specifications. Useful as source material when writing feature pages for RFQ Parameters Panel and Editable Inquiry Fields.

**Active Jira epics of note** (not yet reflected in index):
* XRFQ-2381: Unsolicited RFQ (PI27, At Risk) — spreadsheet upload for creating unsolicited orders
* XRFQ-4065: High Touch: Leave Order — interim until Order Manager GA; backlog
* XRFQ-5100/4991: Auto-Create List Functionality — parity with 1.0; backlog
* XRFQ-2382: Create, Share, Edit Dealer Groups — backlog
* XRFQ-2372: Historical Activity / Blotter — backlog
* XRFQ-2374: Instrument Search — backlog

