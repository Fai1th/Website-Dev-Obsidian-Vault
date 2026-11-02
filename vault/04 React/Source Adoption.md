---
title: "Source Adoption"
type: workflow
status: curated
updated: 2026-11-02
tags: []
---

# Source Adoption

## What is bundled

Unmodified shadcn/ui `new-york-v4` source snapshot at `4aaea19d9cff3e0908e12a8c1d504b8c5ec34610`, with 61 component files, 24 examples, registry definitions, a mobile hook, utility reference, application CSS context and MIT license. This is a dated source collection; some items are legacy relative to the current official registry.

## Adopt into a project

1. Read the target project's instructions, package.json and installed-version documentation. Select a single foundation and only the needed components.
2. For current integrations, prefer the official shadcn installation flow and selected components. The source snapshot's recorded CLI package version is **4.23.0**. Do not assume a later CLI emits identical source.
3. Before executing a registry command, review the registry identity, source/diff, dependency changes and install scripts. A copied command is not trusted merely because it appeared on social media.
4. For offline source adoption, resolve the actual imports from `manifest.json`: package/peer dependencies, `cn`, registry aliases and cross-component imports. Raw files reference repository-specific paths. They will not all compile if copied unchanged into an arbitrary app.
5. Configure appropriate styling/tokens. `globals-context.css` is upstream application context, not a drop-in project stylesheet. Copying it wholesale imports unrelated rules. Use only the needed theme contract.
6. Apply the project profile: font/radius/colour tokens, one icon family, target sizes, focus, motion and complete states. Button defaults can be under 44px; some sources use transition-all and Lucide.
7. Keep MIT copyright/license with copied source. For other catalogued libraries, inspect the actual package license and notices. Open-source code does not license associated images or paid templates.
8. Pin the adopted dependencies, keep a lockfile, record upstream commit and local edits. Run project type/build checks, integration journeys and manual accessibility checks.

## Status levels

`catalogued`: upstream metadata only. `source-snapshot`: local code and hash verified. `integrated`: works in a named target project. `tested`: recorded checks for a named version/environment. `deprecated`: avoid new adoption. Never infer a later status from an earlier one.

No package was installed and no component behavior was certified during collection. Integrity verification proves the bytes match the recorded Git objects, not that the code is safe, current or suitable.
