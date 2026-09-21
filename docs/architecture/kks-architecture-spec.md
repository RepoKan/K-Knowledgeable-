# K-Knowledgeable Architecture Specification

**Specification ID:** `KKS-ARCH-FREE-R1`  
**Repository:** `RepoKan/K-Knowledgeable-`  
**Version:** 1.0  
**Status:** Proposed target state  
**Owner:** RepoKan

## 1. Scope

This specification defines the target architecture for a public personal repository that stores knowledge and contains small Python/AI examples while operating on GitHub Free.

It covers repository layout, data classification, automation, CI/CD, access control, and operational limits. It does not define an enterprise IdP, production service deployment, or a database architecture.

## 2. Architectural requirements

### AR-001 — Text-first storage

Durable knowledge MUST be stored as UTF-8 Markdown, JSON, or plain text. Large binary files and secrets MUST remain outside the repository.

### AR-002 — Reviewable default branch

Changes to `main` SHOULD arrive through pull requests. Direct pushes MAY be used for personal low-risk maintenance, but protected-branch controls and required checks SHOULD be enabled where the plan supports them.

### AR-003 — Least-privilege automation

Workflows MUST declare the minimum `GITHUB_TOKEN` permissions they require. Read-only permissions are the default. A workflow MUST NOT require repository administration merely to validate or generate Markdown.

### AR-004 — Bounded generation

Generated files MUST be written only to an approved path, preferably `chatgpt-generated/` or `docs/generated/`. Generation MUST NOT delete unrelated files or rewrite source governance documents automatically.

### AR-005 — Secret exclusion

Credentials MUST be supplied through local environment variables, GitHub Actions secrets, or an external secret manager. `.env`, tokens, private keys, and webhook secrets MUST be ignored and MUST NOT be copied into generated content.

### AR-006 — Reproducible examples

Each runnable example SHOULD have its own README, dependency declaration, and safe local setup instructions. The cooking agent MUST remain isolated from knowledge-storage conventions.

### AR-007 — Observable failure

CI failures MUST be visible as failed checks with actionable logs. Automatic retries MAY be used for transient network operations but MUST be bounded and MUST NOT hide a failed change.

## 3. Logical components

| Component | Responsibility | Failure boundary |
|---|---|---|
| Knowledge store | Preserve reviewed text and revision history | Bad content remains in a branch until reviewed |
| Generator | Produce Markdown in an approved path | Cannot administer the repository |
| CI validator | Check Markdown, Python, YAML, and secret patterns | Failed check blocks merge where configured |
| Human reviewer | Approve correctness and publication | Final content decision |
| Example applications | Demonstrate isolated Python/AI behavior | Failure does not alter knowledge store |

## 4. Data classification

| Class | Examples | Repository policy |
|---|---|---|
| Public | Guides, sanitized architecture, recipes | Allowed |
| Internal draft | Unpublished notes, generated drafts | Review before publication |
| Secret | Tokens, keys, passwords, private URLs | Never commit |
| Large/binary | APK, ZIP, PDF collections, media | Store externally or omit |

## 5. Required directory contract

```text
.github/workflows/       # small validation workflows
chatgpt-generated/       # generated Markdown, if used
knowledge-supporting/    # durable knowledge and archives
docs/                    # architecture and project guides
cooking-agent/           # isolated Python example
scripts/                 # small deterministic helpers
tests/                   # lightweight tests where applicable
```

## 6. CI/CD contract

At minimum, pull-request validation SHOULD:

1. check Markdown formatting;
2. compile Python files or run focused tests;
3. parse YAML/JSON configuration;
4. scan for obvious credential patterns;
5. report failures through GitHub Actions.

Deployment is intentionally out of scope unless a future application requires it. GitHub Pages or another free static host MAY be added later for sanitized documentation.

## 7. Access and identity

Repository access is managed through the personal GitHub account and collaborator permissions. Enterprise SAML/OIDC SSO is not required for this target architecture. An integration client is an external actor and MUST be scoped independently from repository ownership.

## 8. Acceptance checklist

- [ ] Public files contain no credentials or private operational data.
- [ ] Workflow permissions are explicit and minimal.
- [ ] Generated output has one documented destination.
- [ ] Pull-request validation covers Markdown and Python.
- [ ] Large binary artifacts are excluded.
- [ ] Connector documentation does not imply automatic admin access.
- [ ] Knowledge remains readable and usable without the connector.

## 9. Evolution

This specification should be revised if the project becomes a deployed service, adds private data, gains multiple maintainers, requires releases, or exceeds GitHub Free limits. Those changes may justify a private repository, external storage, stronger branch rules, or a paid plan.
