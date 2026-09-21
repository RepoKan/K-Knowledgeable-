# Free-Tier GitHub Architecture Strategy

This document defines a safer, cheaper, and more maintainable architecture for a personal GitHub repository that uses GitHub Free as its default operating model.

## Objective

Design a repository architecture that keeps the project usable for:

- version control
- pull requests
- issue tracking
- lightweight CI/CD
- docs and knowledge storage
- automation within free-tier limits
- clear separation of secrets and generated content

It should also remain compatible with a personal GitHub account and avoid patterns that require enterprise features or over-privileged repository access.

## Design principles

1. Prefer public, low-risk content in the repository.
2. Store secrets outside the repository, never in committed files.
3. Limit automation to a narrow, documented scope.
4. Keep generated artifacts in one folder such as `docs/` or `generated/`.
5. Use branch protection, pull requests, and required checks when possible.
6. Keep the repository small and readable.
7. Use GitHub Actions only for simple validation and scheduled tasks.
8. Treat GitHub Free as a practical baseline, not as a premium automation platform.

## Recommended architecture

### 1. Repository structure

```text
.
├── .github/
│   ├── workflows/
│   │   ├── validate-docs.yml
│   │   └── scheduled-sync.yml
│   └── dependabot.yml
├── docs/
│   ├── architecture/
│   ├── governance/
│   ├── guides/
│   └── generated/
├── src/
│   └── (app or bot logic)
├── scripts/
│   └── (small automation)
├── tests/
│   └── (basic validation)
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
└── .env.example
```

### 2. Content model

- `docs/` holds durable documentation, architecture references, and user-facing content.
- `generated/` stores output created by automation, but only after validation.
- `src/` contains Python or other code, kept small and testable.
- `scripts/` contains one-off utilities and CI helpers.
- `tests/` confirms parsing, formatting, and build sanity.

### 3. Automation model

Keep automation minimal and governed:

- trigger validation on pull requests
- trigger only simple scheduled processes
- avoid autonomous repository-admin behavior
- use clearly separated script folders
- do not auto-delete files without review
- never write secrets to files or commit tokens

### 4. Security model

Use the principle of least privilege:

- secrets in GitHub Actions secrets or environment variables
- no PATs in repository files
- rotate credentials regularly
- restrict write scopes to the required branch or docs path
- avoid broad admin-level permissions in automation config

### 5. Free-tier operating posture

For GitHub Free, the project should stay within these guardrails:

- public or low-volume private repos only
- small documentation-first repo
- modest GitHub Actions minutes and artifact sizes
- no large binaries in the Git history
- no heavy package caches or large dependencies on a routine basis
- no storage of large PDFs, APKs, or media assets in the repo

## Suggested workflow

### Standard flow

1. contributor creates a branch
2. edits docs or scripts
3. opens pull request
4. CI validates markdown, syntax, or tests
5. reviewer approves
6. merge to main

### Auto-generation flow

1. script reads source data
2. writes generated content to `docs/generated/`
3. validation step checks the output
4. output is reviewed in a PR
5. merge only after successful checks

## Recommended guardrails for this repository

This repository currently includes a strong automation design and a connector-style configuration that assumes broad write and admin rights. For a free-tier best-practice model, those rights should be scaled down.

Recommended changes:

- keep automation focused on docs and generated content only
- avoid `delete` and `admin` permission assumptions in config
- write generated output only to a controlled folder
- use a single validation workflow instead of many broad automation models
- document all automation behavior in `docs/`

## Decision summary

Best total-cost, best-maintenance model for GitHub Free:

- documentation-first repository
- modest automation
- narrow write scopes
- public content and minimal secrets
- review-driven changes
- low operational overhead

This model is safer, easier to maintain, and much more aligned with the spirit of free-tier GitHub usage than broad autonomous repository control.

## Reference links

- GitHub Plans: https://docs.github.com/en/get-started/learning-about-github/githubs-plans
- GitHub Actions billing and limits: https://docs.github.com/en/billing/concepts/product-billing/github-actions
- Repository limits: https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits
- Branch protection: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches

