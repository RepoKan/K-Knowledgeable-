# K-Knowledgeable-: GitHub Connector Governance Guide

**Repository:** `RepoKan/K-Knowledgeable-`  
**Visibility:** Public  
**Purpose:** Sanitized K Knowledge Supporting governance, connector guidance, and project pointers.

## Operating contract

This repository documents how a GitHub connector may be used. A connector's technical capability is not authorization to perform an action.

All repository changes follow this path:

1. Read the exact current file and revision.
2. Create or use a feature branch.
3. Make the smallest scoped change.
4. Run validation and inspect the diff.
5. Open a pull request.
6. Obtain human review and approval before merge.

Direct commits to `main`, automatic merges, deletion, permission changes, workflow administration, and Production/payment/security changes require fresh, action-specific authorization. Never bypass branch protection, rulesets, required checks, or repository permissions.

## Safe connector defaults

- Autonomous processing: disabled.
- Automatic commits: disabled.
- Default write target: feature branch only.
- Pull requests: required for repository changes.
- Human approval: required before merge and other critical actions.
- Secrets: never place tokens, private keys, PAN, SAD, customer data, private endpoints, or unredacted Production logs in this public repository.
- Public boundary: keep only sanitized governance, architecture, connector guidance, and pointers.

The checked-in `chatgpt-connector-channel.json` is descriptive configuration metadata. It does not create GitHub permissions, bypass repository rules, or prove that the active connection can perform an operation.

## Repository layout

| Path | Purpose |
|---|---|
| `AGENTS.md` | Project-wide KKS governance |
| `activation/PROJECT_INSTRUCTIONS.md` | Project startup and permission rules |
| `docs/governance/` | Canonical governance documents |
| `chatgpt-generated/` | Sanitized generated knowledge, when approved |
| `chatgpt-connector-channel.json` | Governance-gated connector metadata |
| `scripts/validate_kks_governance.py` | Deterministic safety validation |
| `.github/workflows/kks-governance-validation.yml` | Pull-request validation |

## Read/write behavior

Read operations may inspect public repository content when the active connection allows it. A write request must identify:

- repository and exact branch;
- file paths in scope;
- intended change;
- evidence or source revision;
- validation plan.

For an existing file, fetch the current content and blob SHA before updating it. Do not overwrite a changed file with a stale SHA. For multiple edits to one path, apply them sequentially.

A failed GitHub API call is an authorization or availability result, not permission to fall back to `main`, an unrelated branch, or a different repository.

## Workflow and synchronization

Synchronization means preparing and reviewing a proposed change. It does not mean silently pushing to `main` or treating the connector as an autonomous administrator. Workflow creation, updates, deletion, dispatch, cancellation, and reruns remain explicit operations governed by the current connection permissions and KKS approval rules.

## Verification checklist

Before opening a pull request:

- [ ] The change is on a feature branch based on the current target revision.
- [ ] The diff contains only the requested scope.
- [ ] Connector config parses as JSON.
- [ ] Autonomous processing and automatic commits are disabled.
- [ ] README and connector guide remain consistent.
- [ ] No credentials or private payment data are present.
- [ ] Validation passes.
- [ ] The pull request is reviewable and is not merged automatically.

## Canonical rules

See `AGENTS.md`, `activation/PROJECT_INSTRUCTIONS.md`, and the governance documents under `docs/governance/`. These rules are authoritative for KKS process and approval boundaries; this guide must not weaken them.
