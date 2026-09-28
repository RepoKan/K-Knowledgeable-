# Sourcebot self-hosted integration

Status: feature-branch integration  
Upstream: `sourcebot-dev/sourcebot`  
Release: `v5.1.14`  
Pinned upstream commit: `3c0e5ca6f07f524b42490a5feef4ff9a0824c990`

## Purpose

Use Sourcebot as a self-hosted code-search and code-context layer for humans and agents while keeping K Knowledge Supporting source-governance rules intact.

## Repository integration

This repository pins Sourcebot as a Git submodule at `tools/sourcebot`. The exact upstream identity is also recorded in `configs/sourcebot/upstream.lock.json`.

Clone with submodules:

```sh
git clone --recurse-submodules https://github.com/RepoKan/K-Knowledgeable-.git
```

For an existing clone:

```sh
git submodule update --init --recursive
```

The submodule is intentionally pinned to an exact release commit. Do not silently move the pin to upstream `main`; review and validate an upstream release before changing the lock and gitlink together.

## Licensing

Sourcebot core code is licensed under FSL-1.1-ALv2, while content under upstream `ee/` uses separate Sourcebot enterprise license terms. The FSL explicitly permits internal use. Preserve upstream notices and review the license before redistribution, commercial service exposure, or derivative distribution.

## Deployment model

For normal self-hosted use, prefer Sourcebot's published container deployment rather than rebuilding from source. Current v5 deployment uses separate Sourcebot, PostgreSQL, and Redis services.

Use `configs/sourcebot/config.example.json` as a sanitized starting point. Keep deployment secrets and private repository credentials outside this public repository.

Recommended secret handling:

- generate `AUTH_SECRET` locally;
- generate `SOURCEBOT_ENCRYPTION_KEY` locally;
- keep database, Redis, OAuth, GitHub, and Sourcebot API credentials in the deployment environment or secret manager;
- never commit real tokens, credentials, or private endpoints here;
- optionally set `SOURCEBOT_TELEMETRY_DISABLED=true` when required by deployment policy.

## Human workflow

Self-hosted Sourcebot provides a fast code-understanding surface for:

- cross-repository code search;
- regex and filtered search;
- file browsing and navigation;
- git history and blame.

## Agent workflow

Sourcebot exposes its MCP endpoint at:

```text
https://your-sourcebot-host.example.com/api/mcp
```

The current Sourcebot product places the MCP agent context layer and Ask Sourcebot behind a paid entitlement. Treat MCP as optional until the deployed instance exposes it.

When MCP is available, connect the active agent to the deployment and use the `sourcebot-code-context` Skill in `.github/skills/sourcebot-code-context/`.

Prefer OAuth when the client and Sourcebot deployment support it. For API-key auth, keep the key in a local environment variable or credential store; do not commit it into MCP JSON.

## Skills

Two reusable instruction layers are included:

- `.github/skills/sourcebot-code-context/`: ChatGPT-style governed skill for using Sourcebot as a multi-repository context layer.
- `sourcebot-skills/k-knowledge-codebase-guide.md`: Sourcebot-native skill that can be synced or adopted inside a self-hosted Sourcebot deployment.

## Authority rules

Sourcebot is an indexed snapshot, not the live GitHub control plane.

Use Sourcebot for:

- code discovery across many repositories;
- file and symbol tracing;
- architecture questions;
- cross-repository impact analysis;
- indexed branch and diff research.

Use the native GitHub connector for:

- current PR and issue state;
- checks and workflow runs;
- permissions and repository settings;
- branch protection and rulesets;
- refs created after the last Sourcebot sync.

For Production-impact analysis, preserve the exact repository, ref, SHA, applicable specifications, and runtime evidence required by K Knowledge Supporting governance.
