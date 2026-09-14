# K Knowledge Supporting

This directory is the primary long-term text/knowledge storage target for the K SUNMI Knowledge Base project.

## Storage policy

- Primary: GitHub repository `RepoKan/K-Knowledgeable-` under `knowledge-supporting/`
- Fallback: persistent ChatGPT Library when GitHub is unavailable or unsuitable for the file type
- Last fallback: local/runtime project storage such as `/mnt/data`
- Runtime/sandbox download links are temporary only
- Weekly SUNMI reports must not generate PDF; weekly archive format is UTF-8 `.txt`
- Preserve old knowledge as revision layers; append updates instead of deleting prior knowledge

## Structure

- `knowledge-base/` — persistent reference and revision knowledge
- `weekly-archives/` — weekly SUNMI text archives and command/rule snapshots
- `project-metadata/` — storage/access/process metadata
- `manifests/` — transfer and migration status

## Binary/raw media

The current GitHub connector write path is UTF-8 text oriented. Binary artifacts such as PDF, PNG, PPTX, DOCX, XLSX, ZIP, or APK-related binaries are not written here through the text contents API. Use a supported GitHub binary path (for example Git LFS or release assets) or a user-approved manual upload flow.

## Safety

Do not publish passwords, API tokens, private keys, keystore passwords, private certificate material, or other secrets to this public repository unless separately and explicitly approved and intentionally publishable or encrypted.
