# SUNMI Official Developer Archive

Status date: 2026-09-16
Branch: `sunmi-official-developer-archive`
Repository: `RepoKan/K-Knowledgeable-`

## Purpose

This branch is a provenance and version-index layer for official SUNMI developer material relevant to Android payment application engineering, with primary focus on SUNMI P3 and P3 MIX.

It tracks publicly verifiable official SUNMI documentation, official product/download references, official SUNMI Maven artifacts, official SUNMI GitHub repositories, and known historical revision signals.

## Completeness statement

`PARTIAL — PUBLICLY DISCOVERABLE OFFICIAL CORPUS INDEXED`

This archive must not claim that every historical SUNMI document or binary is publicly available. SUNMI documentation pages are live/mutable, some historical revisions are not exposed, some source-control links point to access-controlled SUNMI systems, and some product PDFs do not expose a formal revision history.

For that reason, completeness is defined per item:

- `VERSION-COMPLETE`: all public versions found in the authoritative versioned repository/index have been enumerated.
- `CURRENT-VERIFIED`: current official source verified, but historical versions are not fully exposed.
- `HISTORICAL-SIGNAL`: an official-source revision/update date was preserved by prior research, but the old original file is not publicly retrievable now.
- `LINK-ONLY`: official original is linked; it is not copied into this public repository.
- `VERSION-GAP`: one or more historical versions are known or expected but not publicly enumerated/retrievable.
- `BINARY-NOT-MIRRORED`: original binary was not copied into this repository; use the authoritative upstream link/checksum source.

## Archive policy

1. SUNMI official sources remain vendor authority.
2. Maven Central artifacts published under official SUNMI coordinates are version-addressable evidence; their POM/license/source metadata are retained as provenance.
3. Original manuals, datasheets and other copyrighted vendor documents are not blindly republished. This branch stores links, version metadata, hashes when independently available, and concise provenance notes unless redistribution rights are clear.
4. No historical revision is invented. Missing revisions remain explicit gaps.
5. GitHub archive data does not override Production evidence, certified configuration, host specifications, device/ROM evidence, or approved project baselines.
6. P3 and P3 MIX remain separate compatibility/regression targets.

## Structure

- `SUNMI_OFFICIAL_DEVELOPER_COMPLETENESS_2026-09-16.md` — corpus completeness assessment.
- `manifests/official-docs-and-downloads.md` — official developer/product/support/TMS/RKI/document sources.
- `manifests/official-github-sources.md` — official `sunmi-OS` source repositories and pinned evidence.
- `manifests/version-gaps.md` — unresolved historical gaps and non-public sources.
- `versions/PayLib-release.md` — PayLib public version history.
- `versions/printerx.md` — PrinterX public version history.
- `versions/external-printerlibrary2.md` — external/cloud printer public version history.
- `versions/SunmiOpenService.md` — customer/device service historical version index.
- `versions/lib-dmp-api.md` — DMP API public version evidence and remaining gaps.
- `versions/sunmi-ecr-service.md` — ECR service public version evidence and remaining gaps.

## Primary upstream roots

- SUNMI Developer Center: `https://developer.sunmi.com/`
- SUNMI product/support: `https://www.sunmi.com/`
- SUNMI Docs: `https://docs.sunmi.com/`
- Maven Central group: `https://repo1.maven.org/maven2/com/sunmi/`
- Maven Central DMP group: `https://central.sonatype.com/namespace/com.sunmi.dmp`
- Official GitHub organization: `https://github.com/sunmi-OS`

## Current high-risk Android payment domains

Payment SDK / PayLib, SPHS and service binding, EMV L2 split/native libraries, PinPad/security, RKI/key state, printer SDK/service, ECR/device connection, TMS/DMP/app distribution, APK install/update, SUNMI OS/ROM/security bulletins, and P3/P3 MIX product baselines.
