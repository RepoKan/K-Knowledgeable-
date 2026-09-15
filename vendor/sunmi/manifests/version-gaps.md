# SUNMI Official Developer Archive — Version Gap Register

Observed: 2026-09-16

Status: `OPEN — PUBLIC HISTORICAL CORPUS NOT FULLY EXPOSED`

This register is intentional. A gap is preferable to an invented version or an unsupported claim of completeness.

## G1 — Live Developer Center pages

- Source: `developer.sunmi.com` / `docs.sunmi.com`.
- Problem: pages can be updated in place and do not consistently expose a public immutable history for every revision.
- Archive action: store current official URL plus preserved observed update/release signals; pin downloadable/versioned artifacts separately when available.

## G2 — PaySDK downloadable package bundle history

- Public Maven `com.sunmi:PayLib-release` history is enumerated for 22 versions.
- SUNMI has also distributed downloadable PaySDK bundles such as the preserved `SunmiPaySDKV2_v2.0.42_2026-06-12.zip` signal.
- Problem: a complete public index for every historical downloadable SDK ZIP/document bundle was not found.
- Status: Maven history `VERSION-COMPLETE`; vendor bundle history `VERSION-GAP`.

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
- A cached Sonatype result still showed `3.0.15`, demonstrating index freshness variance.
- Problem: complete Maven version sequence was not captured in this run.
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
- Problem: no authoritative public revision manifest mapping all filenames to effective dates/revisions was found.
- Status: `VERSION-GAP / LINK-ONLY`.

## G8 — P3 MIX product PDF history

- Current official P3 MIX PDF/CDN material is discoverable.
- Problem: no complete public historical revision manifest was found.
- Status: `VERSION-GAP / LINK-ONLY`.

## G9 — TMS/private deployment material

- Official TMS/payment solution material is public at product/solution level.
- Customer/private-cloud implementation documents, environment details, release packages or partner-only guides may require authorized access.
- Status: `PUBLIC-CURRENT + RESTRICTED-POSSIBLE`.

## G10 — ROM / firmware binaries

- Firmware/ROM applicability depends on model, SKU, region, channel and TMS/support entitlement.
- This public knowledge repository must not infer that every ROM/firmware package is publicly downloadable.
- Status: `VERSION-GAP / DEVICE-SPECIFIC`.

## G11 — Historical JCenter binaries

- `printerlibrary` and `SunmiOpenService` have historical JCenter-era indexes.
- JCenter retirement means old artifact presence in historical metadata does not guarantee reliable current binary retrieval.
- Status: `HISTORICAL-INDEX / BINARY-AVAILABILITY-UNVERIFIED`.

## G12 — Copyright / redistribution boundary

- Public accessibility of a vendor manual/datasheet does not automatically mean unrestricted republication into a public GitHub repository.
- Action: keep official URL, version/date/provenance and checksum when available; copy original documents only when redistribution rights are clear.

## Closure rule

A gap may be closed only by one of:

1. authoritative SUNMI version/revision manifest;
2. immutable official download/version URL plus verifiable metadata/checksum;
3. official Maven/Git tag/release history;
4. authorized partner/vendor package with recorded provenance and redistribution permission.

Do not close a gap from a community repost, filename guess, cached snippet alone, or undocumented version-number inference.
