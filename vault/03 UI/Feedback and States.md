---
title: "Feedback and States"
type: pattern
status: proposed
updated: 2026-11-02
tags: []
---

# Feedback and States

Map the whole state cycle before styling: idle, hover, focus, pressed, disabled, loading, empty, partial, success and error. Not every component needs every state, but every asynchronous operation needs a deliberate outcome.

Loading indicators should reflect the operation. Reserve dimensions; use a skeleton when it explains the forthcoming layout, not for every short wait. Keep status announcements concise and avoid repeated noisy live updates.

An empty state explains what is missing and what can be done next. Distinguish no records, no matching results and a permission restriction. An error states the issue and an available recovery path without exposing internals.

Use inline feedback near a field or persistent operation. Toasts suit brief noncritical confirmation; do not make the only record of a serious failure disappear automatically. Preserve a path to retry or undo when supported.

React candidates: [React - alert](../04%20React/Components/React%20-%20alert.md), [React - empty](../04%20React/Components/React%20-%20empty.md), [React - progress](../04%20React/Components/React%20-%20progress.md), [React - skeleton](../04%20React/Components/React%20-%20skeleton.md), [React - spinner](../04%20React/Components/React%20-%20spinner.md), [React - sonner](../04%20React/Components/React%20-%20sonner.md). Do not copy decorative status dots into every row.
