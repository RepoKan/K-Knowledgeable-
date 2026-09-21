# K-Knowledgeable Free-Tier Architecture Strategy

**Repository:** `RepoKan/K-Knowledgeable-`  
**Purpose:** Public, personal knowledge storage and small Python/AI experiments  
**Operating model:** GitHub Free, one owner, reviewable automation, no enterprise identity layer  
**Status:** Target architecture

## 1. Project goals

This repository has three related goals:

1. Preserve durable knowledge as searchable Markdown.
2. Provide small, reproducible Python experiments such as the cooking agent and joke generator.
3. Support ChatGPT/Copilot-assisted documentation without granting an automation client unrestricted repository control.

The repository is **not** intended to be a production SaaS backend, a secret store, a binary artifact registry, or an enterprise SSO system.

## 2. Target architecture

```text
Human / ChatGPT / Copilot
          |
          | proposed change
          v
Feature branch or pull request
          |
          v
GitHub Actions: lint + syntax + secret-pattern checks
          |
          v
Human review and merge to main
          |
          +--> knowledge-supporting/   durable knowledge
          +--> docs/                    architecture and guides
          +--> chatgpt-generated/      generated output, if retained
          +--> cooking-agent/          isolated Python example
```

## 3. Repository boundaries

| Area | Purpose | Write policy |
|---|---|---|
| `knowledge-supporting/` | Durable knowledge and archives | Human or reviewed automation |
| `docs/` | Architecture, governance, and guides | Pull request preferred |
| `chatgpt-generated/` | Machine-generated Markdown | Must be validated and reviewed |
| `cooking-agent/` | Independent Python example | Own dependencies and tests |
| `.github/workflows/` | CI configuration | Owner review required |
| Root JSON/config files | Integration metadata | Sanitized, no credentials |

## 4. Security model

- Keep the repository public only for sanitized content.
- Never commit PATs, API keys, webhook secrets, private keys, `.env` files, or signing material.
- Prefer the workflow-provided `GITHUB_TOKEN` for Actions.
- Use the smallest token scope when an external connector is unavoidable.
- Treat configuration files as documentation; they do not grant permissions by themselves.
- Do not describe an integration as having `admin`, `delete`, or unrestricted workflow authority unless that access is actually required and separately controlled.

## 5. Automation model

Automation should be **bounded and reviewable**:

- CI validates changes; it does not administer the repository.
- Generated output is limited to an explicitly documented directory.
- Destructive operations are never automatic.
- Scheduled jobs are low frequency and idempotent.
- Workflow permissions default to read-only and are elevated only for a specific job.
- Automation failures are visible through Actions checks and issues, not hidden retries that mutate more files.

## 6. Free-tier cost controls

- Prefer Markdown, JSON, and small source files.
- Do not store large media, datasets, APKs, ZIPs, or build outputs in Git history.
- Upload only small, temporary CI artifacts when necessary; do not use Actions artifacts as permanent storage.
- Avoid unnecessary scheduled workflows and matrix builds.
- Keep Python dependencies small and cache only when it materially reduces runtime.

## 7. Definition of done

The target is achieved when:

- every change to `main` is reviewable;
- CI validates Markdown and Python content;
- no committed file contains a secret;
- generated content has a documented owner and destination;
- the connector documentation describes least privilege rather than unrestricted access;
- the repository remains useful if ChatGPT/Copilot automation is unavailable.

## References

- [GitHub plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans)
- [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions)
- [Repository limits](https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits)
- [Workflow permissions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#permissions)
