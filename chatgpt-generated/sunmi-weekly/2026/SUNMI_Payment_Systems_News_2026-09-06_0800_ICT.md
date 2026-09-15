# SUNMI Payment Systems News [Weekly 2026-08-31 - 2026-09-06 08:00 ICT]

- Generated Date: 2026-09-16 (historical reconstruction)
- Coverage Period: Monday 00:00 - Sunday 08:00 ICT
- Coverage Window: 2026-08-31 00:00 - 2026-09-06 08:00 ICT
- Schedule Time: Sunday morning, approximately 08:00 ICT
- Time Zone: Asia/Bangkok
- Pinned Topic Check: Passed - P3 and P3 MIX only
- Source Verification Rule: SUNMI Official sources first
- Archive Format: Markdown (.md)
- Persistent Storage: GitHub
- Repository: RepoKan/K-Knowledgeable-
- Connector Revision: 28a4ce5d0bd5e185d338b27cf501cc1af815cc54
- Usage Mode: Weekly Sunday Morning
- Reconstruction Status: Backfilled
- Weekly Decision: No Change — carry-over Security Bulletin and SunmiCustomer API controls

## Weekly Hi light
ไม่พบ P3/P3 MIX-specific SDK, firmware, SUNMI OS, payment-service หรือ printer release ใหม่ในช่วง 2026-08-31 ถึง 2026-09-06 08:00 ICT. สองประเด็น carry-over ที่ยังมีผลต่อ release gate คือ Security Bulletin 17 Aug และ SunmiCustomer API overview 24 Aug; ทั้งสองไม่ถูกนับซ้ำเป็นข่าวใหม่.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## SUNMI Development News
**No Change.** สำหรับ P3/P3 MIX ให้คง current certified payment baseline และใช้ exact device/ROM/API evidence ก่อนเปลี่ยน SDK, firmware หรือ deployment path.

Official references:
- https://www.sunmi.com/en/p3-family
- https://www.sunmi.com/en/p3-mix/
- https://developer.sunmi.com/en-US/
- https://docs.sunmi.com/en-US/cicmeghjk546/xdmxeghjk491
- https://docs.sunmi.com/en-US/cdixeghjk491/xdcxeghjk491

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## SUNMI Lib Update
**No Change.** No confirmed new Payment SDK, PrinterX, SDKLib, OSLib, TMSLib or APILib revision in-window. Carry-over controls remain:
- exact ROM/security-patch mapping before OS rollout
- APK signature/version/ABI/split/install error handling
- RKI/SPHS/key readiness
- P3/P3 MIX separate regression

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Officially SUNMI Verified
- Security Bulletin and SunmiCustomer API changes remain valid carry-over baselines.
- No additional P3/P3 MIX-specific release was identified before this cutoff.
- Existing P3 and P3 MIX platform differences continue to require separate device validation.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Incident Response Guideline
1. Start with exact model/SKU, ROM, patch, app, PayLib, SPHS, RKI, Printer/ECR service versions.
2. For install/update failures use explicit callback/error evidence; do not infer success from package delivery.
3. For OS/security changes require model/ROM mapping and pilot rollout.
4. Re-run Sale/Void/Reversal/Settlement, Insert/Tap/PIN, printer and ECR regression after any update.
5. Preserve staged TMS rollout, monitoring and recovery package.

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Ranking
| Impact Rank | Device / Module | Impact Focus | Recommended Check |
|---|---|---|---|
| High | Payment SDK | No new release | Preserve certified pin |
| High | OS/Security | Carry-over bulletin | Exact ROM mapping |
| High | APK/TMS | Carry-over API controls | Install/upgrade/recovery tests |
| High | EMV/PinPad | Financial path | Real-card regression |
| Medium | RKI | Key readiness | Version/KCV/index check |
| Medium | Printer/ECR | Post-update behavior | Slip/connectivity smoke |

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite

## Checklist
- [x] Official-source verification
- [x] Carry-over not repeated as new news
- [x] P3/P3 MIX-only scope
- [x] Security and deployment controls retained
- [x] Real-device regression requirement retained
- [x] Sunday 08:00 ICT consistency
- [x] Markdown archive created

## Markdown Archive
- Runtime Filename: `SUNMI_Payment_Systems_News_2026-09-06_0800_ICT.md`
- Preferred Path: `chatgpt-generated/sunmi-weekly/2026/SUNMI_Payment_Systems_News_2026-09-06_0800_ICT.md`
- Revision Entry: `2026-09-06 08:00 ICT — Reconstructed No Change; security/deployment carry-over`

สถานะการยืนยันข้อมูล: ยืนยันแล้ว จาก SUNMI Official WebSite
