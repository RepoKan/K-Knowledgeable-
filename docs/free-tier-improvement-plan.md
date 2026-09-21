# Free-Tier Improvement Plan

This plan converts the current repository into a safer, cleaner, and more maintainable GitHub Free architecture.

## Phase 1: Simplify the operating model

### Actions

- move generated files into a dedicated folder such as `docs/generated/`
- remove repo-wide admin assumptions from automation guidance
- reduce connector documentation to a narrow, least-privilege model
- clarify that automation only writes approved content paths

### Result

The repository uses a smaller operational surface area and less risk of broad accidental changes.

## Phase 2: Separate source from generated content

### Proposed structure

```text
docs/
  architecture/
  governance/
  generated/
  guides/
```

### Benefits

- easier review
- cleaner content ownership
- lower accidental overwrite risk
- simpler automation behavior

## Phase 3: Turn validation into a default path

### Recommended checks

- markdown linting
- basic YAML validation
- Python syntax validation
- scan for secret patterns
- verify generated files follow naming conventions

### Result

Every change is validated before merge, even for low-risk content.

## Phase 4: Add review gates

### Recommended gates

- require pull requests before merge
- require at least one reviewer for `main`
- optionally require status checks to pass
- deny force pushes on default branch

### Result

The repo becomes more stable and easier to trust.

## Phase 5: Reduce secret and token exposure

### Rules

- never store tokens in repository files
- define secrets only in GitHub Actions or local environment files
- keep `.env.example` as a template, not a live credential source
- document required scopes clearly

### Result

The risk of token leakage drops sharply.

## Phase 6: Keep automation narrow and explainable

### Examples

- generate docs summaries
- validate markdown structure
- publish static docs if needed
- run low-cost scheduled tasks

### Avoid

- automatic mutation outside a defined path
- admin-level workflow behavior
- broad connector privileges
- destructive automation without review

## Phase 7: Operate as a lightweight knowledge repo

The repository should act as a documentation and knowledge base, not as a broad autonomous repo administration layer.

### Recommended posture

- text-first
- review-first
- documented outputs
- minimal automation
- low-risk free-tier hosting

## Final target state

The final repository design should resemble:

- a documentation-first GitHub project
- small automation set
- narrow output scope
- strong review boundaries
- no broad admin assumptions
- small operational footprint under GitHub Free

## Implementation priority

1. reduce permission scope
2. separate generated files
3. enforce PR review flow
4. add validation workflow
5. document all automation
6. keep the repository minimal and transparent

