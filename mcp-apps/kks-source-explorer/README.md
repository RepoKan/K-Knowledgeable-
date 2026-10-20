# KKS Source Explorer MCP App pilot

STATUS: LOCAL BUILD, MCP AND DEVTOOLS VERIFIED; CANDIDATE; NOT DEPLOYED.

SPEC R1 was approved for two read-only tools using public fixtures on 2026-10-14. The owner authorized resolving and merging the reviewed outstanding PRs on 2026-10-20. Public tunnels, connector registration and deployment still require separate approval.

## Run and verify locally

Use isolated Node >=24.18.0. Review the committed npm v3 lockfile and advisories, then run `npm ci --ignore-scripts`. Set `SKYBRIDGE_TELEMETRY_DISABLED=1` and `DO_NOT_TRACK=1` before any Skybridge command.

- `npm run test:fixture`: public fixture contracts and a real nodemon watcher regression.
- `npm audit --audit-level=high`: dependency gate; no advisory suppression.
- `npx --no-install tsc --noEmit`: complete type check.
- `npm run build` then `npm run test:runtime`: production bundle and actual loopback MCP, including eight cloud/tunnel denial checks.
- `npm run dev -- --plain --no-open`: local DevTools. Do not enable a tunnel. The installed framework's normal listener is not a hardened public service; use a loopback-only test environment.

The tools return packaged public references and a dated candidate snapshot. They do not query current GitHub state. Existing Continue runtime and root MCP configuration are untouched.

## Dependency compatibility

Skybridge 2.0.3 uses PostHog's optional OpenTelemetry import during bundling; @opentelemetry/api 1.9.1 is pinned to make the server build reproducible. tsx 4.23.15 is explicit for development. nodemon.json watches only the literal src directory and includes TSX/MJS fixture changes, using `node --import tsx` rather than the CLI's optional IPC server.

The scoped nodemon -> chokidar 4.0.3 override removes the vulnerable braces dependency chain (GHSA-vfj7-8cjw-p6xm). It is an application compatibility override, not a patched braces release. Chokidar 4 removes glob handling: do not add glob watch paths or assume general nodemon configuration compatibility. The committed regression covers change/add/unlink restarts for this pilot's literal-directory configuration. Reevaluate the override when upstream changes.

## Verification (2026-10-20)

Node 24.19.0/npm 11.9.0: locked installation with lifecycle scripts disabled, 12 fixture/watcher tests, full type checking, production build and zero-vulnerability npm audit passed locally. Actual Skybridge MCP initialize, tools/list, both calls and invalid categories passed on loopback. Both React views rendered in DevTools; filters and provenance expansion were checked. GitHub CI repeats installation, audit, tests, build and runtime protocol/route checks on PRs and main; inspect the exact current head before relying on it.

DevTools includes a cloud-status probe even when CLI telemetry is disabled. Application middleware now returns 403 for all /__skybridge/deploy and /__skybridge/tunnel routes before upstream SDK handlers execute. The local browser check used a loopback SDK base URL, non-loopback fetch/UDP guards and a browser request allowlist; no outbound attempts were recorded after the fix. This scoped test is not a comprehensive packet-level or external-host audit.

## Remaining boundary

No ChatGPT host connection, public tunnel, remote registration or deployment was tested or authorized. The app remains CANDIDATE. Never supply Production/payment data, private files, tokens or internal endpoints. Local checks do not grant Production authority.

Rollback: revert the PR merge or discard this isolated project; preserve existing KKS and Continue configuration.
