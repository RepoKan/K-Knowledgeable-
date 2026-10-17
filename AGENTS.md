# K Knowledge Supporting Agent Governance

## Master rule

Use `KKS-PROJECT-INHERITANCE-R1` as the Project bootstrap contract and `KKS-PROJECT-CHAT-UNIFIED-SCOPE-R1` as the Project-wide chat/permission inheritance rule. Use `KTC-PAYMENT-MASTER-R1` as the sanitized governance baseline for KTC payment inspection workflows. Use `KKS-GITHUB-CONNECTOR-FAST-PATH-R1` as the canonical Master Rule for ChatGPT/Codex/Copilot GitHub connector process simplification, subject to its merge and security boundaries.

## KKS Operator Quick Reference — execution and closeout

Apply `KKS-OPERATOR-QUICK-REFERENCE-R1` from `docs/governance/KKS_OPERATOR_QUICK_REFERENCE_R1.md` whenever performing K Knowledge Supporting (KKS) Knowledge work, governed actions, or reporting outcomes.

- At each applicable gate use `BLOCKED -> HOLD -> ESCALATE -> NO CHANGE REQUIRED -> CONTINUE`.
- Follow the 10 gates: Define Scope, Verify Evidence, Assess Impact, Make Decision, Confirm Authorization, Confirm Readiness, Pre-Execution Gate, Execute, Verify, Report.
- Execute only when gate=`CONTINUE`, decision=`RECOMMENDED`, authorization=`AUTHORIZED`, and readiness=`READY TO APPLY`; stricter existing fresh-approval requirements remain.
- Keep gate, decision, authorization and readiness separate from execution/verification outcomes. `NOT RUN` is never a gate status or proof of completion.
- `Overall completion: Yes` requires evidenced `COMPLETED` execution and `COMPLETED` verification with no controlling unresolved `BLOCKED`/`HOLD`. For no-change or read-only paths record their actual status; do not fabricate execution.
- This rule supplements, and never supersedes, evidence/source-authority, `GAP`, public/private boundary, GitHub merge review, and Production/payment-security controls.

## Project-wide chat scope

Every work chat, thread, or chat box inside **K Knowledge Supporting** is a governance sibling in the same Project.

- Inherit the same Project governance, capability routing, source-authority rules, and baseline permission envelope.
- Project-wide standing non-critical permissions may be reused across Project chats without duplicate grant when the required tool or connector is actually available.
- A permission expressly limited to one chat, action, repository/branch, file, or execution remains limited to that scope.
- Fresh/action-specific approval still applies where the governing rule requires it, including critical Git write/merge/delete, Production/payment/security changes, destructive operations, and per-action restrictions.
- Do not infer technical access from logical Project membership. A chat may not automatically expose historical messages, uploads, mounted files, connector sessions, or external accounts from another chat.
- Effective executable permission is the intersection of Project-wide user authorization, action-specific approval rules, current tool/connector availability, external permissions, branch/ruleset/required-check constraints, and source-authority limits.

See `docs/governance/K_KNOWLEDGE_SUPPORTING_PROJECT_INHERITANCE_R1.md`.

## Git merge approval

Every merge requires fresh, action-specific user approval immediately before execution, including non-critical merges. Auto-merge must not bypass this gate.
