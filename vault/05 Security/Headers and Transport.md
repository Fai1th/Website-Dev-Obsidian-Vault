---
title: "Headers and Transport"
type: security
status: curated
updated: 2026-11-02
tags: []
---

# Headers and Transport

Serve production traffic over HTTPS. Design a Content Security Policy for the actual application and test it before enforcement. Restrict embedding through frame-ancestors where appropriate. Use appropriate content types, nosniff and a considered referrer policy.

Plan HSTS carefully: only include subdomains or preload when their HTTPS readiness is established. Do not paste a generic header block without understanding the app's embeds, scripts, assets and deployment topology.

Verify response headers on the deployed route, not only in configuration. Check errors and redirects as well as the successful page. A CSP is defense in depth and does not replace safe output handling.

Source: [OWASP HTTP Headers](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html).
