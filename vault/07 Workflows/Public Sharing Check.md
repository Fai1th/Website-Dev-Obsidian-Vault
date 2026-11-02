---
title: "Public Sharing Check"
type: checklist
status: curated
updated: 2026-11-02
tags: []
---

# Public Sharing Check

Before sharing a fork or release:

- Review every staged file and the Git diff, including renamed files and hidden directories.
- Exclude credentials, environment files, personal machine paths, private client/project notes and unlicensed images.
- Keep private manifests in a separate vault or the ignored Private folder. Files already tracked by Git remain tracked despite ignore rules.
- Keep the root license and third-party notices. Preserve the upstream license with any copied snapshot.
- Run `python scripts/validate.py` from the repository root. Its pattern scan is a guardrail, not an exhaustive secret detector.
- Recheck source dates, counts, link targets and status claims. Do not promise runtime testing or measured token reductions without evidence.

The shared edition excludes full local skill archives and machine-specific agent instructions. It never installs global settings on another person's computer.
