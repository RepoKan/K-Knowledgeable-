# Free-Tier Improvement Plan for K-Knowledgeable-

## Phase 0 — Safety audit

- Search the full Git history and current tree for tokens, keys, passwords, and private URLs.
- Rotate any credential that may have been committed, even if later deleted.
- Confirm that public `knowledge-supporting/` content is sanitized.

## Phase 1 — Documentation correction

- Replace unrestricted connector language with the `KKS-ARCH-FREE-R1` security model.
- Explain that configuration files do not grant GitHub permissions.
- Correct repository metadata and remove claims that cannot be verified from the repository.

## Phase 2 — Content boundaries

- Keep durable knowledge under `knowledge-supporting/`.
- Keep architecture and governance under `docs/`.
- Keep generated content under `chatgpt-generated/` or `docs/generated/`, not both without a clear reason.
- Keep application examples isolated in their existing directories.

## Phase 3 — CI simplification

- Retain only workflows with a clear purpose.
- Add Markdown, Python syntax, JSON/YAML parsing, and basic secret-pattern checks.
- Set explicit minimal workflow permissions.
- Avoid uploading permanent artifacts to Actions.

## Phase 4 — Review and branch controls

- Use a branch and pull request for generated or structural changes.
- Require successful checks before merging where available.
- Prevent force pushes and accidental deletion of `main`.
- Reserve direct commits for trivial, low-risk personal maintenance.

## Phase 5 — Connector hardening

- Use read-only access for inspection.
- Permit writes only to the approved generated-content path.
- Do not permit automatic deletion or workflow administration.
- Require explicit human approval for workflow, governance, security, or destructive changes.

## Phase 6 — Ongoing maintenance

Monthly or before a significant release:

- review Actions usage and failures;
- remove unused workflows and dependencies;
- check repository size and large files;
- review collaborator and token access;
- update architecture documentation when the project purpose changes.

## Prioritization

**Do first:** secret audit, permission-language correction, generated-path decision.  
**Do next:** workflow cleanup, CI validation, branch/review controls.  
**Do later:** static documentation publishing, richer tests, external artifact storage.

## Success measure

The project remains useful as a public personal knowledge base with small experiments, while a connector failure or accidental automation run cannot administer the repository or silently destroy unrelated content.
