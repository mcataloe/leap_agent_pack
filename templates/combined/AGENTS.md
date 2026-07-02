<!--
LEAP_AGENT_PACK_TEMPLATE:
  template: combined-local-trial
  version: 0.2.0-candidate
  compatible_leap_framework: ">=0.1.0 <1.0.0"
  source: https://github.com/mcataloe/leap_agent_pack
  last_updated: 2026-07-01
  local_modification_notes: Record downstream edits here.
END_LEAP_AGENT_PACK_TEMPLATE
-->

# Master Repo AGENTS.md - LEAP Local Trial Template

Use this single file to test LEAP in one repository before installing separate global instructions.

The file has two scopes:

1. **Locked Global Section** — reusable LEAP behavior.
2. **Editable Repository Section** — project-specific context populated from repository evidence.

Do not edit the locked section during repository onboarding. Preserve all section markers.

---

<!-- LEAP_MASTER_GLOBAL_SECTION_START: DO NOT EDIT DURING REPO POPULATION -->

# Locked Global Section - LEAP Operating Guidance

## Lifecycle

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

LEAP LHS is the Layered House Standard Prompt format for staged implementation. It is not a lifecycle phase and does not define the project's strategic hierarchy.

## Project-documentation model

```text
Mission / Project Charter
        ↓
Strategic Outcome
        ↓
Initiative
        ↓
Delivery Unit
        ↓
Build Unit
```

Supporting views:

```text
Roadmap      = timing, priority, milestones, dependencies, releases, status, parallelism
Domain Map   = persistent responsibility and ownership boundaries
Architecture = technical structure and qualified technical Layers
```

Rules:

- Several Initiatives may run in parallel.
- Roadmap placement does not permanently define Initiative identity.
- Initiatives and Domains are many-to-many.
- Delivery Unit may collapse for small work.
- Build Unit is bounded implementation and is not necessarily independently deployable.
- Generic project-planning `Layer` is legacy-compatible and deprecated.
- Preserve the LEAP name, Layered House Standard, LEAP LHS, qualified Architecture Layers, public paths, and compatibility references.
- Classify a legacy Layer as Initiative, Delivery Unit, Build Unit, Domain, Architecture Layer, Phase, or mixed / unclear before migration.

## Instruction priority

1. System, developer, and tool instructions.
2. Explicit user instructions.
3. Editable Repository Section and closer-scoped instructions.
4. This Locked Global Section.
5. Repository code, tests, docs, and conventions.

Stop when conflicts materially affect source truth, product behavior, Architecture, data, security, compatibility, or validation.

## Default work pattern

1. Inspect repository and documentation evidence.
2. Identify Strategic Outcome and Initiative when material.
3. Treat Roadmap as planning context.
4. Identify affected Domains and Architecture areas.
5. Perform Planning Boundary Review.
6. Define a Delivery Unit when a meaningful release or adoption boundary exists.
7. Define a bounded Build Unit or task.
8. Implement only the approved scope.
9. Test and update docs.
10. Complete Validation/Handoff.

## Planning Boundary Review

Classify the target as:

- Strategic Outcome question
- Initiative
- Delivery Unit
- Build Unit
- Domain concern
- Architecture concern
- Phase
- ambiguous legacy Layer

Do not assume numbered work must be sequential. Do not globally replace `Layer`.

## LEAP command routing

| Command | Expected behavior |
|---|---|
| `Run LEAP Charter` | Establish or reconcile Mission, Outcomes, Initiatives, Roadmap, Domains, Architecture, source truth, and readiness. |
| `Run LEAP Recon` | Investigate a focused Outcome, Initiative, Delivery Unit, Build Unit, Domain, Architecture area, feature, dependency, contract, risk, or legacy Layer. |
| `Generate LEAP Prompt` | Create an agent-ready Prompt only after source truth, repo reality, boundary, validation, stop conditions, and execution configuration are clear. |
| `Generate LEAP LHS` | Create staged execution when an Initiative or Delivery Unit contains several Build Units or integration checkpoints. |
| `Run LEAP Validation` | Verify completed work against scope, acceptance, tests, docs, and stop conditions. |
| `Run LEAP Handoff` | Report changes, validation, deviations, risks, and follow-up work. |

## Implementation rules

- Reuse existing patterns.
- Keep changes within the approved Build Unit or bounded task.
- Preserve compatibility unless approved otherwise.
- Do not invent product or Architecture decisions.
- Do not add dependencies without permission.
- Do not weaken tests.
- Preserve security, privacy, data, auditability, and ownership boundaries.

## Stop conditions

Stop before:

- destructive or irreversible data changes
- auth, permission, security, privacy, billing, or identity changes without approval
- breaking contracts without migration approval
- major Architecture replacement
- adding paid services or major dependencies
- inventing material business rules
- treating archived docs as current source truth
- proceeding with unclear Initiative, Domain, Architecture, Delivery Unit, or Build Unit ownership
- interpreting an ambiguous legacy Layer without enough evidence
- irreversible Git operations

## Validation and commits

Run relevant repository checks and report anything not run.

Prefer one Build Unit per commit where feasible. Use Initiative, Delivery Unit, Build Unit, or task identifiers when available.

<!-- LEAP_MASTER_GLOBAL_SECTION_END -->

---

<!-- LEAP_MASTER_REPO_SECTION_START: EDIT THIS SECTION ONLY DURING REPO POPULATION -->

# Editable Repository Section - Project-Specific Guidance

## Project identity

Project name: `{{PROJECT_NAME}}`

Project summary:

`{{ONE_PARAGRAPH_PROJECT_DESCRIPTION}}`

Primary users or use cases:

- `{{PRIMARY_USER_OR_USE_CASE_1}}`
- `{{PRIMARY_USER_OR_USE_CASE_2}}`

## Documentation starting point

Start with `docs/00_start_here.md` when present.

## LEAP Baseline State

| Item | Value |
|---|---|
| Baseline record | Inline in `AGENTS.md` |
| Last full reconcile | `{{YYYY-MM-DD_OR_NEVER}}` |
| Last reconcile mode | `{{Brownfield Charter / LEAP Governance / Manual / Never}}` |
| Current source-truth entry point | `{{PATH_TO_SOURCE_TRUTH_ENTRYPOINT}}` |
| Canonical docs location | `{{PATH_TO_CANONICAL_DOCS}}` |
| Archive location | `{{PATH_TO_ARCHIVE_DOCS_OR_NA}}` |
| Gap register / known drift | `{{PATH_TO_GAP_REGISTER_OR_NONE}}` |
| Baseline confidence | `{{High / Medium / Low / Unknown}}` |
| Reconcile triggers | `{{STRATEGIC_OUTCOME_CHANGE; INITIATIVE_CHANGE; ROADMAP_REPRIORITIZATION; DOMAIN_OWNERSHIP_CHANGE; ARCHITECTURE_PIVOT; SOURCE_TRUTH_CONFLICT; LARGE_DELIVERY_UNIT; ETC.}}` |

Do not invent reconcile history or silently create baseline metadata.

## Strategic and planning sources

- Mission / Project Charter: `{{PATH_TO_PROJECT_CHARTER_OR_EQUIVALENT}}`
- Strategic Outcomes: `{{PATH_TO_STRATEGIC_OUTCOMES}}`
- Initiative registry: `{{PATH_TO_INITIATIVE_REGISTRY}}`
- Roadmap: `{{PATH_TO_ROADMAP}}`
- Domain map: `{{PATH_TO_DOMAIN_MAP}}`
- Architecture docs: `{{PATH_TO_ARCHITECTURE_DOCS}}`
- Delivery Unit docs: `{{PATH_TO_DELIVERY_UNIT_DOCS_OR_NA}}`
- Build Unit docs / active Prompts: `{{PATH_TO_BUILD_UNIT_DOCS_OR_ACTIVE_PROMPTS}}`
- Contracts: `{{PATH_TO_API_EVENT_SCHEMA_OR_DATA_CONTRACTS}}`
- Legacy Layer docs requiring classification: `{{PATHS_OR_NONE}}`

Canonical docs:

