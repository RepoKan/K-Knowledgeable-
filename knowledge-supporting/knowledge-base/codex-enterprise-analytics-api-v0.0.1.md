# Codex Enterprise Analytics API — Workspace Usage & Code Review Metrics

> **Status: CANDIDATE — PARTIALLY EXTERNALLY VERIFIED / CANONICAL SCHEMA VERIFICATION PENDING.** Public-sanitized knowledge capture from a user-supplied OpenAPI 3.1.0 schema. No admin key, workspace ID, or other secret material is stored here. External OpenAI documentation was reviewed on 2026-09-18, but the authenticated Codex Analytics API reference still needs field-level verification.

## Source identity

- OpenAPI: `3.1.0`
- Title: `codex-backend-enterprise-analytics`
- Version: `0.0.1`
- Server: `https://api.chatgpt.com/`
- API family: `Codex Enterprise Analytics`
- Authentication: HTTP Bearer
- Base path: `https://api.chatgpt.com/v1/analytics/codex`

## Authentication model

The supplied contract describes workspace-scoped ChatGPT/Codex administrator access using an **Admin key** created in the OpenAI Admin Console with custom permission **Codex analytics API = Read**, granting scope:

```text
codex.enterprise.analytics.read
```

Current official OpenAI documentation is internally inconsistent on the credential type. The Admin-key Help Center guidance describes workspace-scoped **Admin keys** and confirms the `codex.enterprise.analytics.read` permission. However, the current English Codex Help Center page and OpenAI Developers/Learn Analytics API pages describe an **organization / Platform organization API key** for Codex Enterprise Analytics. Those pages point to the authenticated Codex Enterprise Analytics API reference as the source of truth for current key provisioning and access requirements. Public access to that reference redirects to ChatGPT login, so the conflict cannot be resolved from unauthenticated public documentation. Treat the credential type as an **official-source conflict pending authenticated-reference verification**.

Security rule: keep the key in a secret manager or environment variable and send it only as:

```http
Authorization: Bearer <admin_api_key>
```

Never commit the key, workspace IDs, or bearer headers to source control.

## External verification matrix — 2026-09-18

| Contract area | Verification state | Evidence boundary |
|---|---|---|
| Codex Enterprise Analytics capability exists | Confirmed externally | Current OpenAI Codex enterprise analytics documentation |
| Admin key + `codex.enterprise.analytics.read` | Confirmed in current Help Center guidance | OpenAI Help Center |
| Authentication credential type | Official-source conflict | Admin-key guidance: workspace-scoped Admin key + `codex.enterprise.analytics.read`; current English Codex Help Center and Developers/Learn: organization / Platform organization API key. Authenticated API reference is required to resolve. |
| `api.chatgpt.com` Admin API host family | Confirmed at host-family level | Current OpenAI Admin API guidance |
| Exact `/v1/analytics/codex/workspaces/{workspace_id}/...` routes | Supplied OpenAPI only | Authenticated API-reference verification pending |
| `start_time`, `end_time`, UTC inclusive/exclusive rules, default 30-day window | Supplied OpenAPI only | Authenticated API-reference verification pending |
| `limit=1..30000`, default `1000`, `page`/`next_page` cursor behavior | Supplied OpenAPI only | Authenticated API-reference verification pending |
| `group=workspace` semantics | Supplied OpenAPI only | Authenticated API-reference verification pending |
| Usage/review/response schemas and field names | Supplied OpenAPI only | Authenticated API-reference verification pending |
| Client/model enums, unknown-value behavior | Supplied OpenAPI only | Authenticated API-reference verification pending |
| Credits/USD/estimated-cost field semantics | Supplied OpenAPI only | Authenticated API-reference verification pending |
| Code-attribution metrics | Supplied OpenAPI only | Authenticated API-reference verification pending |
| P0/P1/P2 and review-response/merged-PR semantics | Supplied OpenAPI only | Authenticated API-reference verification pending |
| HTTP 422 `HTTPValidationError` schema | Supplied OpenAPI only | Authenticated API-reference verification pending |
| OpenAPI title/version `codex-backend-enterprise-analytics` / `0.0.1` | Provenance confirmed only from supplied artifact | No externally published canonical artifact was established |

**Normative boundary:** Public OpenAI documentation confirms that Codex Enterprise Analytics exists and that `codex.enterprise.analytics.read` is an available permission, but current official pages conflict on the credential type. OpenAI identifies the authenticated Codex Enterprise Analytics API reference as the authoritative source for current key provisioning, access requirements, routes, request/response schemas, metrics, time semantics, pagination, and field-level behavior. Because unauthenticated access to that reference redirects to ChatGPT login, the exact authentication mechanism and schema-level contract below remain candidate material until the reference is checked with authorized workspace access.

**Labeling rule:** Unless a section is explicitly marked externally confirmed above, exact routes, parameters, defaults, field names, enum values, response envelopes, error models, and metric semantics below are **Supplied OpenAPI v0.0.1 — authenticated-reference verification pending**.

## Endpoint inventory

| Method | Path | Purpose | Response |
|---|---|---|---|
| GET | `/v1/analytics/codex/workspaces/{workspace_id}/usage` | Daily Codex usage, per user by default or workspace aggregate with `group=workspace` | `UsagePage` |
| GET | `/v1/analytics/codex/workspaces/{workspace_id}/code_reviews` | Daily Codex code-review volume, comments, and P0/P1/P2 severity counts | `PageReviews` |
| GET | `/v1/analytics/codex/workspaces/{workspace_id}/code_review_responses` | Daily replies, reactions, and engagement with Codex review comments | `PageCodeReviewResponses` |

