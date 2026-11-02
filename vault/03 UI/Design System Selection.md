---
title: "Design System Selection"
type: pattern
status: proposed
updated: 2026-11-02
tags: []
---

# Design System Selection

Keep the existing project's foundation when suitable. For a new product, choose one primary behavior/visual system and record why it fits.

| Need | Starting candidates |
|---|---|
| Brand-owned styling and composable behavior | shadcn/ui, Radix, Base UI, React Aria, Headless UI |
| Broad product application components | Mantine or Material UI |
| Microsoft ecosystem | Fluent UI |
| IBM-style enterprise product | Carbon |
| GitHub-style product | Primer React |
| UK public service | GOV.UK Design System, with appropriate integration |
| Table mechanics | TanStack Table |
| Locale-heavy dates and accessible inputs | React Aria |

These are starting points, not endorsements of every version or component. Check current official docs, license, release status and accessibility limitations before adoption. Do not combine multiple systems just to get different default aesthetics.

Use specialist libraries only for a demonstrated need. Keep package dependencies isolated behind small project-owned wrappers where that reduces migration cost. The [React Catalogue](../04%20React/React%20Catalogue.md) records researched repositories and clear status boundaries.
