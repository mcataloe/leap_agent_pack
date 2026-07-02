<!--
LEAP_AGENT_PACK_TEMPLATE:
  template: repo
  version: 0.2.0-candidate
  compatible_leap_framework: ">=0.1.0 <1.0.0"
  source: https://github.com/mcataloe/leap_agent_pack
  last_updated: 2026-07-01
  local_modification_notes: Record downstream edits here.
END_LEAP_AGENT_PACK_TEMPLATE
-->

<!-- LEAP_MANAGED_SECTION_BEGIN -->

# Repository AGENTS.md - LEAP Project Template

## Project identity

This repository uses LEAP for agent-assisted software delivery.

Project name:

`{{PROJECT_NAME}}`

Project summary:

`{{ONE_PARAGRAPH_PROJECT_DESCRIPTION}}`

Current lifecycle:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

LEAP LHS is the Layered House Standard Prompt format for staged implementation. It is not a lifecycle phase and it does not define the project's strategic hierarchy.

## Project-documentation model

Use this hierarchy when material:

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

Treat these separately:

```text
Roadmap      = timing, priority, milestones, dependencies, release targets, status, parallelism
Domain Map   = persistent business, responsibility, ownership, or technical boundaries
Architecture = technical structure and qualified technical Layers
```

Project rules:

- Several Initiatives may run in parallel.
- Roadmap placement does not permanently define Initiative identity.
- Initiatives and Domains have a many-to-many relationship.
- Delivery Unit may collapse for small work.
- Build Unit is bounded implementation and is not necessarily independently deployable.
- Generic project-planning `Layer` is legacy-compatible and deprecated.
- Preserve the LEAP name, Layered House Standard, LEAP LHS, qualified Architecture Layers, public paths, and compatibility references.
- Classify a legacy Layer as Initiative, Delivery Unit, Build Unit, Domain, Architecture Layer, Phase, or mixed / unclear before migration.

<!-- LEAP_MANAGED_SECTION_END -->

<!-- LEAP_PROJECT_SECTION_BEGIN -->

## Documentation starting point

Start with `docs/00_start_here.md` when present.

## LEAP Baseline State

Use this section during Recon to judge whether the baseline appears fresh enough. It is a signal, not a hard gate.

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
| Reconcile triggers | `{{MAJOR_STRATEGIC_OUTCOME_CHANGE; NEW_OR_CHANGED_INITIATIVE; ROADMAP_REPRIORITIZATION; DOMAIN_OWNERSHIP_CHANGE; ARCHITECTURE_PIVOT; SOURCE_TRUTH_CONFLICT; STALE_AGENTS_MD; LARGE_DELIVERY_UNIT; ETC.}}` |

Update this table only after a full Brownfield Charter, Governance pass, major reconciliation, or intentional baseline update.

When `leap.baseline.yaml` exists, treat it as the canonical machine-readable baseline record and keep this table as a compact pointer.

## Strategic and planning docs

- Mission / Project Charter: `{{PATH_TO_PROJECT_CHARTER_OR_EQUIVALENT}}`
- Strategic Outcomes: `{{PATH_TO_STRATEGIC_OUTCOMES}}`
- Initiative registry: `{{PATH_TO_INITIATIVE_REGISTRY}}`
- Roadmap: `{{PATH_TO_ROADMAP}}`
- Domain map: `{{PATH_TO_DOMAIN_MAP}}`
- Architecture docs: `{{PATH_TO_ARCHITECTURE_DOCS}}`
- Delivery Unit plans: `{{PATH_TO_DELIVERY_UNIT_DOCS_OR_NA}}`
- Build Unit plans / active Prompts: `{{PATH_TO_BUILD_UNIT_DOCS_OR_ACTIVE_PROMPTS}}`
- API, event, schema, or data contracts: `{{PATH_TO_API_OR_DATA_CONTRACT_DOCS}}`
- Legacy Layer docs requiring classification: `{{PATHS_OR_NONE}}`

Canonical docs:

- `{{CANONICAL_DOC_1}}`
- `{{CANONICAL_DOC_2}}`
- `{{CANONICAL_DOC_3}}`

Draft, stale, archived, superseded, or do-not-use docs:

- `{{ARCHIVED_OR_STALE_DOC_1}}`
- `{{ARCHIVED_OR_STALE_DOC_2}}`
- `{{ARCHIVED_OR_STALE_DOC_3}}`

Treat canonical docs as source truth. Treat archived docs as historical unless a current canonical document references them.

## Repository layout

- `{{FRONTEND_PATH}}` - Frontend application.
- `{{BACKEND_PATH}}` - API or backend service.
- `{{SHARED_PATH}}` - Shared types, schemas, utilities, or contracts.
- `{{DOCS_PATH}}` - Product, strategy, Domain, Architecture, LEAP, Roadmap, Delivery, and Build documentation.
- `{{TESTS_PATH}}` - Test suites.
- `{{SCRIPTS_PATH}}` - Development and operational scripts.
- `{{INFRA_PATH}}` - Infrastructure-as-code or deployment configuration.

## Technology stack

- Frontend: `{{FRONTEND_STACK}}`
- Backend/API: `{{BACKEND_STACK}}`
- Database: `{{DATABASE_STACK}}`
- Infrastructure: `{{INFRA_STACK}}`
- Package manager: `{{PACKAGE_MANAGER}}`
- Test framework: `{{TEST_FRAMEWORK}}`
- Runtime versions: `{{RUNTIME_VERSIONS}}`

Use the existing stack unless evaluation or migration is explicitly requested.

## Setup commands

```bash
{{INSTALL_COMMAND}}
```

```bash
{{LOCAL_DEV_COMMAND}}
```

```bash
{{DATABASE_SETUP_OR_MIGRATION_COMMAND}}
```

Do not invent commands. Inspect repository evidence first.

## Validation commands

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

Prefer targeted checks first, then broader checks when practical. Report unavailable or prohibitively expensive checks honestly.

## LEAP project rules

Before implementation:

1. Locate the governing Mission, Strategic Outcome, Initiative, and source-truth docs when material.
2. Treat Roadmap placement as scheduling context, not permanent identity.
3. Identify affected Domains and Architecture areas.
4. Determine whether the target is Initiative-sized, Delivery-Unit-sized, Build-Unit-sized, Domain-oriented, Architecture-oriented, a Phase, or an ambiguous legacy Layer.
5. Define a bounded Build Unit or task.
6. Confirm repository reality and existing functionality.
7. Identify dependencies, contracts, tests, documentation, and stop conditions.

Implement only the approved Build Unit or bounded task unless a prerequisite is explicitly included or a material dependency requires human review.

Do not assume numbered work is sequential. Do not skip required dependencies. Do not silently broaden into adjacent Initiatives, Delivery Units, Domains, or Architecture changes.

## Baseline Freshness Check

During Recon:

- inspect this Baseline State and `leap.baseline.yaml` when present
- inspect relevant current docs and repo reality
- continue normally when fresh enough
- continue with disclosed limitations for minor drift
- recommend Charter or Governance for material drift
- stop for unsafe source-truth conflict
- do not silently create or update baseline metadata

## Planning Boundary Review

Classify the target as:

- Strategic Outcome question
- Initiative
- Delivery Unit
- Build Unit
- Domain concern
- Architecture concern
- Phase
- legacy Layer requiring reconciliation

Use a Delivery Unit when several Build Units, repositories, release increments, or a meaningful release, enablement, adoption, or demonstration boundary exists.

Collapse Delivery Unit when one small Build Unit directly delivers the entire Initiative outcome and a separate level adds no safety or clarity.

## Dependency & Contract Recon

Inspect dependency and contract evidence when work touches integrations, APIs, SDKs, generated clients, packages, platform services, events, identity, payments, or infrastructure.

Evidence may include:

- `leap.dependencies.yaml`
- OpenAPI, AsyncAPI, protobuf, or GraphQL schemas
- provider repository or documentation links
- SDKs and generated clients
- package manifests
- integration tests and mocks
- infrastructure dependencies
- event topics and queues
- identity and payment providers

Missing dependency metadata is a limitation, not an automatic blocker. Do not guess external contracts or provider ownership.

## Project source of truth

Use this order unless explicit project guidance overrides it:

1. Explicit user instruction for the current task.
2. Current repository code, tests, schemas, and migrations.
3. Repository and closer-scoped `AGENTS.md` files.
4. Current Project Charter and Strategic Outcomes.
5. Initiative registry and active Initiative docs.
6. Roadmap for timing, priority, dependencies, and status.
7. Domain and Architecture docs.
8. Current Delivery Unit and Build Unit plans or approved Prompts.
9. README and setup docs.
10. Active issue or task text.
11. Archived docs only when referenced by current canonical sources.
12. Clearly labeled inference.

Call out conflicts rather than silently choosing an unsafe source.

## Charter rules

Use Charter when Mission, Strategic Outcomes, Initiative identity, Roadmap, Domains, Architecture, source truth, documentation structure, or implementation posture is unclear.

Brownfield policy:

```text
Canonicalize forward.
Archive backward.
Preserve traceability.
Never let stale docs compete with source-of-truth docs.
```

Classify legacy Layer docs semantically before renaming or moving them. Preserve public paths unless an approved migration says otherwise.

## Architecture rules

Follow existing Architecture and ownership boundaries.

- Keep contracts explicit.
- Keep validation close to data boundaries.
- Reuse existing types, schemas, and DTO patterns.
- Avoid duplicate model or contract definitions.
- Preserve authorization and ownership boundaries.
- Prefer incremental extension over replacement.
- Avoid broad rewrites unless a refactor is approved.

Project-specific Architecture constraints:

- `{{ARCHITECTURE_CONSTRAINT_1}}`
- `{{ARCHITECTURE_CONSTRAINT_2}}`
- `{{ARCHITECTURE_CONSTRAINT_3}}`

## Data and migration rules

Before changing schemas, migrations, seed data, or persistence:

- inspect current models and migrations
- determine environment maturity
- preserve data unless destructive changes are approved
- keep migrations reversible where practical
- update tests and docs
- do not silently change identifiers, ownership, or lifecycle semantics

Project-specific data rules:

- `{{DATA_RULE_1}}`
- `{{DATA_RULE_2}}`
- `{{DATA_RULE_3}}`

## API and contract rules

- Preserve backward compatibility unless approved otherwise.
- Update shared types and validation together.
- Update API and contract tests.
- Update docs and examples.
- Keep error behavior consistent.
- Avoid parallel contract definitions.

Project-specific contract rules:

- `{{CONTRACT_RULE_1}}`
- `{{CONTRACT_RULE_2}}`

## UI and UX rules

- Follow existing component and styling patterns.
- Keep user flows clear and accessible.
- Preserve user-entered data.
- Make loading, success, error, and empty states explicit.
- Avoid broad visual rewrites unless requested.

Project-specific UX rules:

- `{{UX_RULE_1}}`
- `{{UX_RULE_2}}`
- `{{UX_RULE_3}}`

## AI and automation rules

When AI is used:

- keep outputs reviewable
- preserve traceability to source material
- expose uncertainty
- distinguish generated drafts from reviewed or submitted artifacts
- do not fabricate user facts, credentials, claims, metrics, or decisions
- do not automate irreversible user-facing actions without review

Project-specific AI rules:

- `{{AI_RULE_1}}`
- `{{AI_RULE_2}}`
- `{{AI_RULE_3}}`

## Security and privacy rules

Never:

- commit secrets, credentials, private keys, or environment files
- log sensitive data unnecessarily
- weaken authentication or authorization
- bypass validation to make tests pass
- expose sensitive data to clients
- add third-party services without approval
- silently change security-sensitive behavior

Project-specific security and privacy rules:

- `{{SECURITY_RULE_1}}`
- `{{SECURITY_RULE_2}}`
- `{{SECURITY_RULE_3}}`

## Testing expectations

When behavior changes:

- add or update tests
- cover success, failure, and important edge cases
- use existing helpers and factories
- avoid rewriting test infrastructure unless requested
- do not delete or weaken failing tests without explanation and approval

## Documentation expectations

Update docs when changes affect:

- Mission, Strategic Outcomes, or Initiative status
- Roadmap timing, dependencies, priority, or release posture
- Domain ownership or contracts
- Architecture
- Delivery Unit or Build Unit status
- product behavior or workflows
- APIs, events, schemas, or data models
- setup, commands, environment variables, security, or operations

Project-specific docs to keep aligned:

- `{{DOC_PATH_1}}`
- `{{DOC_PATH_2}}`
- `{{DOC_PATH_3}}`

## Commit and branch expectations

When commits are requested:

- keep commits scoped and reviewable
- prefer one Build Unit per commit where feasible
- use Initiative, Delivery Unit, Build Unit, or task identifiers when available
- do not combine unrelated work
- inspect repository status before committing
- include tests and docs with the implementation they validate

Preferred message:

```text
{{INITIATIVE_DELIVERY_BUILD_OR_TASK_ID}} - {{SHORT_DESCRIPTIVE_TITLE}}
```

## Stop conditions

Stop before:

- destructive schema or data changes without approval
- auth, session, ownership, permission, billing, privacy, or security changes without approval
- breaking public contracts without migration approval
- paid services or major production dependencies
- removing major functionality
- replacing established Architecture
- inventing material business rules
- proceeding with unclear Initiative, Domain, Delivery Unit, Build Unit, or Architecture ownership
- treating archived docs as current source truth
- interpreting an ambiguous legacy Layer without enough evidence
- weakening privacy, traceability, auditability, or security controls

Project-specific stop conditions:

- `{{STOP_CONDITION_1}}`
- `{{STOP_CONDITION_2}}`
- `{{STOP_CONDITION_3}}`

## Completion requirements

A task is complete when:

- requested behavior is implemented within the approved Build Unit or bounded task
- existing patterns and compatibility requirements are preserved
- relevant tests and checks were run or honestly reported as unavailable
- source-truth docs were updated when implementation changed reality
- risks, deviations, and follow-up work are recorded
- Validation/Handoff reports Strategic Outcome, Initiative, Delivery Unit, and Build Unit impact when material

Final response should include:

- summary of changes
- traceability confirmed
- files and areas changed
- tests and checks run
- checks not run and why
- docs updated or still needed
- risks, deviations, and follow-up LEAP work

<!-- LEAP_PROJECT_SECTION_END -->

<!-- LEAP_LOCAL_OVERRIDES_BEGIN -->
<!--
Optional local team or developer-specific notes go here.
Keep durable project guidance in the project section above.
-->
<!-- LEAP_LOCAL_OVERRIDES_END -->
