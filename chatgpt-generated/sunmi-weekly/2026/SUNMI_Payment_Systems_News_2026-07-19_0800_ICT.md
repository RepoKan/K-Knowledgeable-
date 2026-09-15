# SUNMI Payment Systems News [Weekly 2026-07-13 - 2026-07-19 08:00 ICT]

- Generated Date: 2026-09-16 (historical reconstruction)
- Coverage Period: Monday 00:00 - Sunday 08:00 ICT
- Coverage Window: 2026-07-13 00:00 - 2026-07-19 08:00 ICT
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
- Reconstruction Status: Backfilled
- Weekly Decision: No Change — RKI remains carry-over

## Weekly Hi light

ไม่พบ P3/P3 MIX-specific SDK, OS, firmware, printer, payment-service หรือ TMS/DMP update ใหม่ในช่วงนี้. ประเด็น RKI จาก 2026-07-10 ยังคงเป็น carry-over security gate: ตรวจ RKI APP/SPHS/libbase, key readiness, KCV และ key index บนอุปกรณ์จริง แต่ไม่ถือเป็นข่าวใหม่ซ้ำ.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## SUNMI Development News

**No Change.** คง P3 Android 11 Go baseline และ P3 MIX SUNMI OS 4.0/Android 13 baseline. ไม่พบ evidence ใหม่ที่เปลี่ยน API contract หรือ payment certification handling.

Official references:
- https://www.sunmi.com/en/p3-family
- https://www.sunmi.com/en/p3-mix/
- https://www.sunmi.com/en/remote-key-injection/

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## SUNMI Lib Update

**No Change.** ไม่มี release ใหม่ที่ยืนยันสำหรับ Payment SDK, PrinterX, SDKLib, OSLib, TMSLib หรือ APILib. RKI เป็น carry-over only และต้องไม่ถูกนำเสนอซ้ำเป็น release ใหม่.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Officially SUNMI Verified

- P3/P3 MIX platform baseline unchanged.
- RKI remains relevant to payment-security readiness.
- No new model-specific release found inside this weekly window.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Incident Response Guideline

1. Preserve certified payment baseline.
2. Capture actual device/service versions before troubleshooting.
3. For RKI incidents verify key index/KCV/key state first.
4. Keep EMV/PinPad/Printer regression on real P3 and P3 MIX.
5. Use staged TMS rollout and explicit rollback plan for future changes.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Ranking

| Impact Rank | Device / Module | Impact Focus | Recommended Check |
|---|---|---|---|
| High | Payment SDK | Certified baseline | No dependency drift |
| High | RKI/Security | Carry-over from 10 Jul | Version + key-state check |
| High | EMV/PinPad | Financial regression | Real-card tests |
| Medium | Printer | No new release | Keep slip regression |
| Medium | P3/P3 MIX OS | Different Android baselines | Separate compatibility matrix |
| Low | TMS/DMP | No new weekly change | Continue monitoring |

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Checklist

- [x] Official-source verification
- [x] Duplicate/carry-over filter
- [x] RKI marked carry-over, not new
- [x] P3/P3 MIX-only scope
- [x] Real-device regression gate preserved
- [x] Sunday 08:00 ICT naming consistency
- [x] Markdown archive created

## Markdown Archive

- Runtime Filename: `SUNMI_Payment_Systems_News_2026-07-19_0800_ICT.md`
- Preferred Path: `chatgpt-generated/sunmi-weekly/2026/SUNMI_Payment_Systems_News_2026-07-19_0800_ICT.md`
- Revision Entry: `2026-07-19 08:00 ICT — Reconstructed No Change; RKI carry-over`

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite
