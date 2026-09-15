# SUNMI Payment Systems News [Weekly 2026-09-07 - 2026-09-13 08:00 ICT]

- Generated Date: 2026-09-13 09:15 ICT
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

รอบสัปดาห์นี้ยังไม่พบประกาศ SUNMI Official ที่ระบุการเปลี่ยนแปลงใหม่ซึ่งเจาะจงต่อ P3 หรือ P3 MIX ในด้าน Payment SDK, SDK interface, printer API, OS/firmware, TMS/DMP, EMV, PinPad หรือการ deploy APK ภายในช่วงเวลาที่กำหนด จึงอยู่ใน No-Change mode และไม่แนะนำให้เปลี่ยน Production behavior จากข้อมูลรอบนี้

ประเด็นที่ควรเฝ้าดูคือหน้า `SUNMI SoftPOS Devices Security Patch Status Bulletin` มี Update Time วันที่ 2026-09-11 ซึ่งอยู่ใน coverage window แต่จากหน้า official ที่ตรวจได้ไม่พบข้อความระบุ P3 หรือ P3 MIX จึงยังไม่นำมาจัดเป็น device-specific change สำหรับสองรุ่นนี้

ผลกระทบต่อ EDC/POS ปัจจุบัน: ไม่มี requirement ใหม่ที่บังคับให้ปรับ Payment flow, EMV kernel integration, PinPad, printer/slip, TMS rollout, ECR/device connection หรือ APK release ในสัปดาห์นี้ ควรรักษา baseline ปัจจุบันและรอ release note หรือ bulletin ที่ระบุรุ่น/เวอร์ชันอย่างชัดเจนก่อนเริ่ม tuning

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## SUNMI Development News

**No Change — P3 / P3 MIX specific development release not found in the current weekly window.**

Carry-over baseline ที่ยังใช้สำหรับการตรวจผลกระทบ:

- P3 Family ยังแสดงชุดความสามารถด้าน payment terminal, printer, IC/NFC/magstripe และ SUNMI OS สำหรับ payment พร้อม TMS, Remote Assistance และ RKI เป็น platform baseline
- P3 MIX ยังแสดง SUNMI OS 4.0, unified SDK concept, centralized device management/DMP และ payment methods หลักเป็น baseline ของอุปกรณ์
- ไม่มี official release note ภายในช่วงนี้ที่ระบุว่าต้องเปลี่ยน API contract, SDK dependency, firmware baseline หรือ certification handling สำหรับ P3/P3 MIX

Official references:
- https://www.sunmi.com/en/p3-family
- https://www.sunmi.com/en/p3-mix/
- https://developer.sunmi.com/en-US/

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## SUNMI Lib Update

**No Change.** จาก official developer sources ที่ตรวจในรอบนี้ยังไม่พบ P3/P3 MIX-specific update ใหม่สำหรับ Payment SDK, SDKLib, OSLib, TMSLib, APILib, printer/device API หรือ integration toolkit ภายใน coverage window

จุดอ้างอิงสำคัญ:

- `Overview of SDK` ใน SUNMI Developer Docs มี Update Time ล่าสุดที่ตรวจได้เป็น 2026-08-24 ซึ่งอยู่นอก coverage window นี้
- `SUNMI Security Update Bulletin` มี Update Time 2026-09-01 ซึ่งอยู่นอก coverage window นี้
- `SUNMI SoftPOS Devices Security Patch Status Bulletin` มี Update Time 2026-09-11 แต่ official page ที่ตรวจได้ไม่แสดง P3 หรือ P3 MIX เป็น affected device จึงยังไม่ถือเป็น library/firmware action item สำหรับสองรุ่นนี้

Official references:
- https://docs.sunmi.com/en-US/cdixeghjk491/xdcxeghjk491
- https://docs.sunmi.com/en-US/cicmeghjk546/xdmxeghjk491
- https://docs.sunmi.com/en-US/cicmeghjk546/xrcaeghjk480

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Officially SUNMI Verified

1. SUNMI Developer Center ยังคงระบุ Device-side APIs & SDKs, Cloud Open API และชุด capability สำหรับ printer, scanning และ device integration เป็นช่องทาง official สำหรับ development integration
2. P3 official product information ยังคงระบุ payment-oriented platform, printer, card readers, SUNMI OS for payment, TMS และ remote assistance เป็น baseline
3. P3 MIX official product information ยังคงระบุ SUNMI OS 4.0, one-set SDK interface concept, DMP/device management และ payment acceptance capability เป็น baseline
4. Official SoftPOS security patch bulletin ถูกอัปเดตในสัปดาห์นี้ แต่ไม่พบการระบุ P3/P3 MIX ในข้อความ official ที่ตรวจได้ จึงไม่ยกระดับเป็น P3/P3 MIX change

