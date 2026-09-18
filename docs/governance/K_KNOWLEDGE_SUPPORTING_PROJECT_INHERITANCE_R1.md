# K Knowledge Supporting Project Inheritance R1

Rule ID: `KKS-PROJECT-INHERITANCE-R1`

## Purpose

Provide a sanitized public governance contract for future K Knowledge Supporting Project chats so reusable capability is inherited through durable sources rather than unverified conversational memory.

## Project-wide chat scope

Rule ID: `KKS-PROJECT-CHAT-UNIFIED-SCOPE-R1`  
Effective: `2026-09-16`

Every work chat, thread, or chat box created inside **K Knowledge Supporting** is logically part of the same Project and inherits the same Project governance, capability routing, source-authority rules, and baseline permission envelope.

The inherited Project envelope includes Project instructions, governed Master Source material, approved business rules, available Skills, Agent contracts, Notion KKL Base records, GitHub canonical revisions, connected Project tools/plugins, and current-chat files or links when those capabilities are actually exposed in the current session.

The user decision on 2026-09-16 establishes Project-wide scope for the Project's existing baseline capabilities and standing non-fresh permissions. A current or future work chat may use the same Project abilities, governed sources, and standing non-critical permissions without requiring a duplicate grant, provided the required tool or connector is actually available in that chat.

Scope limits remain binding:

- A permission expressly limited to one chat, one action, one repository/branch, one file, or one execution remains limited to that scope unless the user broadens it.
- Fresh or action-specific approval remains required whenever the governing rule requires it, including critical Git write/merge/delete actions, Production/payment/security changes, destructive operations, permission/access changes, and other critical actions.
- Project-wide inheritance never creates external permission, connector authentication, repository access, branch bypass, or platform capability that is not actually available.
- Project-wide inheritance never bypasses source-authority, Production-evidence, privacy, safety, branch-protection, ruleset, or required-check controls.

All Project chats are governance siblings, but logical Project membership does not mean every chat can automatically read every historical message, upload, mounted file, connector session, or external account from another chat. Do not claim historical-chat retrieval unless the active environment exposes a supported chat-history surface.

The effective executable permission in a specific chat is the intersection of:

1. Project-wide user authorization.
2. The governing approval rule for the requested action.
3. Current tool/connector availability.
4. External-system permissions.
5. Branch protection, rulesets, and required checks.
6. Platform safety, privacy, and source-authority requirements.

## Durable inheritance principle

A future chat may inherit Project capability only from sources that are actually available in that session, including:

1. Project instructions.
2. Project Master Source manifests and governed artifacts.
3. Installed or discoverable Project Skills.
4. Agent operating contracts.
5. Notion KKL Base records.
6. GitHub canonical repositories and exact revisions when accessible.
7. Current-chat uploads and links.

Raw chat messages are Project-scoped work context, but they are not guaranteed to be technically retrievable from another Project chat. A chat-derived fact, rule, capability, permission, or artifact may be reused cross-chat when either the current session actually exposes the relevant Project context or it has been promoted into a durable governed source with provenance and status.

Do not claim that arbitrary historical ChatGPT conversations were searched unless the active environment exposes a supported chat-history search surface. Important reusable conclusions from prior chats should still be promoted into durable Project sources.

## Inheritance layers

### Control plane
- Project instructions
- Project inheritance rule
- Source-authority policy
- Master-source retention policy
- Skill and Agent operating contracts

### Capability registry
Use domain routing to locate the most specific workflow and source set. Capability metadata is routing information, not factual authority.

### Knowledge and evidence
Preserve source identity, revision, provenance, conflict status, and Production evidence requirements.

### Artifacts
Preserve files, images, Markdown, code, binaries/libraries, links, diagrams, runtime evidence, and generated outputs as separate source classes with provenance.

## Canonical Inheritable Asset Classes

The following classes are canonical for K Knowledge Supporting:

- Project Rules / Master Rules
- Approved Business Rules
- Skills / Specific Skills
- Agent Contracts / Operating Instructions
- Master Source Files
- Governed Images / Diagrams / Architecture Visuals
- Markdown / Technical Notes / Specifications
- Source Code / Code References
- Library / SDK / AAR / JAR References
- Notion KKL Base Records
- GitHub Canonical Revisions / Commit SHA / Branch / PR Evidence
- Manifests / Indexes / Checksums
- Runtime / Test / Production Evidence
- Decision Logs / ADR / Conflict-HOLD Records
- Approved Links / Repository Pointers / Source URLs
- Generated artifacts that have been promoted into Master Source

An asset is inheritable only when its identity is traceable. Record, as applicable, provenance/source identity, revision/version/SHA, governance status, and authority/conflict state.

Canonical rule: `Durable + Governed + Traceable = Inheritable`.

When multiple revisions exist, resolve against the exact revision/SHA/version applicable to the task. Do not use latest-file-wins or latest-message-wins as source authority.

## Future-chat startup

