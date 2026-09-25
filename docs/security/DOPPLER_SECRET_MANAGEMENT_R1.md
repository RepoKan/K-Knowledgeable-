# Doppler Secret Management R1

Rule ID: `KKS-DOPPLER-SECRET-MANAGEMENT-R1`

## Purpose

Define a sanitized, repository-safe way to use Doppler for local development, CI/CD, staging, and Production-adjacent workflows without committing secret values or broad-scope credentials.

## Source basis

Official Doppler guidance:

- CLI installation and usage: https://docs.doppler.com/docs/cli
- CLI installation: https://docs.doppler.com/docs/install-cli
- Service Tokens: https://docs.doppler.com/docs/service-tokens
- GitHub Actions integration: https://docs.doppler.com/docs/github-actions
- Secrets setup: https://docs.doppler.com/docs/secrets-setup-guide

## Mandatory rules

1. **Never commit secret values.**
   - Do not commit Doppler Personal Tokens, CLI tokens, Service Tokens, API keys, passwords, private keys, signing credentials, or Production secrets.
   - Do not paste secret values into README files, Issues, PRs, workflow YAML, logs, screenshots, test fixtures, or example configuration.

2. **Local development uses interactive login.**
   - Install the CLI.
   - Run `doppler login`.
   - Run `doppler setup` from the repository or application directory.
   - Run the application through `doppler run -- <command>`.
   - The repository may document variable names and expected config names, but not secret values.

3. **Live/automation environments use least-privilege Service Tokens.**
   - Do not use a Doppler Personal Token or broad CLI token in CI, staging, Production, or unattended automation.
   - Use a Service Token scoped to the smallest applicable Project + Config.
   - Store that token in the platform's secret store or use the official Doppler GitHub integration.
   - A Service Token value itself must never be committed.

4. **`doppler.yaml` is configuration metadata, not a secret store.**
   - It may declare project/config/path mappings when those names are safe to publish.
   - It must never contain token values or application secret values.
   - If project/config names are sensitive, keep the mapping outside a public repository.

5. **Environment-file compatibility remains optional.**
   - Existing `.env.example` files may document required variable names.
   - Real `.env`, `.env.local`, and environment-specific secret files remain ignored.
   - Doppler is an injection path, not permission to delete a working local fallback without a migration plan.

6. **Compromised-token response.**
   - Any token disclosed in chat, logs, source, screenshots, Issues, PRs, or other broadly visible channels must be treated as compromised.
   - Revoke or rotate it at the provider.
   - Do not copy the exposed value into GitHub while documenting the incident.
   - Replace it with a fresh scoped credential delivered through an approved secret channel.

## Reference command pattern

Local developer:

```bash
doppler login
doppler setup
doppler run -- <development-command>
```

CI / unattended runtime:

```text
DOPPLER_TOKEN = platform-managed secret containing a restricted Service Token
```

Then execute:

```bash
doppler run -- <build-or-runtime-command>
```

## Repository review checklist

Before merging a Doppler-related change:

- [ ] No token or secret value appears in the diff.
- [ ] Real environment files remain ignored.
- [ ] Example files contain names/placeholders only.
- [ ] CI references secret identifiers, never secret values.
- [ ] Personal/CLI tokens are not proposed for live environments.
- [ ] Service-token scope is documented at the Project + Config level.
- [ ] Rollback preserves the previous environment-loading path when required.
- [ ] Public-repository data-boundary rules still pass.

## Scope

This rule governs secret-handling guidance and repository hygiene only. It does not grant access to Doppler, GitHub Secrets, Production credentials, or external environments, and it does not authorize Production/payment/security behavior changes.
