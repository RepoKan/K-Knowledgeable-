# K Knowledge Supporting Project Instructions

## Project identity

All work chats, threads, and chat boxes created inside **K Knowledge Supporting** are part of the same logical Project.

Apply these rules at startup:

1. Load `KKS-PROJECT-INHERITANCE-R1`.
2. Apply `KKS-PROJECT-CHAT-UNIFIED-SCOPE-R1` for cross-chat governance, capability, and standing-permission inheritance.
3. Use the most specific domain rule or Skill for the task.
4. Preserve exact source identity, revision, SHA/version, governance state, and conflicts.
5. For KTC payment-critical work, also apply `KTC-PAYMENT-MASTER-R1`.
6. For Kotlin/Android RCA, also apply `KKS-KOTLIN-ANDROID-RCA-MASTER-R1` and `KKS-RCA-GIT-EXPLICIT-SCOPE-R1`.

## Project-wide chat inheritance

Every Project work chat inherits the same Project governance, capability routing, source-authority rules, and baseline permission envelope.

Project-wide standing non-critical permissions may be reused across Project chats when the required capability is actually available in the current session. Do not ask the user to repeat the same Project-wide grant merely because a new Project chat was opened.

A narrower authorization remains narrow. If the user limited permission to one chat, action, repository/branch, file, or execution, do not broaden it automatically.

Fresh or action-specific approval remains mandatory when required by the governing rule, including critical Git write/merge/delete operations, Production/payment/security changes, destructive operations, permission/access changes, or another explicitly fresh-gated action.

## Effective permission rule

Logical Project membership does not create technical access. Before execution, effective permission is the intersection of:

- Project-wide user authorization;
- the governing approval rule for the action;
- current tool/connector availability;
- external repository/account/service permission;
- branch protection, rulesets, and required checks;
- platform safety, privacy, and source-authority constraints.

Never claim access to historical chats, uploads, mounted files, connector sessions, repositories, or external accounts unless the current session actually exposes that access.

## Source inheritance

Raw Project chat content is Project-scoped context, but it may not be technically retrievable from another chat. For reliable cross-chat reuse, promote important rules, facts, artifacts, evidence, and decisions into durable governed Project sources with provenance and status.

`Durable + Governed + Traceable = Inheritable`.

## Git governance

Project default: `KKS-AUTO-GIT-COMMIT-CRITICAL-APPROVAL-R1`.

Kotlin/Android RCA exception: `KKS-RCA-GIT-EXPLICIT-SCOPE-R1` — `auto Git commit = No`; commit, push, and merge require explicit authorization covering action, target repository/branch, and scope.

Critical actions retain fresh, single-purpose approval immediately before execution. Project-wide permission inheritance does not override this requirement.

## Production evidence

Never use chat recency or latest-file-wins as Production authority. Resolve the exact source/spec/runtime revision applicable to the task. When material evidence is missing, use `HOLD - IMPACT NOT PROVEN`.

## Canonical references

- `docs/governance/K_KNOWLEDGE_SUPPORTING_PROJECT_INHERITANCE_R1.md`
- `docs/governance/K_KNOWLEDGE_SUPPORTING_CAPABILITY_REGISTRY_R1.md`
- `docs/governance/KTC_PAYMENT_THREE_SOURCE_MASTER_RULE_R1.md`
- `AGENTS.md`
- `.github/copilot-instructions.md`
