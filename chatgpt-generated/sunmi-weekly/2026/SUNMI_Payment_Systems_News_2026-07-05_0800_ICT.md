# SUNMI Payment Systems News [Weekly 2026-06-29 - 2026-07-05 08:00 ICT]

- Generated Date: 2026-09-16 (historical reconstruction)
- Coverage Period: Monday 00:00 - Sunday 08:00 ICT
- Coverage Window: 2026-06-29 00:00 - 2026-07-05 08:00 ICT
- Schedule Time: Sunday morning, approximately 08:00 ICT
- Time Zone: Asia/Bangkok
- Pinned Topic Check: Passed - P3 and P3 MIX only
- Source Verification Rule: SUNMI Official sources first
- Archive Format: Markdown (.md)
- Persistent Storage: GitHub
- Repository: RepoKan/K-Knowledgeable-
- Connector Config: chatgpt-connector-channel.json
- Connector Revision: 28a4ce5d0bd5e185d338b27cf501cc1af815cc54
- Usage Mode: Weekly Sunday Morning
- Reconstruction Status: Backfilled from preserved official-source timeline and current SUNMI official product/platform pages
- Weekly Decision: No Change

## Weekly Hi light

ไม่พบการเปลี่ยนแปลงใหม่ที่ยืนยันว่าเจาะจงต่อ SUNMI P3 หรือ P3 MIX ภายในช่วงนี้สำหรับ Payment SDK, EMV, PinPad, Printer, SUNMI OS/firmware, TMS/DMP หรือ APK deployment. ข่าว P3 AIR ที่มี update signal วันที่ 2026-07-01 ถูกตัดออกจากรายงานตาม scope ปัจจุบันที่จำกัดเฉพาะ P3 และ P3 MIX.

สิ่งที่ยังต้อง carry-over คือ PrinterX 1.0.20 / Printer SDK update วันที่ 2026-06-24 ซึ่งอยู่นอก coverage window นี้ จึงไม่ถูกนับเป็นข่าวใหม่ แต่ยังเป็น regression baseline สำหรับ slip/printing.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## SUNMI Development News

**No Change.** ไม่พบ P3/P3 MIX-specific development release ใหม่ในช่วง 2026-06-29 ถึง 2026-07-05 08:00 ICT.

Baseline ที่ยังมีผล:
- P3: SUNMI OS based on Android 11 Go, payment terminal capability, built-in printer, IC/NFC/magstripe, BLE.
- P3 MIX: SUNMI OS 4.0 based on Android 13, one-set SDK concept, payment capability, DMP/device management.

Official references:
- https://www.sunmi.com/en/p3-family
- https://www.sunmi.com/en/p3-mix/
- https://developer.sunmi.com/en-US/

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## SUNMI Lib Update

**No Change.** ไม่มี evidence ในช่วงนี้ที่บังคับให้เปลี่ยน Payment SDK, SDKLib, OSLib, TMSLib, APILib, Printer API หรือ device-service contract สำหรับ P3/P3 MIX.

Carry-over only: PrinterX 1.0.20 จากสัปดาห์ก่อน ต้องคง printer regression matrix แต่ไม่ถือเป็น new weekly update.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Officially SUNMI Verified

- P3 และ P3 MIX ยังคงเป็นคนละ Android/SUNMI OS baseline จึงต้องแยก regression.
- ไม่มี official evidence ในสัปดาห์นี้ที่อนุญาตให้เปลี่ยน certified payment behavior.
- P3 AIR update signal วันที่ 2026-07-01 เป็น out-of-scope และไม่ถูก promote เข้ารายงานนี้.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Incident Response Guideline

1. คง current certified SDK/firmware baseline.
2. ถ้ามี printer issue ให้ตรวจ PrinterX/service version, sale/void/settlement/reprint slips และ callback state.
3. Payment/EMV/PinPad ต้องทดสอบบน real device ก่อน dependency change.
4. P3 และ P3 MIX ต้อง test แยกกันเนื่องจาก Android baseline ต่างกัน.
5. TMS/DMP rollout ต้อง staged deployment พร้อม rollback path.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Ranking

| Impact Rank | Device / Module | Impact Focus | Recommended Check |
|---|---|---|---|
| High | P3 / P3 MIX / Payment SDK | Preserve certified integration | Keep pinned SDK/service versions |
| High | EMV / PinPad | Financial regression risk | Real-card smoke tests |
| Medium | Printer | Carry-over PrinterX baseline | Full slip regression |
| Medium | P3 MIX / Android 13 | Platform-specific behavior | Permission/service regression |
| Medium | P3 / Android 11 Go | Resource/lifecycle behavior | Stability and service tests |
| Low | TMS/DMP | No new weekly change | Continue monitoring |

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Checklist

- [x] SUNMI Official verification first
- [x] P3/P3 MIX-only scope
- [x] Exclude P3 AIR-only update
- [x] Duplicate/carry-over filtering
- [x] SDK/OS/TMS/API/Product classification
- [x] Payment/EMV/PinPad/Printer/TMS/APK mapping
- [x] Real-device regression requirement preserved
- [x] Sunday 08:00 ICT naming consistency
- [x] Markdown archive created

## Markdown Archive

- Runtime Filename: `SUNMI_Payment_Systems_News_2026-07-05_0800_ICT.md`
- Preferred Path: `chatgpt-generated/sunmi-weekly/2026/SUNMI_Payment_Systems_News_2026-07-05_0800_ICT.md`
- Revision Entry: `2026-07-05 08:00 ICT — Reconstructed No Change`
- Reconstruction Note: Created 2026-09-16 to restore missing weekly continuity using the current P3/P3 MIX-only concept.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite
