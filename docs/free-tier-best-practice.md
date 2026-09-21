# Free-Tier Best Practice Guide

This guide is the operational companion to [`kks-architecture-spec.md`](architecture/kks-architecture-spec.md).

## Recommended daily workflow

1. Create a branch for a change.
2. Edit knowledge, docs, or an isolated example.
3. Run local Markdown and Python checks.
4. Open a pull request.
5. Review generated output and changed permissions.
6. Merge only after checks pass.

## Safe generated-content workflow

```text
Prompt or source data
        |
        v
Small deterministic generator
        |
        v
Approved generated directory
        |
        v
CI validation
        |
        v
Pull request review
        |
        v
main
```

## Never do these things

- commit a token, password, private key, or live webhook URL;
- use a public repository as a database for private information;
- let a generator delete unrelated files;
- grant admin access when writing Markdown is enough;
- store large build outputs or binary collections in Git;
- rely on a README claim as evidence of actual GitHub permissions.

## Practical free-tier controls

- Keep Actions workflows short and infrequent.
- Use path filters so documentation checks do not run for unrelated changes.
- Keep artifacts temporary and small.
- Prefer repository history for text revisions and external storage for large media.
- Use issues and pull requests for assignment, review, approval, and decision records.
- Use Actions checks and workflow logs for monitoring instead of building a monitoring service.

## Project-specific storage rule

- `knowledge-supporting/`: durable, reviewed knowledge.
- `docs/`: architecture, policies, and user guides.
- `chatgpt-generated/`: machine-generated drafts or outputs, always subject to validation and review.
- `cooking-agent/`: isolated example application.

If a file does not fit one of these categories, classify it before adding it.
