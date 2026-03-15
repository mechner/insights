
# X-Pro 2.0 Feature Catalog Index

This index lists all features in the x-pro 2.0 feature catalog. Each row represents a feature that should have (or already has) a feature page documenting its functional requirements.

**Scope**: EU and US RFQ, and common components. Auctions/MOC and Nucleus are explicitly out of scope.

**Status values**: `existing` — Confluence page exists | `wip` — page exists but incomplete | `pending` — no page yet

| # | Feature | Scope | Primary Figma | Confluence | Status | Notes |
|---|---------|-------|--------------|------------|--------|-------|
| **Activity Console** |
| AC-01 | Activity Console | MFE — left-hand order list panel | [AC Microfrontend](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend) | | pending | Top-level overview of the AC MFE; scope, layout, lifecycle |
| AC-02 | AC: Tab Bar & Navigation | AC tabs (All Orders, Staged, In Progress, Spotting, Done, Auto-X, Auction Eligible); counts; pop-out | [Tabs](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=989-30898) | | pending | |
| AC-03 | AC: Order Grid — Single Bond Row | Per-row layout, fields, status badges, action buttons for single-bond orders | [All Orders](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=723-273460) | | pending | |
| AC-04 | AC: Order Grid — List / Basket Row | List rows (expandable), list-level fields, expand/collapse behavior | [All Orders](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=723-273460) | | pending | |
| AC-05 | AC: Workflow Status Banner | Summary boxes (Staged / In Progress / Done counts) above the grid | [Prototype: AC](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=1-91259) | | pending | |
| AC-06 | AC: Summary Tiles / Metrics Bar | Aggregate metrics displayed above the grid per tab | [Summary Tiles](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=989-30781) | | pending | |
| AC-07 | AC: Filters & Search | Filter panel, search, item count display | [Filters](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=985-92867) | | pending | |
| AC-08 | AC: Context Menus & Row Actions | Per-row overflow menu; bulk action bar for multi-select | [Context Menus](https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend?node-id=1699-34899) | | pending | |
| AC-09 | Opportunities Column | Axe and AI-Select hints displayed inline on AC order rows | [Prototype: AC](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=1-91259) | [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5128355882) | existing | |
| **Pre-Trade Intelligence** |
| PT-01 | Market Depth Panel | Single-bond inline pre-trade panel: bid/offer depth, axe data, TRACE last print, My History | [Market Depth](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=5-280945) | | pending | |
| PT-02 | List Analytics Panel | Floating analytics overlay for list orders: analytics grid, distribution charts | [List Analytics](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=5-288880) | | pending | |
| **RFQ — Single Bond** |
| RFQ-01 | Inquiry Parameters — Single Bond | Submission form for a single-bond RFQ: all input fields, defaults, validation | | [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5022548145) | existing | |
| RFQ-02 | Direct RFQ | The single-bond RFQ right-panel: Trade Ticket header, status bar, tabs | | [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5155815530) | wip | |
| RFQ-03 | Trade Ticket: Responses | Dealer response grid (Responses tab); per-response fields; Buy Best / Sell Best; counter-quote | [Details Panel](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=73-46108) | | pending | |
| RFQ-04 | Trade Ticket: Details | Post-trade details tab: collapsible sections (Pricing, Trade Proceeds, Instrument Details, Identifiers) | [Details Panel](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=73-46108) | | pending | May be covered by RFQ-02 |
| RFQ-05 | Trade Ticket: Activity Log | Audit trail of events on an inquiry | [Details Panel](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=73-46108) | | pending | |
| RFQ-06 | Process Trades | Workflow for executing a trade from a response: Trade at Best, select response, confirm | | [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5027496006) | existing | |
| RFQ-07 | Trade at Best | One-click best-response execution behavior and rules | | [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5149294689) | wip | |
| RFQ-08 | Editable Inquiry Fields | Rules for which inquiry fields are editable after submission, and under what conditions | | [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5028380695) | existing | Has sub-pages: Field Specs, Tech Design, UX Considerations, Decisions Log |
| **RFQ — List** |
| LIST-01 | RFQ List: Submission / Trading Options | Trading Options panel for a list in Staging: Protocol, Timer, Auto-X, Visibility, CP Selection, Submit | [EU List](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=18-32065) | | pending | US and EU variants; see also LIST-04 |
| LIST-02 | RFQ List: Negotiation Panel | Right panel during quoting: progress indicator, timer, Cancel; per-bond Buy/Sell/Pass actions | [RFQ List](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=5-221094) | | pending | |
| LIST-03 | RFQ List: Items Grid | Bond-level grid within a list during quoting: status, timer, workflow (High Touch/Low Touch), CP+ data | [RFQ List](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=5-221094) | | pending | |
| **PT List** |
| PTL-01 | PT List: Submission Panel | Portfolio Trading submission: Trade type toggle, Pricing, Timing, Protocol, Cross, Dealer selection | [PT](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=1-146072) | | pending | |
| PTL-02 | PT List: Items Grid | Bond-level grid for PT list: Included toggle, Starred, Reference, Side, Sector, Protocol per bond | [PT](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=1-146072) | | pending | |
| **Auto-X (ADX)** |
| ADX-01 | ADX Panel | Adaptive Auto-X panel: Summary by list, Parent bond grid, eligibility, TAKE / SEEK actions | [ADX](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=19-29554) | | pending | |
| **Trade Manager** |
| TM-01 | Trade Manager | Order takeover / reassignment workflow; TM role; filtered views (Mine / Others) | [Trade Manager](https://www.figma.com/design/0cvRqbb7fVqoM5bs0HSLEJ/Trade-Manager) | [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5087100951) | existing | |
| **Common / Shared** |
| CMN-01 | Standard Formatters | Price, yield, spread, size/quantity, date/time formatting rules; decimal places by product | | | pending | |
| CMN-02 | Standard Enums | Display mappings for CanAPI coded values: order status, trade type, direction, etc. | | | pending | |
| CMN-03 | Security Description | Standard display of bond identity: issuer, coupon, maturity, callable flag | | | pending | Common across all panels |
| CMN-04 | Direction Indicator | B / S / B+S display and color conventions | | | pending | |
| CMN-05 | Status Badge | Order/inquiry status badge: colors, labels per status value | | | pending | |
| CMN-06 | Timer Component | Countdown timer display: formatting, expiry behavior, color states | | | pending | |
| CMN-07 | Counterparty Selection Widget | Multi-select CP picker: Open Trading toggle, Disclosed CPs, dealer groups | [EU List](https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=18-32065) | | pending | |
| CMN-08 | Restricted Dealer Selection | Rules and UI for restricting which dealers can be selected | | [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5149294649) | existing | |
| CMN-09 | Workspace Layout Persistence | Saving and restoring panel sizes, column widths, tab state across sessions | | [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5132877825) | existing | |
| CMN-10 | User Preference Parity | x-pro 2.0 user preferences: feature parity with xp1/xp1.5 | | [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5152931974) | existing | |
| **Reference** |
| REF-01 | Glossary | Terminology definitions | | [Confluence](https://marketaxess.atlassian.net/wiki/spaces/XE/pages/5150769269) | existing | |