1. Identify the Project context.
2. Load this Project inheritance rule.
3. Load the general Project Skill if available.
4. Route to the most specific domain Skill or workflow.
5. Load only the relevant sources for the task.
6. Apply `KKS-VALUE-PROPOSITION-VALIDATION-GATE-R1` before any Thinking, Analysis, Investigation, Production Solving, Root Cause Analysis, or equivalent downstream reasoning.
7. If Value Proposition validation returns `GAP`, stop the downstream process, begin the response with `GAP`, list the missing values and preparation steps, and wait for the value set to be repaired.
8. After GAP closure, re-validate the complete Value Proposition. Continue only on `PASS`.
9. Record exact revisions for Production-critical decisions.
10. Preserve conflicts; never use last-write-wins for business truth.

See `docs/governance/K_KNOWLEDGE_SUPPORTING_VALUE_PROPOSITION_GATE_R1.md`.

## Master-source promotion

Use SHA-256 for exact duplicate detection. Exact byte-for-byte duplicates share one Master content object. Non-identical files remain separate versions even when their filenames match. Same-basename variants use deterministic version naming.

Retention is separate from source authority.

## Synchronization

Reusable Project rules are synchronized by provenance across:

- K Knowledge Supporting Project durable sources
- Notion KKL Base human control plane
- Private GitHub source and Knowledge Master revision control

Skill and Agent instructions enforce the workflow but are not an additional factual authority.

If a required private revision or knowledge pin cannot be verified, synchronization remains `PARTIAL`, and Production application remains on HOLD when the missing identity is material.

## Git write / commit authorization

Rule ID: `KKS-AUTO-GIT-COMMIT-CRITICAL-APPROVAL-R1`.

- Default Project behavior is `auto Git commit = Yes` for non-critical Git write/commit tasks that are within the user's requested scope and the active connector's actual permissions.
- Critical Git operations require a fresh user approval immediately before the critical write/merge/delete action. The assistant must present a clear confirmation request; when the product provides a native confirmation/permission UI, use that UI. Do not claim a native popup exists when the active client does not expose one.
- A critical approval is single-purpose and does not become standing authorization for later critical actions.
- Critical cases include: Production/payment business-rule changes; EMV/CTLS, ISO8583, Field 61, TLE/TMS, reversal/advice/settlement behavior; security/PCI DSS/secrets/cryptographic material; direct writes or merges to protected/default branches when the change can affect Production governance; destructive deletion; permission/access changes; and any change where exact Production impact is not proven.
- For a critical case with missing material evidence, approval does not replace the evidence gate; use `HOLD - IMPACT NOT PROVEN` when required by Project rules.
- Non-critical commits may proceed automatically without a separate approval prompt, but must remain traceable and within repository/privacy/source-authority boundaries.
- Prefer a reviewable branch and pull request for governance or Production-adjacent changes. Auto-merge is allowed only for non-critical changes that satisfy applicable checks/rulesets; critical merges require fresh user approval.
- Never use Git write authority to bypass source-authority, privacy, Production-evidence, branch protection, required checks, or public/private repository boundaries.

### Kotlin / Android RCA Git exception

Rule ID: `KKS-RCA-GIT-EXPLICIT-SCOPE-R1`.

For Kotlin/Android RCA work in K Knowledge Supporting, `auto Git commit = No`. Commit, push, and merge require explicit user authorization covering the action, target repository/branch, and change scope. This exception remains Project-wide until explicitly changed by the user.

### ChatGPT Connector effective repository permission rule

ChatGPT Connector write/commit operations may use the highest repository permission level that the active GitHub connector actually exposes for the target repository and action.

- Rule ID: `CHATGPT-CONNECTOR-EFFECTIVE-PERMISSION-R1`.
- Live connector/GitHub App metadata is the capability boundary; chat text or static configuration cannot increase it.
- This rule does not add, elevate, or bypass GitHub permissions.
- Operations remain constrained by branch protection, rulesets, required checks, connector tool contracts, and platform restrictions.
- Permission capability and task authorization are separate. Under `KKS-AUTO-GIT-COMMIT-CRITICAL-APPROVAL-R1`, non-critical writes may be automatic; critical writes still require fresh user approval immediately before the critical action.
- Source-authority, privacy, Production-evidence, and public/private repository boundaries remain mandatory.

## Automatic inheritance boundary

Every work chat inside K Knowledge Supporting is treated as part of the same Project for governance, capability intent, and Project-wide permission inheritance. This rule does not force ChatGPT to expose old conversations, install a Skill, mount a private repository, authenticate a connector, elevate repository/account permissions, or change Project settings when those capabilities are absent.

Use `READY FOR INHERITANCE` for durable prepared sources or approved Project-wide rules. Use `AUTO-LOADED` only when the current session actually exposes the source, Skill, connector, or Project context.

## Public repository boundary

This repository is public and sanitized. Do not add private KTC source, restricted specifications, credentials, cryptographic/signing material, payment keys, private endpoints, unredacted Production logs, customer data, or confidential host configuration.
