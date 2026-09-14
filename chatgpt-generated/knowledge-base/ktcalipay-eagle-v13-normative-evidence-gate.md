---
title: KTCAlipay Eagle v13 Normative Evidence Gate
generated_at: 2026-09-14
classification: Public Sanitized Governance
source_classification: Restricted
status: HOLD - IMPACT NOT PROVEN
normative_scope: NONE
---

# KTCAlipay Eagle Web Service for POS Integration v13 - Normative Evidence Gate

## Purpose

This record preserves the sanitized evidence assessment for deciding whether "KTCAlipay Eagle Web Service for POS Integration v13" may be treated as normative for Android POS implementation.

It intentionally excludes specification text, private endpoints, credentials, signing or payment keys, customer/payment payloads, unredacted logs, and confidential host configuration. Restricted source files remain in approved private storage.

## Current verdict

**HOLD - IMPACT NOT PROVEN**

- KKL authority classification: A2
- KKL source type: Approved Spec
- Source confidentiality: Restricted
- Source verification: not established
- Normative scope: none
- Production application: prohibited until all mandatory evidence gates close

The A2 and Approved Spec labels are catalog classifications. They do not independently prove that the exact attached artifact was formally approved, mapped to the inspected Android revision, or certified against a matched host environment.

## Artifact identity

| Artifact | Identified metadata | SHA-256 | Evidence role |
| --- | --- | --- | --- |
| KTCAlipay Eagle Web Service for POS Integration v13 | Version 13; dated 2023-04-04; 31 pages; confidentiality marking present | `9ce59f3577b8636cb166a15297ef91477ae83124598b5e741687506f1092b7ea` | Candidate normative specification |
| KTCAlipay Eagle Web Service for POS Integration v7 | Version 7; dated 2018-04-15; 23 pages; confidentiality marking present | `3b5aec95f41f0f46e6b18dfe0941c887cfdb1e0c349a60c768652b7db3e6b705` | Historical compatibility/delta reference |
| KTC Gateway Merchandize Server-Side Direct Connection Integration Guide v2.4 Option 3 | Version 2.4; dated 2026; 31 pages; confidentiality controls present | `b5d2f8acf8427132ca95b0ccc953200bc27b209e000d13197dcd33307916f3ea` | Adjacent gateway integration family; not automatically applicable |
| KTC Electronic Data Capture API Specification v0.1.1.0 | Version 0.1.1.0; dated 2025; 22 pages | `f9276c457c0fa9e2db87bf45877bc54d31fc2b6d2b4d93390c180ef69f9246ef` | Adjacent EDC API/security family; not automatically applicable |

No embedded PDF digital signature was established for these copies. Document authorship and revision history are not substitutes for a formal approval record.

## Evidence state

| Gate | State | Established | Required closure evidence |
| --- | --- | --- | --- |
| Provenance | PARTIAL | Exact candidate files, revisions, dates, page counts, confidentiality markings, and hashes are identifiable | Protected master-source location; issuer/custodian; acquisition record; confirmation that the candidate v13 hash is the officially issued master; KKL source pointer |
| Authoritative approval | MISSING | A2/Approved Spec catalog labels and revision authors exist | Approver; approving organization; approval record; approval/effective dates; final-versus-draft state; product/merchant/host scope; supersession/expiry state; approval tied to exact hash |
| Specification request/response definitions | PRESENT | v13 contains transaction definitions, request/response structures, security/signing rules, and uncertain-result handling | Sanitized traceability into exact Android properties and behaviors |
| Android implementation identity | MISSING | No applicable Android build is linked to this source | Android repository and commit SHA; Knowledge Master SHA; verified submodule/pin; app version/versionCode; build identity |
| Android implementation mapping | MISSING | None linked | Feature entry point; modules/packages/classes/functions; request builder; service/client; response verifier/parser; ViewModel/use-case/state; persistence; journal; receipt; UI mapping |
| Transaction lifecycle | MISSING | Spec-level lifecycle intent exists | Android evidence for success, decline, timeout, unknown, inquiry, cancellation, void, refund, reversal, retry, duplicate prevention, process recovery, batch, and settlement outcomes |
| Security boundary | PARTIAL | The specifications define security mechanisms | Secret provisioning/ownership; Android secure storage; rotation/revocation; canonicalization; response verification; replay protection; TLS/certificate validation; sensitive URL/payload/log redaction; approved threat assessment |
| Environment | PARTIAL | Specification environments are described | Approved build-to-environment mapping; protected configuration identifiers; merchant/terminal profile; certificate/key aliases; TMS parameter source; device/OS/SDK/app versions; matched host deployment evidence |
| Test evidence | MISSING | Defined test operations are not execution evidence | Unit, serialization, security-vector, parser, negative/error-code, timeout, retry, duplicate, device-integration, persistence, receipt, recovery, host-UAT, and certification results tied to exact revisions |
| Compatibility/rollback | PARTIAL | v7 plus the v13 revision history provide a specification-level change trail | v7-to-v13 Android impact matrix; added/removed-field handling; host compatibility window; mixed-terminal behavior; regression results; deployment sequencing; rollback proof |
| Human release approval | MISSING | None linked | Android technical reviewer; host/product owner; security reviewer; release approver; signed normative scope/exclusions; closure of every conflict and HOLD |

