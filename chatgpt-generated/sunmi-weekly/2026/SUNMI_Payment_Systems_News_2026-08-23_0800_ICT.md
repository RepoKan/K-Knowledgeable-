# SUNMI Payment Systems News [Weekly 2026-08-17 - 2026-08-23 08:00 ICT]

- Generated Date: 2026-09-16 (historical reconstruction)
- Coverage Period: Monday 00:00 - Sunday 08:00 ICT
- Coverage Window: 2026-08-17 00:00 - 2026-08-23 08:00 ICT
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
- Weekly Decision: Change Detected — SUNMI Security Update Bulletin updated 2026-08-17

## Weekly Hi light
SUNMI Security Update Bulletin มี update signal วันที่ 2026-08-17 ซึ่งอยู่ใน coverage window นี้. Preserved official-source evidence ระบุว่า bulletin มี scheduled/unscheduled security updates และเก็บประวัติ ROM/security bulletin หลายเดือน โดยมี P3 ROM history ปรากฏใน 2026 records. อย่างไรก็ตาม evidence ที่เก็บไว้ไม่ได้ยืนยันว่า P3 MIX หรือ P3 ทุก SKU ได้รับ ROM ใหม่ในสัปดาห์นี้ ดังนั้น action ที่ถูกต้องคือ **review exact model/SKU/ROM**, ไม่ใช่ forced upgrade.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## SUNMI Development News
**Security / OS watch elevated.** สำหรับ P3/P3 MIX ต้อง capture Android/SUNMI OS build, security patch level, SPHS, PayLib, Printer service และ ECR service ก่อนเทียบกับ bulletin. P3 และ P3 MIX มี Android baseline ต่างกัน จึงห้ามใช้ผล compatibility ข้ามรุ่นโดยตรง.

Official references:
- https://docs.sunmi.com/en-US/cicmeghjk546/xdmxeghjk491
- https://www.sunmi.com/en/p3-family
- https://www.sunmi.com/en/p3-mix/

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## SUNMI Lib Update
ไม่มี Payment SDK/PrinterX release ใหม่ที่ยืนยันในสัปดาห์นี้. Change หลักเป็น security/ROM bulletin layer จึงกระทบ compatibility validation มากกว่าการเปลี่ยน library โดยตรง.

Required regression if an applicable ROM is identified:
- Pay SDK service binding/reconnect
- EMV insert/tap/fallback
- PinPad PIN entry/cancel/timeout
- Printer service and slip output
- RKI/key state
- ECR/device connection
- APK install/update and TMS deployment

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Officially SUNMI Verified
- SUNMI Security Update Bulletin update signal is dated 2026-08-17 in the preserved official-source timeline.
- SUNMI security maintenance must be evaluated against exact device/ROM rather than Android version alone.
- Current P3 and P3 MIX official pages confirm different platform baselines.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Officially SUNMI Unverified
ไม่พบ evidence เพียงพอที่จะกล่าวว่า **P3 MIX ได้ ROM ใหม่ในสัปดาห์นี้** หรือว่า **P3 ทุก SKU ต้องอัปเกรดทันที**. ข้อสรุปดังกล่าวจึงไม่ถูก promote เป็น action item จนกว่าจะมี exact model/build mapping.

สถานะการยืนยันข้อมูล: ยังไม่ได้รับการยืนยันจาก SUNMI Official WebSite

## Incident Response Guideline
1. Capture model/SKU, ROM build, Android security patch, SPHS, PayLib, Printer/ECR/RKI versions.
2. Map bulletin entry to exact device before rollout.
3. Pilot update on controlled devices first.
4. Run payment + EMV + PinPad + Printer + ECR + install/update regression.
5. Stop rollout if binding, transaction state, print evidence, key state or install behavior regresses.
6. Keep known-good APK and TMS recovery group ready; do not assume generic ROM downgrade is supported.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Ranking
| Impact Rank | Device / Module | Impact Focus | Recommended Check |
|---|---|---|---|
| High | P3/P3 MIX / OS-Security | Bulletin update | Exact ROM/SKU mapping |
| High | Payment SDK | Service after ROM change | Bind/reconnect smoke |
| High | EMV/PinPad | Financial compatibility | Real-card regression |
| High | RKI/Security | Key-service compatibility | Key/KCV/version check |
| Medium | Printer | Service after ROM change | Full slip regression |
| Medium | APK/TMS | Deployment/recovery | Pilot + rollback plan |

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Checklist
- [x] Security Bulletin mapped to 17 Aug window
- [x] Exact model/ROM gate retained
- [x] No forced upgrade inferred
- [x] P3/P3 MIX regression separated
- [x] Payment/EMV/PinPad/RKI/Printer/TMS impact mapped
- [x] Sunday 08:00 ICT consistency
- [x] Markdown archive created

## Markdown Archive
- Runtime Filename: `SUNMI_Payment_Systems_News_2026-08-23_0800_ICT.md`
- Preferred Path: `chatgpt-generated/sunmi-weekly/2026/SUNMI_Payment_Systems_News_2026-08-23_0800_ICT.md`
- Revision Entry: `2026-08-23 08:00 ICT — Reconstructed Change Detected — Security Update Bulletin`

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite
