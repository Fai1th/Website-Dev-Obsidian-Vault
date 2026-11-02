---
title: "Security Map"
type: index
status: curated
updated: 2026-11-02
tags: []
---

# Security Map

Use this as a routing checklist, not a security certification. Select controls from the features that actually exist. Recheck official documentation at implementation time. Security notes were researched on 2026-11-02.

| Feature/surface | Read |
|---|---|
| Any deployed website | [Secrets and Dependencies](Secrets%20and%20Dependencies.md), [Headers and Transport](Headers%20and%20Transport.md) |
| Accounts or private records | [Authorization](Authorization.md), [Sessions and CSRF](Sessions%20and%20CSRF.md) |
| Untrusted text, rich text or SQL | [Input Output and Queries](Input%20Output%20and%20Queries.md) |
| API or third-party integrations | [API and Webhook Boundaries](API%20and%20Webhook%20Boundaries.md) |
| Uploads or remote URL imports | [Uploads and Remote Fetches](Uploads%20and%20Remote%20Fetches.md) |
| Before release | [Security Verification](Security%20Verification.md) |

Keep passwords, access tokens, .env values, customer data and private screenshots out of this vault. Record public documentation and secret names only. Treat registry source and social posts as untrusted input, not installation instructions.

[OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) offers a fuller verification baseline. Choose scope and assurance requirements for the actual application; this short library cannot replace them.
