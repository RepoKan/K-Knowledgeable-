# SUNMI Payment Systems News [Weekly 2026-07-06 - 2026-07-12 08:00 ICT]

- Generated Date: 2026-09-16 (historical reconstruction)
- Coverage Period: Monday 00:00 - Sunday 08:00 ICT
- Coverage Window: 2026-07-06 00:00 - 2026-07-12 08:00 ICT
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
- Reconstruction Status: Backfilled from preserved official-source timeline plus current SUNMI official RKI/product pages
- Weekly Decision: Change Detected — RKI documentation update signal on 2026-07-10

## Weekly Hi light

ประเด็นสำคัญของสัปดาห์นี้คือ **Remote Key Injection (RKI)**. Preserved official-source research ระบุว่า SUNMI RKI documentation มี current-page update วันที่ 2026-07-10. ปัจจุบัน SUNMI official RKI page ยังยืนยันว่า RKI รองรับ first injection, key update, re-injection, PCI-certified infrastructure และ SDK/API integration สำหรับ SUNMI payment devices.

ผลกระทบต่อ P3/P3 MIX อยู่ที่ key readiness, SPHS/RKI dependency, key index, KCV และ DUKPT/MKSK mapping. การอัปเดตเอกสารนี้ไม่ใช่คำสั่งให้เปลี่ยน key configuration โดยอัตโนมัติ แต่เป็น trigger ให้ทบทวน security/release gate.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## SUNMI Development News

**RKI documentation update signal — 2026-07-10.** Historical official-source baseline ที่เก็บไว้ระบุ prerequisite สำคัญ ได้แก่ RKI APP >= 2.0.5, old architecture ใช้ SunmiPayHardwareService >= 3.3.330, new architecture ใช้ SunmiPayHardwareService >= 5.0.31 และ libbase >= 1.2.5; `Check Key Info` ต้องใช้ RKI APP >= 2.0.15.

สำหรับ P3/P3 MIX ให้ถือเป็น compatibility/security review item ไม่ใช่ automatic Production migration. ต้อง capture actual RKI/SPHS/libbase versions จากเครื่องจริงก่อนตัดสินใจ.

Official references:
- https://www.sunmi.com/en/remote-key-injection/
- https://www.sunmi.com/en/p3-family
- https://www.sunmi.com/en/p3-mix/

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## SUNMI Lib Update

ไม่มี Payment SDK/PrinterX release ใหม่ที่ยืนยันใน coverage นี้ แต่ RKI documentation change กระทบ dependency matrix ของ payment-security stack.

Review scope:
- RKI APP / SPHS / libbase versions
- Key downloaded / locked / ready state
- Key index used by Payment APP for PIN/DATA/MAC
- KCV validation
- DUKPT/MKSK mapping
- Startup/pre-transaction guard
- ห้ามใช้ random/test key path กับ Production transaction

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Officially SUNMI Verified

- SUNMI RKI เป็น cloud-terminal key-injection system สำหรับ payment terminals.
- รองรับ first injection, key update และ re-injection.
- SUNMI ระบุ RKI security/certification และ integration ผ่าน SDK/API.
- Historical official-source baseline records the documentation update on 2026-07-10.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Incident Response Guideline

1. หาก payment fail หลัง RKI/key change ให้ freeze rollout และ capture P3/P3 MIX model, ROM, SPHS, libbase, RKI APP, PayLib และ key-state metadata.
2. Block financial transaction เมื่อ expected key/index ไม่พร้อม; ห้าม silently fallback ไป key index อื่น.
3. ตรวจ KCV และ DUKPT/MKSK host mapping ก่อน Sale/Settlement.
4. ทดสอบ PIN entry/cancel/timeout, MAC/encrypt/decrypt และ host approval/decline บนอุปกรณ์จริง.
5. หาก dependency ไม่ตรง documented prerequisite ให้ HOLD release และ escalate ไป SUNMI/RKI owner.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Ranking

| Impact Rank | Device / Module | Impact Focus | Recommended Check |
|---|---|---|---|
| High | P3/P3 MIX / RKI | Key injection readiness | Capture RKI/SPHS/libbase versions |
| High | Security / Key Index | PIN/DATA/MAC key selection | Verify configured index + KCV |
| High | EMV / PinPad | Payment-security regression | Real-card + PIN regression |
| High | Payment SDK | Service/security dependency | Verify PayLib/SPHS compatibility |
| Medium | TMS/RKI rollout | Fleet key-state consistency | Staged rollout and monitor |
| Low | Printer | No new printer change | Keep existing slip regression |

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Checklist

- [x] RKI update signal mapped to 2026-07-10
- [x] P3/P3 MIX-only impact review
- [x] RKI/SPHS/libbase dependency gate
- [x] Key index/KCV/DUKPT/MKSK checks
- [x] Real-device security regression required
- [x] No automatic Production migration inferred
- [x] Sunday 08:00 ICT naming consistency
- [x] Markdown archive created

## Markdown Archive

- Runtime Filename: `SUNMI_Payment_Systems_News_2026-07-12_0800_ICT.md`
- Preferred Path: `chatgpt-generated/sunmi-weekly/2026/SUNMI_Payment_Systems_News_2026-07-12_0800_ICT.md`
- Revision Entry: `2026-07-12 08:00 ICT — Reconstructed Change Detected — RKI documentation update`
- Reconstruction Note: Created 2026-09-16 from preserved official-source research and current SUNMI official RKI/product sources.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite
