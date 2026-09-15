# SUNMI Official Developer Archive

Status date: 2026-09-16
Branch: `sunmi-official-developer-archive`
Repository: `RepoKan/K-Knowledgeable-`

## Purpose

This branch is a provenance and version-index layer for SUNMI developer material relevant to Android payment application engineering, with primary focus on SUNMI P3 and P3 MIX.

It tracks publicly verifiable official SUNMI documentation, official product/download references, official SUNMI Maven artifacts, official SUNMI GitHub repositories, known historical revision signals, and authorized user-supplied vendor evidence. Internal/partner/project evidence is indexed separately and never silently promoted to vendor authority.

## Completeness statement

`PARTIAL — PUBLIC + AUTHORIZED SUPPLIED OFFICIAL EVIDENCE INDEXED`

The largest newly closed gap is the **SUNMI PaySDK V2 document lineage through v3.3.20**. A supplied official vendor document identifies Shanghai Sunmi Tech Co., Ltd., is hash-pinned, and contains 128 revision-history rows spanning `3.0.0 (2017-11-30)` through `3.3.20 (2026-01-06)`.

This does **not** mean every historical original document file, SDK ZIP/AAR, SPHS build, firmware package, TMS manual, ROM or datasheet revision is now archived. Those remaining gaps stay explicit.

## Classification vocabulary

- `VERSION-COMPLETE`: every version exposed by the authoritative versioned index has been enumerated.
- `DOCUMENT-LINEAGE-CLOSED`: an authorized vendor document supplies an internal revision lineage through a defined revision.
- `OFFICIAL-VENDOR`: vendor-issued source evidence.
- `CURRENT-VERIFIED`: current official source verified, but historical versions are not fully exposed.
- `HISTORICAL-SIGNAL`: an official-source revision/update date is preserved but the prior page/file state is not fully available.
- `PARTNER/CONTRACTUAL`: SUNMI/partner material whose scope is customer/device/agreement specific.
- `PARTNER/OPERATIONAL` / `INTERNAL`: operational evidence that is not vendor normative authority.
- `DERIVED`: analysis/checklist/summary based on underlying sources; it never outranks those sources.
- `PROJECT-EVIDENCE`: build/runtime/test/source evidence from a project.
- `LINK-ONLY`: official original remains at its upstream location rather than being copied here.
- `VERSION-GAP`: historical versions are known/expected but not fully enumerated/retrievable.
- `BINARY-NOT-MIRRORED`: original binary is not copied into this public repository.

## Archive policy

1. SUNMI official/vendor sources remain vendor authority.
2. Authorized supplied vendor documents may close a provenance/version-lineage gap when issuer, revision and exact bytes can be pinned.
3. Maven Central artifacts under SUNMI coordinates are version-addressable evidence; POM/license/source metadata are retained as provenance.
4. Internal, derived and project evidence is useful for compatibility/RCA but is never promoted to vendor specification.
5. Original manuals, contractual files, logs and binaries are not blindly republished into this public repository. Store hashes, source relationships, version/date metadata and concise engineering findings unless redistribution rights are explicit.
6. No historical revision is invented. Missing revisions remain explicit gaps.
7. GitHub archive data does not override Production evidence, certified configuration, host specifications, device/ROM evidence or approved project baselines.
8. P3 and P3 MIX remain separate compatibility/regression targets.

## Structure

- `SUNMI_OFFICIAL_DEVELOPER_COMPLETENESS_2026-09-16.md` — current corpus completeness assessment and remaining high-value gaps.
- `manifests/official-docs-and-downloads.md` — official developer/product/support/TMS/RKI/document sources plus uploaded official PaySDK evidence.
- `manifests/official-github-sources.md` — official `sunmi-OS` source repositories and pinned evidence.
- `manifests/version-gaps.md` — unresolved historical gaps and non-public sources.
- `manifests/uploaded-evidence-classification-2026-09-16.md` — **canonical authority classification** for the supplied file set.
- `manifests/uploaded-evidence-2026-09-16.md` — supplementary hash/provenance registry for the same intake.
- `versions/pay-sdk-v2-document-revision-history.csv` — canonical 128-row metadata extraction from the supplied official PaySDK V2 document revision table.
- `versions/paysdk-v2-document-revisions.md` — curated engineering interpretation of key PaySDK document revisions.
- `versions/PayLib-release.md` — PayLib public Maven version history.
- `versions/printerx.md` / `printerlibrary.md` — printer artifact histories.
- `versions/external-printerlibrary.md` / `external-printerlibrary2.md` — external/cloud-printer history.
- `versions/SunmiOpenService.md` — service historical version index.
- `versions/lib-dmp-api.md` — DMP API evidence and remaining gaps.
- `versions/sunmi-ecr-service.md` — ECR service public version evidence and remaining gaps.

## Primary upstream roots

- SUNMI Developer Center: `https://developer.sunmi.com/`
- SUNMI product/support: `https://www.sunmi.com/`
- SUNMI Docs: `https://docs.sunmi.com/`
- Maven Central group: `https://repo1.maven.org/maven2/com/sunmi/`
- Maven Central DMP group: `https://central.sonatype.com/namespace/com.sunmi.dmp`
- Official GitHub organization: `https://github.com/sunmi-OS`
- SUNMI source-control coordinates discovered from artifact metadata may point to access-controlled `code.sunmi.com` / Codeup systems and are tracked as restricted upstreams rather than assumed public sources.

## Current high-risk Android payment domains

Payment SDK / PayLib, SPHS and service binding, EMV L2 split/native libraries, PinPad/security, RKI/key state, printer SDK/service, ECR/device connection, TMS/DMP/app distribution, APK install/update, SUNMI OS/ROM/security bulletins, cradle/base/serial integration, and P3/P3 MIX platform differences.

## Current authority rule

For Production payment decisions, pin the exact applicable device/SKU, ROM/security patch, SPHS/service version, PayLib/AAR, EMV/kernel package, TMS parameters, host/acquirer specification, key/RKI state and real-device regression evidence. The archive is a knowledge/provenance layer, not a substitute for those release artifacts.
