# Private Repository Bootstrap R1

Status: Public/sanitized bootstrap guide  
Date: 2026-09-11

## Required private repositories

Create two private repositories outside this public framework repository:

- `KTC-EDC-P3-Android`
- `KTC-Knowledge-Master`

The exact names may change, but the separation must remain.

## Android repository requirements

The Android repository should contain application source, Gradle wrapper/configuration, tests, AI instructions, inspection documents, and a pinned `knowledge/master` git submodule.

Do not import a production ZIP directly. First remove local/generated state, keystores/signing material, plaintext signing credentials, local configuration, and runtime evidence that is not approved for source control.

## Knowledge Master requirements

The Knowledge Master should contain approved derived knowledge, source-authority rules, versioned business rules, QA rules, source manifests/hashes, and revision history. Restricted source documents or vendor binaries should be stored only when policy/licensing allows; otherwise retain immutable hashes and approved references.

## Pinned submodule

After the private Knowledge Master exists:

```bash
git submodule add <PRIVATE_KNOWLEDGE_REPOSITORY_URL> knowledge/master
git add .gitmodules knowledge/master
git commit -m "docs: pin Knowledge Master"
```

Each release/investigation must record both the Android commit SHA and the Knowledge Master gitlink commit SHA.

## PR/Impact gate

Recommended protected flow:

```text
ai-review/* or fix/*
    -> pull request
    -> source hygiene / secret scan
    -> knowledge pin validation
    -> impact report
    -> build/lint/tests
    -> device/integration validation where applicable
    -> human approval
    -> merge
```

The public `RepoKan/K-Knowledgeable-` repository should retain only reusable, sanitized framework guidance and connector patterns.
