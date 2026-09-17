# K Knowledge Supporting Model Routing R1

Rule ID: `KKS-MODEL-ROUTING-R1`

Last externally verified: `2026-09-17`

This is a sanitized capability-routing rule. It controls **which currently available model tier should be preferred for a job**. It is not Production evidence and does not change payment, device, host, security, or business-rule authority.

## Why this rule exists

The repository `mcp_config.json` is an MCP transport/tool configuration. Its current job is to expose the GitHub MCP server and toolsets. It does **not** select an OpenAI model and should not be overloaded with model-routing policy.

Model routing belongs in the Project capability/agent/skill governance layer because:

1. MCP availability and model availability change independently.
2. Static MCP configuration cannot grant a model that the active ChatGPT/Work/Codex/API workspace does not expose.
3. The best model depends on task complexity, execution surface, latency/cost sensitivity, and required reasoning depth.
4. Model names and access can change faster than Project governance revisions.

## Source-of-truth order for model availability

When a task requires an explicit model choice, resolve availability in this order:

1. The active product/workspace model picker or model-access settings for the actual user/workspace.
2. Current official OpenAI Help Center / OpenAI API model documentation.
3. This rule's last-verified matrix as a routing fallback only.

If the current workspace does not expose the preferred model, do not claim it is available. Select the strongest appropriate model that is actually available and record the fallback when quality could materially change.

For managed ChatGPT Business workspaces, administrators can use **Admin Console → Models → Test** to inspect which models a member can access and which settings contribute to that access. This test is observational; it does not grant access or change usage limits.

## Current verified model families

As verified from official OpenAI sources on 2026-09-17:

- `GPT-5.6 Sol` / API `gpt-5.6-sol` (alias `gpt-5.6`) — flagship choice for complex reasoning, coding, research, science, computer use, and difficult professional work.
- `GPT-5.6 Terra` / API `gpt-5.6-terra` — balanced capability/cost choice for routine professional work and everyday coding.
- `GPT-5.6 Luna` / API `gpt-5.6-luna` — fastest / lowest-cost GPT-5.6 tier for simple, repetitive, or high-volume workloads.
- `GPT-5.6 Sol Pro` — Pro-model route for particularly difficult or longer-running ChatGPT work where exposed by the user's plan/workspace.
- `GPT-6 Pro`, powered by `GPT-6 Astra` — highest-capability route when the active Chat/Work/Codex surface exposes it and the job benefits from a difficult or long-running multi-step workflow.

Current official guidance reports that Astra in Codex requires Codex CLI `0.153.0` or newer. GPT-5.6 in Codex requires Codex CLI `0.144.0` or newer.

OpenAI has announced retirement of GPT-5.5 from ChatGPT, ChatGPT Work, and Codex on `2026-10-14`. Do not create new Project routing rules that depend on GPT-5.5. Existing saved model selections should be migrated to a currently supported GPT-5.6/Astra route before that date. This retirement does not apply to the OpenAI API.

## Surface availability rule

Model names cannot be treated as globally selectable across every surface.

- **Standard ChatGPT conversations:** GPT-5.6 Sol is the primary complex-work route on eligible paid plans. Free/Go users receive GPT-5.6 Luna. Terra and Luna are **not manually selectable** in ordinary ChatGPT conversations.
- **ChatGPT Work:** eligible plans can expose Sol/Terra/Luna; Astra availability depends on plan/workspace permissions.
- **Codex:** eligible plans can expose Sol/Terra/Luna; Astra availability depends on plan/workspace permissions and minimum client version.
- **OpenAI API:** use explicit model IDs such as `gpt-5.6-sol`, `gpt-5.6-terra`, and `gpt-5.6-luna` according to current API documentation.

Always resolve the active surface before applying the job matrix below.

## Job-to-model routing

| Job class | Preferred route | Reasoning guidance | Fallback rule |
|---|---|---|---|
| KTC Payment / Production debugging / EMV / CTLS / ISO8583 / TLE / reversal / settlement RCA | GPT-5.6 Sol | High / Extra High where available | Use the strongest available reasoning model; do not silently downgrade a material Production-impact review |
| Complex Kotlin/Android/SUNMI P3 debugging, architecture, multi-file impact tracing | Codex or Work with GPT-5.6 Sol | High / Extra High | Terra only when the task is bounded and lower risk; disclose downgrade for material RCA |
| Very large multi-step coding/research/computer-use workflow with many tools or long execution | GPT-6 Pro / Astra when actually available | Highest product-supported effort | GPT-5.6 Sol High / Extra High; Sol Pro where exposed |
| Routine feature coding, code explanation, ordinary refactor, test scaffolding | GPT-5.6 Terra in Work/Codex/API | Medium / High | Sol when ambiguity/impact increases; Luna for mechanical edits only |
| Requirements comparison, RFI/spec analysis, technical documentation with moderate complexity | GPT-5.6 Terra in Work/API | Medium / High | Sol for conflicting evidence or cross-domain synthesis |
| Simple summarization, formatting, extraction, renaming, repetitive classification | GPT-5.6 Luna where exposed | Lowest effort that preserves correctness | Terra when context or ambiguity grows |
| High-volume low-risk API automation | GPT-5.6 Luna | Lowest effort that preserves correctness | Terra when error rate or ambiguity rises |

## K Knowledge Supporting escalation rules

Model selection never replaces the Project evidence gates.

For payment-critical or Production-impacting work:

- Prefer capability over cost/latency.
- Load exact source/spec/runtime revisions before drawing conclusions.
- Use the highest appropriate reasoning level available for cross-file or cross-system impact analysis.
- Escalate from Luna/Terra to Sol when evidence conflicts, behavior is ambiguous, or downstream impact is material.
- GPT-6 Pro/Astra may be used for very large agentic investigations when available, but it does not waive source authority, test requirements, approval gates, or `HOLD - IMPACT NOT PROVEN`.
- If a preferred model is unavailable, state the actual fallback model when that could affect confidence or completeness.

## Freshness rule

This routing matrix is **not a permanent model catalog**.

Before an explicit model-selection decision that affects an operational workflow:

1. Check the active workspace/product model availability first.
2. Re-check official OpenAI model documentation when the last external verification is older than 7 calendar days, when a model disappears/changes name, or when a new model is offered by the active product.
3. For managed workspaces, use the Admin Console model-access test when exact member access is material and available to the administrator.
4. Record the new verification date and update this rule when the change alters routing behavior.
5. Prefer durable capability tiers (`highest-capability`, `balanced`, `fast/cost-efficient`) in automation logic and resolve them to current model IDs at runtime.
6. Never hard-code a deprecated model as the only route.

## MCP separation-of-concerns rule

`mcp_config.json` remains a tool transport configuration. Model routing must not be embedded there unless the consuming MCP client explicitly defines a model-routing schema.

The live connector/tool contract is the capability boundary. Static JSON cannot increase connector permissions, install Notion/GitHub access, enable a model, or bypass workspace policy.

## Official sources used for this verification

- https://help.openai.com/en/articles/20001354-gpt-5-6
- https://help.openai.com/en/articles/20001275/
- https://platform.openai.com/docs/models
- https://openai.com/products/release-notes/

## Status

- Governance status: `READY_FOR_INHERITANCE`
- Model catalog status: `TIME-SENSITIVE / VERIFY AT USE`
- Production authority: `NONE — ROUTING METADATA ONLY`
