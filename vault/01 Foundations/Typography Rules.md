---
title: "Typography Rules"
type: rules
status: curated
updated: 2026-11-02
tags: []
---

# Typography Rules

Use a compact type system with display, heading, body, label and metadata roles. Begin with one sans family; introduce a second only for a clear brand or reading purpose. Check font licensing before shipping or self-hosting.

Use roughly 16px body text as a practical starting point, with comfortable line height and a reading measure near 45-65 characters. These are design defaults, not WCAG pass/fail thresholds. Test the actual font at narrow widths and enlarged text.

Keep headline emphasis within the same family. Do not inject a decorative serif word automatically. Avoid clipped accents/descenders, forced line breaks that fail on mobile and letter spacing that makes long labels hard to read.

Specify typography with semantic tokens and fluid, bounded scales. Ensure fallback fonts retain acceptable layout. Use tabular figures for aligned numeric comparisons. Underline links where surrounding copy otherwise makes their role unclear.

Library preferences: Inter is conditional; Fraunces and Instrument Serif are not default display choices; em-dash decoration is excluded. [Strict Product Profile](Strict%20Product%20Profile.md) additionally forbids italic emphasis. Other genres can use it intentionally.

Verify real headings, localized copy, long names, empty values, 200% text resize and narrow viewport wrapping. Do not shrink text to rescue a poor content hierarchy.
