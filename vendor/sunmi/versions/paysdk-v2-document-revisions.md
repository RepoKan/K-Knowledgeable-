# SUNMI PaySDK V2 Development Document — Uploaded Official Revision Evidence

Observed/uploaded: 2026-09-16
Source file: `SUNMI PAY SDK V2 Development Document_v3.3.20_20260106(20260915-220103).docx`
SHA-256: `0f127673f1f467546ba8f5fe48d3de01abb96c0f59afd79e70634b32d9b8878b`
Issuer shown in document: Shanghai Sunmi Tech Co., Ltd.
Current document revision in uploaded copy: **3.3.20**
Current document revision release date: **2026-01-06**
Classification: `VENDOR-OFFICIAL / UPLOADED-SOURCE / HASH-PINNED`

## Why this is higher-value evidence

Unlike a mutable live documentation page, this uploaded vendor document contains its own revision history and maps documentation changes to SunmiPaySDKService / SunmiPayHardwareService versions. It therefore closes part of the historical PaySDK documentation gap while preserving a hash-pinned source copy outside the public archive.

The public GitHub branch intentionally stores the provenance/index rather than redistributing the entire uploaded document.

## Historical range confirmed by the document

The revision table begins at document version **3.0.0 (2017-11-30)** and continues through **3.3.20 (2026-01-06)**. Selected engineering milestones are recorded below without reproducing the vendor manual verbatim.

| Document revision | Date | Curated engineering significance |
|---|---|---|
| 3.0.0 | 2017-11-30 | Initial documented baseline. |
| 3.0.8 | 2018-08-16 | DUKPT support appears in the revision history. |
| 3.2.0 | 2018-10-12 | V2 API support introduced. |
| 3.2.17 | 2019-01-07 | RSA interface support added. |
| 3.2.20 | 2019-03-18 | DUKPT/KSN and APDU/EMV-related changes. |
| 3.2.25 | 2019-07-30 | Key injection and expanded card/EMV functions. |
| 3.2.29 | 2019-11-29 | Expanded DUKPT/security/TR-31/RSA functionality. |
| 3.2.32 | 2020-04-22 | Expanded card/basic/system and EMV-related capability. |
| 3.2.40 | 2020-09-11 | Revision lineage continues into later SPHS 3.3.x generation. |
| 3.3.8 | 2025-04-18 | NFC parameter documentation explicitly covers P3/P3H/P3K/P3KH. |
| 3.3.16 | 2025-09-25 | RSA encrypt/decrypt padding description updated. |
| 3.3.17 | 2025-10-21 | ReadCard/NFC and TLV documentation changes. |
| 3.3.18 | 2025-10-27 | Error-code table expanded. |
| 3.3.19 | 2025-11-06 | Expansion-SAM and keyboard-mode documentation added/updated. |
| **3.3.20** | **2026-01-06** | System-parameter additions; `getSecStatus()` deprecated; `getSecStatusEx()` added; security/key/PinPad parameter documentation expanded; error-code definitions updated. |

## Integration baseline in uploaded document

The document describes both local AAR and Maven integration. One Maven example uses:

`com.sunmi:PayLib-release:2.0.27`

This is an integration example within the document, not a statement that 2.0.27 is the latest PayLib artifact.

### EMV L2 split-library boundary

The document distinguishes SPHS generations:

- EMV L2 split-library integration is available for devices with SPHS `5.x.x` under the documented conditions.
- Devices on SPHS `3.3.xx` continue to use the EMV interfaces in SPHS rather than the split-library path.
- Exact runtime SPHS, PayLib/AAR, native libraries and device model must therefore be captured before applying integration guidance.

## P3 / P3 MIX applicability

The uploaded document's supported-device appendix includes both:

- `P3`
- `P3_MIX`

It also contains device-specific notes for P3-family behavior, including NFC parameter constraints and physical-keyboard/PinPad distinctions for related models.

## Production-use rule

For a Production Android Payment release, do not treat document revision 3.3.20 alone as proof that a specific API is available on a terminal. Pin and verify:

1. exact device model/SKU;
2. Android/ROM build and security patch;
3. SPHS / SunmiPayHardwareService version;
4. PayLib AAR/Maven version;
5. EMV/kernel/native package where applicable;
6. RKI/key state and host certification requirements;
7. real-device regression evidence.

## Archive state change

Previous state: `PaySDK downloadable document bundle history = VERSION-GAP`.

New state after upload: `OFFICIAL DOCUMENT REVISION 3.3.20 HASH-PINNED; INTERNAL REVISION HISTORY CONFIRMED FROM 3.0.0 → 3.3.20; HISTORICAL RAW FILE SET STILL INCOMPLETE`.

This means the archive now knows the vendor-declared revision lineage from the uploaded copy, but it does **not** claim to possess a separate original file for every historical document revision.