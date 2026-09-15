# Uploaded SUNMI / Android Payment Evidence — 2026-09-16

Repository: `RepoKan/K-Knowledgeable-`
Branch: `sunmi-official-developer-archive`
Purpose: provenance registry for user-supplied files used to strengthen the SUNMI Android Payment knowledge base.

## Authority classes

- `VENDOR-OFFICIAL` — document identifies SUNMI / Shanghai Sunmi Tech as issuer or is a SUNMI corporate/vendor artifact.
- `PARTNER-CONTRACTUAL` — SUNMI-origin contractual/partner document with customer-specific or signed content; treat as restricted evidence.
- `PARTNER/INTERNAL` — Loxbit/team procedure or implementation document; useful operational evidence but not SUNMI normative authority.
- `DERIVED` — analysis/checklist/simulation derived from official material; never promoted above the cited vendor source.
- `PROJECT-EVIDENCE` — source/runtime/build/test evidence from an application or prototype.
- `EXCLUDED-FROM-OFFICIAL` — useful context but not part of the SUNMI official corpus.

## Registered files

| File | SHA-256 | Classification | Archive interpretation |
|---|---|---|---|
| `SUNMI PAY SDK V2 Development Document_v3.3.20_20260106(20260915-220103).docx` | `0f127673f1f467546ba8f5fe48d3de01abb96c0f59afd79e70634b32d9b8878b` | **VENDOR-OFFICIAL** | Authoritative uploaded PaySDK V2 developer document. Doc revision `3.3.20`, release `2026-01-06`. Binary is not mirrored to this public branch; provenance/hash and derived revision index are stored. |
| `SUNMI-GMS-Third-party-Disclaimer-LC07072026.docx` | `69d56909d984a4c2c799d2f7f21d9999f4ac3166f4815e58006adda37cca747b` | **PARTNER-CONTRACTUAL** | SUNMI third-party-products/services disclaimer, signed for Loxbit. Customer/device-specific; treat as restricted contractual evidence, not public developer documentation. |
| `SUNMI-ESG.pdf` | `5a1e041eb19dcbc17226c41949b65d4d4c45f63be11a26ca5c3afd74f63c0f86` | **VENDOR-OFFICIAL / CORPORATE** | SUNMI corporate/ESG material. Useful ecosystem history (App Store, DMP, OS 4.0) but not an SDK/API normative source. |
| `P3 Cradle upgrade (Loxbit).docx` | `a10708db00323887275939746e683a497721e55df44a98de8e588fd40d00d35c` | **PARTNER/INTERNAL** | P3 cradle/base upgrade procedure. Operationally useful; contains device-management instructions and vendor UI/screens, but issuer/provenance is Loxbit-side rather than a verified SUNMI release manifest. |
| `วิธีตั้งค่าการใช้งาน_Cradle_V1.0.docx` | `e1ff040d134a142083c0bf6e2b0720711081b4c9dd611a887aa599e3d071728d` | **PARTNER/INTERNAL** | Cradle configuration manual v1.0; covers LAN/IP setup, Asia/Bangkok configuration, MAC filtering and P3 Wi-Fi MAC workflow. Not promoted as SUNMI normative documentation. |
| `Thailand_SUNMI_Allowlist_Color_By_Usage_Type.pdf` | `0c7744a15f4960a2371837a6dc2ce0fa15669ddea809c0f2c1342725c3aca7ba` | **DERIVED / NETWORK CONTROL** | Thailand-specific firewall classification. Source notes indicate it was derived from a user-provided domain list. Must be vendor-verified before Production firewall policy is treated as SUNMI normative. |
| `SUNMI_TMS_Server_Architecture_Summary.docx` | `a086bb684113c12511afb92bba9b2473a3a17baa252a0204dfdc4066f55f68c4` | **DERIVED / ARCHITECTURE** | Implementation-oriented TMS summary. It explicitly states the public SUNMI Root User Deployment page body was not fully exposed and that exact server values require verification against official deployment material. |
| `SUNMI_High_Risk_Source_Code_Checklist_Official_2026-08-17_Checklist_8695.pdf` | `43c48a99eebb9587b1ae6dbb48ed082312249fc88c9835b56a95d783b11bf932` | **DERIVED / RELEASE-GATE** | Official-source-based risk checklist for Payment SDK/EMV/PinPad/Security, OS, Printer, ECR, APK/TMS and RKI. Use as engineering gate, not vendor specification. |
| `SUNMI_Development_Brief_2026-06-27_1630_ICT_3449.pdf` | `16ea6a412f1d06585e23e769ce7733a577ce64fd7fe1e22b2503d5e421b08555` | **DERIVED / HISTORICAL-WEEKLY** | Preserved historical weekly brief. Its old 16:30 schedule is legacy evidence only; current canonical weekly policy is Sunday 08:00 ICT. |
| `Simulator Get GPRS P3.pdf` | `55392208b3ef7320c8a1ffdc491bc07bf19f13e877bb6945918a3819019b5844` | **DERIVED / SIMULATION** | P3/Baidu location simulation. The document marks its logs/coordinates as synthetic; never use as Production execution evidence. |
| `SH_ENV_TEST_KTC_V1.0.20_VC39_2026-08-26.html` | `4e5620310c9dde7269d8f555c811d4f83bcae5e0ecdc3177c33a9b96a9e02f7c` | **PROJECT-EVIDENCE / BUILD-BASELINE** | KTC app environment snapshot. Captures PayLib `2.0.17`, Customer API `1.3.36 release`, TMS Params `1.2.1`, Printer Library `1.0.21`, ECR Service `2.0.8`; runtime ROM/SPHS fields remain intentionally unresolved. |
| `ECHO.txt` | `0247331783670c3c7eb4039267c0fe4844725b9c325ac62ed25455e431b790de` | **PROJECT-EVIDENCE / ECR TEST** | ECR ECHO exchange showing POS→EDC request, ACK, SUNMI P3 model response, and POS ACK. Test evidence only. |
| `SunmiCradleNow.zip` | `607920cfda9d7d00577ee9c610baa878abb8b6a91aa32b62c36ce18dfd802a3c` | **PROJECT-EVIDENCE / SOURCE** | Internal Android prototype `SunmiCradleJsonBridge_PathMapping`; app version `1.7`/VC8, target/compile 34, Java/Kotlin target 17, dependency `com.sunmi:sunmi-ecr-service:3.0.6@aar`; RS232 JSON bridge default profile 9600/7E1. Source is not SUNMI official. |
| `PROJECT_CONTEXT.md` | `cb7b4f86d0f5f56fcac8fd0d7220deafa9d7424ff627144ba9affb35183fcecf` | **PROJECT-EVIDENCE / CONTEXT** | Internal context for an Android Java serial-port mini app and JNI serial transport prototype. Not SUNMI vendor documentation. |
| `import-202609141750_6227.log` | `92121e3b6bcce6053e88406864802782ef0027f0294161850c33e0b946f759b0` | **PROJECT-EVIDENCE / LOG** | Runtime/import log retained only by hash/provenance in the public archive; content may contain operational details and must be reviewed/redacted before publication. |
| `Banking_Payment_System_Specialist_V3_Enterprise (1).md` | `b1690a74b055b092a4ba500bad92ff35bbd126f1b4df3b173623d20f19015e6b` | **EXCLUDED-FROM-OFFICIAL** | AI/system-specialist operating profile. Useful workflow context but not SUNMI evidence. |

