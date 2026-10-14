# KKS Source Explorer MCP App pilot

STATUS: IMPLEMENTED, NOT DEPLOYED, RUNTIME UNVERIFIED.

The user approved SPEC R1 on 2026-10-14 for two read-only tools using public fixtures. This approval does not include merge, public tunnel, connector registration, or deployment.

## What the app does

- list_reference_sources: only allowlisted HTTPS URLs for public KKS and Skybridge references.
- get_integration_status: dated CANDIDATE fixture with open verification gates, not live GitHub status.
- Two Skybridge React views: source browser and integration readiness.

## Developer environment

Use a separate Node.js >=24.18.0 host; do not alter Continue's Node 20 baseline.

1. Audit package.json dependencies and official Skybridge source before installation.
2. Generate a genuine package-lock.json using npm install --package-lock-only --ignore-scripts, inspect hashes, then commit/review that lockfile.
3. Run npm ci --ignore-scripts after review. Investigate necessary native installation hooks separately.
4. Set SKYBRIDGE_TELEMETRY_DISABLED=1 and DO_NOT_TRACK=1 in the shell before executing any Skybridge CLI.
5. Run npm run test:fixture, npm run build, then npm run dev; no public tunnel.
6. Verify actual MCP initialize, tools/list, both tools/call, invalid categories, and React view rendering in localhost DevTools.
7. Audit egress, confirm latest GitHub head SHA/CI and obtain separate merge or deployment approval.

Upstream reviewed: alpic-ai/skybridge@6dd443908113b5218d20a5016ed6c34d223e5146.
Node/npm registry is unavailable for real install on the preparation container. No real runtime validation has been claimed.

## Hold conditions

- No npm lockfile or actual runtime protocol/UI validation yet.
- The governance CI failed previously on expected merge-policy text in AGENTS.md; investigate independently, do not weaken governance.
- Do not use Production/payment data, private specs/logs, tokens or internal endpoints.
- The app never becomes authority for real Production or current GitHub status.

Rollback: discard this isolated project; leave all existing KKS and Continue configuration untouched.
