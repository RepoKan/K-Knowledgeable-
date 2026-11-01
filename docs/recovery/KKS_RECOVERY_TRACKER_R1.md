# KKS Recovery Tracker R1

**Status:** IN PROGRESS — feature-branch proposal; not merged  
**Target repository:** `RepoKan/K-Knowledgeable-` (public, sanitized repository)  
**Base branch:** `main`  
**Feature branch:** `recovery/kks-infrastructure-and-knowledge-sync-r1`

## Repository identity boundary

The originally requested `RepoKan/KTC-Knowledge-Master` repository is not currently accessible through the connected GitHub integration. This recovery proposal therefore targets the accessible `RepoKan/K-Knowledgeable-` repository only. It does not claim that the two repositories are identical, and it does not migrate, delete, or overwrite any historical knowledge.

## Objective A — infrastructure and MCP reliability

### Confirmed baseline

- The MCP Source Explorer is a local-only, fixture-backed candidate. It is not deployed and has no authenticated GitHub or payment-system integration.
- The existing MCP validation workflow already runs fixture tests, `npm audit --audit-level=high`, TypeScript validation, build, and loopback runtime checks.
- The latest inspected CI failures stop at the dependency audit. Subsequent TypeScript, build, and runtime stages are skipped because the audit gate fails.
- The failing dependency set includes `@hono/node-server`, `body-parser`, `vite`, and/or `zod`, depending on the Dependabot update branch.
- The existing Dependabot update path reported a compatibility constraint: Skybridge 2.0.3 and its MCP dependency chain require `@hono/node-server@^1.19.9`. A forced major-version override is not accepted as a safe fix without compatibility tests.
- Open Dependabot PR #42 updates Vite in the MCP app; it must be evaluated with the full lockfile audit and runtime checks before adoption.

### Remediation policy

1. Preserve `npm audit --audit-level=high`; do not suppress advisories or lower the threshold to make CI green.
2. Refresh the lockfile only with a dependency graph that satisfies upstream peer/range constraints.
3. Prefer upstream compatible releases and reviewed Dependabot changes over speculative overrides.
4. Run locked installation with lifecycle scripts disabled, fixture tests, full TypeScript check, production build, actual loopback MCP protocol checks, and dependency audit.
5. Record the exact commit SHA and all CI outcomes. A local result or old successful run is not proof for a new head SHA.
6. If no compatible patched dependency graph exists, leave the gate failing and document the upstream blocker rather than weakening the security boundary.

### Explicit non-goals

No public tunnel, cloud deployment, host registration, secrets, private repository access, payment processing, Production configuration, or changes to existing Continue/Copilot MCP settings.

## Objective B — governed knowledge synchronization

### Implemented proposal in this branch

- Add an allowlisted catalog of official Kotlin, Android Compose, Kotlin Multiplatform, OpenAI Codex developer, and GitHub Actions documentation.
- Add a metadata-only source freshness checker. It records HTTP status, final allowlisted URL, content type, ETag, Last-Modified, and a bounded response-body digest.
- Add a weekly GitHub Actions schedule and manual trigger. The report is retained as a workflow artifact and job summary.
- The workflow has read-only repository permissions. It does not commit, open PRs, replace knowledge files, or promote source content automatically.
- Keep Codex Enterprise Analytics schema and authentication claims explicitly unresolved until checked against the authenticated canonical reference. General Codex developer docs are not evidence for Analytics API routes or schemas.

### Human review / promotion process

1. Inspect the source freshness report and source revision/date.
2. Confirm the page is official and relevant to the exact topic.
3. Compare substantive content against the existing knowledge entry.
4. Record changed facts, version, provenance, conflicts, and uncertainty.
5. Prepare a separate reviewable content change on a feature branch.
6. Run governance validation and request human review before merge.

A successful HTTP check means only that a URL responded. It does not prove semantic correctness, official status beyond the catalog decision, API compatibility, or approval to update knowledge.

## Governance gates

| Gate | Current state | Evidence / next action |
|---|---|---|
| 1. Define scope | CONTINUE | Both objectives; accessible public repository only |
| 2. Verify evidence | CONTINUE | Current tree, workflow, package metadata, governance docs, and prior run evidence inspected |
| 3. Assess impact | CONTINUE | Changes are isolated to source-check automation and recovery documentation |
| 4. Make decision | RECOMMENDED | Add metadata-only source freshness; retain strict security audit |
| 5. Confirm authorization | AUTHORIZED WITH BOUNDARIES | User approved both objectives; no merge/deploy/Production/payment actions |
| 6. Confirm readiness | PARTIAL | Source-sync proposal is implementable; dependency remediation needs compatible patched graph |
| 7. Pre-execution gate | CONTINUE FOR FEATURE-BRANCH PROPOSAL | No main-branch write |
| 8. Execute | IN PROGRESS | Feature branch and proposal files |
| 9. Verify | NOT RUN | Must run PR checks against exact head SHA |
| 10. Report | PENDING | Complete after PR creation and check inspection |

## Acceptance criteria

- [ ] Feature branch contains only scoped changes.
- [ ] JSON catalog parses and every source has a valid allowlisted host.
- [ ] Python checker passes syntax and unit tests; redirect-host restrictions work.
- [ ] Scheduled/manual workflow passes on the exact PR head.
- [ ] Existing MCP dependency audit passes without advisory suppression.
- [ ] Fixture, TypeScript, build, and runtime protocol checks pass.
- [ ] Codex Analytics conflict remains explicitly marked until authenticated verification.
- [ ] Human review is complete before merge.
- [ ] No Production/payment or external deployment boundary is crossed.

## Rollback

Close the proposal PR and delete the feature branch if rejected. The workflow is read-only and creates no repository commits or external deployments. Existing knowledge files and production/payment systems remain untouched.
