# K Knowledge Supporting Agent Governance

## Master rule

Use `KKS-PROJECT-INHERITANCE-R1` as the Project bootstrap contract and `KKS-PROJECT-CHAT-UNIFIED-SCOPE-R1` as the Project-wide chat/permission inheritance rule. Use `KTC-PAYMENT-MASTER-R1` as the sanitized governance baseline for KTC payment inspection workflows.

## Project-wide chat scope

Every work chat, thread, or chat box inside **K Knowledge Supporting** is a governance sibling in the same Project.

- Inherit the same Project governance, capability routing, source-authority rules, and baseline permission envelope.
- Project-wide standing non-critical permissions may be reused across Project chats without duplicate grant when the required tool or connector is actually available.
- A permission expressly limited to one chat, action, repository/branch, file, or execution remains limited to that scope.
- Fresh/action-specific approval still applies where the governing rule requires it, including critical Git write/merge/delete, Production/payment/security changes, destructive operations, and permission/access changes.
- Do not infer technical access from logical Project membership. A chat may not automatically expose historical messages, uploads, mounted files, connector sessions, or external accounts from another chat.
- Effective executable permission is the intersection of Project-wide user authorization, action-specific approval rules, current tool/connector availability, external permissions, branch/ruleset/check constraints, and platform safety/privacy/source-authority requirements.

See `docs/governance/K_KNOWLEDGE_SUPPORTING_PROJECT_INHERITANCE_R1.md`.

## Dynamic model routing

Use `KKS-MODEL-ROUTING-R1` from `docs/governance/K_KNOWLEDGE_SUPPORTING_MODEL_ROUTING_R1.md` whenever an explicit model choice is relevant.

- Resolve model availability from the active ChatGPT/Work/Codex/API surface first; a static repository file never grants model access.
- Prefer GPT-5.6 Sol for complex reasoning, coding, research, Production debugging, and cross-system RCA.
- Prefer GPT-5.6 Terra for routine professional work where capability/cost balance matters.
- Prefer GPT-5.6 Luna for simple, repetitive, high-volume, cost-sensitive work.
- Use GPT-6 Pro/Astra only when the active product/workspace actually exposes it and the task benefits from the highest-capability or long-running agentic workflow.
- Re-check current official OpenAI model availability when the routing verification is more than 7 calendar days old, when a model disappears or is renamed, or when a new model appears in the active surface.
- Model choice is routing metadata, not factual evidence; it never replaces exact Production source, approved specifications, runtime evidence, testing, or HOLD gates.

## Source synchronization

Treat the following as synchronized operational sources by revision and provenance, not as equal authorities:

1. K Knowledge Supporting Project
2. Notion KKL Base
3. Private GitHub Android + Knowledge Master pair

The exact Production source and approved evidence retain authority according to the master source-precedence rule. Skill and agent instructions enforce the process; they do not become authoritative Production evidence themselves.

## Git authorization

- Project default: `KKS-AUTO-GIT-COMMIT-CRITICAL-APPROVAL-R1`.
- Kotlin/Android RCA exception: `KKS-RCA-GIT-EXPLICIT-SCOPE-R1` — `auto Git commit = No`; commit, push, and merge require explicit authorization covering action, target repository/branch, and scope.
- Critical operations retain fresh, single-purpose approval immediately before the critical action even when Project-wide baseline permissions exist.
- Never use Project-wide inheritance to bypass branch protection, rulesets, required checks, external repository permissions, or Production evidence gates.

## Public repository boundary

This repository is public. Keep only sanitized governance, architecture, connector guidance, and pointers here. Do not add private KTC source, private specifications, credentials, payment/signing keys, private endpoints, unredacted Production logs, customer data, or confidential host configuration.

## Agent review gate

For Production-critical analysis:

- Identify exact source and Knowledge Master revisions.
- Verify the Android repository pins the exact Knowledge Master SHA used by the review.
- Identify applicable specification/runtime evidence when required.
- Trace relevant callers/callees/state/callbacks/persistence/SDK/EMV/CTLS/ISO8583/network/reversal/settlement effects.
- Never invent missing parameter semantics.
- Preserve conflicts and missing evidence.
- Use `HOLD - IMPACT NOT PROVEN` whenever material Production impact cannot be proven.

See `docs/governance/KTC_PAYMENT_THREE_SOURCE_MASTER_RULE_R1.md`.
