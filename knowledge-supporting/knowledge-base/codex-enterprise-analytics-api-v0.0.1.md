# Codex Enterprise Analytics API — Workspace Usage & Code Review Metrics

> Public-sanitized knowledge capture from a user-supplied OpenAPI 3.1.0 schema. No admin key, workspace ID, or other secret material is stored here. This capture has **not** been independently verified against external OpenAI documentation.

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

Use an Admin key, not an API Platform project key.

Security rule: keep the key in a secret manager or environment variable and send it only as:

```http
Authorization: Bearer <admin_api_key>
```

Never commit the key, workspace IDs, or bearer headers to source control.

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
- Verification state: candidate / not externally verified in this capture
- Confidential data stored: none
