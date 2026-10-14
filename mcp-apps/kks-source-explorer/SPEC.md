# KKS Source Explorer — MCP App Pilot

**Status:** DRAFT SPEC / NOT APPROVED FOR IMPLEMENTATION  
**Version:** R1 (2026-10-14)  
**Repository:** `RepoKan/K-Knowledgeable-` (public, sanitized metadata only)  
**Baseline:** `main@22406760ae8653003819141186d68d0a368e08b2`  
**Related draft:** [PR #34](https://github.com/RepoKan/K-Knowledgeable-/pull/34)

## 1. Value proposition

**Users:** K Knowledge Supporting engineers reviewing external MCP-framework references and the public KKS integration boundary.

**Problem:** A developer must switch between the framework docs, the KKS reference, the GitHub revision, and the review gates to answer two simple questions: what sources are in scope and what integration state is proven.

**Pain today:** A chat answer can conflate a published reference, a passed static test, and a live MCP App. It is difficult to distinguish authority and validation state at a glance.

**Core actions (exactly two):**
1. `list_reference_sources` — return public, explicitly allowlisted references with provenance and source classification.
2. `get_integration_status` — return evidence-backed readiness, open gates, and exact revision metadata.

This is a deliberately narrow non-Production pilot, not a payment tool, repository browser, or enterprise knowledge search.

## 2. Why inside an AI assistant?

A user can ask “show the official MCP sources” or “is KKS MCP ready?” without knowing source URLs or version/approval rules. The assistant interprets the request, calls one read-only tool, and explains the returned evidence. A small interactive view makes source and gate inspection easier.

**LLM contribution:** natural-language intent interpretation and summarization only.  
**LLM cannot supply:** authenticated repository access, fresh version truth, deployment evidence, or approval that a tool does not return. Missing facts remain `UNVERIFIED` or `NOT RUN`.

## 3. UI/user journey

**Initial state:** “KKS Source Explorer” header; a concise `CANDIDATE` status and links to official public sources.  
**Interactions:** show all/framework/governance filters; expand source provenance; inspect validation gates.  
**End state:** the user knows which sources and tests are confirmed and which live checks remain.  
**UI constraints:** responsive compact view; keyboard accessible; external links explicit; readable in ChatGPT/MCP clients; avoid a full-page dashboard, automatic editing, or background actions.

## 4. Data contract and tool definitions

All values are returned by the server from a reviewed, built-in allowlist. User input never becomes a URL, filesystem path, repository identifier, command, or query to external services.

### Tool: `list_reference_sources`

Input: `{ category?: "all" | "framework" | "governance" | "integration" }`; default `all`.  
Output: `{ sources: Array<{ id, title, url, category, authority, provenance, verified_at? }>, evidence_state }`.

Initial sources (public only):
- `https://github.com/alpic-ai/skybridge` — Skybridge framework upstream; third-party framework authority.
- `https://github.com/alpic-ai/skybridge/blob/main/docs/get-started/quickstart.mdx` — upstream quickstart; documentation, not a pinned release.
- `https://docs.skybridge.tech/` — canonical framework documentation.
- `https://github.com/RepoKan/K-Knowledgeable-/pull/34` — public KKS candidate implementation reference; not Production authority.

### Tool: `get_integration_status`

Input: `{}` (no optional free-form parameters in R1).  
Output: `{ status: "CANDIDATE", repository, baseline_sha, reviewed_head_sha?, checks: Array<{ name, state, evidence }>, blockers: string[], next_review_action }`.

The default status remains `CANDIDATE` until current GitHub, runtime, host-connection and explicit approval evidence support promotion. Historic CI runs must never be displayed as current unless the exact head SHA and status are supplied by a verified source. The initial fixture is a snapshot, not live monitoring.

### View behavior

The UI may filter or expand returned data locally. It must not create changes, call arbitrary endpoints, trigger model/provider routing, or request deployment. Tool output must remain useful to the LLM even when a client does not support the rich UI.

## 5. Product and framework context

**Framework:** official `alpic-ai/skybridge` and Skybridge docs (verify exact upstream SHA, version and dependency lock at implementation).  
**Runtime:** isolated Node.js >=24; do not upgrade the existing Continue Node 20.20.1 runtime.  
**Transport:** localhost during pilot; DevTools at `http://localhost:3000/` and MCP endpoint at `http://localhost:3000/mcp` as documented by upstream.  
**Credentials:** none for a public-fixture-only local pilot.  
**Backend:** packaged public-reference fixture; no GitHub token, Notion, payment/TMS service, file access or production environment integration.  
**Deployment:** explicitly out of scope; no tunnel, public registration, cloud release, or ChatGPT connector install in this stage.

## 6. Security and KKS authority controls

1. Data allowlist only; reject unknown categories; no unrestricted path, URL, command or user-provided repository traversal.
2. No secret collection, credentials, confidential KTC material, card/customer data, private host endpoints or unredacted logs.
3. Do not modify `mcp_config.json`, Copilot MCP settings, Continue source, model routing, or any Production/payment files.
4. GitHub is revision truth; Notion is the human-readable decision record; Skills govern workflow; neither the view nor the LLM may approve itself.
5. No outbound telemetry or unexpected egress permitted with any project-private data. Review upstream runtime dependency and telemetry behavior before use beyond fixtures.
6. No merge into `main` or deployment without required fresh action-specific approval.

## 7. Acceptance criteria

- [ ] Product `SPEC.md` accepted by the user (this document is currently a draft).
- [ ] Official upstream commit/version and lockfile pinned and reviewed.
- [ ] Clean isolated Node.js >=24 host confirmed.
- [ ] Skybridge dev server starts locally without Production material.
- [ ] MCP initialize, `tools/list`, both tool calls and invalid-input handling verified with actual protocol requests.
- [ ] React view renders and both data states are inspected in DevTools.
- [ ] LLM-visible data remains meaningful if the view is unavailable.
- [ ] Offline and runtime tests are distinguished from exact-head GitHub CI.
- [ ] Secret/private-data negative tests pass; network egress/telemetry reviewed.
- [ ] GitHub feature diff confirmed scoped, CI head SHA checked, rollback path documented.
- [ ] Separate human approval obtained before merge, public tunnel, external connector registration or deployment.

## 8. Non-goals and rollback

**Not included:** Android code, SUNMI device interaction, payment processing, EMV/ISO8583/Field 61, production secrets, private repositories, live GitHub API calls, persistent storage, worker execution, document editing, command execution, and automatic model routing.

**Rollback:** discard the isolated local pilot; close the draft PR if not adopted. Existing KKS source, payment applications, MCP config and Continue runtime remain unchanged.

## 9. Outstanding product decision

**Approval required before implementation:** confirm that this two-tool read-only Source Explorer and the fixture-only/non-deployed scope are the intended R1 product. Creating this document is not permission to install packages, start public tunnels, connect private accounts, or deploy.

**Official external references reviewed:** https://github.com/alpic-ai/skybridge and https://github.com/alpic-ai/skybridge/blob/main/docs/get-started/quickstart.mdx (2026-10-14).