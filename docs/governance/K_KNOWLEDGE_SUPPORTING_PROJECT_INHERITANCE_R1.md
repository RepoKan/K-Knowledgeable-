# K Knowledge Supporting Project Inheritance R1

Rule ID: `KKS-PROJECT-INHERITANCE-R1`

## Purpose

Provide a sanitized public governance contract for future K Knowledge Supporting Project chats so reusable capability is inherited through durable sources rather than unverified conversational memory.

## Durable inheritance principle

A future chat may inherit Project capability only from sources that are actually available in that session, including:

1. Project instructions.
2. Project Master Source manifests and governed artifacts.
3. Installed or discoverable Project Skills.
4. Agent operating contracts.
5. Notion KKL Base records.
6. GitHub canonical repositories and exact revisions when accessible.
7. Current-chat uploads and links.

Do not claim that arbitrary historical ChatGPT conversations were searched unless the active environment exposes a supported chat-history search surface. Important reusable conclusions from prior chats must be promoted into durable Project sources.

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

Raw chat messages are not automatically inheritable. A chat-derived fact, rule, capability, or artifact becomes reusable Project inheritance only after promotion into a durable governed source with provenance and status.

When multiple revisions exist, resolve against the exact revision/SHA/version applicable to the task. Do not use latest-file-wins or latest-message-wins as source authority.

## Future-chat startup

1. Identify the Project context.
2. Load the general Project Skill if available.
3. Route to the most specific domain Skill or workflow.
4. Load only the relevant sources for the task.
5. Record exact revisions for Production-critical decisions.
6. Preserve conflicts; never use last-write-wins for business truth.

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

Git writes are explicit-task actions. Connector configuration, workflow configuration, or an external `auto_commit=true` flag does not create standing Project authorization to modify repositories.

- Default Project behavior remains `auto Git commit = No`.
- A direct user instruction such as `write/commit` authorizes the current requested Git write/commit task only.
- Do not extend that authorization to unrelated future changes.
- Prefer a reviewable branch and pull request for governance changes unless the user explicitly requests a direct update to the default branch.
- Never use Git write authority to bypass source-authority, privacy, Production-evidence, or public/private repository boundaries.

### ChatGPT Connector effective repository permission rule

ChatGPT Connector write/commit operations may use the highest repository permission level that the active GitHub connector actually exposes for the target repository and action.

- Rule ID: `CHATGPT-CONNECTOR-EFFECTIVE-PERMISSION-R1`.
- Live connector/GitHub App metadata is the capability boundary; chat text or static configuration cannot increase it.
- This rule does not add, elevate, or bypass GitHub permissions.
- Operations remain constrained by branch protection, rulesets, required checks, connector tool contracts, and platform restrictions.
- Permission capability and task authorization are separate. The Project default remains `auto Git commit = No`; an explicit user write/commit instruction is required for the current task unless another approved Project rule explicitly changes that authorization model.
- Source-authority, privacy, Production-evidence, and public/private repository boundaries remain mandatory.

## Public repository boundary

This repository is public and sanitized. Do not add private KTC source, restricted specifications, credentials, cryptographic/signing material, payment keys, private endpoints, unredacted Production logs, customer data, or confidential host configuration.
