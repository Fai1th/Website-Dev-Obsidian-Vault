---
title: "Core Design Rules"
type: rules
status: curated
updated: 2026-11-02
tags: []
---

# Core Design Rules

These are opinionated starting defaults. They are aesthetic preferences, not a reliable detector of whether a site used AI. See [Source Provenance](../90%20Sources/Source%20Provenance.md) and [Conflict Decisions](Conflict%20Decisions.md).

- Begin with audience, content and the visitor's task. Preserve an existing brand unless the brief authorizes a redesign.
- Use specific copy, genuine work and attributable evidence. No invented testimonials, customer logos, statistics, urgency or product capabilities.
- Avoid automatic purple glow, centered dark-mesh heroes, identical feature cards, default component styling, oversized empty headings and decorative micro-labels.
- Default to a suitable sans-serif. Do not automatically choose Inter, Fraunces or Instrument Serif. Justify serif, purple, warm craft palettes and other established-brand exceptions.
- Use one coherent neutral family, accent system, radius scale, spacing system and icon family. Status colours have semantic roles and require text or shape support.
- Give each section a job. Vary marketing compositions when content warrants it. Keep repeated product rows consistent.
- Keep heroes concise, navigation clear, assets meaningful and actions truthful. Do not fabricate product previews out of decorative rectangles.
- Avoid decorative section numbers, irrelevant time/weather strips, status dots, faux version stamps and em-dash flourishes. Real operational state is allowed.
- Implement loading, empty, error, success, disabled and keyboard-focus states. Keep mobile order explicit. Maintain normal scrolling.
- Accessibility and security are release requirements. They cannot be waived to make a reference look more exact.
- Respect reduced motion. Prefer subtle, short, meaningful transitions. The [Strict Product Profile](Strict%20Product%20Profile.md) has stricter motion and typography rules, applied only in that project.
- Use established React behavior primitives, then give them brand-specific tokens and compositions. See [Source Adoption](../04%20React/Source%20Adoption.md).

Exceptions: a professional site may use a centered hero, restrained gradient, cards, neutral font or serif when it serves the content and brand. Record the reason, scope and evidence with [Exception Template](../09%20Templates/Exception%20Template.md). Conventional usability patterns are not flaws by themselves.
