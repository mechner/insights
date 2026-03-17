
# Feature Catalog Guidelines
**Features** are confluence pages that document functionality and requirements for parts of x-pro. They should provide enough specific detail for devs to implement and QA to verify. They also then serve as common reference for developers, QA, and product team as the product evolves.

The x-pro **feature catalog** is the collection of the x-pro features. It represents a cumulative, always up to date description of the x-pro product as it evolves over time. *Note: The x-pro feature catalog need not document our entire trading system’s functionality, only the x-pro UI functionality per se.*

The x-pro **feature index** is an index of the features in the catalog, providing a single location to easily understand how the product is organized in terms of features, and to link to the individual feature pages.

## Feature Index

Feature index is a bulleted list, one line per feature or sub-feature. 
* {name} - {description} · \[Confluence]\(url) · \[Figma]\(url)

Omit a link if not applicable. Use `· [Confluence (wip)](url)` for pages that exist but are incomplete.

Where:
* name is the feature name (matching the title of the feature page)
* description is a brief (1-line) description of the feature’s scope in terms of user-facing functionality or behavior
* confluence link is a link to the feature page in the feature catalog
* figma link is a link to the main figma page for the feature if applicable, for quick reference

Large or complex features should be broken down into subfeatures, indented bullets under the enclosing feature.

Links should be formatted not to display the entire link URL, but just "Confluence" or "Figma", for readability.

## Feature Page Guidelines

*The following applies when writing individual feature pages. Skip this section when working only on the feature index.*

Features should:

* Contain pointers to figma diagram links, if applicable (and a static image from that design as a quick visual reference). 
* Clearly define the scope of the feature. Where possible, it should be a UI component that is likely to be developed as a unit, or is natural to think about as a separate feature or component, for example:
  * A micro-frontend - for example a panel or tab with specific content and functionality. 
  * A component of a microfrontend (especially when common to multiple frontends) that’s complex enough to warrant its own feature page. 
  * A set of interactions, workflows, or related behaviors that span multiple components, and have complex enough logic that it represents material scope for implementation and testing. 
  * A collection of relatively small, related functional specifications that are likely to follow similar implementation patterns and be used in the same place - for example standard formatters. 
* Provide a table with all the fields that are displayed or represented in the component, where relevant. Each row represents a data element that appears, with columns:
  * **Label** that a user should see (matching Figma design where relevant); or exact text and templates for more complex labels and messages, using CanAPI {fieldName} placeholders. 
  * **Data source**, a CanAPI field name(s) or other calculation or source for calculated or composite columns. Where forms offer multiple choices, how is that set of options sourced? For inputs, what are the defaults, if not provided by the back end? 
  * **Formatting and decoration** for numbers, dates, etc. including conditional formatting e.g. by product (decimals), side (color), or comparison between two fields; decoration such as icons, colors, etc. 
  * **Conditional behavior** where appearance, label, modifiability, or behavior is conditional or state-dependent - including specifying what CanAPI fields, user or company settings, etc. control. 
  * **Validation** for input, what logic should the UI perform to ensure that the input is valid, either on an individual field basis or across fields where relevant.

Complex functionality that logically spans multiple fields should be referenced in the table, but be specified in detail outside the table.

A checklist of other relevant information to include in the feature page, if applicable: 
* **Side effects** of user interactions should be specified, for example, if a user input should trigger an update to another field, or a call to the back end, etc.
* **Empty States** — "no results" UX for grids, panels, etc. when there is no applicable content 
* **Secondary Workflows** - for example modals and confirmations that may appear as part of the feature’s functionality, but are not the main workflow.


The existence of feature pages means that Jira stories that we use to define and track dev work can be “lighter” - they don’t need to duplicate content that already exists in the feature: they can just reference the feature, clarify the portion that’s being implemented or changed, and address technical questions.

 