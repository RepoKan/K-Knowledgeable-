# SUNMI Payment Systems News [Weekly 2026-09-07 - 2026-09-13 08:00 ICT]

- Generated Date: 2026-09-16 03:21 ICT
- Coverage Period: Monday 00:00 - Sunday 08:00 ICT
- Coverage Window: 2026-09-07 00:00 - 2026-09-13 08:00 ICT
- Schedule Time: Sunday morning, approximately 08:00 ICT
- Time Zone: Asia/Bangkok
- Pinned Topic Check: Passed - P3 and P3 MIX only
- Source Verification Rule: Verify SUNMI official sources first; use non-official information only when materially useful and clearly separated
- Archive Format: Markdown (.md)
- Persistent Storage: GitHub
- Repository: RepoKan/K-Knowledgeable-
- Connector Config: chatgpt-connector-channel.json
- Connector Revision: 28a4ce5d0bd5e185d338b27cf501cc1af815cc54
- Usage Mode: Weekly Sunday Morning
- Duplicate / Carry-over Check: No prior SUNMI weekly archive was found under the configured target path or repository search, so this run uses official SUNMI pages as the comparison baseline
- Consistency Validation: Passed - report title, cutoff, metadata, runtime filename, and archive path all use the Sunday 08:00 ICT convention

## Weekly Hi light

รอบสัปดาห์นี้ไม่พบประกาศ SUNMI Official ที่ยืนยันการเปลี่ยนแปลงใหม่แบบเจาะจงต่อ P3 หรือ P3 MIX ในด้าน Payment SDK, SDK interface, printer API, SUNMI OS/firmware, TMS/DMP, EMV, PinPad หรือ APK deployment ภายใน coverage window ที่ตรวจสอบ จึงใช้ No-Change mode และไม่เปลี่ยน Production behavior จากข้อมูลรอบนี้

สิ่งที่ควรเฝ้าดูต่อคือ release note, security bulletin หรือ SDK/API revision ที่ระบุ model, firmware, OS build หรือ package version ของ P3/P3 MIX อย่างชัดเจน เพราะสองรุ่นมี platform baseline ต่างกันและควรแยก regression matrix

ผลกระทบต่อ EDC/POS ปัจจุบัน: ไม่มี requirement ใหม่ที่ยืนยันให้ปรับ Payment flow, EMV kernel integration, PinPad, printer/slip, TMS/DMP rollout, ECR/device connection หรือ APK release ในรอบนี้

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## SUNMI Development News

**No Change — ไม่พบ P3 / P3 MIX specific development release ที่ยืนยันจาก SUNMI Official ภายใน current weekly window.**

Carry-over baseline ที่ยังใช้สำหรับ impact review:

- P3 Family: SUNMI OS based on Android 11 Go สำหรับรุ่น P3, payment terminal capabilities, IC/NFC/magstripe, built-in 58 mm printer, BLE, SUNMI OS for payment, TMS และ RKI
- P3 MIX: SUNMI OS 4.0 based on Android 13, Qualcomm hexa-core, 4 GB RAM + 32 GB ROM, payment acceptance, one-set SDK concept และ DMP/device management
- ยังไม่พบ official release note ในรอบนี้ที่บังคับเปลี่ยน API contract, SDK dependency, firmware baseline หรือ payment certification handling สำหรับ P3/P3 MIX

Official references:
- https://www.sunmi.com/en/p3-family
- https://www.sunmi.com/en/p3-mix/
- https://developer.sunmi.com/en-US/

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## SUNMI Lib Update

**No Change.** จาก SUNMI official sources ที่ตรวจสอบ ไม่พบ P3/P3 MIX-specific update ใหม่ที่ยืนยันได้สำหรับ Payment SDK, SDKLib, OSLib, TMSLib, APILib, printer/device API หรือ integration toolkit ภายใน coverage window

Development action สำหรับสัปดาห์นี้คือคง version pin ปัจจุบันไว้ และไม่เปลี่ยน SDK/service contract จนกว่าจะมี official revision ที่ระบุ package/version/device mapping ชัดเจน

Official references:
- https://developer.sunmi.com/en-US/
- https://www.sunmi.com/en/p3-family
- https://www.sunmi.com/en/p3-mix/

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Officially SUNMI Verified

- P3 official product information ระบุ P3 บน SUNMI OS based on Android 11 Go, Quad-Core A53 2.0 GHz, payment card interfaces, Bluetooth 5.0/BLE และ built-in 58 mm thermal printer
- P3 Family official page เชื่อมโยง platform capabilities กับ SUNMI OS for payment, Remote Key Injection และ Terminal Management System
- P3 MIX official product information ระบุ SUNMI OS 4.0, payment acceptance methods, Qualcomm hexa-core, 4 GB RAM + 32 GB ROM, one-set SDK concept และ DMP/device management
- SUNMI TMS official page ระบุ remote device management, app distribution/version management และ bulk transaction/device parameter configuration เป็น core TMS capabilities

