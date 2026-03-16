
# X-Pro 2.0 Feature Catalog Index

**Scope**: EU and US RFQ, and common components only. Auctions/MOC, Nucleus, PT, Rates, EM, and Munis are out of scope.

Links: [Figma] refers to the primary design frame. [Confluence] means a feature page already exists there.

---

## Activity Console
*[Figma: AC Microfrontend](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend) · [Figma: AC Prototype](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=1-91259)*

* **Activity Console** — the left-hand order-list microfrontend: overall layout, panel lifecycle, and tab structure
  * **Tab Bar & Navigation** — tab set (All Orders, Staged, In Progress, Spotting, Done, Auto-X, Auction Eligible) with live counts and pop-out support · [Figma](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=989-30898)
  * **Order Grid — Single Bond Row** — per-row field layout, status badge, inline action buttons, and state-dependent rendering for single-bond inquiries · [Figma](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=723-273460)
  * **Order Grid — List / Basket Row** — expandable list-level row with child-bond expansion, list-level fields, and aggregate status · [Figma](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=723-273460)
  * **Workflow Status Banner** — Staged / In Progress / Done summary counts displayed above the grid · [Figma](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=1-91259)
  * **Summary Tiles / Metrics Bar** — per-tab aggregate metrics displayed above the order grid · [Figma](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=989-30781)
  * **Filters & Search** — filter panel and keyword search with result count display · [Figma](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=985-92867)
  * **Context Menus & Row Actions** — per-row overflow menu (Edit, Cancel, Pass, New ADQ, Open in new tab, Copy ISIN/identifiers, Export to Excel, Counter, Orders) and bulk-action bar for multi-selected orders · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=2858-628994)
  * **Opportunities Column** — inline axe and AI-Select opportunity hints on AC order rows · [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5128355882)

## Pre-Trade Intelligence

* **Market Depth Panel** — inline single-bond pre-trade panel; pre-trade summary header (Tradability, best pre-trade levels, axed size, pre-trade depth, CP+, last print); toggles between depth view and trade history · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=113-12963)
  * **Market Depth tab** — live Bid/Offer depth grid by source (Axe, Algo, MKT, QTE, CP+); columns: Direct, Source, Type, Cpty, Qty(M), Yield, Spread; Type filter; Focus on toggle (Price / Spread / Yield)
  * **My History tab** — user's own prior trades and inquiries for this security; columns: My Action, Formatted Size, Trade Level, Best Level, Price, Cpty, Depth, Status, Trader, Company, Date · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=925-70063)
* **Summary Ribbon** — persistent compact single-row analytics bar above the AC grid showing key list metrics (e.g. Tradability, best levels, DV01) · [Figma](https://www.figma.com/design/vQYE6xznZXiYBeDQFGWLlI/List-Analytics-Ribbon?node-id=3-8) · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=1283-31123)
* **List Analytics Panel** *(out of scope for July)* — separate panel displaying an aggregation grid grouped by side (and other groupings) with YTW, VWAP, DWAS, Duration, DV01, Tradability; pricing mode selector (CP+ | CP+ Close | Ref Limit | Near-touch | Mid | Far-touch) and distribution charts · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=401-43176)
* **Trace/TRAX** — pre-trade last-print and recent trade data display for a bond in the global RFQ context · [Figma](https://www.figma.com/design/dpD5uLu4D22Pc1xTNjchLr/Trace-TRAX?node-id=4-21)

## RFQ — Single Bond

* **Direct RFQ** — the right-panel for a standard single-bond inquiry from submission through traded state · [Confluence (wip)](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5155815530) · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=118-4905)
  * **Inquiry Parameters** — submission form: all input fields, defaults, and validation rules; includes Targeted toggle + dealer selection widget when Targeted is ON · [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5022548145) · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=0-1)
  * **Trade Ticket: Responses** — live dealer response grid (Responses tab); Buy Best / Sell Best actions; counter-quote flow · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=111-11298)
    * **Countering** — optional counter-quote: trader proposes a less favorable level to a dealer; 3-step flow: hit Counter → populate level field → submit · [Figma](https://www.figma.com/design/LgGqkaz17hRBiyCwOMLDun/Countering)
  * **Trade Ticket: Details** — post-trade summary tab with collapsible sections: Pricing, Trade Proceeds, Instrument Details, Identifiers · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=161-27675)
  * **Trade Ticket: Activity Log** — chronological audit trail of all events on an inquiry · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=161-38809)
* **Direct (HT)** — High Touch direct flow: client initiates from Market Depth by clicking a specific dealer; lifecycle: Market Depth → Direct Modal → Bin (awaiting response) → Live (with optional Countering) → Done · [Figma](https://www.figma.com/design/uLEut9g8NJEyB6tEuBB2jN/Direct-(HT)?node-id=3-8)
* **Process Trades** — workflow for executing a trade: selecting a response, confirming, and completing settlement · [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5027496006)
  * **Trade at Best** — one-click best-response execution: eligibility rules, behavior, and confirmation · [Confluence (wip)](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5149294689)
* **Editable Inquiry Fields** — rules governing which inquiry fields are editable after submission and under what conditions · [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5028380695)

## Spot Negotiation

* **Amend Inquiry** — modifying inquiry parameters (level, settlement date) for an in-flight order · [Figma](https://www.figma.com/design/EWt91nQV6zncWrO9PNmsQe/Spot-Negotiation)
* **Spotting** — Awaiting Spot state: order has traded but requires FX spot rate agreement before settlement; visible as Spotting tab in AC with "Spot Now" action
* **Spot Negotiation** — FX spot rate negotiation workflow for cross-currency trades: client and dealer agree on the spot rate to complete the trade · [Figma](https://www.figma.com/design/EWt91nQV6zncWrO9PNmsQe/Spot-Negotiation)

## RFQ — List
*[Figma: EU List](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=18-32065) · [Figma: RFQ List quoting](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=5-221094)*

* **RFQ List** — right-panel workflow for multi-bond RFQ list orders from submission through quoting
  * **RFQ List: Submission / Trading Options** — Trading Options panel (Staging state): Protocol, Timer, Auto-X, Visibility, Counterparty Selection, Submit / Cancel; US and EU variants
  * **RFQ List: Negotiation Panel** — right panel during quoting: progress indicator, timer, Cancel; per-bond Buy / Sell / Pass actions
  * **RFQ List: Items Grid** — bond-level grid during quoting: status, timer, High Touch / Low Touch workflow, CP+ data

## Auto-X (ADX)

* **ADX Panel** — Adaptive Auto-X panel: Summary by list, Parent bond grid with eligibility status, and TAKE / SEEK actions · [Figma](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=19-29554)
  * **Summary view tabs** — tabs switch the aggregation view of eligible orders: List | Product | Side | Liq Score
  * **Parent grid filter tabs** — tabs filter the parent bond grid: All | Eligible | Take Eligible

## Trade Manager

* **Trade Manager** — order takeover and reassignment workflow for the Trade Manager role; filtered views (Mine / Others / All) · [Figma](https://www.figma.com/design/0cvRqbb7fVqoM5bs0HSLEJ/Trade-Manager) · [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5087100951)

## Common Components

* **Standard Formatters** — display formatting rules for price, yield, spread, quantity, date/time; decimal places by product type
* **Standard Enums** — display label mappings for CanAPI coded values: order status, trade type, direction, protocol, and other enumerations
* **Security Description** — standard display of bond identity (issuer, coupon, maturity, callable flag) used across all panels
* **Direction Indicator** — B / S / B+S side indicator: label text, color conventions, and conditional rendering
* **Status Badge** — order/inquiry status badge: label and color mapping per status value · [Figma](https://www.figma.com/design/HQAq0qmgWefd8b9JfgkxMk/RFQ-Statuses)
* **Timer Component** — countdown timer: display format, color-state transitions, and expiry behavior
* **Counterparty Selection Widget** — multi-select dealer picker: Open Trading toggle, Disclosed CPs, dealer groups · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=5-5540)
* **Restricted Dealer Selection** — rules and UI for excluding specific dealers from counterparty selection · [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5149294649)
* **Modals** — system modal dialogs: Rename list, Trade confirmation (with partials), Amend order, Choose spot time, Update limit levels; warning/error modals (Limit worse than Limit, Not best level, Negative Spread/Yield, 2 Warnings combined) · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=820-53018)
* **Validation Messages** — inline tooltip/banner validation errors and warnings on forms: required field errors, non-standard settlement date, minimum increment warnings · [Figma](https://www.figma.com/design/1BASLVXWRKMUzvPU23o3am/RFQ-Micro-frontends---MVP?node-id=1703-136075)
* **Workspace Layout Persistence** — saving and restoring panel sizes, column widths, and tab selection across sessions · [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5132877825)
* **User Preference Parity** — x-pro 2.0 user preference coverage: feature parity with xp1 / xp1.5 · [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5152931974)

## Reference

* **Glossary** — definitions of key terms and concepts used across x-pro 2.0 · [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5150769269)