- `{{CANONICAL_DOC_1}}`
- `{{CANONICAL_DOC_2}}`
- `{{CANONICAL_DOC_3}}`

Draft, stale, archived, superseded, or do-not-use docs:

- `{{NON_CANONICAL_DOC_1}}`
- `{{NON_CANONICAL_DOC_2}}`

## Repository layout

- Frontend: `{{FRONTEND_PATH_OR_NA}}`
- Backend/API: `{{BACKEND_PATH_OR_NA}}`
- Shared code/contracts: `{{SHARED_PATH_OR_NA}}`
- Docs: `{{DOCS_PATH}}`
- Tests: `{{TESTS_PATH}}`
- Scripts: `{{SCRIPTS_PATH_OR_NA}}`
- Infrastructure: `{{INFRA_PATH_OR_NA}}`

## Technology stack

- Frontend: `{{FRONTEND_STACK}}`
- Backend/API: `{{BACKEND_STACK}}`
- Database: `{{DATABASE_STACK}}`
- Infrastructure: `{{INFRA_STACK}}`
- Package manager: `{{PACKAGE_MANAGER}}`
- Test framework: `{{TEST_FRAMEWORK}}`
- Runtime versions: `{{RUNTIME_VERSIONS}}`

## Setup and validation commands

```bash
{{INSTALL_COMMAND}}
```

```bash
{{LOCAL_DEV_COMMAND}}
```

```bash
{{FORMAT_COMMAND}}
```

```bash
{{LINT_COMMAND}}
```

```bash
{{TYPECHECK_COMMAND}}
```

```bash
{{TEST_COMMAND}}
```

```bash
{{BUILD_COMMAND}}
```

Do not invent commands. Report unknown commands as `TBD`.

## Project-specific Architecture and coding rules

- `{{ARCHITECTURE_OR_CODING_RULE_1}}`
- `{{ARCHITECTURE_OR_CODING_RULE_2}}`
- `{{ARCHITECTURE_OR_CODING_RULE_3}}`

## Data and contract rules

- `{{DATA_OR_CONTRACT_RULE_1}}`
- `{{DATA_OR_CONTRACT_RULE_2}}`
- `{{DATA_OR_CONTRACT_RULE_3}}`

## Security and privacy rules

- `{{SECURITY_OR_PRIVACY_RULE_1}}`
- `{{SECURITY_OR_PRIVACY_RULE_2}}`
- `{{SECURITY_OR_PRIVACY_RULE_3}}`

Never commit secrets, weaken access controls, expose sensitive data, bypass validation, or add third-party services without approval.

## Testing and documentation expectations

- Add or update tests for changed behavior.
- Use existing test helpers and patterns.
- Do not weaken or delete failing tests without explanation and approval.
- Update Strategy, Initiative, Roadmap, Domain, Architecture, Delivery Unit, Build Unit, product, contract, setup, and operational docs when implementation changes reality.

Project docs to keep aligned:

- `{{DOC_PATH_1}}`
- `{{DOC_PATH_2}}`
- `{{DOC_PATH_3}}`

## Branch and commit expectations

- `{{BRANCH_OR_PR_RULE_1}}`
- `{{BRANCH_OR_PR_RULE_2}}`
- Prefer one Build Unit per commit where feasible.
- Use `{{INITIATIVE_DELIVERY_BUILD_OR_TASK_ID}} - {{SHORT_TITLE}}` when identifiers exist.

## Project-specific stop conditions

- `{{STOP_CONDITION_1}}`
- `{{STOP_CONDITION_2}}`
- `{{STOP_CONDITION_3}}`

## Completion requirements

Report:

- summary of changes
- Strategic Outcome / Initiative / Delivery Unit / Build Unit impact when material
- files and areas changed
- tests and checks run
- checks not run and why
- docs updated or still needed
- deviations, risks, and follow-up LEAP work

<!-- LEAP_MASTER_REPO_SECTION_END -->

<!-- LEAP_LOCAL_OVERRIDES_BEGIN -->
<!-- Optional local notes. Keep durable project guidance in the editable repository section. -->
<!-- LEAP_LOCAL_OVERRIDES_END -->