Official references:
- https://www.sunmi.com/en/p3-family
- https://www.sunmi.com/en/p3-mix/
- https://www.sunmi.com/en/tms/
- https://developer.sunmi.com/en-US/

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Incident Response Guideline

เนื่องจากรอบนี้เป็น No-Change จึงไม่ควร forced upgrade หรือเปลี่ยน Production behavior โดยไม่มี P3/P3 MIX-specific evidence หากมี official change ในรอบถัดไป ให้ดำเนินการดังนี้:

1. แยก scope: P3, P3 MIX, SUNMI OS, firmware, Payment SDK, printer service, TMS/DMP หรือ security component
2. Payment SDK / EMV / PinPad: ตรวจ service binding, kernel/config, card interface, secure input, reversal, settlement และ host regression
3. Printer/slip: ทดสอบ merchant/customer receipt, text/bitmap alignment, paper width, callback/error handling และ print lifecycle บนอุปกรณ์จริง
4. TMS/DMP/firmware: ใช้ staged rollout, inventory version, app dependency, monitoring และ rollback path
5. ECR/device connection: ทดสอบ USB/Bluetooth/network reconnect, timeout, duplicate request และ transaction-state preservation
6. APK release: ตรวจ signing, ABI/SDK compatibility, install/update path และ smoke/regression แยก P3 กับ P3 MIX
7. Incident triage: freeze rollout, เก็บ device model + firmware + SUNMI OS + SDK/app version, reproduce, scope isolation, rollback decision และ team communication พร้อม evidence

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Ranking

| Impact Rank | Device / Module | Impact Focus | Development Concern | Recommended Check |
|---|---|---|---|---|
| High | P3 / P3 MIX / Payment SDK | No confirmed new release; preserve certified integration | SDK/service change อาจกระทบ transaction flow | Keep pinned baseline; verify official version mapping before upgrade |
| High | P3 / P3 MIX / EMV | Card-interface and kernel regression risk | ICC/NFC behavior ต้องทดสอบบนอุปกรณ์จริง | Maintain SALE/VOID/REVERSAL/SETTLEMENT regression |
| High | P3 / P3 MIX / PinPad/Security | Secure-input and key-management compatibility | หลีกเลี่ยงการเปลี่ยน security service โดยไม่มี official evidence | Verify PinPad/key state and certification dependencies |
| Medium | P3 / P3 MIX / Printer | Different hardware/OS baseline | Slip layout/callback regression อาจเกิดเมื่อ SDK/OS เปลี่ยน | Keep real-device print regression suite |
| Medium | P3 MIX / Android 13 baseline | Modern Android permission/background behavior | App behavior อาจต่างจาก P3 | Maintain separate Android 13 regression matrix |
| Medium | P3 / Android 11 Go baseline | Resource/lifecycle constraints | Memory/startup/service behavior ต้องเฝ้าระวัง | Test long-run stability and foreground services |
| Medium | P3 / P3 MIX / APK Release | Deployment/update compatibility | TMS/manual update ต้องมี rollback | Verify signing, staged rollout, rollback and version inventory |
| Low | P3 / P3 MIX / TMS-DMP | No confirmed weekly change | ไม่มี action ใหม่ในรอบนี้ | Continue monitoring official TMS/DMP documentation |

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Checklist

- [x] Verify SUNMI official sources first
- [x] Check duplicate/carry-over against configured archive baseline
- [x] Classify SDK / OS / TMS / API / Product impact
- [x] Map Payment / EMV / PinPad / Printer / ECR / TMS / APK Release modules
- [x] Assess P3 and P3 MIX separately
- [x] Confirm no current evidence requires Production tuning
- [x] Maintain regression coverage for payment, printer, connectivity and deployment
- [x] Require real-device testing for future SDK/firmware/OS changes
- [x] Keep rollback and monitoring plan ready
- [x] Prepare team summary: No confirmed P3/P3 MIX-specific change this week
- [x] Validate headings and P3/P3 MIX-only scope
- [x] Validate Sunday 08:00 ICT coverage/title/archive naming consistency
- [x] Create Markdown archive
- [x] Persist canonical archive to GitHub target

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Markdown Archive

- Runtime Status: Final weekly Markdown generated and verified
- Runtime Filename: `SUNMI_Payment_Systems_News_2026-09-13_0800_ICT.md`
- Repository Target: `RepoKan/K-Knowledgeable-`
- Preferred Path: `chatgpt-generated/sunmi-weekly/2026/SUNMI_Payment_Systems_News_2026-09-13_0800_ICT.md`
- Persistence Status: Complete — GitHub Contents API write succeeded
- Connector Config Revision: `28a4ce5d0bd5e185d338b27cf501cc1af815cc54`
- Version Control Status: Git-backed history preserved; final verification commit recorded by GitHub connector
- Revision Entry: `2026-09-13 08:00 ICT — No Change — no official P3/P3 MIX-specific development update requiring Production action`

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite
