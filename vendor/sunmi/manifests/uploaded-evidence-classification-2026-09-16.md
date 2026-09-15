# Uploaded Evidence Classification — 2026-09-16

Purpose: classify newly supplied material before using it in the public SUNMI vendor-provenance archive.

Rule: `OFFICIAL-VENDOR` material may close a provenance/version gap. `PARTNER/CONTRACTUAL`, `INTERNAL`, `DERIVED`, and `TEST-EVIDENCE` material can support engineering analysis but does not become vendor authority. Proprietary or identity-bearing source files are not republished into this public branch without explicit redistribution clearance.

| Supplied file | Classification | Archive use |
|---|---|---|
| `SUNMI PAY SDK V2 Development Document_v3.3.20_20260106(...).docx` | `OFFICIAL-VENDOR` | Closes PaySDK V2 document revision-lineage gap through doc v3.3.20; version/date/SPHS metadata indexed separately. Original full document not republished here. |
| `P3 Cradle upgrade (Loxbit).docx` | `PARTNER/OPERATIONAL` | P3 cradle/base upgrade evidence. Useful for cradle firmware/service analysis; not treated as canonical public SUNMI publication without vendor provenance metadata. |
| `วิธีตั้งค่าการใช้งาน_Cradle_V1.0.docx` | `INTERNAL/PARTNER-MANUAL` | Local P3 cradle installation/configuration evidence; revision v1.0. Not vendor-authoritative. |
| `SUNMI-GMS-Third-party-Disclaimer-LC07072026.docx` | `SUNMI-PARTNER/CONTRACTUAL` | Confirms SUNMI partner-platform/GMS third-party-service context. Contains organization/device/signature information, so only non-sensitive provenance metadata is retained publicly. |
| `Thailand_SUNMI_Allowlist_Color_By_Usage_Type.pdf` | `INTERNAL/LOCALIZED-OPERATIONS` | Thailand firewall/domain allowlist working evidence; not promoted to official SUNMI domain policy unless each endpoint is independently verified. |
| `SUNMI-ESG.pdf` | `OFFICIAL-CORPORATE` | SUNMI corporate/ESG background only; outside Android payment developer canonical scope. |
| `SUNMI_TMS_Server_Architecture_Summary.docx` | `DERIVED-ENGINEERING-SUMMARY` | Useful TMS architecture interpretation; explicitly not a verbatim SUNMI manual. Does not close partner/private TMS documentation gap. |
| `SUNMI_Development_Brief_2026-06-27_1630_ICT_3449.pdf` | `DERIVED-WEEKLY-BRIEF` | Historical weekly evidence and source-timing record; not vendor documentation. |
| `SUNMI_High_Risk_Source_Code_Checklist_Official_2026-08-17_Checklist_8695.pdf` | `DERIVED-CHECKLIST` | Engineering release-gate knowledge based on official sources; not vendor-issued document. |
| `Simulator Get GPRS P3.pdf` | `SIMULATION/TRAINING` | P3/Baidu integration model and test template; synthetic logs are not production evidence. |
| `PROJECT_CONTEXT.md` | `INTERNAL-PROJECT-CONTEXT` | Serial-port prototype context only; not vendor evidence. |
| `import-202609141750_6227.log` | `INTERNAL-SOURCE/REVIEW-EVIDENCE` | Android implementation evidence; not vendor authority. |
| `SH_ENV_TEST_KTC_V1.0.20_VC39_2026-08-26.html` | `INTERNAL-ENVIRONMENT-BASELINE` | Captures observed KTC app/toolchain/SUNMI dependency baseline; useful for compatibility comparisons, not SUNMI release authority. |
| `ECHO.txt` | `INTERNAL-TEST-EVIDENCE` | ECR request/ACK/response trace for P3 integration; not vendor documentation. |
| `SunmiCradleNow.zip` | `INTERNAL-SAMPLE/INTEGRATION-EVIDENCE` | Sample Android bridge using `com.sunmi:sunmi-ecr-service:3.0.6@aar`; useful as observed integration evidence, not an official SUNMI source package. |
| `Banking_Payment_System_Specialist_V3_Enterprise (1).md` | `INTERNAL-AI/WORKFLOW-PROFILE` | Development workflow guidance only; excluded from vendor corpus. |

## Newly closed evidence gap

The supplied official `SUNMI PAY SDK V2 Development Document` contains an internal revision-history table spanning document version `3.0.0` (2017-11-30) through `3.3.20` (2026-01-06), with mapped SunmiPaySDKService/SunmiPayHardwareService versions where the source provides them.

Canonical metadata index:

- `vendor/sunmi/versions/pay-sdk-v2-document-revision-history.csv`
- 128 source rows preserved exactly at metadata level.
- Source anomalies/typos are preserved rather than silently normalized, including values such as `3.3.26`, `3.3.42`, `3.2.66T02`, `3.2.81T`, and one `3.2.81` row without a release date.

## Public-repository boundary

Do not publish full partner/contractual manuals, device identifiers, signatures, customer-specific environment values, credentials, proprietary binaries, or complete vendor manuals into this public branch unless redistribution rights are explicit. Store provenance, version/date metadata, checksums and non-sensitive engineering classification instead.
