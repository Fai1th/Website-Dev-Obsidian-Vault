---
title: "Performance Rules"
type: rules
status: curated
updated: 2026-11-02
tags: []
---

# Performance Rules

Performance is measured on real pages and representative devices, not inferred from using a popular framework.

Core Web Vitals good thresholds: LCP at most 2.5 seconds, INP at most 200ms and CLS at most 0.1, assessed at the 75th percentile of page loads, separately for mobile and desktop. Use field data when available. Lab checks are diagnostic, not a substitute for field evidence. [Google web.dev Web Vitals](https://web.dev/articles/vitals).

Practical defaults: reserve media dimensions; serve appropriately sized images; do not lazy-load the essential LCP image; defer below-the-fold media; limit font families/weights; load only necessary JavaScript and isolate interactive islands when the framework supports it.

Avoid large decorative video, expensive blur on scrolling content, layout thrashing and unnecessary per-frame React updates. Budget third-party widgets and analytics. Virtualize only when measurement justifies the complexity.

Record environment, route, device, network assumptions and measurement method. Recheck after a meaningful asset, dependency or interaction change. Do not call a single Lighthouse score a guarantee of real-user speed.
