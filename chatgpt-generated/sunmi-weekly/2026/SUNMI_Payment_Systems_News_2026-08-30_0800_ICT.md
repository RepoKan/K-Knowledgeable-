# SUNMI Payment Systems News [Weekly 2026-08-24 - 2026-08-30 08:00 ICT]

- Generated Date: 2026-09-16 (historical reconstruction)
- Coverage Period: Monday 00:00 - Sunday 08:00 ICT
- Coverage Window: 2026-08-24 00:00 - 2026-08-30 08:00 ICT
- Schedule Time: Sunday morning, approximately 08:00 ICT
- Time Zone: Asia/Bangkok
- Pinned Topic Check: Passed - P3 and P3 MIX only
- Source Verification Rule: SUNMI Official sources first
- Archive Format: Markdown (.md)
- Persistent Storage: GitHub
- Repository: RepoKan/K-Knowledgeable-
- Connector Revision: 28a4ce5d0bd5e185d338b27cf501cc1af815cc54
- Usage Mode: Weekly Sunday Morning
- Reconstruction Status: Backfilled from preserved SUNMI official-source research
- Weekly Decision: Change Detected — SunmiCustomer API overview updated 2026-08-24

## Weekly Hi light
Preserved official-source timeline ระบุว่า **SunmiCustomer API Overview** มี page update วันที่ 2026-08-24 และมี install/package error-code catalog ที่เกี่ยวข้องกับ silent install, signature/certificate, ABI, downgrade, split APK, target SDK และ installation session failures. สำหรับ P3/P3 MIX นี่เป็น release/deployment control signal ที่สำคัญ แม้จะไม่ใช่ Payment SDK release โดยตรง.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## SUNMI Development News
การเปลี่ยนแปลงรอบนี้อยู่ที่ device/software-management API layer. Application release บน P3/P3 MIX ควร map install/update failure เป็น deterministic deployment state และไม่ถือว่า APK rollout สำเร็จเพียงเพราะ package ถูกส่งถึงเครื่อง.

Official references:
- https://docs.sunmi.com/en-US/cdixeghjk491/xdcxeghjk491
- https://www.sunmi.com/en/p3-family
- https://www.sunmi.com/en/p3-mix/
- https://developer.sunmi.com/en-US/

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## SUNMI Lib Update
SunmiCustomer API overview update เป็น API/documentation change ที่เกี่ยวข้องกับ install/update/device management. Preserved official-source research records:
- `installAppV2(String appFilePath, boolean autoStart, OnInstallAppListener listener)` และ `installApp(...)`
- success/failure ผ่าน callbacks
- error classes ครอบคลุม signature mismatch, shared-user incompatibility, DEX/native ABI verification, package/UID mismatch, downgrade, missing split APK, target SDK, AndroidManifest/certificate/path/session failures
- system OTA path มี device/version/package validation และไม่ควรสมมติว่ารองรับ generic downgrade

ผลสำหรับ P3/P3 MIX: เพิ่ม install/upgrade/recovery regression gate ก่อน TMS rollout.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Officially SUNMI Verified
- SunmiCustomer API overview update signal is dated 2026-08-24 in the preserved official-source timeline.
- API/install error handling is directly relevant to APK deployment and maintenance on SUNMI devices.
- P3/P3 MIX remain separate compatibility targets because their OS baselines differ.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Officially SUNMI Unverified
ไม่ควรสรุปว่า update นี้บังคับให้เปลี่ยน Production installer code ทันทีโดยไม่มี evidence ว่า project เรียก API path ที่ได้รับผลกระทบจริง. Exact device permission/API availability ยังต้องยืนยันจาก P3/P3 MIX build ที่ใช้งาน.

สถานะการยืนยันข้อมูล: ยังไม่ได้รับการยืนยันจาก SUNMI Official WebSite

## Incident Response Guideline
1. Capture APK versionCode/versionName, signing certificate, target SDK, ABI/split packaging และ device OS/ROM.
2. Map install callback/error code เป็น explicit deployment state.
3. Test fresh install, same-signature upgrade, blocked downgrade, insufficient storage, bad package, missing split, reboot-after-install.
4. Run staged TMS/DMP rollout separately on P3 and P3 MIX.
5. Keep known-good source available; recovery APK should preserve signing identity and use a valid higher versionCode rather than assuming package downgrade.
6. Re-run Payment/EMV/PinPad/Printer smoke tests after application or system update.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Ranking
| Impact Rank | Device / Module | Impact Focus | Recommended Check |
|---|---|---|---|
| High | APK Release | Install/update correctness | Fresh/upgrade/failure matrix |
| High | P3/P3 MIX / TMS | Staged deployment | Pilot + recovery group |
| High | Payment App | Post-upgrade integrity | Payment smoke test |
| Medium | OS/System Update | Version/device validation | Do not assume downgrade |
| Medium | Printer | Post-install regression | Slip smoke test |
| Medium | RKI/Security | Preserve key/service state | Version/key readiness check |

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Checklist
- [x] SunmiCustomer API update mapped to 24 Aug
- [x] Install/update error taxonomy captured
- [x] P3/P3 MIX deployment impact separated
- [x] APK signing/version/ABI/split gates included
- [x] TMS staged rollout + recovery included
- [x] No unsupported generic downgrade assumption
- [x] Sunday 08:00 ICT consistency
- [x] Markdown archive created

## Markdown Archive
- Runtime Filename: `SUNMI_Payment_Systems_News_2026-08-30_0800_ICT.md`
- Preferred Path: `chatgpt-generated/sunmi-weekly/2026/SUNMI_Payment_Systems_News_2026-08-30_0800_ICT.md`
- Revision Entry: `2026-08-30 08:00 ICT — Reconstructed Change Detected — SunmiCustomer API overview`

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite
