# SUNMI Payment Systems News [Weekly 2026-06-22 - 2026-06-28 08:00 ICT]

- Generated Date: 2026-09-16 (historical normalization)
- Coverage Period: Monday 00:00 - Sunday 08:00 ICT
- Coverage Window: 2026-06-22 00:00 - 2026-06-28 08:00 ICT
- Schedule Time: Sunday morning, approximately 08:00 ICT
- Time Zone: Asia/Bangkok
- Pinned Topic Check: Passed - P3 and P3 MIX only
- Source Verification Rule: SUNMI Official sources first
- Archive Format: Markdown (.md)
- Persistent Storage: GitHub
- Repository: RepoKan/K-Knowledgeable-
- Connector Revision: 28a4ce5d0bd5e185d338b27cf501cc1af815cc54
- Usage Mode: Weekly Sunday Morning
- Reconstruction Status: Normalized from preserved 2026-06-29 legacy PDF/HTML/TXT weekly artifacts
- Weekly Decision: Change Detected — Printer SDK / PrinterX 1.0.20

## Weekly Hi light
Preserved weekly artifacts show SUNMI Printer SDK / SDK Release Notes activity inside this coverage period, including PrinterX 1.0.20 dated 2026-06-24 and Printing SDK documentation changes. Under the current P3/P3 MIX-only concept, the direct impact is receipt/slip regression and APK release readiness on payment terminals with built-in printers.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## SUNMI Development News
The relevant official-source signal in this week is Printer SDK/Printing SDK. This is not a Payment SDK change, but printing is part of merchant/customer transaction evidence and therefore remains a release gate for P3/P3 MIX applications.

Official references:
- https://www.sunmi.com/en/p3-family
- https://www.sunmi.com/en/p3-mix/
- https://developer.sunmi.com/en-US/

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## SUNMI Lib Update
- PrinterX / Printer SDK: version 1.0.20 dated 2026-06-24 in preserved official-source research.
- Review focus: LineStyle setter structure, edge-case exceptions, asynchronous printer acquisition/listener lifecycle, print-service compatibility and `destroy()` cleanup.
- No new Payment SDK version is promoted from this week; PaySDK remains baseline context only.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Officially SUNMI Verified
- PrinterX 1.0.20 is the relevant library signal for this week.
- P3 has built-in 58 mm thermal printing capability; P3 MIX is also a payment device with integrated printer options.
- Printer change must be validated independently from payment approval/EMV state.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Incident Response Guideline
1. Separate transaction result from print result; approved payment + failed print must not become a duplicate financial attempt.
2. Regression Sale, Void, Settlement, Reprint, QR/DCC receipt paths used by the application.
3. Validate text/bitmap/logo/alignment/paper feed and callbacks on real P3/P3 MIX hardware.
4. Capture PrinterX + printer-service + app version in incident logs.
5. Block APK release if slip evidence/layout or callback behavior regresses.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Ranking
| Impact Rank | Device / Module | Impact Focus | Recommended Check |
|---|---|---|---|
| High | P3/P3 MIX / Printer | PrinterX 1.0.20 | Full receipt regression |
| High | APK Release | Printing compatibility | Signed build smoke |
| High | Payment App | Transaction/print state separation | Approved + print-fail case |
| Medium | Printer lifecycle | Listener/destroy path | Reconnect/re-init tests |
| Medium | EMV/PinPad | Ensure no state coupling | Card/PIN smoke |
| Low | TMS | No new TMS release | Monitor |

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Checklist
- [x] Legacy evidence preserved, not deleted
- [x] Current P3/P3 MIX-only scope applied
- [x] PrinterX 1.0.20 mapped to regression gate
- [x] Transaction/print state separation retained
- [x] Real-device slip testing required
- [x] Sunday 08:00 ICT normalized naming
- [x] Markdown archive created

## Markdown Archive
- Runtime Filename: `SUNMI_Payment_Systems_News_2026-06-28_0800_ICT.md`
- Preferred Path: `chatgpt-generated/sunmi-weekly/2026/SUNMI_Payment_Systems_News_2026-06-28_0800_ICT.md`
- Legacy Artifacts: Existing 2026-06-29 PDF/HTML/TXT artifacts remain historical evidence and are not deleted.
- Revision Entry: `2026-06-28 08:00 ICT — Normalized historical weekly report — Printer SDK/PrinterX 1.0.20`

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite
