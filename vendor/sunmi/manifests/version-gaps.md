# SUNMI Official Developer Archive — Version Gap Register

Observed: 2026-09-16

Status: `OPEN — PUBLIC/RESTRICTED HISTORICAL CORPUS NOT FULLY EXPOSED`

This register is intentional. A gap is preferable to an invented version or an unsupported claim of completeness.

## G1 — Live Developer Center pages

- Source: `developer.sunmi.com` / `docs.sunmi.com`.
- Problem: pages can be updated in place and do not consistently expose a public immutable history for every revision.
- Archive action: store current official URL plus preserved observed update/release signals; pin downloadable/versioned artifacts separately when available.

## G2 — PaySDK downloadable package bundle history

- Public Maven `com.sunmi:PayLib-release` history is enumerated for 22 versions.
- The supplied official `SUNMI PAY SDK V2 Development Document v3.3.20` closes the **document revision lineage** through 2026-01-06: 128 revision-history rows from doc v3.0.0 through v3.3.20 are now indexed at `vendor/sunmi/versions/pay-sdk-v2-document-revision-history.csv`.
- The document maps revisions to SunmiPaySDKService/SunmiPayHardwareService versions where SUNMI supplied that mapping.
- Remaining problem: a complete authoritative catalog of every historical downloadable PaySDK ZIP/AAR/EMV-L2 bundle is still not available from the evidence currently archived.
- Status: Maven history `VERSION-COMPLETE`; PaySDK **document lineage `CLOSED THROUGH v3.3.20`**; vendor downloadable-bundle history `VERSION-GAP`.

## G3 — SUNMI internal/access-controlled SCM

Examples from official Maven POM metadata:

- `code.sunmi.com/androidos/sunmipaylib_v3.0.git`
- `code.sunmi.com/androidos/SunmiPrinterLibrary`
- `code.sunmi.com/ta/sunmi-ecr-service`
- `codeup.teambition.com/sunmi/Android/lib-dmp-api`

Problem: provenance URLs exist, but complete source history may require SUNMI/partner credentials.

Status: `LINK-ONLY / ACCESS-CONTROLLED`.

## G4 — ECR full version enumeration

- Current newest version independently observed: `3.0.16` dated 2026-08-15.
- Exact earlier evidence captured: `2.0.14`, `2.0.22`.
- A supplied internal sample uses `com.sunmi:sunmi-ecr-service:3.0.6@aar`; this is useful compatibility evidence but does not replace an authoritative ECR version index.
- Problem: complete Maven/version sequence was not captured in this run.
- Status: `VERSION-GAP`.

## G5 — DMP full version enumeration

- `com.sunmi.dmp:lib-dmp-api` public index reports 11 Central versions.
- Exact captured versions: `v0.0.4`, `v0.0.10`, `v0.0.11`, `v0.0.12`.
- Remaining exact labels were not exposed in the retrieved view.
- Status: `VERSION-GAP`.

## G6 — Legacy external-printerlibrary historical label

- Public index reports 14 entries total.
- 13 exact labels were resolved across Central/JCenter/Spring Lib Release.
- One historical JCenter row was rendered as `unspecified` in the retrieved index.
- Status: `LABEL-UNRESOLVED`.

## G7 — P3 product PDF history

- Official P3 CDN includes at least `p3.pdf` and `p3-new.pdf` variants.
- Supplied P3 cradle documents add operational/partner evidence but do not constitute an authoritative SUNMI product-datasheet revision manifest.
- Problem: no authoritative complete revision manifest mapping every P3 product/manual filename to effective dates/revisions is archived yet.
- Status: `VERSION-GAP / PARTNER-EVIDENCE-ADDED`.

## G8 — P3 MIX product PDF history

- Current official P3 MIX PDF/CDN material is discoverable.
- Problem: no complete public historical revision manifest was found.
- Status: `VERSION-GAP / LINK-ONLY`.

## G9 — TMS/private deployment material

- Official TMS/payment solution material is public at product/solution level.
- A supplied TMS architecture summary explicitly states it is derived from limited public metadata and is not a verbatim SUNMI deployment manual, so it does not close the restricted/private TMS documentation gap.
- Customer/private-cloud implementation documents, environment details, release packages or partner-only guides may require authorized access.
- Status: `PUBLIC-CURRENT + RESTRICTED-POSSIBLE`.

## G10 — ROM / firmware binaries

- Firmware/ROM applicability depends on model, SKU, region, channel and TMS/support entitlement.
- A supplied P3 cradle upgrade guide demonstrates a cradle firmware-update workflow, but does not provide a complete authoritative firmware catalog.
- Status: `VERSION-GAP / DEVICE-SPECIFIC`.

## G11 — Historical JCenter binaries

- `printerlibrary` and `SunmiOpenService` have historical JCenter-era indexes.
- JCenter retirement means old artifact presence in historical metadata does not guarantee reliable current binary retrieval.
- Status: `HISTORICAL-INDEX / BINARY-AVAILABILITY-UNVERIFIED`.

## G12 — Copyright / redistribution boundary

- Public accessibility or partner access to a vendor manual/datasheet does not automatically mean unrestricted republication into this public GitHub repository.
- Action: keep official/partner provenance, version/date metadata and checksum when available; copy original documents only when redistribution rights are clear.
- Identity-bearing contractual material and customer/device-specific documents must not be mirrored publicly without explicit authorization.

## G13 — Uploaded partner/internal evidence

- Classification manifest: `vendor/sunmi/manifests/uploaded-evidence-classification-2026-09-16.md`.
- Partner/internal/derived artifacts can support compatibility and RCA decisions but do not become SUNMI vendor authority solely because they reference SUNMI products.
- Status: `CLASSIFIED / NOT PROMOTED TO VENDOR AUTHORITY`.

## Closure rule

A gap may be closed only by one of:

1. authoritative SUNMI version/revision manifest;
2. immutable official download/version URL plus verifiable metadata/checksum;
3. official Maven/Git tag/release history;
4. authorized partner/vendor package with recorded provenance and redistribution permission.

Do not close a gap from a community repost, filename guess, cached snippet alone, internal simulation, or undocumented version-number inference.