## Missing information checklist

### 1. Authoritative provenance

- Protected master-source location
- Issuer and document custodian
- Acquisition and chain-of-custody record
- Confirmation that the v13 SHA-256 above identifies the official issued artifact
- Source pointer registered in KKL without exposing restricted content

### 2. Formal approval

- Approver and approving organization
- Approval record/reference
- Approval and effective dates
- Final-versus-draft confirmation
- Applicable product, merchant, terminal, and host scope
- Superseded, expired, or still-effective status

### 3. Exact implementation identity

- Android repository and commit SHA
- Knowledge Master repository and commit SHA
- Verified Android-to-Knowledge pin
- Application version, versionCode, package, and build configuration covered

### 4. Android implementation mapping

- Feature entry point and supported transaction flows
- Modules, packages, classes, functions, callers, and callbacks
- Request builder, signing component, and network client
- Response verification and parser
- ViewModel/use-case/state transitions
- Database, journal, receipt, and UI mappings

### 5. Complete lifecycle mapping

- Success, decline, timeout, and unknown handling
- Inquiry and cancellation behavior
- Void, refund, reversal, and advice behavior where applicable
- Retry and duplicate-prevention rules
- Recovery after application/process interruption
- Batch and settlement consequences

### 6. Sanitized request/response traceability

- Specification field to Android property mapping
- Required/optional validation
- Type, length, formatting, and normalization rules
- Amount, currency, and timestamp behavior
- Response code to application outcome mapping
- Unknown, malformed, null, and missing-field behavior

### 7. Security implementation evidence

- Secret/key provisioning and ownership
- Approved Android secure-storage location
- Rotation and revocation procedure
- Request canonicalization test evidence
- Response verification and failure behavior
- Replay protection
- TLS and certificate-validation configuration
- Sensitive URL, payload, and log redaction

### 8. Environment mapping

- Development/SIT/UAT/Production configuration ownership
- Protected configuration identifiers
- Merchant and terminal profile mapping
- Certificate and key aliases, never values
- TMS parameter source
- Device model, OS, vendor SDK, application, and network-library versions
- Exact host deployment correspondence

### 9. Test evidence

- Unit and serialization tests
- Known security/signature vector tests using non-secret samples
- Contract and response-code tests
- Timeout, retry, duplicate, and idempotency tests
- Invalid-signature and transport-security tests
- SUNMI device integration tests
- Persistence, receipt, process-recovery, and lifecycle tests
- Host UAT/certification results

Every test result must identify Android SHA, Knowledge SHA, specification hash, environment, configuration identifier, execution date, and reviewer.

### 10. Compatibility evidence

- v7-to-v13 field and behavior delta
- Android impact of every applicable change
- Removed-field and unknown-field handling
- Host-supported migration window
- Mixed terminal/application version behavior
- Regression evidence
- Deployment, feature-gate, and rollback plan
- Proof that rollback cannot create transaction-state ambiguity

### 11. Relationship to adjacent specifications

- Owner-approved applicability matrix for Gateway v2.4
- Owner-approved applicability matrix for EDC API v0.1.1.0
- Explicit protocol-boundary rule preventing either source from silently overriding or supplementing Eagle v13

### 12. Human release decision

- Android technical review
- Host/product-owner review
- Security review
- Release approval
- Signed normative scope and exclusions
- Closure of all source conflicts and HOLD items

## Promotion criteria

Promotion requires the following reproducible inspection identity:

`v13 SHA-256 + approval record + Android SHA + Knowledge SHA + sanitized implementation mappings + environment ID + test/UAT evidence + compatibility/rollback review + human sign-off`

Recommended progression:

`UNVERIFIED -> CONFIRMED PROVENANCE -> CONFIRMED MAPPING -> TESTED -> HUMAN APPROVED -> NORMATIVE FOR EXPLICIT SCOPE`

"Reviewed" alone must never be interpreted as "verified," "approved," or "normative."

## Protocol and security boundaries

- Keep Eagle POS behavior separate from core ISO8583, EMV, CTLS, Field 61, gateway, and other EDC API semantics unless an approved source explicitly links them.
- Never infer applicability because sources share the KTC, payment, POS, QR, or EDC domain.
- Do not store restricted specification text, credentials, private endpoints, signing/payment keys, unmasked PAN, customer payloads, or unredacted Production logs in public GitHub or convenience documentation.
- Public repositories may contain this sanitized governance record and content hashes only.
- Restricted source artifacts remain in approved private storage and are referenced by controlled identifiers.

## Synchronization state

- Project artifact: prepared for K Knowledge Supporting
- Notion KKL Knowledge Index: target entry identified; update must retain A2/Restricted and record HOLD plus sanitized evidence
- Public GitHub governance: sanitized record only
- Private Knowledge Master: unavailable through the current authorized GitHub connection; restricted-source synchronization remains pending
- Production readiness: HOLD - IMPACT NOT PROVEN

## Change log

### 2026-09-14

- Added exact SHA-256 identity for four inspected source artifacts.
- Reclassified provenance, security, environment, and compatibility as PARTIAL rather than wholly missing.
- Preserved approval, Android mapping, test evidence, and human release approval as missing.
- Explicitly separated the two adjacent integration families from Eagle v13.
- Retained HOLD - IMPACT NOT PROVEN and normative scope NONE.
