
# Specific Knowledge

This document contains specific knowledge and clarifications that should be relied on when generating or evaluating features in the feature catalog. This includes information about the systems, their interactions, and any other relevant details, including clarifications and resolution of conflicting information found in the resources.

## Figma Designs

All designs live in the **MarketAxess** Figma team (ID: `1613317744861427514`), under the **Activity Console 2.0** project (ID: `344298335`): https://www.figma.com/files/1279115914045676988/project/344298335

### Authoritative files

* **Activity Console Microfrontend** — key `Q4keHW9QtaM3adu9y6Nsjq` — https://www.figma.com/design/Q4keHW9QtaM3adu9y6Nsjq/Activity-Console-Microfrontend
  * Primary designs for the Activity Console (left-hand order list panel): tabs, grids, row states, filters, context menus, empty states, summary tiles.
  * Key pages: `Activity Console` (830:279214), `Grids`, `Tabs`, `Filters`, `Context Menus`, `Summary Tiles`.
  * Pages to ignore: `Archive`, `Errors WIP` (still in progress), `Components - Misc (To delete?)`.

* **Activity Console Prototype** — key `2q1qq3C53E0sqnqmgChTgw` — https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype
  * Contains the **right-hand details/RFQ panel** designs and full-screen layouts showing both panels together.
  * Key frames (Page 1): `Details Panel//US RFQ` (73:46108) — https://www.figma.com/design/2q1qq3C53E0sqnqmgChTgw/Activity-Console-Prototype?node-id=73-46108; `RFQ List` full-screen (5:221094).
  * The Details Panel contains: App Header, Title/Header, Input Fields (RFQ parameters), Trade Ticket (header, timer, tabs, response body).

### Other files (Features project)
* **Trade Manager** (`0cvRqbb7fVqoM5bs0HSLEJ`) — designs for the Trade Manager role: order takeover/reassignment workflow. Separate from core RFQ panel.
* **Loading States** (`LkCk1f2EOgKC0NH89kVSHy`) — component-level loading state designs.
* **Open Trading Errors** (`2i2fmG1E226mvkolADhrhn`) — error state designs for Open Trading flows.


## Other 
* Field definitions in @mktx-data/schema-documentation/field-dictionary.csv should be treated as reliable and reflecting target naming conventions for canon schemas. Fields that appear in schemas that don't match one of these names are still suspect. 
