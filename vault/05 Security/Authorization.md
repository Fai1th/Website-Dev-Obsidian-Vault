---
title: "Authorization"
type: security
status: curated
updated: 2026-11-02
tags: []
---

# Authorization

Enforce permissions on the server for each operation and object. Default to denial. Check ownership, tenant, role and action; being signed in does not grant access to every record. Never rely on hidden buttons or unguessable IDs.

Scope database queries to authorized records. Recheck permissions when actions execute, including bulk actions and background work. Protect download and export routes too. Cache keys must not mix users or tenants.

Verification: user A cannot read, edit, delete or export user B's records; ordinary users cannot perform admin operations; missing or revoked permission denies access; list and direct-ID routes agree.

Source: [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html). This is an implementation summary, not a full policy model.
