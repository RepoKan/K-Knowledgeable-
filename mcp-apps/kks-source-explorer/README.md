# KKS Source Explorer MCP App pilot

STATUS: LOCAL BUILD AND MCP VERIFIED; SECURITY AND UI REVIEW HOLD; NOT DEPLOYED.

The user approved SPEC R1 on 2026-10-14 for two read-only tools using public fixtures. This approval does not include merge, public tunnel, connector registration, or deployment.

## What the app does

- list_reference_sources: only allowlisted HTTPS URLs for public KKS and Skybridge references.
- get_integration_status: dated CANDIDATE fixture with open verification gates, not live GitHub status.
- Two Skybridge React views: source browser and integration readiness.

## Developer environment

Use a separate Node.js >=24.18.0 host; do not alter Continue's Node 20 baseline.

1. Audit package.json dependencies and official Skybridge source before installation.
2. Review the committed npm v3 package-lock.json and current dependency advisories before installation. Regenerate it deliberately when dependencies change.
3. Run npm ci --ignore-scripts after review. Investigate necessary native installation hooks separately.
4. Set SKYBRIDGE_TELEMETRY_DISABLED=1 and DO_NOT_TRACK=1 in the shell before executing any Skybridge CLI.
5. Run npm run test:fixture, npm run build, then npm run dev; no public tunnel.
6. Verify actual MCP initialize, tools/list, both tools/call, invalid categories, and React view rendering in localhost DevTools.
7. Audit egress, confirm latest GitHub head SHA/CI and obtain separate merge or deployment approval.

Upstream reviewed: alpic-ai/skybridge@6dd443908113b5218d20a5016ed6c34d223e5146.
Verified on 2026-10-20 using isolated Node 24.19.0/npm 11.9.0: genuine lockfile generation, installation with lifecycle scripts disabled, 11 fixture tests, full TypeScript checking and production build passed. An exact @opentelemetry/api 1.9.1 dependency satisfies PostHog's optional peer import that otherwise breaks Skybridge's server bundle.

Actual built Skybridge MCP passed initialize, tools/list, both tools/call and invalid-category rejection through its Express adapter bound only to 127.0.0.1 on an ephemeral port. This used the framework's VERCEL=1 adapter locally; it was not a Vercel deployment. React rendering and the normal dev-server process were not tested.

The installed CLI telemetry gate and tool-call metric middleware both honor SKYBRIDGE_TELEMETRY_DISABLED=1 and DO_NOT_TRACK=1. Those flags were set for build and protocol checks. This source review is not a network packet/egress audit.

## Hold conditions

- npm audit reports five high-severity affected packages through braces -> chokidar -> nodemon -> Skybridge and its Vite plugin. Advisory GHSA-vfj7-8cjw-p6xm (CVE-2026-93687) has no published patched braces version as of this verification. Do not treat this lockfile as security approval or apply npm's unrelated major downgrades automatically.
- React/DevTools rendering, normal dev-server startup and observed network egress remain unverified. The dependency advisory must be resolved or explicitly reviewed before broader use.
- Root AGENTS.md now states the merge approval policy explicitly; the governance check passed at b3957a6. Always verify CI again on the latest PR head.
- Do not use Production/payment data, private specs/logs, tokens or internal endpoints.
- The app never becomes authority for real Production or current GitHub status.

Rollback: discard this isolated project; leave all existing KKS and Continue configuration untouched.
