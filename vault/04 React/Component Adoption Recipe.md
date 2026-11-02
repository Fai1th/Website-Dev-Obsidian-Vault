---
title: "Component Adoption Recipe"
type: recipe
status: curated
updated: 2026-11-02
tags: []
---

# Component Adoption Recipe

A repeatable recipe for adopting a dialog with a form. This is an integration plan, not a bundled application.

1. Inspect the actual project package.json, framework documentation and existing UI foundation.
2. Open [React - dialog](Components/React%20-%20dialog.md), [React - field](Components/React%20-%20field.md), [React - input](Components/React%20-%20input.md) and [React - button](Components/React%20-%20button.md). Load only their source/dependencies.
3. Choose current official registry output or the pinned offline snapshot deliberately. Do not mix versions by accident.
4. Review license, imports, aliases, peer dependencies and the target project's tokens. Record exact adopted versions and local changes.
5. Give the dialog a meaningful title, accessible descriptions and suitable initial focus. Give every input a persistent visible label.
6. Define submitting, success, validation error, server error and retry behavior. Preserve recoverable input. Keep server validation authoritative.
7. Verify opening, Tab/Shift-Tab, Escape where appropriate, closing, focus restoration and outside-content behavior.
8. Check long content, small screens, zoom, target sizes and supported themes. Run the project's type/build checks.
9. Record results before marking the integration tested. Source integrity alone does not establish behavior.

The raw source stays unchanged in the archive. Project-specific adapted code belongs in the target project with upstream attribution. Use [Source Adoption](Source%20Adoption.md) and [Dialogs and Overlays](../03%20UI/Dialogs%20and%20Overlays.md) for details.
