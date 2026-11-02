---
title: "Tables and Filters"
type: pattern
status: proposed
updated: 2026-11-02
tags: []
---

# Tables and Filters

Choose a semantic table for records people compare across columns. Use a list for independent items. A table library supplies mechanics; column meaning and accessible operation remain application responsibilities.

Define stable IDs, column labels, alignment, units and empty values. Align numbers and use tabular figures. Separate sorting, filtering, pagination and selection semantics. Show total/filtered counts when useful.

For server data, represent loading, stale, empty, failed and retry states. Keep query keys and URL state consistent with active filters. Cancel or ignore obsolete responses. Never let a late request replace newer results.

Selection needs a scope: this page, visible rows or all matching results. Explain destructive bulk actions and confirm the actual scope. Authorization is enforced on the server.

Use virtualization only when it helps a measured bottleneck. Test reading order, keyboard navigation, screen readers and focus retention when rows leave the DOM. Mobile needs scoped scrolling or an intentionally different record view.

React candidates: [React - table](../04%20React/Components/React%20-%20table.md), [React - pagination](../04%20React/Components/React%20-%20pagination.md), [TanStack Table](../04%20React/Libraries/TanStack%20Table.md), [TanStack Virtual](../04%20React/Libraries/TanStack%20Virtual.md), [Recharts](../04%20React/Libraries/Recharts.md). Include an accessible data/text alternative to essential charts.
