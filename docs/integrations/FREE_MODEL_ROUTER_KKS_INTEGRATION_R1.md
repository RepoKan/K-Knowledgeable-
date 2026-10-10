# Free Model Router v1.5.0 -> K Knowledge Supporting Integration R1

Status: `CANDIDATE / REVIEWABLE INTEGRATION DESIGN`

Date: 2026-10-02

External source: https://gitlab.com/snipedbywifi-workspace/free-model-router/-/releases/v1.5.0

## Purpose

Integrate Free Model Router / Router Chat v1.5.0 into K Knowledge Supporting as an optional execution and model-routing workspace without allowing it to become a new factual or revision authority.

The integration follows the existing KKS authority chain:

```text
FACTS
  -> EVIDENCE
  -> KNOWLEDGE
  -> WORKFLOW
  -> IMPLEMENTATION
  -> REVISION
  -> HUMAN-GOVERNED CHANGE
```

Router Chat operates in the WORKFLOW / IMPLEMENTATION support layers. It does not override exact repository revision truth, Production evidence, approved specifications, or human-governed change gates.

## KKS role assignment

| Layer | System | Role |
| --- | --- | --- |
| Revision truth | GitHub | Canonical public/sanitized governance and integration revision record |
| Knowledge control | Notion KKL Base | Human-readable architecture, decisions, provenance, status, and links |
| AI execution workspace | Router Chat | Project workspace, file-context orchestration, model routing, worker/subagent execution, governed command execution |
| Project orchestration | ChatGPT / KKS Skills | Capability routing, evidence gating, source-authority enforcement, cross-source synthesis |
| Production authority | Exact Production source/spec/runtime evidence | Highest authority when applicable |

## Router Chat integration boundary

Router Chat may be used for:

- isolated project workspaces;
- source/document review using project-scoped files;
- task decomposition through workers/subagents;
- model-provider experimentation;
- command execution when the local command policy explicitly permits it;
- draft architecture, tests, documentation, refactoring proposals, and investigation notes.

Router Chat must not independently:

- declare Production truth from generated output;
- replace exact GitHub SHA/ref evidence;
- promote an inferred business rule into an approved rule;
- publish secrets, credentials, private endpoints, confidential logs, payment/cardholder data, or private Production source;
- bypass branch protection, required checks, review gates, or human approval;
- treat a successful worker response as proof that code was built, tested, or deployed.

## Proposed workspace layout

```text
Router Chat
└── K-Knowledge-Supporting
    ├── 00-governance
    │   ├── AGENTS.md
    │   └── PROJECT_INSTRUCTIONS.md
    ├── 10-public-knowledge
    │   └── sanitized KKS docs
    ├── 20-working
    │   ├── drafts
    │   ├── investigations
    │   └── temporary artifacts
    └── 90-local-private
        └── non-synced local material only
```

The `90-local-private` area is intentionally excluded from public Git synchronization. Sensitive or confidential sources remain in approved private stores and are referenced by provenance rather than copied into the public repository.

## Model-routing rule

Router Chat model selection is execution metadata, not evidence.

Use the existing KKS model policy first. The model selected inside Router Chat may vary by task, cost, latency, or provider availability, but changing the model must not change source authority or approval requirements.

Recommended pattern:

```text
KKS task classification
  -> risk / evidence gate
  -> choose Router Chat workspace
  -> choose model / worker
  -> execute bounded task
  -> capture result + provenance
  -> validate against source
  -> persist only reviewed output
```

## GitHub integration

Repository: `RepoKan/K-Knowledgeable-`

GitHub remains the revision plane for sanitized KKS integration material.

Required discipline:

1. pin the current base ref and full SHA before a version-sensitive change;
2. use a feature branch for Router integration changes;
3. keep public-repository content sanitized;
4. compare the complete `base...head` diff;
5. record CI as `NOT RUN` when no validation run exists;
6. use a PR for review;
7. require fresh merge approval under KKS governance.

## Notion integration

Notion KKL Base remains the human-readable control plane.

The Router Chat record should capture:

- external release/source link;
- KKS integration status;
- GitHub base SHA and integration branch/PR;
- architecture and authority boundaries;
- current capability assumptions;
- validation gaps;
- follow-up decisions and test evidence.

Notion does not replace GitHub revision truth or Production evidence.

## Optional external-source expansion

GitLab can remain the upstream external source for Router Chat releases.

A future direct GitLab MCP integration is allowed only after the active Router Chat environment is proven to support the required MCP client/transport and authentication flow. Until then, use the upstream release/repository as an external reference rather than assuming live MCP capability.

## Acceptance gates

The Router Chat integration can move from `CANDIDATE` to `ACTIVE` only when the applicable checks pass:

- exact KKS GitHub base/ref/SHA recorded;
- Notion knowledge record created and linked;
- public/private data boundary verified;
- one non-Production pilot workspace completed;
- command policy verified with a harmless read-only command;
- project-skill scope verified;
- worker/subagent output trace reviewed;
- no secret or private Production material synchronized to the public repo;
- rollback/removal path documented.

## Pilot recommendation

Start with a non-Production documentation/research task.

Example pilot:

```text
GitHub sanitized docs
   -> Router Chat KKS workspace
   -> worker/subagent review
   -> draft improvement
   -> source comparison
   -> Notion evidence note
   -> optional GitHub PR
```

Do not use a payment-critical Kotlin/EMV/ISO8583 change as the first integration test.

## Rollback

Rollback is administrative:

1. stop using the Router Chat KKS workspace;
2. revoke any external provider/API credentials from the credential owner;
3. remove local project mappings;
4. close or revert unmerged GitHub integration changes;
5. mark the Notion integration record `INACTIVE / RETIRED`.

Existing KKS source authority and governance remain unchanged.

## Current conclusion

`INTEGRATION DESIGN READY FOR PILOT`

Router Chat is treated as a replaceable execution layer. KKS governance, GitHub revision truth, Notion knowledge control, and exact Production evidence remain the durable authority structure.