Official references:
- https://developer.sunmi.com/en-US/
- https://www.sunmi.com/en/p3/
- https://www.sunmi.com/en/p3-mix/
- https://docs.sunmi.com/en-US/cicmeghjk546/xrcaeghjk480

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Incident Response Guideline

เนื่องจากรอบนี้เป็น No-Change จึงไม่ควรเปลี่ยน Production behavior หรือทำ forced upgrade โดยไม่มี release note ที่ผูกกับ P3/P3 MIX โดยตรง หากมี bulletin ใหม่ในรอบถัดไป ให้ใช้ลำดับตอบสนองดังนี้:

1. แยก scope ก่อนว่าเป็น P3, P3 MIX, firmware, SUNMI OS, Payment SDK, printer service, TMS/DMP หรือ security component
2. สำหรับ Payment SDK / EMV / PinPad ให้ตรวจ transaction path, kernel/config, secure input, reversal/settlement และ regression กับ host ก่อน deploy
3. สำหรับ printer ให้ทดสอบ merchant/customer slip, bitmap/text alignment, paper width, reconnect/retry และ print service lifecycle บนอุปกรณ์จริง
4. สำหรับ TMS/DMP/firmware ให้ตรวจ staged rollout, device policy, app version dependency, rollback path และ monitoring ก่อนขยายวง
5. สำหรับ ECR/device connection ให้ทดสอบ USB/Bluetooth/network reconnect, timeout, duplicate command และ transaction state preservation
6. สำหรับ APK release ให้ตรวจ signing, target environment, backward compatibility และ real-device smoke/regression บน P3 และ P3 MIX แยกกัน
7. หากเกิด incident ให้ isolate scope, freeze rollout, collect device/app/SDK/firmware version, reproduce บนอุปกรณ์จริง, ตัดสินใจ rollback และสื่อสารทีมพร้อม evidence

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Ranking

| Impact Rank | Device / Module | Impact Focus | Development Concern | Recommended Check |
|---|---|---|---|---|
| Medium | P3 / P3 MIX Security Watch | SoftPOS security bulletin updated in-window | ยังไม่มีข้อความ official ระบุ P3/P3 MIX เป็น affected device | Monitor bulletin revision; act only when device/version mapping is explicit |
| Low | P3 / P3 MIX Payment SDK / EMV | No new device-specific release found | ไม่ควรเปลี่ยน payment flow หรือ kernel integration จากข่าวทั่วไป | Keep current certified baseline; re-check next official release note |
| Low | P3 / P3 MIX PinPad / Secure Input | No new change found | ไม่มี requirement ใหม่สำหรับ secure input path | Maintain regression baseline and security configuration |
| Low | P3 / P3 MIX Printer | No new printer API/service change found | Slip regression risk only if future SDK/OS update occurs | Keep real-device print regression suite ready |
| Low | P3 / P3 MIX SUNMI OS / Firmware | No model-specific firmware change found | Forced upgrade อาจเพิ่ม regression โดยไม่จำเป็น | Do not upgrade solely from generic platform pages |
| Low | P3 / P3 MIX TMS / DMP / APK Release | No new rollout rule found | Device policy or deployment behavior remains baseline | Keep staged rollout, rollback, and version inventory ready |

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Checklist

- [x] Verify against SUNMI official developer sources and official SUNMI product pages first
- [x] Run duplicate/carry-over check against configured GitHub archive location and repository search
- [x] Classify update type: SDK / OS / TMS / API / Product / Security
- [x] Map affected modules: Payment / EMV / PinPad / Printer / ECR / TMS / APK Release
- [x] Assess device impact separately for P3 and P3 MIX
- [x] Confirm no Production tuning is justified by current official evidence
- [x] Keep regression matrix ready for payment, printer, TMS, device connection and APK deployment
- [x] Require real-device testing before any future model-specific rollout
- [x] Keep rollback and monitoring plan ready
- [x] Prepare compact team summary: No P3/P3 MIX-specific change this week
- [x] Validate headings and P3/P3 MIX-only scope
- [x] Validate Sunday 08:00 ICT coverage/title/archive naming consistency
- [x] Create Markdown archive
- [x] Persist archive to configured GitHub target using Contents API

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Markdown Archive

- Runtime Status: Final weekly Markdown generated
- Runtime Filename: `SUNMI_Payment_Systems_News_2026-09-13_0800_ICT.md`
- Repository Target: `RepoKan/K-Knowledgeable-`
- Preferred Path: `chatgpt-generated/sunmi-weekly/2026/SUNMI_Payment_Systems_News_2026-09-13_0800_ICT.md`
- Persistence Status: GitHub Contents API write requested for canonical archive
- Connector Config Revision: `28a4ce5d0bd5e185d338b27cf501cc1af815cc54`
- Version Control Status: Git-backed versioning enabled; exact commit SHA is returned by the GitHub write operation and reported in the run result
- Revision Entry: `2026-09-13 08:00 ICT — No Change — no official P3/P3 MIX-specific development update requiring action`

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite
