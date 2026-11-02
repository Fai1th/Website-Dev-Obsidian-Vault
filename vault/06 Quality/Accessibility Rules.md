---
title: "Accessibility Rules"
type: rules
status: curated
updated: 2026-11-02
tags: []
---

# Accessibility Rules

Apply the full standard required by the project; this is a compact starting checklist.

Normal-sized text needs at least 4.5:1 contrast at WCAG AA. Large text can use 3:1; large generally means at least 18pt regular or 14pt bold (roughly 24px/18.67px). Secondary text is not exempt. Measure actual rendered combinations. [Contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

Prefer 44 by 44 CSS pixel touch targets as this library's design target. WCAG 2.2 AA SC 2.5.8 uses 24 by 24 CSS pixels with defined exceptions. [Target size guidance](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).

Keep ordinary content usable at 320 CSS pixel width without two-dimensional scrolling. Tables and other necessary two-dimensional content have scoped exceptions. Test zoom and enlarged text. [Reflow guidance](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).

Use semantic HTML, visible labels, logical headings and reading order. Provide text alternatives, keyboard operation, visible/unobscured focus and non-colour state cues. Check modal focus and recovery, error associations and dynamic announcements. Avoid hover-only and drag-only essential interactions. Honor reduced motion.

Verify manually with keyboard and a screen reader alongside automated checks. Passing an automated scan does not prove full compliance. Test the final composition, not just the underlying library.
