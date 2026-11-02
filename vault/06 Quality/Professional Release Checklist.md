---
title: "Professional Release Checklist"
type: checklist
status: curated
updated: 2026-11-02
tags: []
---

# Professional Release Checklist

Keep a project-specific evidence log for these gates. A polished screenshot is one part of release quality.

## Content and visual system

- Correct audience, purpose, page hierarchy and primary task.
- Approved copy, brand assets, source rights and supported claims.
- Consistent type, spacing, colour, radius, layers and icon family.
- Reviewed hero, navigation, section rhythm and footer destinations.
- Real product evidence; sample data clearly labeled; no unfinished placeholders.

## Interaction and accessibility

- Every link/button performs its stated operation.
- Loading, empty, error, success, disabled and retry behavior reviewed.
- Forms preserve values and show associated errors.
- Keyboard, screen-reader essentials, focus, zoom, contrast and reduced motion checked; see [Accessibility Rules](Accessibility%20Rules.md).
- Small/large screens, long content and all supported themes verified.

## Engineering and operations

- Installed-version documentation read; dependencies and licenses reviewed.
- Type/build/lint checks appropriate to the repository pass.
- Critical user journeys verified against real APIs/data where applicable.
- [Security Verification](../05%20Security/Security%20Verification.md) scoped and recorded; failures resolved or explicitly documented.
- [Performance Rules](Performance%20Rules.md) measured where applicable.
- Page title/description, canonical/indexing intent, social metadata and sitemap needs reviewed.
- Error/404 behavior, useful logging, privacy expectations, backup/rollback and release owner are clear.

Record the actual commands, routes, screenshots where useful, dates and limitations. Distinguish tested facts from assumptions. Do not promote a component card to tested merely because upstream advertises accessibility.