## Shared request semantics

All endpoints use:

- `workspace_id`: required UUID path parameter.
- `start_time`: optional Unix seconds, inclusive, UTC.
- `end_time`: optional Unix seconds, exclusive, UTC.
- `limit`: integer `1..30000`, default `1000`.
- `page`: opaque cursor copied from the previous response's `next_page`.

When both time bounds are omitted, the supplied schema defines the reporting window as the last 30 calendar days ending today in UTC. When `end_time` alone is omitted, the reporting window ends at today in UTC.

The usage endpoint additionally supports:

```text
group=workspace
```

Use it for workspace-wide aggregate rows; omit it for per-user rows.

## Pagination contract

Page responses follow this pattern:

```json
{
  "object": "page",
  "data": [],
  "has_more": true,
  "next_page": "cursor-token"
}
```

When `has_more` is true, pass `next_page` unchanged as the next request's `page` value. Do not parse or synthesize the cursor.

## Usage data model

A `UsageRow` contains:

- daily `start_time` and exclusive `end_time`
- `user_id` and `actor` for per-user rows; null for workspace aggregates
- `totals`
- `clients`
- optional `models`
- optional `code_attribution`

### Totals

`Usage` tracks:

- threads
- turns
- credits
- native `cost_usd`
- `estimated_cost_usd`
- uncached text input tokens
- cached text input tokens
- text output tokens
- total text tokens

Do not collapse these billing concepts:

- `credits` = consumed credit-billed usage.
- `cost_usd` = native USD-billed usage, separate from credits.
- `estimated_cost_usd` = estimate based on the workspace's current credit-overage rate and may differ from invoiced charges.

### Client usage

`ClientUsage` adds per-client threads, turns, credits, optional cost values, and optional token counters.

The supplied `CodexClient` enum spans major Codex surfaces including CLI, web, Chrome side panel, desktop apps, ChatGPT desktop, cloud/general agent, Atlas, Flora, Work web/mobile/desktop, VS Code, Slack, GitHub/GitHub Action, TypeScript SDK, service execution, Android Studio, Xcode, and multiple JetBrains IDE variants. Unknown clients map to `CODEX_UNKNOWN_DEFAULT`.

### Model usage

`ModelUsage` provides:

- model bucket name
- optional `speed` (`standard` or `fast`)
- credits
- native USD cost
- estimated USD cost
- token counters

Unrecognized model names are returned as `other` according to the supplied schema.

### Code attribution

`CodeAttributionMetrics` contains line-of-code attribution and optional commit attribution.

Line metrics include accepted added lines and optional removed, committed, total committed, and committed percentage values.

Commit metrics include:

- commits with at least one added line attributed to Codex
- contribution percentage
- total commit denominator

## Code review metrics

`GET /code_reviews` returns daily `ReviewsRow` objects with:

- `pull_request_reviews`
- `comments`
- `comment_details.p0`
- `comment_details.p1`
- `comment_details.p2`

This dataset represents review volume and comment severity.

## Code review response metrics

`GET /code_review_responses` returns daily `CodeReviewResponseRow` objects with:

- pull-request review count
- comments
- replies
- reactions
- `comment_response_details`
- `reaction_details`

Comment response details distinguish engaged, reacted, upvoted, downvoted, other-reacted, and replied comments. Reaction details expose raw upvote, downvote, and other-reaction counts.

The supplied response descriptions tie these engagement metrics to pull requests merged in the reporting period. Preserve that definition in dashboards rather than silently treating the data as all reviewed or open PRs.

## Validation error model

HTTP `422` uses `HTTPValidationError` with `detail[]` entries containing:

- `loc`
- `msg`
- `type`
- optional `input`
- optional `ctx`

## Collector behavior contract

A reusable analytics collector should:

1. Resolve a workspace UUID from the ChatGPT Admin workspace settings.
2. Load the Admin key from secret storage only.
3. Use UTC boundaries and remember that `end_time` is exclusive.
4. Paginate until `has_more=false`.
5. Persist raw daily rows before dashboard aggregation.
6. Keep credits, native USD cost, and estimated USD cost separate.
7. Keep per-user and workspace aggregate datasets distinguishable.
8. Preserve returned client/model identifiers exactly and handle unknown values defensively.
9. Treat null optional metrics as unavailable rather than automatically converting them to zero.
10. Never log bearer tokens or secret-bearing request headers.

## Reusable capability map

This contract can support:

- workspace adoption dashboards
- per-user usage reporting
- daily thread/turn/credit/token trends
- usage by Codex client and model
- code-attribution reporting
- code-review volume and P0/P1/P2 distributions
- engagement analysis for Codex review comments
- cursor-safe incremental data collection

## Provenance

- Capture date: 2026-09-17
- Source: OpenAPI 3.1.0 JSON supplied directly in the K Knowledge Supporting conversation
- Spec version: `0.0.1`
- External verification review: 2026-09-18
- Verification state: CANDIDATE — partially externally verified; canonical schema verification pending
- Promotion gate: use the authorized authenticated Codex Enterprise Analytics API reference to resolve the current official credential conflict and verify exact routes, parameters, response schemas, pagination, time semantics, metric definitions, enum values, and error models; reconcile every divergence before promotion
- Confidential data stored: none
