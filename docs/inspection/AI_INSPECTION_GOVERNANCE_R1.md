# AI Inspection Governance R1

Status: Public/sanitized framework guidance  
Date: 2026-09-11

## Purpose

Define the generic inspection contract used by private application repositories that link to a private Knowledge Master. This public file intentionally contains no production source, credentials, restricted specifications, production logs, or confidential endpoint/configuration data.

## Inspection identity

Every investigation must bind these identities before a fix is proposed:

```text
application source commit SHA
+ pinned Knowledge Master commit SHA
+ approved specification/version
+ matched runtime/device/log evidence identity when applicable
```

## Required analysis chain

```text
Problem
 -> exact source file/function
 -> caller/callee graph
 -> state/callback/thread behavior
 -> SDK/database/network boundary
 -> protocol/business-rule impact
 -> risk
 -> validation matrix
 -> rollback
```

## Source authority

1. Exact source revision under inspection
2. Approved project/customer specification
3. Official vendor documentation
4. Matched runtime evidence
5. Approved project business rules
6. Derived knowledge/design documents
7. General AI/model knowledge

A lower authority may explain a gap but must not silently override a higher authority.

## AI output states

- `READY TO APPLY` — evidence and impact checks are complete.
- `HOLD - IMPACT NOT PROVEN` — a required source/spec/runtime path cannot be proven.
- `NO CHANGE REQUIRED` — inspected behavior already satisfies the authoritative requirement.

## PR/Impact Gate

AI-generated production-relevant proposals must be made on a review branch/PR, never committed directly to the production baseline. The PR should include finding, evidence, impacted files/functions, protocol/state impact, validation cases, and rollback.

## Security boundary

Do not place credentials, signing keys, private keys, payment security keys, customer/card data, production secrets, restricted logs, or confidential source into this public framework repository. Private application and Knowledge Master repositories enforce their own access controls.
