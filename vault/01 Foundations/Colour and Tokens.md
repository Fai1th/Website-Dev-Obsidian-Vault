---
title: "Colour and Tokens"
type: rules
status: curated
updated: 2026-11-02
tags: []
---

# Colour and Tokens

Define semantic roles before hex values: canvas, surface, elevated surface, primary text, secondary text, border, action, focus, success, warning and danger. Map every role for each supported theme.

Use one neutral family and normally one brand accent. Status colours are separate semantic tokens, not extra decorative accents. Preserve actual brand identity. Purple is supported in [Dark Accent Profile](Dark%20Accent%20Profile.md); it is not the automatic answer to every technical product.

Keep text readable in all states and over imagery. A secondary label is still text; reduced visual prominence does not justify low contrast. See [Accessibility Rules](../06%20Quality/Accessibility%20Rules.md). Test disabled states for recognizability without confusing them with enabled controls.

Document radius, border, shadow, spacing, type and layer scales. A valid shape system can use pill buttons and square tables if the rule is explicit. Avoid arbitrary component-by-component styling.

Provide solid-fill fallbacks for blur. Check forced-colour and high-contrast behavior. Test actual rendered colour pairs rather than inferring contrast from token names. Dark mode is a coherent palette, not a mechanical inversion.

Professional exception: a brand can use multiple accents if they encode a documented hierarchy or category system. Do not make every section a separate visual brand.
