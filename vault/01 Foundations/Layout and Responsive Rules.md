---
title: "Layout and Responsive Rules"
type: rules
status: curated
updated: 2026-11-02
tags: []
---

# Layout and Responsive Rules

Start with content priority and reading order. Use a small spacing scale, often multiples of 4px, and explain deliberate departures. Use Grid for page grids; use Flexbox for one-dimensional alignment.

Choose breakpoints when content stops fitting, not because a device has a fashionable width. Explicitly define the mobile order of text, imagery, action and supporting proof. Test at 320, 375, 768, 1024 and 1440 CSS pixels plus content-specific failure widths.

Use bounded content widths and fluid gutters. Prevent accidental page-level horizontal overflow; allow clearly scoped scrolling for wide tables and other truly two-dimensional content. Keep sticky bars from covering headings, focus targets or final form actions.

Do not require a full-screen hero. When viewport-relative height is justified, consider dynamic viewport units and content growth; prefer min-height to hard height. At high zoom, allow vertical growth instead of clipping content to keep a CTA above the fold.

Plan z-index as a small layer system. Reserve media dimensions. Avoid absolute positioning for normal text layout. Test mobile navigation, landscape, long translations and the browser back button.

Marketing pages benefit from varied section rhythm. Product screens benefit from repeated, predictable components. Do not apply a marketing anti-repetition rule to invoices, rows or repeated form groups.
