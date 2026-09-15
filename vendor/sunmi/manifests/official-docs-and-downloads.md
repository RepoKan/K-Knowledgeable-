# SUNMI Official Docs and Downloads Manifest

Observed: 2026-09-16
Scope: Android payment engineering with primary device focus P3 / P3 MIX.

## Developer / API roots

| Area | Official source | Status | Notes |
|---|---|---|---|
| SUNMI Developer Center | https://developer.sunmi.com/ | CURRENT-VERIFIED | Primary discovery root for device APIs/SDKs, Cloud Open API, product/OS updates, community and application distribution. |
| SUNMI Docs | https://docs.sunmi.com/ | CURRENT-VERIFIED | Technical documentation and bulletins; individual pages are live/mutable. |
| SUNMI official website | https://www.sunmi.com/ | CURRENT-VERIFIED | Product, solution, support, TMS/RKI and downloadable collateral. |
| Maven Central SUNMI namespace | https://repo1.maven.org/maven2/com/sunmi/ | CURRENT-VERIFIED | Version-addressable Android/JVM artifacts. |
| Maven Central SUNMI DMP | https://central.sonatype.com/namespace/com.sunmi.dmp | CURRENT-VERIFIED | DMP API artifacts. |
| SUNMI GitHub | https://github.com/sunmi-OS | CURRENT-VERIFIED | Official OpenAPI/source repositories discovered publicly. |

## P3

- Product family: https://www.sunmi.com/en/p3-family
- Current platform signal: SUNMI OS based on Android 11 Go for P3 baseline.
- Official CDN PDF variants observed:
  - https://file.cdn.sunmi.com/newebsite/products/p3-family/specs/p3.pdf
  - https://file.cdn.sunmi.com/newebsite/products/p3-family/specs/p3-new.pdf
- Archive classification: `CURRENT-VERIFIED / VERSION-GAP / LINK-ONLY`.
- Gap: no authoritative public manifest was found that explains the complete chronological relationship between every P3 datasheet filename/revision.

## P3 MIX

- Product page: https://www.sunmi.com/en/p3-mix/
- Current platform signal: SUNMI OS 4.0 based on Android 13.
- Official CDN PDF observed:
  - https://cdn.sunmi.com/public/generalfile/mgt_import/0f9ccf5962ce469b9d93e6d588ced0b2.pdf
- Archive classification: `CURRENT-VERIFIED / VERSION-GAP / LINK-ONLY`.
- Gap: full historical PDF revision manifest is not public.

## TMS / Payment Solution

- TMS: https://www.sunmi.com/en/tms/
- Payment solution: https://www.sunmi.com/sunmi-solution/payment/
- Historical/solution PDF observed:
  - https://cdn.sunmi.com/public/generalfile/mgt_import/2b802eaf1b8841e9bb04019542d41bb5.pdf
- Older localized payment devices/solutions PDF observed:
  - https://www.sunmi.co.th/download/user-manual/01-Payment-devices-and-solutions.pdf
- Development relevance: APK/application management, parameter delivery, device policy, staged rollout, remote support, private deployment, security controls.
- Archive classification: `CURRENT-VERIFIED / VERSION-GAP / LINK-ONLY`.

## Remote Key Injection (RKI)

- Product page: https://www.sunmi.com/en/remote-key-injection/
- Official datasheet PDF: https://file.cdn.sunmi.com/newebsite/products/RKI/appendix/RKI-en.pdf
- Preserved official revision signal: RKI developer documentation update observed 2026-07-10.
- Development relevance: RKI APP/SPHS/libbase prerequisites, key assignment, key status, KCV, key index, DUKPT/MKSK/security readiness.
- Archive classification: `CURRENT-VERIFIED / HISTORICAL-SIGNAL / LINK-ONLY`.

## Security / OS

- SUNMI Docs contains the SUNMI Security Update Bulletin and model/ROM security information.
- Preserved official-source update signal: 2026-08-17.
- Current live page/history may differ from the page state observed on that date.
- Archive classification: `CURRENT-VERIFIED / HISTORICAL-SIGNAL`.
- Engineering rule: exact device model/SKU/ROM/security patch must be captured before applying a bulletin to P3/P3 MIX Production.

## Printer

- Maven artifact: `com.sunmi:printerx`.
- Official Maven POM points to SUNMI source control: `https://code.sunmi.com/androidos/SunmiPrinterLibrary`.
- Historical official release-note signal: PrinterX 1.0.20 dated 2026-06-24; Maven publication is 2026-06-25.
- External/cloud printer docs are linked by the `external-printerlibrary2` POM to:
  - https://developer.sunmi.com/docs/zh-CN/xeghjk491/rxceghjk502
- Archive classification: `VERSION-COMPLETE` for the enumerated Maven artifacts; documentation page history remains `VERSION-GAP`.

## Payment SDK

- Maven artifact: `com.sunmi:PayLib-release`.
- Current public Maven latest observed: `2.0.42`.
- POM SCM: `http://code.sunmi.com/androidos/sunmipaylib_v3.0.git`.
- Preserved vendor package signal: `SunmiPaySDKV2_v2.0.42_2026-06-12.zip`; Maven 2.0.42 publication observed 2026-06-13.
- Archive classification: `VERSION-COMPLETE` for public Maven PayLib versions; downloadable SDK package/document bundle history remains `VERSION-GAP`.

## ECR / Device Connection

- Maven artifact: `com.sunmi:sunmi-ecr-service`.
- POM SCM: `https://code.sunmi.com/ta/sunmi-ecr-service`.
- Version 3.0.16 is publicly indexed with publication date 2026-08-15; some Sonatype search representations were still showing 3.0.15, so repository/index freshness must be recorded.
- Archive classification: `CURRENT-VERIFIED / VERSION-GAP` until the complete public version enumeration is pinned.

## DMP

- Maven artifact: `com.sunmi.dmp:lib-dmp-api`.
- Current latest observed: `v0.0.12`.
- POM SCM: `https://codeup.teambition.com/sunmi/Android/lib-dmp-api`.
- Public index reports 11 Central versions; exact list is only partially enumerated in this archive today.
- Archive classification: `CURRENT-VERIFIED / VERSION-GAP`.

## SunmiCustomer API

- Preserved official-source page update signal: 2026-08-24.
- Development relevance: application install/update, package/signature/ABI/version/manifest/certificate failure catalog, software management callbacks and OTA/system update behavior.
- Archive classification: `HISTORICAL-SIGNAL / CURRENT-DOC-REVIEW-REQUIRED`.

## Redistribution rule

The presence of a public official URL does not automatically authorize republishing a complete copyrighted manual or datasheet into this public repository. Original documents remain linked unless licensing/redistribution rights are clear. Maven artifacts carrying Apache-2.0 metadata are tracked by coordinates and upstream version/checksum sources; binary mirroring is a separate operation and is not implied by this manifest.
