# SUNMI Official GitHub Source Manifest

Observed: 2026-09-16
Official organization used for public-source monitoring: `https://github.com/sunmi-OS`

## Verified repository evidence

### sunmi-openapi-java-sdk

- Repository: `https://github.com/sunmi-OS/sunmi-openapi-java-sdk`
- Public code-search evidence pinned a README at commit:
  - `113a2fc8307558612c2ac1d6f7ebc0733f79436a`
- Role: SUNMI OpenAPI Java SDK/reference implementation.
- Archive rule: use exact commit SHAs for engineering evidence; do not cite only the moving default branch when reproducibility matters.

### sunmi-openapi-go-sdk

- Repository: `https://github.com/sunmi-OS/sunmi-openapi-go-sdk`
- Public code-search evidence pinned `go.mod` at commit:
  - `b84a065cda2af783334f5aabf9a0f29ce46799e4`
- Role: SUNMI OpenAPI Go SDK/reference implementation.

## Monitoring rule

The `sunmi-OS` organization is an official-secondary engineering source. It is useful for source history, examples and OpenAPI implementation changes, but absence of a commit here does **not** prove that Payment SDK, firmware, SPHS, TMS, printer service or other SUNMI components did not change.

Authority order for payment engineering:

1. exact official product/payment/security/TMS documentation or certified vendor package applicable to the device;
2. exact versioned Maven/vendor artifact and POM provenance;
3. official SUNMI GitHub source at a pinned commit;
4. official community/social signal;
5. unverified third-party evidence.

## Gap

Not every SUNMI SDK is mirrored in the public `sunmi-OS` GitHub organization. Maven POMs for PayLib, PrinterX and ECR point to `code.sunmi.com`, and DMP points to a SUNMI Codeup/Teambition repository. Those upstream source repositories can be access-controlled and are therefore recorded as provenance links rather than assumed publicly fetchable source history.
