# Model Routing Review Receipt — 2026-09-17

Scope: review the current MCP configuration and make model selection a reusable, time-sensitive Project ability.

## Findings

- `mcp_config.json` is transport/tool configuration for the GitHub MCP server; it is not a model-selection contract.
- Model routing is maintained under `KKS-MODEL-ROUTING-R1` in Project governance, Agent, Skill, and capability-routing sources.
- Explicit model selection must resolve the active ChatGPT/Work/Codex/API surface first, because model selectors and plan/workspace access differ by surface.
- The routing matrix was checked against current official OpenAI model documentation on 2026-09-17.
- Production evidence rules are unchanged: model choice cannot replace source/spec/runtime evidence, validation, approvals, or HOLD gates.

## Current routing baseline

- Complex reasoning, coding, KTC Production debugging and cross-system RCA: GPT-5.6 Sol; use higher reasoning effort when available.
- Routine professional/coding work where exposed: GPT-5.6 Terra.
- Simple/high-volume/cost-sensitive work where exposed: GPT-5.6 Luna.
- Very difficult or long-running multi-step workflows: GPT-6 Pro/Astra when the active plan/workspace/product exposes it.

## Freshness

Re-check current official availability when the verification is older than 7 calendar days, when a model is renamed/removed, or when the active product presents a new model. Managed Business admins may use Admin Console → Models → Test when exact member model access is material.

Status: `READY_FOR_REVIEW`.
