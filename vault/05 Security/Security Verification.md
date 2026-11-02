---
title: "Security Verification"
type: security
status: curated
updated: 2026-11-02
tags: []
---

# Security Verification

Keep feature-specific evidence, not a checkbox claiming the application is secure.

- Identify protected data, user roles, tenant boundaries and state-changing operations.
- Verify anonymous, authorized, unauthorized and revoked-access paths.
- Exercise cross-user and cross-tenant IDs on direct routes, lists, downloads and exports.
- Test server validation and safe output handling with unexpected and oversized data.
- Verify cookie, CSRF, transport and header behavior on the deployed environment.
- Check dependency advisories, copied code, licenses and accidental secret exposure.
- Test upload/remote-fetch restrictions only when those features exist.
- Verify retry/duplicate-event behavior for consequential integrations.
- Record results, environment, date, unresolved limitations and responsible owner.

Use only systems you own or are authorized to test. The controls in [Security Map](Security%20Map.md) link to the relevant primary guidance. This checklist is a project verification aid, not an audit report or guarantee.
