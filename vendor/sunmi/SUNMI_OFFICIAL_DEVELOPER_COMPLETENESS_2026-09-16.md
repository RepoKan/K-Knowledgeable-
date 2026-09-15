# SUNMI Official Developer Corpus Completeness — 2026-09-16

## Decision

**The publicly accessible SUNMI developer corpus is not historically complete, but the supplied authorized evidence materially improves the archive.**

The current official ecosystem is broad enough to support a strong Android payment engineering knowledge base, but no single public SUNMI index exposes every historical documentation revision, SDK binary, firmware/ROM package, TMS document, or product datasheet version.

Archive state: `PARTIAL — PUBLIC + AUTHORIZED SUPPLIED OFFICIAL EVIDENCE INDEXED`

## Current coverage matrix

| Domain | Current official/authorized source | Version history | Archive state |
|---|---|---:|---|
| Developer Center / Device APIs / Cloud Open API | developer.sunmi.com / docs.sunmi.com | Partial/live pages | CURRENT-VERIFIED |
| Payment SDK / PayLib | Maven Central + supplied official `SUNMI PAY SDK V2 Development Document v3.3.20` | Maven PayLib: 22 public versions; PaySDK document: 128 revision-history rows | `VERSION-COMPLETE` for Maven `com.sunmi:PayLib-release`; `DOCUMENT-LINEAGE-CLOSED THROUGH v3.3.20` |
| PrinterX | Maven Central + SUNMI docs/release notes | Yes | VERSION-COMPLETE for `com.sunmi:printerx` |
| External/cloud printer | Maven Central + SUNMI developer URL in POM | Yes | VERSION-COMPLETE for `external-printerlibrary2` |
| ECR / Device Connection | Maven Central + SUNMI source URL in POM + supplied internal integration evidence | Partial public enumeration captured | VERSION-GAP |
| DMP API | Maven Central + SUNMI Codeup SCM metadata | 11 public versions reported, partial exact list captured | VERSION-GAP |
| SunmiOpenService | Maven indexes | 21 historical versions indexed across Central/JCenter-era metadata | VERSION-COMPLETE as an index; binary availability varies |
| RKI | SUNMI product/docs/downloads | Live/current plus preserved revision signals | CURRENT-VERIFIED / HISTORICAL-SIGNAL |
| TMS / Payment solution | SUNMI official solution/product material + supplied derived/partner context | No complete authoritative revision index | CURRENT-VERIFIED / VERSION-GAP |
| P3 product/docs/downloads | SUNMI official product/CDN + supplied cradle operational evidence | Multiple official PDF filenames observed; no formal full revision manifest | CURRENT-VERIFIED / VERSION-GAP |
| P3 MIX product/docs/downloads | SUNMI official product/CDN | Current official PDF found; no complete historical manifest | CURRENT-VERIFIED / VERSION-GAP |
| Security Update Bulletin | SUNMI Docs | Live bulletin/history; old page revisions not fully exportable | CURRENT-VERIFIED / HISTORICAL-SIGNAL |
| Official OpenAPI source | `sunmi-OS` GitHub organization | Git history is version-addressable | CURRENT-VERIFIED |

## PaySDK V2 official document lineage — newly closed

The supplied `SUNMI PAY SDK V2 Development Document v3.3.20` is vendor-issued material identifying Shanghai Sunmi Tech Co., Ltd. and includes its own revision-history table.

The archive now preserves 128 revision-history rows at metadata level:

- first recorded document revision: `3.0.0` — `2017/11/30` — first draft — `SunmiPaySDKService1.0.1`;
- later history maps revisions to SunmiPaySDKService / SunmiPayHardwareService versions where the source provides that relationship;
- latest supplied revision: `3.3.20` — `2026/01/06` — appropriate SDK `SunmiPayHardwareService_v5.0.56`;
- v3.3.20 includes security/API updates such as `getSecStatusEx()`, TR31/key-export metadata, PinPad sensitive-mode configuration, system parameters and error-code updates;
- source-document anomalies/typos are intentionally preserved rather than silently corrected.

Canonical index:

`vendor/sunmi/versions/pay-sdk-v2-document-revision-history.csv`

Status: `DOCUMENT-LINEAGE-CLOSED THROUGH v3.3.20`.

This closure does **not** prove that every historical downloadable PaySDK ZIP, AAR, EMV-L2 split bundle or firmware package is archived. That separate vendor-bundle gap remains open.

