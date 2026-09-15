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
- User-uploaded `SUNMI_TMS_Server_Architecture_Summary.docx` is classified as `DERIVED / ARCHITECTURE`, not a verbatim SUNMI manual; it explicitly states that exact deployment values must be verified against official deployment material.
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
- User-uploaded P3 cradle manuals are retained in the uploaded-evidence manifest as partner/internal operational evidence; they are not promoted to SUNMI normative documentation.
- Archive classification: `VERSION-COMPLETE` for the enumerated Maven artifacts; documentation page history remains `VERSION-GAP`.

## Payment SDK

- Maven artifact: `com.sunmi:PayLib-release`.
- Current public Maven latest observed: `2.0.42`.
- POM SCM: `http://code.sunmi.com/androidos/sunmipaylib_v3.0.git`.
- Preserved vendor package signal: `SunmiPaySDKV2_v2.0.42_2026-06-12.zip`; Maven 2.0.42 publication observed 2026-06-13.

### Uploaded official vendor document

A user-supplied vendor document materially closes part of the previous documentation-history gap:

- File: `SUNMI PAY SDK V2 Development Document_v3.3.20_20260106(20260915-220103).docx`
- Issuer shown in document: Shanghai Sunmi Tech Co., Ltd.
- Document revision: `3.3.20`
- Revision release date: `2026-01-06`
- SHA-256: `0f127673f1f467546ba8f5fe48d3de01abb96c0f59afd79e70634b32d9b8878b`
- Vendor-declared revision lineage in this copy: `3.0.0 (2017-11-30) → 3.3.20 (2026-01-06)`.
- Supported-device appendix includes `P3` and `P3_MIX`.
- The document includes PaySDK V2 integration, Basic/Card/PinPad/Security/EMV APIs, EMV L2 split-library guidance, error codes, entities and security/key material handling documentation.
- Curated revision index: `../versions/paysdk-v2-document-revisions.md`.
- Uploaded-file provenance registry: `uploaded-evidence-2026-09-16.md`.

Archive classification is now:

`VERSION-COMPLETE` for public Maven PayLib versions + `OFFICIAL-DOC-3.3.20-HASH-PINNED` + `VENDOR-DECLARED-DOC-LINEAGE-CONFIRMED`.

Remaining gap: the archive does not possess a separate original raw file for every historical document revision or every historical downloadable SDK bundle.

## ECR / Device Connection

- Maven artifact: `com.sunmi:sunmi-ecr-service`.
- POM SCM: `https://code.sunmi.com/ta/sunmi-ecr-service`.
- Version 3.0.16 is publicly indexed with publication date 2026-08-15; some Sonatype search representations were still showing 3.0.15, so repository/index freshness must be recorded.
- User-uploaded ECR/project evidence includes a P3 ECHO request/ACK/response sequence and an internal cradle/RS232 JSON-bridge prototype; both are classified as `PROJECT-EVIDENCE`, not vendor specifications.
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
- A user-provided project environment snapshot records a deployed Customer API baseline `1.3.36 release`; this is `PROJECT-EVIDENCE`, not proof of the current vendor latest version.
- Archive classification: `HISTORICAL-SIGNAL / CURRENT-DOC-REVIEW-REQUIRED`.

## Partner / contractual SUNMI-origin evidence

The uploaded `SUNMI-GMS-Third-party-Disclaimer-LC07072026.docx` identifies Shanghai SUNMI Technology Co., Ltd. and affiliates as the issuer context and was signed on behalf of Loxbit. It is customer/device-specific contractual evidence, not general developer documentation. Its raw file is therefore not mirrored to this public branch; its SHA/provenance is registered in `uploaded-evidence-2026-09-16.md`.

## Corporate context

The uploaded `SUNMI-ESG.pdf` is retained as SUNMI corporate context. It contains ecosystem-history signals such as SUNMI App Store, DMP and OS 4.0 development history, but it is not used as an SDK/API normative source.

## Redistribution rule

The presence of a public official URL or a user-supplied vendor document does not automatically authorize republishing a complete copyrighted manual, customer-specific agreement or datasheet into this public repository. Original documents remain linked or hash-pinned unless licensing/redistribution rights are clear. Maven artifacts carrying Apache-2.0 metadata are tracked by coordinates and upstream version/checksum sources; binary mirroring is a separate operation and is not implied by this manifest.
