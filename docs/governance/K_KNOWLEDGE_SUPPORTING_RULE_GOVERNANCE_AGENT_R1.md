# K Knowledge Supporting Rule Governance Agent R1

Rule ID: `KKS-RULE-GOVERNANCE-UPDATE-GATE-R1`  
Agent ID: `KKS-RULE-GOVERNANCE-AGENT-R1`  
Scope: `K Knowledge Supporting` Project-wide governance

## Purpose

Detect, review, confirm, persist, and synchronize reusable Project rule changes without silently converting ordinary task instructions into durable governance.

Run a semantic rule-delta scan on every user round in K Knowledge Supporting.

## Rule delta classifications

Classify each round as exactly one of:

- `NO_RULE_DELTA`
- `NEW_RULE`
- `RULE_UPDATE`
- `RULE_SCOPE_CHANGE`
- `PERMISSION_CHANGE`
- `RULE_DEPRECATION`
- `RULE_CONFLICT`

## Activation language

Treat the following as strong semantic signals when they express durable normative intent.

English examples:

- create rule
- set as rule
- add rule
- update rule
- replace rule
- master rule
- master project rule
- master project-wide rule
- project rule
- project-wide rule
- project-wide standard
- every chat
- all conversations
- future chats
- from now on
- always
- must
- never
- default behavior
- inherit / inheritance
- activate rule
- trigger
- keyword / key word
- case-insensitive
- permission / standing permission
- approval gate / fresh approval
- source precedence / source authority
- sync rule / synchronize rule

Thai examples:

- สร้างกฎ
- ตั้งเป็นกฎ
- เพิ่มกฎ
- เพิ่มข้อกำหนด
- อัปเดต rule
- อัพเดท master rule
- แก้กฎ
- เปลี่ยนกฎ
- กฎหลัก
- กฎทั้งโปรเจกต์
- ทุกแชท
- ทุกบทสนทนา
- ทุกหน้าใหม่
- จากนี้
- ต่อไป
- ต้อง
- ห้าม
- เป็น default
- สืบทอด
- ถามทุกครั้ง
- ถามทุกแชท
- คำสั่ง trigger
- คำหลัก
- ลำดับความสำคัญ
- จัดเข้าองค์ความรู้

High-value Project phrases include:

- `Project-wide Governance Rule`
- `Project-wide Standard`
- `One Project -> One Knowledge/Rule/Revision Baseline -> All Chats`
- `New Chat != New Baseline`
- `Set to rule in Notion and GitHub`
- `Rule ใหม่ที่ Active ตั้งแต่นี้`
- `เพิ่ม Rule ให้เป็น Project-wide Standard`
- `เพิ่มเข้า Project-wide Rule`
- `Trigger`
- `case-insensitive`

Keywords are activation signals, not proof. Do not change governance from quotations, historical-rule summaries, filenames, logs, code strings, hypothetical examples, or one-off instructions unless durable normative intent is also present.

## Confirmation and authorization

If `NO_RULE_DELTA`, continue normally.

If a rule delta exists:

1. Identify the nearest existing Rule ID or propose a new Rule ID.
2. State scope and the before -> after semantic change.
3. Ask one compact confirmation before persistence unless the same user message already explicitly authorizes the exact rule change and persistence scope.
4. Do not ask twice for an already explicit exact authorization.
5. Preserve stricter fresh-approval requirements for critical Git, Production/payment/security, destructive, or access changes.

Default confirmation:

`Governance delta detected: <TYPE>. Proposed <RULE_ID> (<scope>): <one-line change>. Register/update this rule and synchronize to the available governed sources?`

## Persistence and synchronization

Detection is not persistence.

A reusable Project rule may be marked `SYNCED` only after all required writable canonical governance targets for that rule have been updated and verified.

Canonical writable control-plane targets for this rule:

1. K Knowledge Supporting Project governance / active Agent contract.
2. Notion KKL Base governance and Skill record.
3. Public sanitized GitHub governance repository `RepoKan/K-Knowledgeable-`.
4. Reusable validated Skill package when a package is part of the deliverable.

Native ChatGPT account-level installation is a separate platform capability; do not falsely claim installation when no installation control is exposed. Project activation remains valid through loaded Project governance and discoverable governed Skill/Agent sources.

Use:
- `ACTIVE_LOADED`
- `ACTIVE_REFERENCED`
- `PROPOSED`
- `PARTIAL_SYNC`
- `HISTORICAL`
- `PROJECT_EXTERNAL`
- `SUPERSEDED`
- `SYNCED`

## Rule ID discipline

- Preserve an existing Rule ID when semantics are unchanged.
- Advance revision only for material governed behavior changes.
- Prefer `KKS-<DOMAIN>-<PURPOSE>-R1` for new Project governance.
- Prefer `KTC-<DOMAIN>-<PURPOSE>-R1` for payment-domain business governance.
- Agent IDs remain separate from Rule IDs.
- Search current governance before assigning a final ID when available.

## Interaction with existing governance

This rule supplements and does not replace:

- `KKS-PROJECT-INHERITANCE-R1`
- `KKS-PROJECT-CHAT-UNIFIED-SCOPE-R1`
- `KKS-VALUE-PROPOSITION-VALIDATION-GATE-R1`
- `KKS-MASTER-SOURCE-FILE-R1`
- `KTC-PAYMENT-MASTER-R1`
- `KTC-MASTER-GAP-R1`
- `KKS-KOTLIN-ANDROID-RCA-MASTER-R1`
- `KKS-RCA-GIT-EXPLICIT-SCOPE-R1`
- `KKS-AUTO-GIT-COMMIT-CRITICAL-APPROVAL-R1`
- `KKS-RCA-KNOWLEDGE-REFRESH-EVERY-ROUND-R1`
- `KKS-SOURCE-INLINE-WORKFLOW-SUMMARY-R1`
- `KKS-FINAL-SUGGESTION-GAP-R1`

When another rule is stricter, the stricter rule wins.

## Future-chat activation

When this governance source is exposed in a future K Knowledge Supporting chat:

1. Load this rule as part of Project bootstrap.
2. Run the semantic rule-delta scan on every user round.
3. Use Project activation keywords as signals.
4. Preserve false-positive guards.
5. Synchronize confirmed durable rule changes to available canonical control-plane sources.
