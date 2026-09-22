---
applyTo: "knowledge-supporting/**/*.md,knowledge-supporting/**/*.txt,knowledge-supporting/**/*.json"
---

# Instructions for knowledge-supporting/

## Purpose

`knowledge-supporting/` is the durable, long-term knowledge store for the K Knowledge Supporting project.

Use it for:
- reviewed knowledge snapshots
- revision-layered project knowledge
- SUNMI weekly archives and process rules
- sanitized manifests and migration metadata
- traceable project decisions and evidence summaries

## Storage rules

- Preserve historical knowledge; do not delete or overwrite prior revisions unless explicitly requested.
- Prefer append-only revision updates.
- Preserve exact source identity, revision, date, SHA, provenance, and status where applicable.
- Do not use “latest file wins” as a source-authority rule.
- Keep UTF-8 text, Markdown, and JSON human-readable.
- Do not store large binary artifacts through the text-oriented repository path.

## Authority and evidence

Knowledge files are not automatically Production authority.

When documenting technical or payment-related information:
1. identify the exact source and revision;
2. distinguish facts, observations, assumptions, and recommendations;
3. preserve conflicts;
4. identify missing evidence;
5. use `HOLD - IMPACT NOT PROVEN` when material impact cannot be established.

Do not promote derived knowledge into normative Production behavior without the required source, specification, runtime, approval, and revision evidence.

## Public repository boundary

This repository is public and sanitized. Never add:

- credentials, API keys, PATs, passwords, or tokens;
- private keys, signing material, payment keys, or certificates;
- private endpoints or confidential host configuration;
- customer data, PAN, PIN, OTP, or payment payloads;
- unredacted Production logs;
- restricted specifications or private source code;
- binary artifacts containing confidential information.

Use placeholders, hashes, controlled references, or sanitized summaries instead.

## Revision and provenance requirements

For new or revised knowledge, include relevant metadata such as:

- document title;
- generated or updated date;
- source repository or system;
- source revision, commit SHA, or version;
- authority/classification;
- status;
- scope;
- known limitations;
- synchronization state.

When a file is reconstructed or backfilled, label it clearly as reconstructed or historical. Do not present reconstruction as a Production approval.

## SUNMI weekly archive rules

For SUNMI weekly content:

- keep the scope limited to the approved device families;
- preserve the exact coverage window and cutoff;
- apply duplicate and carry-over filtering;
- use official SUNMI sources first;
- separate verified and unverified information;
- do not move later evidence backward across an earlier reporting cutoff;
- preserve old archives;
- follow the current archive format and filename convention recorded in the active weekly rules file.

Do not create PDF or binary weekly archives when the active weekly rule requires UTF-8 text or Markdown only.

## Editing behavior

Before editing:
1. read the target file and related index or manifest;
2. identify whether the change is additive, corrective, or a new revision;
3. preserve unrelated historical content;
4. check for conflicting higher-authority material;
5. validate links, dates, paths, and metadata.

After editing:
- verify the file remains valid UTF-8;
- check Markdown or JSON syntax as applicable;
- update related indexes only when the task requires it;
- report the exact files changed and any unresolved evidence gaps.

## Connector and permission boundary

Connector configuration files describe intended behavior only. They do not prove that ChatGPT, OpenAI, or another connector has full repository, write, delete, workflow, or administrator permission.

Do not claim that an operation succeeded unless the active tool reports success. Do not perform deletion or destructive history changes without explicit, task-specific authorization.

## GitHub connector fast-path boundary

Apply `KKS-GITHUB-CONNECTOR-FAST-PATH-R1` to connector-backed knowledge maintenance.

- Routine non-critical, non-security updates already authorized by Project scope may proceed without duplicate permission prompts.
- Connector write/admin capability is not security authorization.
- Never use the fast path for access/permission changes, rulesets, branch protection, required checks/reviews, secrets, Actions policies, security settings, destructive history changes, or Production/security-critical work.
- Existing GitHub controls and stricter Project approval rules always remain enforceable.

## Required response behavior

If required source identity, revision, approval, or evidence is missing, stop and return:

`GAP`

Then list:
1. the missing value;
2. why it is required;
3. how to obtain it;
4. the evidence or format needed to close the gap.

Do not guess or silently substitute generic knowledge.