
**This is a hand-generated index of features. AI do not modify without explicit human approval.**

## Common Grid Components
* Filter Bar - top-of-grid filter bar providing quicksearch and column filters
* ((Column selection, other options behind vertical dots button))
* Selection - checkbox row selection behavior and appearance
* Common Renderers - a description of common renderers used cross 

## Common Panel Features  
* Common Panel Tab Behavior - standard behavior for dragging, arranging, and sizing tabs

## Single Order or Bond Scoped Features
* Market Depth Panel - displays two-sided market data: axes, inventory, and CP+ for a given instrument
* Responses Panel - displays the responses to an RFQ, with state-dependent actions
* Trade Ticket Panel - displays the details of a completed trade, including pricing and proceeds
* Activity Log Panel - displays a detailed audit trail of all activity related to a given RFQ
* My History - displays the user's own trade and inquiry history for a given instrument
* Single Item Panel Header - summarizes an order, its current state, and provides action buttons

## List or Multi-Order Scoped Features
* Summary Ribbon - a compact horizontal list or multi-item selection analytics summary
* List Panel Header - summarizes list items, their current state, and provides list action buttons

## Single/List Combined Scoped Features
* RFQ Parameters Panel - a panel for configuring RFQ parameters
  * Single/List Overrides - where list level parameters are overridden for an individual item
* Dealer Selection Panel - a panel for selecting 
  * Open Trading (Anonymous) 
  * Disclosed OT counterparties
  * Bilateral Counterparties - 

* Not Yet In Scope?
* List Analytics Panel
* **Parameters** (node 0:1) — Inquiry parameter form variants (List, List+single-selected, Single, Error states); counterparty picker; date controls; EU RFQ variant. **Note: contains xp1 reference screenshots — treat as background only; use sub-pages for authoritative detail.** [web](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=0-1)
  * **Open Trading** (659:88942) — Open Trading variant of parameters
  * **Disclosed OT** (1853:529776) — Disclosed Open Trading counterparty selection
  * **Disclosed Counterparties** (5:5540) — Disclosed CP selection widget
  * **Auto-X (WIP)** (1994:143667) — Auto-X parameter variant
* **List Analytics** (node 401:43176) — Floating List Analytics panel with summary grid and distribution charts; also shows the Summary Ribbon context. [web](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=401-43176)
* **Context Menus** (node 2858:628994) — Column settings menu + order-level context menus for Single bond, Staged, and In Progress row states; options include: Edit, Cancel, Pass, New ADQ, Open in new tab, Copy ISIN/identifiers, Column settings, Export to Excel, Counter, Orders sub-menu. [web](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=2858-628994)
* **Modals** (node 820:53018) — Full modal dialog inventory: Rename list, Add items to list, Remove items, Trade confirmation (with partials warning), Buy partial order, Amend order, Choose spot time, Update limit levels; validation warning modals: Limit worse than Limit, Not the best level, Negative Spread/Yield, 2 Warnings combined, Error example. [web](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=820-53018)
* **Tooltips (Errors + Warnings)** (node 1703:136075) — Inline validation tooltip designs: warning (yellow) for minimum increment and amount outstanding; error (red) for required fields and non-standard settlement date. [web](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=1703-136075)
* **Headers** (node 41:14118) — Panel header component designs.
* **EM** (node 2471:16551) — Emerging Markets variants (out of scope per prompt).
