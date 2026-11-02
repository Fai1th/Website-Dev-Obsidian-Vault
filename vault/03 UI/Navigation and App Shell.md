---
title: "Navigation and App Shell"
type: pattern
status: proposed
updated: 2026-11-02
tags: []
---

# Navigation and App Shell

Start with destinations and task hierarchy. Prefer literal, concise labels. Use links for destinations and buttons for actions. Indicate the active page and preserve meaningful URL state.

Desktop navigation must fit its available width. Collapse before labels wrap awkwardly. A mobile menu needs a labeled trigger, open state, close action and keyboard/focus behavior. Do not treat hover as the only way to discover a submenu.

Use side navigation for persistent workspace hierarchy; use tabs for related panels in the current context. Do not combine competing navigation structures at the same level. Provide breadcrumbs when they explain a meaningful hierarchy, not as decoration.

Keep skip links and focus visible. Sticky nav must not obscure anchored headings or focused controls. Test deep links, refresh, back/forward navigation, long labels and signed-in/out states.

React candidates: [React - navigation-menu](../04%20React/Components/React%20-%20navigation-menu.md), [React - sidebar](../04%20React/Components/React%20-%20sidebar.md), [React - breadcrumb](../04%20React/Components/React%20-%20breadcrumb.md), [React - tabs](../04%20React/Components/React%20-%20tabs.md), [React - sheet](../04%20React/Components/React%20-%20sheet.md). Library behavior still needs application-level semantics and responsive verification.