## Key new authoritative finding

The uploaded **SUNMI PAY SDK V2 Development Document v3.3.20** materially improves the corpus because it supplies a vendor revision history and direct SDK contract details rather than only live-page/Maven metadata.

Confirmed from the uploaded document:

- Document revision: `3.3.20`, release date `2026-01-06`.
- It identifies SUNMI PaySDK V2 modules including basic/terminal, card, PinPad, EMV and security.
- It documents Maven/local AAR integration; one integration example uses `com.sunmi:PayLib-release:2.0.27`.
- It documents EMV L2 split-library integration and differentiates SPHS 5.x.x versus 3.3.xx behavior.
- Appendix supported-device list includes both **P3** and **P3_MIX**.
- Recent revision history contains explicit P3/P3H/P3K/P3KH NFC parameter behavior and additional security/PinPad/API changes through revision 3.3.20.

See `../versions/paysdk-v2-document-revisions.md` for the curated revision/provenance index.

## Public-branch handling rule

This public branch stores **hashes, provenance, version metadata, compatibility findings, and source relationships**. It does not automatically mirror uploaded proprietary/customer-specific binaries or complete manuals. Files classified `PARTNER-CONTRACTUAL`, internal logs, source archives and customer-specific artifacts require an explicit redistribution decision before their raw bytes can be published.

## Production authority

Uploaded files strengthen evidence but do not automatically supersede the exact certified runtime package. A Production decision must still pin the applicable device/SKU, ROM/security patch, SPHS/service version, PayLib/AAR, EMV/kernel package, TMS parameters, host/acquirer specification, and real-device evidence.