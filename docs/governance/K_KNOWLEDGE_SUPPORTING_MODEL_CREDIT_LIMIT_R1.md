# K Knowledge Supporting Model and Credit Limit Gate R1

Rule ID: `KKS-MODEL-CREDIT-LIMIT-GATE-R1`

Effective: `2026-09-26`

Scope: all current and future **K Knowledge Supporting** Project chats, ChatGPT Work/Codex tasks, API workflows, and governed Freebuff processing when this Project governance is loaded and the relevant execution surface exposes the required model/quota controls.

## Purpose

Keep model quality, rate limits, and credit/spend consumption inside the Project's current authorized quota without inventing account state or silently reducing the quality of Production-critical work.

This rule governs routing and budget behavior only. It does not grant model access, API credentials, billing authority, connector permission, Production evidence, or approval to change external account settings.

## Project model profile

The Project-wide preferred routing profile is:

- `PRIMARY = gpt-5.6-sol`
- `SECONDARY = gpt-5.6-terra`
- `ECONOMY = gpt-5.6-luna`
- `CODEX = gpt-5.6-sol`

Use `KKS-MODEL-ROUTING-R1` to resolve the actual model on the active surface. The active product/workspace remains the technical source of truth for availability.

Routing intent:

1. Use PRIMARY for complex reasoning, difficult coding, cross-system analysis, and Production-sensitive investigation.
2. Use SECONDARY for bounded professional work where capability/cost balance is appropriate.
3. Use ECONOMY for simple, repetitive, high-volume, or low-risk work.
4. Use CODEX for coding-agent work unless the active Codex surface exposes a stronger user-approved route.
5. Never silently downgrade a Production-critical task merely to save credits. If the model required for reliable work cannot fit the available governed budget, stop with a credit/budget hold instead.

## OpenAI project target

The logical OpenAI API project target for K Knowledge Supporting is **Loxbit → KKL**.

Public governance must not contain OpenAI API keys, secret values, or account credentials. Public governance also avoids binding to an internal project identifier; exact project identifiers belong in the private control plane.

Selecting KKL in governance does not itself switch the OpenAI Platform account default. Account-side project selection must be performed and verified through an authorized OpenAI Platform control surface.

## Freebuff API rate-limit profile

For governed Freebuff processing under the KKL API project, the desired project-level overrides are:

| Model | Role | max_requests_per_1_minute | max_tokens_per_1_minute |
|---|---|---:|---:|
| `gpt-4o` | Primary/default Freebuff interactive workload | 5 | 20,000 |
| `gpt-5.5` | Secondary/high-quality Freebuff escalation | 1 | 20,000 |

Every other model remains **Inherited** from the organization unless a later Project-wide rule explicitly changes it.

These are Freebuff API controls only. They do not replace the Project-wide GPT-5.6 ChatGPT/Work/Codex routing profile above.

A project override may not exceed the effective organization limit. If the organization grants less capacity, the lower effective limit wins.

Repository governance records the desired state; it must not claim the OpenAI Platform override is active until the live Platform setting is read back or otherwise verified.

## Credit and quota gate

Run this gate per governed workload/turn before any **additional** billable model or tool action whenever the active app/API exposes an authoritative quota, credit, hard-spend, or remaining-balance signal.

### CREDIT_OK

Use `CREDIT_OK` only when the authoritative app-local remaining amount is greater than zero and the next governed action is allowed by the effective limit.

### CREDIT_STOP

If the authoritative remaining amount is `<= 0`:

1. stop immediately before the next billable model/tool action;
2. do not retry through another paid model merely to bypass the exhausted pool;
3. do not borrow or infer credits from a different app/project/account;
4. report `CREDIT_STOP` and identify the exhausted app-local pool when known.

### CREDIT_STOP_BEFORE_EXECUTION

If a supported projection based on the authoritative current balance and current pricing/usage evidence shows:

`remaining - projected_next_step <= 0`

stop before executing that next billable action.

A projection must be evidence-based. Never invent token counts, prices, balances, or unexposed ChatGPT/Codex quotas to manufacture a stop condition.

### CREDIT_UNKNOWN

If the current app does not expose an authoritative remaining-credit/quota value:

- use `CREDIT_UNKNOWN`, not zero;
- never claim that credits are exhausted or sufficient;
- do not fabricate a numerical balance from conversation length or subjective task difficulty;
- for an external paid API action whose budget compliance must be proven and no hard platform cap is verified, hold the additional paid action until an authoritative budget signal or enforced cap is available;
- for product-managed ChatGPT/Work/Codex usage where the platform itself owns enforcement and does not expose a numeric remaining balance to the assistant, allow the platform to enforce its own limit and state the limitation only when it materially affects the requested workflow.

## Same-app accounting rule

Credit/quota arithmetic is app-local by default.

Do not combine or transfer balances among ChatGPT, Work, Codex, OpenAI API, Freebuff, or another provider unless an authoritative billing source proves they share the same pool.

Rate limits (RPM/TPM), monetary spend limits, and product message/credit quotas are different controls. Never convert one into another without an authoritative conversion.

## Warning and stop precedence

1. External/platform hard enforcement always wins.
2. A lower organization/project rate limit wins over a requested higher override.
3. `CREDIT_STOP` and `CREDIT_STOP_BEFORE_EXECUTION` override model-routing preference.
4. Production/source/evidence HOLD gates override model and budget convenience.
5. When credits are positive but constrained, route to the lowest-cost model that still satisfies the task's required quality and risk class.
6. If no compliant model fits the available verified budget, stop rather than silently lowering the required quality.

## Verification boundary

A governance document, environment file, or chat instruction is not proof that an external OpenAI project default, rate limit, hard spend limit, or key has changed.

Use:

- `DESIRED` for a requested control recorded in governance;
- `APPLIED_UNVERIFIED` only when a mutation was accepted but not read back;
- `CONFIRMED` only after the live external state is verified;
- `NOT APPLIED` when the active connector/tool exposes no mutation path.

## Status

- Governance status: `READY_FOR_INHERITANCE`
- External OpenAI Platform mutation authority: `SEPARATE / VERIFY LIVE`
- Production authority: `NONE — ROUTING AND BUDGET GOVERNANCE ONLY`
