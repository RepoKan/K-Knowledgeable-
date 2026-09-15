# SUNMI Official Android Artifact Family Inventory

Observed from public Maven namespace `com.sunmi` on 2026-09-16.

This file is a discovery inventory, not a claim that every artifact below is applicable to P3/P3 MIX payment applications.

## Public SUNMI Maven families observed

- `AIDLWrapper-SDK`
- `EIDCard-android-sdk-SDK`
- `L3AndRemoteOuterSDK`
- `PayLib-release`
- `PosRouterAndChannelCommon`
- `PosUiLib`
- `ProtocolSDK`
- `SunmiAuthorize-SDK`
- `SunmiDock-SDK`
- `SunmiEID-SDK`
- `SunmiEID-SDK-CORE`
- `SunmiHttpLib`
- `SunmiIOTDepend-SDK`
- `SunmiISO8583Tool-SDK`
- `SunmiOpenService`
- `SunmiPassportReader-SDK`
- `SunmiPosRouterChannelLib`
- `SunmiProtocolSDK`
- `SunmiSenrty-SDK`
- `ThingAdapter-SDK`
- `ThingAdapterAuthorize`
- `ThingAdapterAuthorize-Android`
- `external-printerlibrary`
- `external-printerlibrary2`
- `printerlibrary`
- `printerx`
- `sunmi-card-tool-SDK`
- `sunmi-ecr-service`

Additional SUNMI Maven families may exist or be added after this observation. The upstream namespace remains the discovery authority.

## Primary payment-development tier

The following are prioritized for the P3/P3 MIX Android Payment knowledge base:

- `PayLib-release`
- `printerx`
- `printerlibrary`
- `external-printerlibrary`
- `external-printerlibrary2`
- `sunmi-ecr-service`
- `SunmiOpenService`
- `SunmiISO8583Tool-SDK`
- `PosRouterAndChannelCommon`
- `SunmiPosRouterChannelLib`
- `SunmiEID-SDK` / `SunmiEID-SDK-CORE` when identity/EID functions are in project scope
- `SunmiPassportReader-SDK` when passport/NFC identity reading is in project scope

DMP is published under the separate `com.sunmi.dmp` namespace and is tracked independently.

## Completeness rule

An artifact family is not labelled `VERSION-COMPLETE` until its authoritative public version list is enumerated. Presence in this discovery list only means the official namespace contains the artifact family.

This prevents the archive from confusing namespace discovery with historical-version completeness.
