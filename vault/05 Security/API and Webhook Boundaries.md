---
title: "API and Webhook Boundaries"
type: security
status: curated
updated: 2026-11-02
tags: []
---

# API and Webhook Boundaries

Apply authentication and authorization at every protected endpoint. Validate content types, payload shape and size; constrain methods. Return useful public errors without exposing internals. Bound request cost and apply abuse limits appropriate to the operation.

CORS controls browser access; it is not authentication. Keep an intentional origin policy. Avoid leaking sensitive parameters through URLs and logs.

For webhooks, verify the provider's signature using its documented raw-body rules. Address replay and duplicate delivery, make state transitions idempotent where required and recheck provider-specific instructions. Never mark payment complete from a client redirect alone.

Verification: missing/invalid credentials, cross-tenant IDs, wrong method/content type, oversized requests and duplicate events. Record which provider-specific webhook rules were actually tested.

Source for API boundaries: [OWASP REST Security](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html). Webhook details must come from the active provider's official documentation.
