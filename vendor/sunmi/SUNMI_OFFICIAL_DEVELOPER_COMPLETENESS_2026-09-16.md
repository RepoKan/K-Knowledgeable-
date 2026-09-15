# SUNMI Official Developer Corpus Completeness — 2026-09-16

## Decision

**The publicly accessible SUNMI developer corpus is not historically complete.**

The current official ecosystem is broad enough to support a strong Android payment engineering knowledge base, but no single public SUNMI index exposes every historical documentation revision, SDK binary, firmware/ROM package, TMS document, or product datasheet version.

Archive state: `PARTIAL — PUBLICLY DISCOVERABLE OFFICIAL CORPUS INDEXED`

## Current coverage matrix

| Domain | Current official source | Public version history | Archive state |
|---|---|---:|---|
| Developer Center / Device APIs / Cloud Open API | developer.sunmi.com | Partial/live pages | CURRENT-VERIFIED |
| Payment SDK / PayLib | Maven Central + SUNMI developer material | Yes for public Maven artifact | VERSION-COMPLETE for `com.sunmi:PayLib-release` |
| PrinterX | Maven Central + SUNMI docs/release notes | Yes | VERSION-COMPLETE for `com.sunmi:printerx` |
| External/cloud printer | Maven Central + SUNMI developer URL in POM | Yes | VERSION-COMPLETE for `external-printerlibrary2` |
| ECR / Device Connection | Maven Central + SUNMI source URL in POM | Partial public enumeration captured | VERSION-GAP |
| DMP API | Maven Central + SUNMI Codeup SCM metadata | 11 public versions reported, partial exact list captured | VERSION-GAP |
| SunmiOpenService | Maven indexes | 21 historical versions indexed across Central/JCenter-era metadata | VERSION-COMPLETE as an index; binary availability varies |
| RKI | SUNMI product/docs/downloads | Live/current plus preserved revision signals | CURRENT-VERIFIED / HISTORICAL-SIGNAL |
| TMS / Payment solution | SUNMI official solution/product material | No complete public revision index | CURRENT-VERIFIED / VERSION-GAP |
| P3 product/docs/downloads | SUNMI official product/CDN | Multiple official PDF filenames observed; no formal full revision manifest | CURRENT-VERIFIED / VERSION-GAP |
| P3 MIX product/docs/downloads | SUNMI official product/CDN | Current official PDF found; no complete historical manifest | CURRENT-VERIFIED / VERSION-GAP |
| Security Update Bulletin | SUNMI Docs | Live bulletin/history; old page revisions not fully exportable | CURRENT-VERIFIED / HISTORICAL-SIGNAL |
| Official OpenAPI source | `sunmi-OS` GitHub organization | Git history is version-addressable | CURRENT-VERIFIED |

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

The branch is considered **public-source complete for a component** only when every version exposed by its authoritative public version index has been enumerated, with upstream coordinates/URL and date where available.

The whole SUNMI corpus cannot currently be labelled complete because:

1. developer.sunmi.com pages can be updated in place;
2. historical page snapshots are not consistently exposed;
3. SUNMI SCM URLs in Maven POMs can point to access-controlled `code.sunmi.com` or Codeup/Teambition systems;
4. product/CDN files do not consistently publish revision manifests;
5. TMS/private-cloud/support material can require customer/partner access;
6. ROM/firmware availability may depend on exact device/SKU/region/TMS channel;
7. some older artifacts were historically indexed through JCenter and may no longer have reliable binary availability.

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

## Authority boundary

This archive is curated developer knowledge and provenance. It is not a substitute for the exact approved Production SDK, ROM, TMS parameter set, host specification, certification package, or device evidence used by an actual payment release.
