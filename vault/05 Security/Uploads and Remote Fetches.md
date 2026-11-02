---
title: "Uploads and Remote Fetches"
type: security
status: curated
updated: 2026-11-02
tags: []
---

# Uploads and Remote Fetches

Allow only business-required file types. Validate extension, content type and content/signature appropriately; a client MIME header is not trustworthy. Limit size, count and decompressed processing cost. Generate safe storage names and separate untrusted uploads from executable application content.

Enforce authorization for upload, retrieval and deletion. Scan/process files according to risk; do not publicly serve active content unintentionally.

A server fetching a user-supplied URL creates an SSRF boundary. Restrict protocols and destinations; control redirects, DNS resolution and outbound access. Prevent access to private/internal services and metadata endpoints. Use an allowlist where the use case permits.

Verification: spoofed types, oversized files, unsafe filenames, unauthorized downloads, redirect chains and blocked internal destinations.

Sources: [OWASP File Upload](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html), [OWASP SSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html).
