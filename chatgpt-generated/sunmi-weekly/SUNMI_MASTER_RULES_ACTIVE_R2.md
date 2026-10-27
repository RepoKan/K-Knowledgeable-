# SUNMI Android Development Master Rules R2

Rule ID: `SUNMI-KNOWLEDGE-MASTER-R2`
Effective: 2026-10-28
Category: Android Development
Scope: SUNMI weekly news, SUNMI payment-device development knowledge, and weekly knowledge maintenance only.

## 1. Hard category boundary

- SUNMI knowledge belongs to `Android Development`.
- SUNMI weekly news, P3/P2/P3 MIX, Payment SDK, PayLib, SPHS, EMV/CTLS, PinPad, Printer, ECR, TMS/DMP, RKI, APK, ROM, security compatibility, Android Studio/Kotlin/Java and related device-development evidence stay in this category.
- ISO9001 knowledge is a separate authority domain and MUST NOT be merged into this SUNMI knowledge set.
- QP, WI, LB documents, audit checklists, audit summaries, corrective-action records, FDC-ML Master List and other ISO9001 controlled documents are excluded from SUNMI weekly knowledge and SUNMI Memory.

## 2. Knowledge planes and authority

1. Current SUNMI vendor facts: SUNMI-controlled official sources.
2. Weekly curated knowledge/archive: `RepoKan/K-Knowledgeable-` under `chatgpt-generated/sunmi-weekly/`.
3. Human-readable knowledge control: Notion SUNMI Android Development page(s) and SUNMI Work Memory.
4. Implementation/runtime evidence: repositories such as `RepoKan/KKL-CellId-P3-MiniApp`; code proves implementation state only and MUST NOT be treated as current SUNMI vendor news.
5. Historical weekly archives and snapshots: provenance/history only; they do not prove current vendor state.

No source may self-promote to a higher authority class.

## 3. Source trust tiers

### Tier A — SUNMI Official Technical
Preferred for verified technical claims:
- `https://docs.sunmi.com/`
- `https://developer.sunmi.com/` when the resulting content is SUNMI-controlled technical documentation
- SUNMI official SDK/API/release-note/security-bulletin pages on SUNMI-controlled domains.

### Tier B — SUNMI Official Product / Security / News
Accepted as official vendor information, but classify the page type before using it:
- `https://www.sunmi.com/`
- `https://sunmi.com/`
- official SUNMI CDN assets such as `cdn.sunmi.com`, `static.cdn.sunmi.com`, and `file.cdn.sunmi.com`.

Product/news/marketing pages are not automatically SDK release notes.

### Tier C — Secondary Package Evidence
Examples: Maven Central / Sonatype package metadata.
- May confirm that an artifact/version exists.
- MUST be labeled Secondary Package Evidence.
- MUST NOT use the status line “ยืนยันแล้ว จาก SUNMI Official WebSite” solely from this tier.
- Before recommending dependency change, map the package/version to SUNMI official documentation or explicitly retain `UNVERIFIED/GAP`.

### Tier D — Unverified / Community / Lookalike
Examples include third-party package mirrors, forums, Reddit, GitHub issues, community posts, support reposts, and domains whose official ownership is not independently verified.
- Never use as sole proof of a SUNMI official change.
- Keep under `Officially SUNMI Unverified`.
- A title, logo, author label, or visual similarity is not sufficient evidence of official ownership.
- `sunmideveloper.com` is NOT on the canonical allowlist in this rule; treat it as unverified until ownership/authority is independently established.

### Tier H — Historical Internal Knowledge
GitHub weekly archives, Notion snapshots, prior reports, saved baselines and project memories.
- Valid for duplicate/carry-over/provenance comparison.
- Not valid by themselves as proof of current SUNMI state.

## 4. Weekly source acceptance gate

Before a finding is promoted to `Officially SUNMI Verified`, verify:

1. Host/domain is an approved SUNMI-controlled source.
2. Page type is identified: documentation, SDK/API, release note, security bulletin, product, news, TMS/MDM/RKI, or other.
3. Publication/update time is captured when available.
4. Product/module/device mapping is explicit enough for the claimed impact.
5. A documentation update date is NOT treated as an artifact release date unless the source states that.
6. A package-registry version is NOT treated as a SUNMI official release unless mapped to an official SUNMI source.
7. Evidence is inside the report coverage window for “new” classification; otherwise mark Carry-over/Previous Revision.
8. Current facts are re-fetched; do not use “latest-file-wins”, stale memory, or prior report wording as current proof.
9. When an official page is inaccessible, ambiguous, or contradictory, use `UNVERIFIED/GAP`; do not substitute a third party and claim official verification.

## 5. Staleness and revision rules

