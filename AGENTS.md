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

## Mandatory Value Proposition validation gate

Apply `KKS-VALUE-PROPOSITION-VALIDATION-GATE-R1` from `docs/governance/K_KNOWLEDGE_SUPPORTING_VALUE_PROPOSITION_GATE_R1.md` before using material inputs in Thinking, Analysis, Investigation, Production Solving, Root Cause Analysis, or equivalent reasoning workflows.

- Validate objective, scope, source/evidence identity, observed vs expected behavior, constraints, conflicts, environment/version/revision, and acceptance/decision criteria as applicable to the job.
- A present value is not automatically sufficient: it must be relevant, traceable where required, internally consistent, and recent enough for the decision.
- If the gate returns `GAP`, stop before downstream reasoning and do not provide the downstream conclusion, solution, root cause, Production fix, or equivalent answer.
- A blocked response must begin with the heading `GAP` and provide a numbered list stating the missing value, why it is required, how to prepare/obtain it, and the evidence/format required to close it.
- Do not guess or silently fill missing material values from generic knowledge, stale memory, unsupported inference, or latest-file-wins.
- After the user closes the listed GAP items, re-run the complete Value Proposition validation from the start. Continue only on `PASS`.
- After downstream work completes, validate the result before reporting it to the user, then apply the normal Project final-response GAP rule.

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

## GitHub Connector fast path

Apply `KKS-GITHUB-CONNECTOR-FAST-PATH-R1` for ChatGPT/Codex/Copilot GitHub connector work.

- For routine non-critical, non-security repository work already inside the authorized Project scope, bypass duplicate conversational approval/process and proceed through the available GitHub connector.
- Connector permission is capability only; it is never standing authorization for security or administrative changes.
- Do not use connector `admin`, `maintain`, `push`, `write`, `delete`, or workflow capabilities to bypass rulesets, branch protection, required checks, review requirements, access controls, security settings, secrets, Actions policies, or stricter fresh-approval gates.
- Security/access/ruleset/branch-protection/secret/Actions-policy mutations remain outside the fast path and require the applicable explicit task-specific authorization.
- When another rule is stricter, the stricter rule wins.

See `docs/governance/K_KNOWLEDGE_SUPPORTING_GITHUB_CONNECTOR_FAST_PATH_R1.md`.

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


## Rule Governance Agent

Apply `KKS-RULE-GOVERNANCE-UPDATE-GATE-R1` and `KKS-RULE-GOVERNANCE-AGENT-R1` from `docs/governance/K_KNOWLEDGE_SUPPORTING_RULE_GOVERNANCE_AGENT_R1.md` on every K Knowledge Supporting user round.

- Detect reusable rule creation/update/scope/permission/deprecation/conflict semantics.
- Treat phrases such as master rule, master project rule, master project-wide rule, project-wide rule/standard, every chat, future chats, from now on, default, inherit, trigger/keyword, permission/approval, source precedence/authority, and equivalent Thai wording as semantic activation signals.
- Do not promote quotations, filenames, logs, old-rule summaries, hypotheticals, or one-off instructions into durable rules without normative intent.
- If the current user message explicitly authorizes the exact rule change and persistence scope, do not ask a duplicate confirmation.
- Synchronize confirmed reusable rule changes only through authorized canonical governance targets and preserve all stricter approval gates.
