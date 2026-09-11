# Private Android + Knowledge Repository Design R1

Status: LOCKED ARCHITECTURE BASELINE  
Date: 2026-09-11

## Architecture decision

Use four controls together:

1. **Private Android Source Repository**
2. **Private Knowledge Master Repository**
3. **Pinned Git submodule** from Android source to the exact Knowledge Master commit
4. **AI instructions + PR/Impact Gate** before production-affecting changes

The current public `RepoKan/K-Knowledgeable-` repository remains a sanitized AI/connector/framework repository only. It must not receive KTC production source ZIPs, signing material, internal credentials, restricted specifications, production logs, or confidential host/payment configuration.

## Target topology

```text
RepoKan/K-Knowledgeable-                 PUBLIC / SANITIZED FRAMEWORK
        |
        +-- generic AI governance
        +-- connector / workflow patterns
        +-- repository design rules
        +-- no KTC production secrets or restricted source

PRIVATE: KTC-EDC-P3-Android              ANDROID SOURCE
        |
        +-- app/
        +-- Gradle wrapper/config
        +-- tests
        +-- AGENTS.md
        +-- .github/copilot-instructions.md
        +-- .github/instructions/
        +-- docs/inspection/
        +-- knowledge/master -------------+
                                           |
PRIVATE: KTC-Knowledge-Master             |
        |                                  |
        +-- source-authority/              |
        +-- field61-location/              |
        +-- iso8583/                       |
        +-- emv-ctls/                      |
        +-- tle/                           |
        +-- tms/                           |
        +-- sunmi/                         |
        +-- production-debugging/          |
        +-- ai/                            |
        +-- revision/                      |
        +----------------------------------+
             pinned submodule commit SHA
```

## Source precedence

1. Exact production source commit/version under inspection
2. Approved KTC specification
3. Official vendor SDK documentation
4. Matched production log/device/runtime evidence
5. Approved project business rules
6. Derived knowledge/design documents
7. General AI/model knowledge

Lower-authority material must never silently override higher-authority material.

## Security boundary

The Android repository must exclude:

- keystores and signing keys
- signing passwords / credentials
- `local.properties`
- `.gradle/`, `build/`, IDE state
- secrets/config files containing credentials
- packet captures or logs containing production/payment data unless stored through an explicitly approved restricted evidence process

The Knowledge Master is private and may contain approved derived knowledge and restricted references only under the organization's access policy. It still must not contain plaintext secrets or payment cryptographic key material.

## Knowledge pinning

The Android source repository must record the exact Knowledge Master commit used for inspection/release.

Recommended location:

```text
knowledge/master
```

The effective inspection identity is:

```text
Android source commit SHA
+ Knowledge Master commit SHA
+ approved specification version
+ matched runtime evidence identity
```

## Branch and PR policy

Recommended branches:

- `main` - approved baseline
- `develop` - integration
- `feature/*` - normal development
- `fix/*` - bug fixes
- `hotfix/*` - urgent production fixes
- `release/*` - release candidate
- `ai-review/*` - AI-generated proposal/inspection work

AI must not directly modify or merge production baseline. Production-relevant AI work must flow through a PR and the impact gate.
