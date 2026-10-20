# KKS MCP Apps / Skybridge Integration R1

- Status: **CANDIDATE / REVIEW ONLY** (not a deployed or connected MCP App)
- Reviewed: **2026-10-13**
- Baseline: `RepoKan/K-Knowledgeable- main@22406760ae8653003819141186d68d0a368e08b2`
- Official framework: https://github.com/alpic-ai/skybridge
- Starter: https://github.com/alpic-ai/apps-sdk-template
- Current quickstart source: https://github.com/alpic-ai/skybridge/blob/main/docs/get-started/quickstart.mdx

## Decision

Use Skybridge as a replaceable, separately hosted **MCP app / UI layer**, not a source authority. Keep KKS GitHub revision truth, Notion human-readable decisions, governed Skills/Agents, and applicable Production source/spec/log evidence unchanged.

Skybridge requires **Node.js 24+**. Keep that runtime isolated from the current local-first Continue **Node.js 20.20.1** baseline. Do not upgrade Continue or replace root `mcp_config.json`; KKS already has a separate GitHub/Copilot MCP policy and does not need a duplicate GitHub server.

## Approved local pilot, not a deployed integration

- Users: KKS engineers reviewing sanitized integration facts.
- Pain: official external framework guidance and local approval gates are split across sources.
- Proposed natural-language actions (read-only): `list_reference_sources`, `get_integration_status`.
- LLM advantage: identify which approved source/gate answers the user's question; never fabricate evidence.
- UI concept: a compact source list + candidate/gap status, not an operational payment dashboard.
- Data: explicit allowlist of sanitized public references; no unrestricted filesystem or repository traversal.
- Auth: none needed for public fixture-only pilot. A future private-data design requires reviewed OAuth and permission scope.

The user approved the two-tool fixture-only SPEC R1 on 2026-10-14. The implementation and current verification record are in `mcp-apps/kks-source-explorer/SPEC.md`. On 2026-10-20 the user additionally authorized resolving and merging the reviewed outstanding PRs. Neither approval authorizes public tunnels, connector registration or deployment.

## Architecture

```text
ChatGPT / compatible MCP client
  -> reviewed HTTPS + auth boundary when applicable
    -> isolated Skybridge MCP service (Node >=24)
       -> read-only public-reference tool handlers + React views
          -> sanitized allowlisted metadata
Separate: Continue Node 20 / KTC payment execution / private Production evidence / keys
```

## Official local quickstart (only on a trusted Node 24+ host)

The documented bootstrap command is `npx skybridge create kks-mcp-pilot`; inspect downloaded scripts, generated code and lockfile before execution. Then run `npm run dev` in the generated directory. Upstream documents the local MCP endpoint `http://localhost:3000/mcp` and DevTools at `http://localhost:3000/`. Do not enable `--tunnel`, register a ChatGPT connector or deploy the app in this initial phase.

## Promotion gates

1. Confirm use case, 1–3 actions, user/LLM/UI interactions, source authority, and approved `SPEC.md`.
2. Pin and verify upstream release, source SHA, package version and dependency lockfile.
3. Run isolated Node 24+ startup, MCP initialize/tools/list/tool call tests and a real React-view test.
4. Reject unauthorized inputs; verify fail-closed behavior and no secret/private data in tools or view state.
5. Validate GitHub `base...head` diff, exact commit and actual CI status; `NOT RUN` is not `PASSED`.
6. No merge, Production/payment/security changes, outbound public tunnel or deployment without applicable separate approval.

## Current evidence

- Official GitHub documentation: checked 2026-10-13.
- KKS governance, MCP policy and source SHA: confirmed from connected GitHub.
- Static candidate policy/unit tests: 6 local tests passed on reference files.
- Local checks on 2026-10-20: Node 24.19.0 locked installation, zero-vulnerability npm audit, 12 fixture/watcher tests, full type checking, production build, actual loopback MCP and both DevTools React views passed. Cloud/tunnel routes are denied by application middleware. See the app SPEC and PR #34 for exact-head CI; this record is not live monitoring.
- External ChatGPT host connection and deployment: **NOT RUN / NOT APPROVED**. Local egress was checked with loopback/fetch/UDP guards and a browser request allowlist; this is not a comprehensive packet-level audit.
- Rollback: discard this candidate / trial service; do not alter KKS existing MCP config or Production source.

This record contains no private source, credentials or payment material.
