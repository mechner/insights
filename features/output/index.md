
# X-Pro 2.0 Feature Catalog Index

**Scope**: EU and US RFQ, and common components only. Auctions/MOC, Nucleus, PT, ADX, Rates, EM, Munis are out of scope.

Links: [Figma] refers to the primary design frame. [Confluence] means a feature page already exists there.

---

## Common Components or Features
* **Application Shell and Nav Bar** — outer application frame, navigation, and app switching
* **Tooltips** — standard tooltip for errors and warnings · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=1703-136075)
* **Toast Notifications** — toast notifications with multiple severity levels and actionable variants · [Figma](https://www.figma.com/design/4MgZjcHNNywWXOtQwAoQ1h/Notifications-Alerts-2.0)
* **Common Panel Tab Behavior** — standard behavior for dragging, arranging, and sizing tabs with the three tab levels · [Figma](https://www.figma.com/design/GRNFTbZpvkhIQdmaipUsEX/Desktop-Components)
* **Workspace Layout Persistence** — saving and restoring panel sizes, column widths, and tab selection across sessions · [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5132877825)
* **Panel Popout** — ability to pop out panels into separate windows **(WIP - Not for July)**
* **Notifications Center** — notification center for displaying alerts, with actionable variants **(WIP - Not for July)**
* **User Preference Framework** - framework for user preferences and settings, including persistence and application across features **(WIP - Not for July)**

## Common Grid Components
* **Filter Bar** — top-of-grid filter bar providing column filters and "global" search · [Figma](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=985-92867) · [Figma: Global Search](https://www.figma.com/design/CcpJ6jo6jiq1ascqoBfn4N/Activity-Console-Functionality?node-id=23-43424)
* **Grid Column Selection Panel** — panel for configuring which columns are displayed and in what order
* **Common Grid Behavior**
  * **Row Selection** — checkbox row selection behavior and appearance
  * **Sorting** — clicking column header to sort ascending/descending
  * **Column selection panel** — to configure which columns are displayed in the grid and where
  * **Resizing and Reordering** — allowing users to persistently resize and reorder columns by dragging
* **Common Renderers** — shared cell renderers used across AC and panel grids · [Figma](https://www.figma.com/design/HQAq0qmgWefd8b9JfgkxMk/RFQ-Statuses)
  * **Status Badge** — icon + colored label per inquiry status · [Figma](https://www.figma.com/design/HQAq0qmgWefd8b9JfgkxMk/RFQ-Statuses)
  * **Timer** — countdown timer with color-coded background and timer description text
  * **Direction Indicator** — colored letter badge for B, S or B/S
  * **Level Formatter** — renders based on level type (prefix) and product market convention (decimals)
  * **Date/Time Formatter** — ((tbd))
  * **Size Formatter** — formatted quantity numbers in 000s with comma separators
  * **Auction Eligible Flag** — bell icon indicator for auction-eligible orders
* **Auto-X Column** — Auto-X eligibility and enablement toggle and detail
* **Auto-X Expandable Column Section** — expandable column section for Auto-X related columns

## Activity Console
* **Activity Console** — the left-hand order-list microfrontend assembly
* **Tab Bar & Navigation** — workflow-stage tabs with live counts · [Figma](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=989-30898)
* **Order Grid — Single Bond Row** — per-row field layout, status badge, inline action buttons, and state-dependent rendering · [Figma](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=723-273460)
* **Order Grid — List / Basket Row** — expandable list-level row with child-bond expansion and aggregate status · [Figma](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=723-273460)
* **Workflow Status Banner** — Staged / In Progress / Done summary counts above the grid · [Figma](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=1-91259)
* **Summary Tiles / Metrics Bar** — per-tab aggregate metrics above the order grid · [Figma](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=989-30781)
* **Bulk Action Bar** — bulk-action bar for multi-selected orders · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=2858-628994)
* **Single Item Action Button** - state-dependent action button (e.g. Submit, Buy Best, etc.)
* **Opportunities Column** — inline opportunity icon and action buttons · [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5128355882)
* **Trade Type Column** — protocol label with icon
* **Trade Manager** — ownership filtered views (Mine / Others / All) and order takeover actions · [Figma](https://www.figma.com/design/0cvRqbb7fVqoM5bs0HSLEJ/Trade-Manager) · [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5087100951)
* **List Structure Operations** — create list from selected singles, or move selected items from a list 

## Instrument Context Features
* **Market Depth Panel** — two-sided pre-trade market data panel: axes, inventory, and CP+ for a given instrument · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=113-12963)
* **My History Panel** — user's own prior trades and inquiries for this security · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=925-70063)
* **Trace/TRAX** — pre-trade last-print and recent trade data display for a bond in the global RFQ context · [Figma](https://www.figma.com/design/dpD5uLu4D22Pc1xTNjchLr/Trace-TRAX?node-id=4-21)

## Single Order Context Features
* **Single Order Panel Header** — summarizes order terms, state, and provides action buttons
* **Responses Panel** — live dealer response grid with state-dependent actions · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=111-11298)
* **Trade Ticket Panel** — post-trade summary with collapsible detail sections · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=161-27675)
* **Activity Log Panel** — chronological audit trail of all events on an inquiry · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=161-38809)
* **Single Order Panel** — rhs assembly for a single order context

## Multi-Order Context Features
* **List Panel Header** — summarizes list items, their current state, and provides list action buttons
* **Analytics Ribbon** — compact horizontal list analytics summary · [Figma](https://www.figma.com/design/vQYE6xznZXiYBeDQFGWLlI/List-Analytics-Ribbon?node-id=3-8) · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=1283-31123)
* **List Items Grid** — displays the items in a list with key fields and inline actions
* **List Analytics Panel** aggregation grid with key analytics by side, pricing modes, and distribution charts *(WIP - Not for July)* · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=401-43176)
* **Order List Panel** — rhs assembly for a multi-order (list) context

## Single/List Context Features
* **RFQ Parameters Panel** — panel for configuring RFQ parameters before submission · [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5022548145) · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=0-1)
* **Dealer Selection Panel** — panel for selecting counterparties to receive an inquiry · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=5-5540)
  * **Disclosed Cptys** — disclosed dealer selection; dealer groups; Targeted RFQ toggle · [Figma](https://www.figma.com/design/RYefL603oPOdeldqcAaWlv/Targeted-(HT)?node-id=3-8)
  * **Open Trading** — anonymous counterparty selection via visibility groups
  * **Disclosed Open Trading** — disclosed inquiry to dealers without a bilateral relationship, settling through MKTX · [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5160665141)
  * **Smart Select** — AI-driven dealer selection based on inquiry parameters; shown as a dealer group option
  * **Restricted Dealer Selection** — rules and UI for excluding specific dealers · [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5149294649)
* **List Item Override** — overriding list-level parameters or dealer selection for individual item
* **Countering Workflow** — optional counter-quote: trader proposes a level to a dealer · [Figma](https://www.figma.com/design/LgGqkaz17hRBiyCwOMLDun/Countering)
* **Spot Negotiation** — Amend Inquiry, Spotting (Awaiting Spot state), and FX spot rate negotiation for cross-currency trades · [Figma](https://www.figma.com/design/EWt91nQV6zncWrO9PNmsQe/Spot-Negotiation)
* **Process Trades** — workflow for booking a pre-negotiated trade · [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5027496006)
* **Editable Inquiry Fields** — rules governing which inquiry fields are editable after submission and under what conditions · [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5028380695)
* **Direct (HT)** — High Touch direct flow: client initiates from Market Depth targeting a single dealer · [Figma](https://www.figma.com/design/uLEut9g8NJEyB6tEuBB2jN/Direct-(HT)?node-id=3-8)
* **Spreadsheet Upload** — creating unsolicited orders from a spreadsheet
