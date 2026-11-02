---
title: "Motion Rules"
type: rules
status: curated
updated: 2026-11-02
tags: []
---

# Motion Rules

Motion should explain change, preserve spatial relationships or provide action feedback. Start with no motion, then add only what improves understanding.

Prefer transform and opacity, usually around 150-250ms for small transitions. Do not make input or essential content wait for entrance choreography. Fast repeated operations can be immediate. Avoid broad transition-all rules and check what is actually animating.

Respect prefers-reduced-motion. Remove parallax, automatic panning, continuous decorative motion and large spatial transitions in the reduced variant. Keep status feedback understandable without animation.

Maintain normal scrolling and keyboard access. A scroll-pinned story needs a straightforward mobile/reduced-motion reading path. Avoid custom cursors, forced smooth scrolling and drag-only interactions.

Use one animation approach per element. Avoid competing libraries controlling the same properties. Load heavyweight animation only when a specific effect justifies it. Inspect lower-powered mobile behavior.

Some creative briefs justify expressive motion, while [Strict Product Profile](Strict%20Product%20Profile.md) requires all motion under 300ms and no animation on frequent actions. Project scope resolves the difference. Genre values are starting heuristics, not universal standards.
