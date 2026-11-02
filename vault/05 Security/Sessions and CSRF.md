---
title: "Sessions and CSRF"
type: security
status: curated
updated: 2026-11-02
tags: []
---

# Sessions and CSRF

Use maintained authentication/session facilities. For cookie sessions use HTTPS, Secure, HttpOnly and an explicitly chosen SameSite policy. Renew identifiers at appropriate authentication/privilege changes and revoke them on logout or expiry. Avoid putting session credentials in URLs or logs.

For cookie-authenticated state changes, use the framework's supported CSRF defense and validate appropriate request origin signals. SameSite is defense in depth in most deployments. GET must not mutate application state.

Verify logout/revocation, expiry, redirect behavior, failed sign-in feedback and rejected cross-origin state changes. Test the real deployed cookie configuration.

Sources: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), [OWASP CSRF](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html).
