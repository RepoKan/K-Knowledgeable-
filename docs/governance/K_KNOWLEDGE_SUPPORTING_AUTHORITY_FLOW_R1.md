# K Knowledge Supporting Authority Flow R1

Rule ID: `KKS-AUTHORITY-FLOW-R1`

Effective: `2026-09-29`

## Purpose

Establish a one-way, auditable authority flow for K Knowledge Supporting so facts, evidence, knowledge, workflow instructions, implementation, revision state, and governed change approval cannot silently replace one another.

Canonical flow:

```text
FACTS
  ↓
EVIDENCE
  ↓
KNOWLEDGE
  ↓
WORKFLOW
  ↓
IMPLEMENTATION
  ↓
REVISION
  ↓
HUMAN-GOVERNED CHANGE
```

## Authority separation

### FACTS

Facts are claims about the real system, code, specification, runtime, device, transaction, environment, or observed event.

Facts must be supported by the applicable source-authority rules. A workflow, preference, model output, Notion note, or Git branch name does not become a fact merely because it exists.

### EVIDENCE

Evidence is the traceable material used to support or challenge facts: exact source revision, approved specification, runtime log, trace, screenshot, test result, device state, host response, or other governed evidence.

Evidence determines factual support. Preserve provenance, revision, time, environment, conflict state, and uncertainty.

### KNOWLEDGE

Knowledge is the human-readable recording of supported findings, decisions, context, conflicts, and reusable conclusions.

Notion KKL Base is a knowledge/control plane. It records knowledge and provenance but does not replace source, specification, runtime evidence, or Git revision truth.

### WORKFLOW

Workflow defines how work is performed.

Skills, Agent contracts, Project instructions, and governed procedures determine workflow. They may require gates, checks, routing, validation, and reporting, but they do not create factual evidence.

`AGENTS.md` determines working style and operating constraints for agents. It does not supersede facts, evidence, approved specifications, or exact code revisions.

### IMPLEMENTATION

Implementation is the concrete code, configuration, document, automation, or artifact change produced after applicable evidence and workflow gates pass.

Implementation must not rewrite or self-approve the evidence that justified it. Proposed implementation remains a proposal until revision and approval gates are satisfied.

### REVISION

GitHub determines revision truth for governed repository content through exact repository, ref, commit SHA, tree/blob identity, compare state, pull request state, and merged target-branch head.

Notion summaries, chat descriptions, generated reports, and local working copies do not replace canonical Git revision evidence.

### HUMAN-GOVERNED CHANGE

Human approval determines governed changes where the applicable rule requires approval.

A component must not approve its own promotion into a higher authority layer. Critical or explicitly approval-gated operations remain blocked until the required user authorization is present and current.

## One-way promotion rule

Each layer may consume the output of the layer above it only through an explicit, traceable handoff.

- Evidence may support or challenge facts.
- Knowledge may record evidence-backed conclusions.
- Workflow may consume governed knowledge and evidence requirements.
- Implementation may execute an approved workflow.
- Revision control may record the implementation.
- Human approval may authorize governed promotion, merge, deployment, permission change, or other gated action.

No layer may silently promote its own output into another authority layer.

## Prohibited authority inversions

Do not allow any of the following shortcuts:

```text
Research output        -> self-declared fact without evidence
Preference learning    -> direct implementation mutation
Notion note            -> replacement for exact source/revision
Skill instruction      -> replacement for Production evidence
Generated code         -> rewrite of the evidence used to justify it
Feature branch         -> claim that main contains the change
CI not run             -> passed
Agent/tool capability  -> user authorization
Implementation         -> self-approval for merge/deploy
```

When an attempted shortcut is detected, stop the promotion and return the item to the correct authority layer.

## Auto Preference Learner boundary

Auto Preference Learner is a working-style learning mechanism only.

Its permitted flow is:

```text
Codex history
  ↓
Evidence extraction
  ↓
Candidate preference rule
  ↓
Scoped reconciliation
  ↓
SUGGEST
  ↓
Human acceptance of numbered proposal
  ↓
Managed AGENTS.md block
  ↓
Future governed workflow
```

It must not directly modify implementation, code architecture, WebMCP tools, Production behavior, factual conclusions, source authority, Git revision truth, or merge/deploy decisions.

Default mode remains `Suggest`. No candidate rule is written or committed until the user explicitly accepts the numbered proposal(s).

## GitHub and Notion handoff

GitHub is the revision control plane. Record exact repository/ref/SHA and validate `base...head` before promotion.

Notion is the knowledge/control plane. Record objective, evidence identity, findings, conflicts, decisions, validation state, and the corresponding Git revision or PR when applicable.

The two planes may cross-reference one another but neither silently overwrites the other's authority.

## Execution gates

For a material change:

1. Validate the Value Proposition and source identity.
2. Establish evidence and factual support.
3. Record reusable knowledge when appropriate.
4. Route through the most specific Skill/workflow.
5. Produce the smallest scoped implementation.
6. Verify the implementation and exact Git revision.
7. Present the reviewable diff, validation state, gaps, and risks.
8. Obtain fresh human approval when required by the governing rule.
9. Perform only the authorized governed change.
10. Re-fetch the resulting canonical revision and record the outcome.

## Status language

Use the following when material:

- `CONFIRMED` — directly supported by the applicable authority.
- `INFERRED` — reasoned from evidence but not directly observed.
- `NOT RUN` — validation or workflow execution did not occur.
- `SOURCE BOUNDARY` — evidence exists but cannot be promoted across the authority boundary.
- `GAP` — material input is missing or insufficient for the next stage.
- `HOLD` — downstream promotion is blocked until required proof or approval exists.
- `READY FOR REVIEW` — implementation/revision is prepared but not yet human-approved for a gated promotion.
- `SYNCED` — only when required governed knowledge/revision targets were updated and verified.

## Relationship to existing governance

This rule supplements and does not replace:

- `KKS-PROJECT-INHERITANCE-R1`
- `KKS-PROJECT-CHAT-UNIFIED-SCOPE-R1`
- `KKS-VALUE-PROPOSITION-VALIDATION-GATE-R1`
- `KKS-RULE-GOVERNANCE-UPDATE-GATE-R1`
- `KKS-GITHUB-CONNECTOR-FAST-PATH-R1`
- `KTC-PAYMENT-MASTER-R1`
- `KKS-RCA-GIT-EXPLICIT-SCOPE-R1`

When another rule is stricter, the stricter rule wins.

## Public repository boundary

This is sanitized governance only. Do not copy private KTC source, restricted specifications, credentials, keys, private endpoints, unredacted Production logs, customer/cardholder data, or confidential host configuration into this public repository.

Status: `ACTIVE / MERGED / VALIDATED`

Activation merge commit: `c0fa7592b7aee705447565b3ff23c1d582f04409`

Post-merge validation: GitHub Actions `KKS governance validation` run `36483961800` completed successfully on activation merge commit `c0fa7592b7aee705447565b3ff23c1d582f04409`.
