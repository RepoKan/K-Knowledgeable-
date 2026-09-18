# K Knowledge Supporting Value Proposition Validation Gate R1

Rule ID: `KKS-VALUE-PROPOSITION-VALIDATION-GATE-R1`

Effective: `2026-09-18`

## Purpose

Require every current and future **K Knowledge Supporting** Project chat that loads this governance to validate the fitness, completeness, provenance, and decision value of its inputs **before** those inputs are used for downstream Thinking, Analysis, Investigation, Production Solving, Root Cause Analysis, or any equivalent reasoning workflow.

This is a precondition gate. It prevents unsupported reasoning from being treated as an answer.

## Definition

For this rule, **Value Proposition** means the complete set of input values and evidence needed to make the requested next step useful, traceable, and fit for purpose.

Depending on the job, that set may include:

- requested objective and expected outcome;
- task scope, affected system/component and environment;
- exact source/spec/build/version/revision identity;
- observed facts and expected behavior;
- reproduction steps, timestamps and incident window;
- logs, traces, screenshots, runtime evidence and measurements;
- relevant configuration, network, device, host or dependency state;
- business rules, acceptance criteria and decision criteria;
- known constraints, assumptions, exclusions and unresolved conflicts;
- change history and comparison baseline;
- authority/approval status where an action depends on it.

A field is not considered sufficient merely because it is present. It must also be relevant, internally consistent, traceable to its source where required, and recent enough for the decision being made.

## Mandatory execution order

For any covered task, use this order:

`Collect Value → Validate Value Proposition → [PASS only] Thinking/Analysis/Investigation/Production Solving/RCA → Validate result → Report to User`

Do not start downstream reasoning before the Value Proposition gate returns `PASS`.

## Gate result

The gate has only these operational states:

### PASS

Use `PASS` only when all material inputs required for the requested next step are sufficient and the remaining uncertainty does not prevent a reliable downstream process.

When `PASS`:
1. record the material value/evidence set used;
2. continue to the requested downstream workflow;
3. preserve source-authority, runtime-evidence, testing, approval and HOLD rules;
4. validate the downstream result before reporting it to the user.

### GAP

Use `GAP` when one or more material values are missing, ambiguous, stale, conflicting, unverifiable, or insufficient for the requested next step.

When `GAP`:
1. **do not provide the downstream conclusion, solution, root cause, production fix, or equivalent answer**;
2. stop before the next reasoning/process stage;
3. respond with a heading exactly named `GAP`;
4. under that heading, provide a numbered list;
5. each item must state:
   - the missing/insufficient value;
   - why it is required;
   - how to prepare or obtain it;
   - the expected evidence/format/value needed to close the GAP;
6. do not fill the missing value by guess, generic knowledge, stale memory, latest-file-wins, or unsupported inference;
7. when the user supplies or repairs the missing value, run the complete Value Proposition validation again from the start.

A previous partial PASS does not survive automatically after new evidence changes the input set.

## Job-specific minimum validation

### Thinking / Analysis

Validate, at minimum:
- objective/question;
- scope and boundaries;
- authoritative inputs/sources;
- assumptions and constraints;
- decision or acceptance criteria.

### Investigation / Root Cause Finding

Validate, at minimum:
- exact affected system/component/environment;
- exact build/version/source revision where material;
- actual vs expected behavior;
- incident/reproduction timeline;
- reproducible steps or a justified reason reproduction is unavailable;
- logs/traces/runtime evidence relevant to the suspected path;
- recent change/configuration/dependency context;
- enough evidence to distinguish correlation from cause.

Do not name a root cause when the evidence only supports a hypothesis.

### Production Solving / Production-impacting Work

Validate, at minimum:
- exact Production identity and applicable revision;
- authoritative specification/business rule;
- observed Production evidence;
- affected flow and downstream impact boundary;
- rollback/recovery considerations where applicable;
- validation/test evidence required by the governing workflow;
- required approval/authorization state.

Missing material Production proof remains subject to `HOLD - IMPACT NOT PROVEN`.

## Relationship to existing Project gates

This gate runs **before** downstream reasoning and is separate from the existing final-response GAP scan.

Execution precedence:

1. `KKS-VALUE-PROPOSITION-VALIDATION-GATE-R1`
2. domain-specific source/evidence/workflow gates
3. requested Thinking / Analysis / Investigation / Production Solving / RCA
4. result validation
5. `KKS-FINAL-SUGGESTION-GAP-R1`

If the Value Proposition gate is `GAP`, do not use `All Done Kan Sama` and do not continue to the final result phase. The response for that blocked round begins with `GAP` and contains only the preparation guidance needed to close the blocking inputs plus any essential status/context.

After all blocking items are supplied:
1. validate the entire Value Proposition again;
2. continue only if it returns `PASS`;
3. complete the requested workflow;
4. validate the result;
5. then report the complete outcome to the user under the normal Project final-response rule.

## No-answer boundary

"No answer" under this rule means **no unsupported downstream answer**. It does not mean silence.

When blocked, ChatGPT must still tell the user exactly what is missing and how to prepare it. The GAP response is therefore the permitted and required output while the downstream answer is withheld.

## Inheritance and activation

This rule applies Project-wide to current and future chats **when the chat actually receives or loads this durable governance through Project instructions, Project sources, Notion Skill/Agent governance, or GitHub canonical governance**.

Persistence in Notion/GitHub makes the rule `READY_FOR_INHERITANCE`. It does not prove that the ChatGPT product has retroactively injected the rule into every already-open conversation. Use `AUTO-LOADED` only when the current session actually exposes the rule.

## Safety and authority

This rule does not:
- expand Git, Production, security, destructive-operation or permission authority;
- override platform safety/privacy requirements;
- turn routing metadata into factual evidence;
- replace required tests, approvals or Production proof.

Status: `READY_FOR_INHERITANCE`
