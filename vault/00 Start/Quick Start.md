---
title: "Quick Start"
type: guide
status: curated
updated: 2026-11-02
tags: []
---

# Quick Start

## In Obsidian

1. Download the repository ZIP from GitHub's **Code > Download ZIP**, or clone it.
2. Extract the ZIP if needed.
3. In Obsidian, choose **Open folder as vault** and select the repository's `vault` folder.
4. Open [START HERE](../START%20HERE.md). No community plugins are required.

Keep the repository's LICENSE and THIRD_PARTY_NOTICES.md with the vault when redistributing it. Prefer sharing the full repository or ZIP rather than separating the content from its notices.

## With an agent

Use this prompt after granting the agent access to your local checkout:

> Read `vault/AGENT START.md` and `vault/01 Foundations/Core Design Rules.md`. Choose only the notes relevant to this project's audience, genre, UI and security surface. Follow the project's own instructions. Record the selected note paths, dependency versions and exceptions in a project manifest.

The root AGENTS.md provides the same entry point when working inside this repository. Other tools may need the explicit prompt. The library does not install global instructions, plugins, packages or background tasks.

## A first project

Use [Example Project Manifest](../10%20Projects/Example%20Project%20Manifest.md) as a model. Choose one genre, one primary React foundation and a small reference set. Use [Source Adoption](../04%20React/Source%20Adoption.md) before copying components. Finish with [Professional Release Checklist](../06%20Quality/Professional%20Release%20Checklist.md).
