---
title: "Versioning and Updates"
type: workflow
status: curated
updated: 2026-11-02
tags: []
---

# Versioning and Updates

The React archive is intentionally pinned. It is not a rolling mirror of upstream main.

For documentation edits, update the note date and explain meaningful changes in the changelog. Preserve attribution and distinguish current recommendations from dated research observations.

For source updates:

1. Select an exact upstream commit and inspect its license and file inventory.
2. Review differences, dependencies, deprecated APIs and relevant advisories.
3. Update the matching code, examples, component cards, import manifest and license together.
4. Recalculate Git blob/SHA-256 hashes and sizes. Do not edit bytes while describing source as unmodified.
5. Run the repository validator. Runtime integration still requires separate target-project checks.
6. Update counters, source-status notes, artwork and changelog if scope changed.

For inspiration, recheck links when using the reference. Keep inaccessible leads labeled candidate. Never silently replace original creator attribution with a repost.

Tag a release only after validation and a human review of the staged files. This repository does not auto-publish or auto-install dependencies.
