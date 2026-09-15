# com.sunmi:sunmi-ecr-service — Public Version Evidence

Archive state: `VERSION-GAP`
Packaging: AAR
License metadata: Apache-2.0
POM SCM: `https://code.sunmi.com/ta/sunmi-ecr-service`

## Current version signal

- `3.0.16` — publicly indexed with publication date 2026-08-15.
- A Sonatype result cached during this run still displayed `3.0.15`, demonstrating search-index freshness lag. The archive therefore records both the artifact source and observation date rather than trusting one cached search representation.

## Earlier exact versions captured

| Version | Publication date |
|---|---|
| 2.0.14 | 2024-07-10 |
| 2.0.22 | 2025-01-15 |
| 3.0.16 | 2026-08-15 |

## Gap

The full public ECR version sequence has not yet been enumerated from authoritative Maven metadata in this run. Missing entries are not inferred from version-number gaps.

Status remains `VERSION-GAP` until the complete metadata sequence is captured.

## Engineering relevance

ECR/device connection changes are payment-critical when ECR commands can trigger financial transactions. Required review includes bind/readiness lifecycle, transport failure, reconnect, ACK/NAK, timeout, payload limits and application-level idempotency/duplicate transaction protection.

## Binary policy

`BINARY-NOT-MIRRORED`: Maven Central remains the canonical binary source.