Each material SUNMI fact should preserve:
- source title;
- source URL;
- source tier/type;
- product/module;
- observed version/revision;
- source publication/update date when available;
- `last_verified_at`;
- previous state;
- current state;
- duplicate/carry-over decision.

Staleness rules:
- A previously known version/date is Carry-over until reverified.
- Documentation timestamp and package version are separate dimensions.
- Historical archives are immutable evidence; corrections are append-only revision layers.
- If current official source changes interpretation, mark the old layer `Superseded` or `Previous Revision`; never silently overwrite history.

## 6. Conflict rules

- Official current SUNMI source vs historical archive: current official source governs current vendor state; archive remains historical.
- Official source vs secondary registry: record both. Do not promote registry-only evidence to official status.
- Official source vs implementation repository: record `IMPLEMENTATION_DELTA`; code state is not vendor-release state.
- Conflicting official SUNMI pages: record `HOLD/GAP`, preserve both URLs and timestamps, and do not infer which is correct without stronger evidence.
- Missing expected weekly archive: record `ARCHIVE_CONTINUITY: GAP`; do not fabricate/backfill without evidence.

## 7. Known reconciliation items as of 2026-10-28

- Historical Sunday 08:00 Markdown sequence is preserved as Historical Lineage.
- Active weekly policy is Sunday 16:30 ICT with one UTF-8 TXT archive.
- `SUNMI_Knowledge_Consistency_Status.md` still contains historical 08:00/P3+P3 MIX active wording and requires maintenance classification.
- `SUNMI_Weekly_Archive_Index_2026.md` does not yet enumerate every later 16:30 archive.
- 2026-10-11 16:30 TXT archive is not present on `automation/sunmi-weekly` at this review.
- 2026-10-25 16:30 TXT archive/revision is not present on `automation/sunmi-weekly` at this review.
- Historical task-state text saying “ACTIVE” is not proof the ChatGPT Automation is enabled; task state must be checked through the Automation system.
- Prior ECR baseline `com.sunmi:sunmi-ecr-service:3.0.6` must not be treated as current. Secondary Maven Central evidence currently exposes `3.0.16`; this remains Secondary until mapped to a SUNMI official technical source.
- Payment SDK official documentation and package metadata must be treated separately.

## 8. Weekly post-news maintenance gate

Run after the Sunday SUNMI Weekly Report is generated.

1. Re-fetch this Master Rules file and the source registry rules.
2. Verify the scheduled task state and distinguish:
   - `TASK_CONFIGURED`
   - `UNATTENDED_RUN_VERIFIED`
   - `INTERACTIVE_WRITE_ROUNDTRIP_VERIFIED`
3. Verify canonical source-domain allowlist and flag new/unrecognized domains.
4. Re-fetch material SUNMI official pages used by the report.
5. Compare update dates/versions with prior weekly revision.
6. Check archive coverage and continuity for the expected Sunday coverage end.
7. Check archive index, revision metadata, commit/blob/readback consistency.
8. Review Notion SUNMI Work Memory and SUNMI knowledge pages for stale/conflicting pointers.
9. Review GitHub SUNMI knowledge references and implementation-repo deltas without treating implementation code as vendor news.
10. If rule policy itself changes, append a Master Rules revision. Otherwise record `NO RULE CHANGE`.
11. Update Notion SUNMI control page/Memory only with durable rule/status changes; do not save temporary weekly facts as personal Memory unless they materially change future workflow.
12. Do not modify global `AGENTS.md` from weekly preference learning.
13. Do not import ISO9001 knowledge into this category.

Required maintenance statuses:
- `RULES_RECHECK: PASSED | GAP | HOLD`
- `SOURCE_REGISTRY: CURRENT | STALE`
- `ARCHIVE_CONTINUITY: OK | GAP`
- `NOTION_SYNC: VERIFIED | GAP`
- `GITHUB_READBACK: VERIFIED | BLOCKED`
- `AUTOMATION_STATE: ENABLED | DISABLED`

## 9. Current source examples checked during R2 creation

- SUNMI Payment SDK for P series: https://docs.sunmi.com/en-US/cdixeghjk491/xfdqeghjk513
- SUNMI Remote Key Injection: https://www.sunmi.com/en/remote-key-injection/
- SUNMI Terminal Security: https://www.sunmi.com/en/privacy-and-security/terminal-security/
- Secondary ECR package metadata: https://central.sonatype.com/artifact/com.sunmi/sunmi-ecr-service

## 10. Change-control rule

This rule is task/domain scoped to SUNMI Android Development.
It does not modify global `AGENTS.md`.
It does not authorize Production/payment behavior changes.
It does not authorize writing to `main`.
It does not change ISO9001 knowledge.
Historical evidence remains preserved.

Status: ACTIVE
