# Free-Tier Best Practice Architecture

This architecture is optimized for a personal GitHub account operating under GitHub Free and focused on documentation, knowledge management, and small automation.

## Goals

- stay within GitHub Free limits
- keep repository safe and maintainable
- use clear review and governance patterns
- avoid unnecessary admin or automation privileges
- support a lightweight knowledge-driven workflow without enterprise features

## Architecture layers

### 1. Source layer

The source layer is the human-maintained part of the repository.

Recommended areas:

- `README.md`
- `docs/architecture/`
- `docs/guides/`
- `docs/governance/`
- `src/`
- `tests/`

Rules:

- keep source human-readable
- avoid committing secrets
- keep the repo mostly text-based
- prefer markdown and scripts over large binary assets

### 2. Processing layer

Use scripts or GitHub Actions to process knowledge or generated content. Keep processing deterministic.

Examples:

- markdown validation
- content linting
- small generated summaries
- scheduled updates limited to docs or generated folders

Recommended practices:

- no delete-by-default automation
- no direct repo-admin operations
- all generated content goes to a controlled directory
- pipeline is idempotent and reviewable

### 3. Validation layer

Use CI to validate:

- markdown structure
- YAML syntax
- Python syntax
- script execution against sample data
- missing required metadata

Example workflow responsibilities:

- `markdownlint` or comparable checks
- Python unit tests
- static validation of generated files
- check for unsafe secret patterns

### 4. Review layer

Use pull requests as the main policy model.

Recommended controls:

- require review for `main`
- restrict direct pushes if possible
- enforce checks before merge
- review generated content before publishing

### 5. Monitoring layer

Use built-in platform feedback instead of custom heavy observability.

Use:

- Actions status pages
- workflow logs
- repository checks
- issue and pull request review history

Avoid:

- large custom monitoring stacks
- per-commit event pipelines
- external monitoring solutions unless they are essential

## Recommended automation policy

### Allowed automation

- scheduled doc refresh
- generated Markdown summary creation
- CI validation
- simple content quality checks
- small repository health scripts

### Avoided automation

- repo-wide delete operations
- broad bot permissions
- admin-level automation
- high-frequency network polling
- writing secrets into config files
- uncontrolled binary generation

## Recommended repository policy

- keep generated files in `docs/generated/` or similar
- allow bot writes only to a known folder
- use manual review for large changes
- prefer deterministic, small files
- keep history clean and intentional

## Security best practices

1. Use `GITHUB_TOKEN` in workflows where possible.
2. If PATs are necessary, use the smallest scope required.
3. Store secrets in repository secrets or environment variables.
4. Never commit API keys, tokens, or credentials.
5. Review workflow triggers and branch scopes.
6. Validate code before using it in automation.

## Summary

The best free-tier architecture is not a large autonomous connector. It is a disciplined, text-first, review-driven repository with narrow automation, clear folder boundaries, and minimal permissions. This is the safest model for a personal repository under GitHub Free.

