---
title: "Secrets and Dependencies"
type: security
status: curated
updated: 2026-11-02
tags: []
---

# Secrets and Dependencies

Keep secrets in the deployment's secret store or appropriate local environment configuration. Do not embed private credentials in client bundles, copied command URLs, screenshots, notes or source control. Public environment variable prefixes expose values to clients.

Use least privilege and separate environments. Document credential ownership and revocation/rotation procedures without storing values. Remove sensitive values from logs and error telemetry.

For components: review source, transitive dependencies, install scripts, license, advisories and maintenance. Pin actual adopted versions and retain the lockfile. Review registry diffs before accepting updates. A repository's star count or recent push is not a security audit.

Verification: secret scanning, client-bundle inspection for private values, dependency review, reproducible install and a documented update owner.

Source for secret lifecycle: [OWASP Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html). Component adoption policy is this library's recommendation; see [Source Adoption](../04%20React/Source%20Adoption.md).