## Authorized evidence intake classification — 2026-09-16

Newly supplied material has been classified before use:

`vendor/sunmi/manifests/uploaded-evidence-classification-2026-09-16.md`

Key classifications:

- `OFFICIAL-VENDOR`: SUNMI PAY SDK V2 Development Document v3.3.20 — may close vendor-document lineage gaps.
- `SUNMI-PARTNER/CONTRACTUAL`: GMS third-party disclaimer — establishes partner/platform provenance but identity/device/signature data is not mirrored publicly.
- `PARTNER/OPERATIONAL` / `INTERNAL/PARTNER-MANUAL`: P3 cradle upgrade/configuration material — useful operational evidence, not promoted to canonical vendor documentation without authoritative provenance.
- `DERIVED`: TMS architecture summary, weekly development brief and high-risk checklist — useful engineering knowledge but not vendor-issued authority.
- `SIMULATION/TRAINING`: P3/Baidu simulation — synthetic evidence, not Production evidence.
- `INTERNAL-ENVIRONMENT/TEST/SOURCE`: KTC environment baseline, ECR ECHO trace, implementation logs/source and cradle sample project — useful compatibility/RCA evidence only.
- `OFFICIAL-CORPORATE`: SUNMI ESG material — official company background, outside the canonical Android-payment developer corpus.

## High-value historical signals already preserved

- P3 MIX developer/product documentation update signal: 2026-05-15.
- P3 developer/product documentation update signal: 2026-05-29.
- PaySDK V2 package `2.0.42` vendor package date signal: 2026-06-12; Maven publish date is 2026-06-13.
- Printer SDK / PrinterX `1.0.20` release-note signal: 2026-06-24; Maven publish date is 2026-06-25.
- Remote Key Injection documentation update signal: 2026-07-10.
- SUNMI Security Update Bulletin update signal: 2026-08-17.
- SunmiCustomer API overview update signal: 2026-08-24.

Dates from live page revision signals and repository publication dates are tracked separately because they are different provenance events.

## What 'complete' means for this branch

The branch is considered **source-complete for a component** only when every version exposed by an authoritative version/revision index or authorized official vendor package has been enumerated, with upstream coordinates/URL and date where available.

The whole SUNMI corpus cannot currently be labelled complete because:

1. developer.sunmi.com pages can be updated in place;
2. historical page snapshots are not consistently exposed;
3. SUNMI SCM URLs in Maven POMs can point to access-controlled `code.sunmi.com` or Codeup/Teambition systems;
4. product/CDN files do not consistently publish revision manifests;
5. TMS/private-cloud/support material can require customer/partner access;
6. ROM/firmware availability may depend on exact device/SKU/region/TMS channel;
7. some older artifacts were historically indexed through JCenter and may no longer have reliable binary availability;
8. possession/access to a partner/vendor document does not itself establish public redistribution rights.

## Remaining highest-value gaps

1. complete authorized TMS/private-deployment manual and release-package lineage;
2. ECR full version/tag history and source revision mapping;
3. DMP exact 11-version enumeration plus source/tag mapping;
4. complete PaySDK downloadable ZIP/AAR/EMV-L2 bundle catalog beyond the now-closed document revision lineage;
5. P3/P3 MIX datasheet/manual revision manifests;
6. device/SKU/region-specific ROM, SPHS and firmware catalogs with applicability metadata;
7. authorized source/tag history from `code.sunmi.com` / Codeup repositories.

## Android Payment development priority

For P3/P3 MIX, the archive must prioritize:

1. Payment SDK / PayLib / SunmiPayHardwareService contract
2. EMV L2 / PinPad / Security and native library requirements
3. RKI / key lifecycle / KCV / key-index requirements
4. Printer SDK / printer service
5. ECR / external device connection
6. TMS / DMP / application distribution / parameters
7. APK install/update/signing/version constraints
8. OS / ROM / security bulletin compatibility
9. P3 vs P3 MIX Android baseline differences
10. Cloud Open API when it affects device/application management

## Authority and redistribution boundary

This archive is curated developer knowledge and provenance. It is not a substitute for the exact approved Production SDK, ROM, TMS parameter set, host specification, certification package, or device evidence used by an actual payment release.

The public branch stores non-sensitive provenance, version/date metadata and compatibility classification. Complete partner/vendor manuals, identity-bearing contractual records, device identifiers, signatures, customer-specific environment details, credentials and proprietary binaries are not mirrored publicly unless redistribution rights are explicit.
