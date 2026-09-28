# Doppler Secret Management R1

Rule ID: `KKS-DOPPLER-SECRET-MANAGEMENT-R1`

Last externally verified: `2026-09-29`

Status: `READY_FOR_REVIEW`

## Purpose

Define a sanitized, repository-safe way to use Doppler for local development, CI/CD, staging, and Production-adjacent workflows without committing secret values or introducing long-lived credentials where short-lived identity authentication is available.

## Source basis

Official Doppler guidance:

- Service Account Identities (OIDC): https://docs.doppler.com/docs/service-account-identities
- GitHub integration / Actions: https://docs.doppler.com/docs/github-actions
- CLI installation and usage: https://docs.doppler.com/docs/install-cli

## Mandatory rules

1. **Never commit secret values.**
   - Do not commit Doppler Personal Tokens, Service Tokens, short-lived identity tokens, application API keys, passwords, private keys, signing credentials, or Production secrets.
   - Do not paste secret values into README files, Issues, PRs, workflow YAML, logs, screenshots, test fixtures, or example configuration.

2. **Local development uses interactive login.**
   - Use `doppler login`.
   - Use `doppler setup` from the repository/application directory.
   - Run the application through `doppler run -- <command>`.
   - Repositories may document variable/config names only when those names are safe to publish.

3. **GitHub CI prefers OIDC identity authentication.**
   - Preferred chain: **GitHub-issued OIDC token → Doppler Service Account Identity → short-lived Doppler credential**.
   - Do not create a permanent `DOPPLER_TOKEN` merely because CI needs Doppler access when OIDC is supported.
   - Configure Doppler identity claim validation with explicit audience and subject rules; avoid wildcards unless there is a documented necessity.
   - Treat the Doppler Identity ID as configuration metadata, not as a secret, while still keeping unnecessary internal identifiers out of the public repository.
   - Short-lived credentials returned from identity authentication must not be persisted.

4. **Static Service Tokens are fallback-only.**
   - Use a Service Token only where OIDC/identity authentication is unavailable, unsupported by the deployment/plan, or explicitly rejected by the governing environment.
   - Scope any fallback token to the smallest applicable project/config and permissions.
   - Store it only in an approved platform secret store.
   - Never use a Personal Token or broad developer credential for unattended automation.

5. **GitHub integration is an alternative synchronization path.**
   - Doppler's GitHub integration may synchronize selected secrets into GitHub Actions/Environments.
   - This is separate from OIDC identity authentication and does not make GitHub a source of secret truth.
   - Public-repository rules and environment scoping remain mandatory.

6. **`doppler.yaml` is metadata, not a secret store.**
   - Safe project/config/path mappings may be committed when their names are not sensitive.
   - Secret values and credentials must never be placed in the file.

7. **Compromised-token response.**
   - Any token disclosed in chat, source, screenshots, logs, Issues, or PRs must be treated as compromised.
   - Revoke/rotate at the provider.
   - Do not copy the exposed value into remediation documentation.
   - Replace it through an approved secret channel.

## GitHub OIDC implementation boundary

OIDC setup itself is a security-sensitive change because it can involve GitHub workflow permissions, Doppler Service Account Identities, claim rules, and trust configuration.

Repository guidance may describe the pattern, but actual mutation of:

- GitHub Actions `id-token: write` permissions,
- Doppler identity creation/editing,
- OIDC claim rules,
- repository/environment secrets,
- token scopes,
- access roles,

requires the applicable explicit authorization and live read-back verification.

## Reference flow

```text
GitHub Actions job
  -> GitHub OIDC token
  -> Doppler Service Account Identity validation
  -> short-lived Doppler credential
  -> Doppler CLI/API access
  -> credential expires; do not persist
```

## Repository review checklist

Before merging a Doppler-related change:

- [ ] No token or secret value appears in the diff.
- [ ] OIDC is preferred for GitHub CI when supported.
- [ ] Audience/subject claim rules are explicit and least-privilege.
- [ ] No unnecessary permanent `DOPPLER_TOKEN` is introduced.
- [ ] Any fallback Service Token is documented as fallback-only and least-privilege.
- [ ] Real environment files remain ignored.
- [ ] Example files contain names/placeholders only.
- [ ] Security/admin mutations remain behind explicit authorization.
- [ ] Public-repository data-boundary rules pass.
- [ ] Validation runs on the exact PR head.

## Scope

This rule governs secret-handling guidance and repository hygiene only. It does not create Doppler identities, change GitHub OIDC permissions, grant secret access, configure Production credentials, or authorize payment/security behavior changes.
