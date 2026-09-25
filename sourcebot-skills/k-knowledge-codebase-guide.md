---
name: K Knowledge Codebase Guide
command: k-knowledge-codebase-guide
description: Governed guidance for investigating K Knowledge Supporting repositories with Sourcebot. Use for cross-repository search, architecture tracing, code navigation, symbol impact, and ref-aware codebase questions while preserving exact source identity and public-repository boundaries.
---

Use Sourcebot to accelerate discovery, not to replace source authority.

1. Record repository identity and ref or SHA before version-sensitive conclusions.
2. Use search to discover candidate files, then read exact implementations.
3. Trace symbol definitions and references before impact conclusions.
4. Distinguish Sourcebot's indexed snapshot from live GitHub state.
5. Use the native GitHub connector for PRs, checks, permissions, branch protection, and immediately-created refs.
6. Never expose secrets, private endpoints, payment data, confidential Production logs, or restricted specifications in Sourcebot prompts or shared skills.
7. For Production-impact work, apply the K Knowledge Supporting evidence and HOLD gates before concluding.
