---
title: "Dialogs and Overlays"
type: pattern
status: proposed
updated: 2026-11-02
tags: []
---

# Dialogs and Overlays

A modal is for a bounded task or consequential decision. Use normal navigation for full pages. A dialog needs an accessible name, clear purpose, suitable initial focus and a reliable close path.

Keep keyboard focus within a modal while open, make outside content inert and restore focus to a sensible trigger on close. Support Escape where appropriate. Long content needs a clear scroll strategy and reachable actions.

For destructive decisions, name the affected object and the consequence. Avoid vague confirmation copy. Preserve ongoing work when closing or navigating away where the product requires it.

Popover, tooltip and menu are different patterns. A tooltip is supplementary, not the only place for essential information or actionable controls. A menu is not a generic container for arbitrary form fields.

Source: [W3C modal dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/). Check these behaviors in the composed product; importing a primitive alone is not a complete accessibility assessment.

React candidates: [React - dialog](../04%20React/Components/React%20-%20dialog.md), [React - alert-dialog](../04%20React/Components/React%20-%20alert-dialog.md), [React - drawer](../04%20React/Components/React%20-%20drawer.md), [React - popover](../04%20React/Components/React%20-%20popover.md), [React - tooltip](../04%20React/Components/React%20-%20tooltip.md).
