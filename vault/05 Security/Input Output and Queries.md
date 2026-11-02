---
title: "Input Output and Queries"
type: security
status: curated
updated: 2026-11-02
tags: []
---

# Input Output and Queries

Validate untrusted input on the server with explicit types, lengths, formats and allowed values. Client validation is assistance, not a trust boundary.

Use framework escaping and output encoding appropriate to the destination context. Avoid raw HTML injection. If rich HTML is required, sanitize with a maintained sanitizer and a restrictive policy; validation alone does not prevent XSS. Treat URLs, attributes, CSS and scripts as distinct contexts.

Use bound parameters for SQL. Allowlist dynamic identifiers such as sort columns; do not concatenate arbitrary input into query structure.

Verify oversized/malformed input, HTML payloads remaining inert, forbidden URL schemes and parameterized database operations.

Sources: [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html), [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html).
