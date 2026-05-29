<!--
LEAP_AGENT_PACK_TEMPLATE:
  template: combined-example
  version: 0.1.0
  compatible_leap_framework: ">=0.1.0 <1.0.0"
  source: https://github.com/mjcataldi/leap_agent_pack
  last_updated: 2026-05-29
  local_modification_notes: Record downstream edits here.
END_LEAP_AGENT_PACK_TEMPLATE
-->

# Master Repo AGENTS.md - LEAP Local Trial Template

Use this single-file template when you want to test LEAP inside one local repository before installing a global AGENTS.md system-wide.

This file has two sections:

1. **Locked Global Section** - reusable LEAP operating behavior copied from the global AGENTS.md template.
2. **Editable Repository Section** - project-specific AGENTS.md content that should be populated from the current repository.

When this file is placed at the root of a repository as `AGENTS.md`, the code assistant should treat the locked global section as global LEAP behavior and the editable repository section as the repository-level AGENTS.md content.

Populate only the editable repository section during repo onboarding.

---

<!-- LEAP_MANAGED_SECTION_BEGIN -->

<!-- LEAP_MASTER_GLOBAL_SECTION_START: DO NOT EDIT DURING REPO POPULATION -->

# Locked Global Section - LEAP Operating Template

## Purpose

Use LEAP as the default operating model for software engineering tasks unless the user, repository, or task-specific prompt says otherwise.

Current lifecycle:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

LEAP Charter establishes or reconciles project direction, source-of-truth docs, roadmap, and implementation posture.

LEAP Recon investigates a focused area, gap, risk, feature, or architectural question.

LEAP Prompt produces Codex-ready instructions for analysis, documentation, implementation, or remediation.

LEAP LHS is a structured LEAP Prompt format for layered implementation work using the House Standard. It is not a mandatory lifecycle stage.

LEAP Prompt is the instruction artifact family. It includes Charter, Recon, standard implementation, fix, refactor, governance, validation, and LHS prompts. Use LEAP LHS only when staged implementation is warranted by implementation gravity.

Validation/Handoff is the required completion step where Codex verifies changes, checks docs/tests, summarizes work, and recommends follow-up prompts.

## Instruction Priority

When working in a repository, follow instructions in this order:

1. System/developer/tool instructions.
2. Explicit user instructions for the current task.
3. The editable repository section below and closer scoped agent instruction files.
4. This locked global section.
5. Existing source code, tests, documentation, and conventions.

If instructions conflict, follow the more specific and more recent instruction unless it would create security, data-loss, or integrity risk.

## Documentation Starting Point

When present, start with `docs/00_start_here.md`.

Treat canonical docs as source of truth. Treat archived docs as historical unless a current canonical document explicitly references them.

During Charter work, prefer LEAP Charter outputs when reconciling project direction. Create LEAP Recon or LEAP Prompt recommendations instead of making risky implementation changes during Charter work.

Use LEAP Recon outputs for focused investigation findings. Use LEAP LHS only when the task needs staged implementation, commit boundaries, tests, docs, compatibility checks, rollback awareness, or multi-area coordination. Do not treat LHS as a mandatory stage after every LEAP Prompt.

## Default Work Pattern

For non-trivial implementation tasks:

1. Understand the task.
2. Perform repository reconnaissance before editing.
3. Locate relevant canonical docs, code, tests, and existing patterns.
4. Make a concise implementation plan.
5. Implement the smallest coherent change.
6. Add or update relevant tests.
7. Run practical validation checks.
8. Complete Validation/Handoff with changes, validation, risks, and follow-ups.

Do not treat the task as greenfield unless the repository clearly lacks an existing implementation path.

## LEAP Command Shortcuts

When the user asks to run LEAP Charter, use `/prompts/leap-charter-standard.md` from the LEAP framework repository.

When the user asks to run LEAP Recon, use `/prompts/leap-recon-standard.md` from the LEAP framework repository.

Default Recon behavior:

1. Use the editable repository section first.
2. Inspect the current repository state.
3. Use source-of-truth documents identified by this file.
4. Treat Brownfield Charter outputs as source-truth inputs when present.
5. Return Recon only.
6. Do not implement code changes.
7. Do not generate the final LEAP implementation prompt unless the user asks after Recon.

## Stop Conditions

Stop and ask before destructive data changes, auth/security changes, public contract changes, new paid services, major dependencies, major architecture replacement, unclear business rules, treating archived docs as current source truth, or irreversible git operations.

<!-- LEAP_MASTER_GLOBAL_SECTION_END -->

<!-- LEAP_MANAGED_SECTION_END -->

---

<!-- LEAP_PROJECT_SECTION_BEGIN -->

<!-- LEAP_MASTER_REPO_SECTION_START: EDIT THIS SECTION ONLY DURING REPO POPULATION -->

# Editable Repository Section - LEAP Project Template

## Project Identity

Project name:

`{{PROJECT_NAME}}`

Project summary:

`{{ONE_PARAGRAPH_PROJECT_DESCRIPTION}}`

## Documentation Starting Point

Start with `docs/00_start_here.md` when present.

LEAP Prompt is the instruction artifact family. Use LEAP Recon outputs for focused investigation findings. Use LEAP LHS only when the task needs staged implementation, commit boundaries, tests, docs, compatibility checks, rollback awareness, or multi-area coordination. Do not treat LHS as a mandatory stage after every LEAP Prompt.

Primary product/architecture docs:

- `{{PATH_TO_PRIMARY_STRATEGY_DOC}}`
- `{{PATH_TO_ARCHITECTURE_DOCS}}`
- `{{PATH_TO_LAYER_OR_ROADMAP_DOCS}}`
- `{{PATH_TO_API_OR_DATA_CONTRACT_DOCS}}`

Canonical docs:

- `{{CANONICAL_DOC_1}}`
- `{{CANONICAL_DOC_2}}`
- `{{CANONICAL_DOC_3}}`

Archived, stale, superseded, or do-not-use docs:

- `{{ARCHIVED_OR_STALE_DOC_1}}`
- `{{ARCHIVED_OR_STALE_DOC_2}}`
- `{{ARCHIVED_OR_STALE_DOC_3}}`

Treat canonical docs as source of truth. Treat archived docs as historical unless a current canonical document explicitly references them.

## Repository Layout

- `{{FRONTEND_PATH}}` - Frontend application.
- `{{BACKEND_PATH}}` - API/backend service.
- `{{SHARED_PATH}}` - Shared types, schemas, utilities, or contracts.
- `{{DOCS_PATH}}` - Product, architecture, LEAP, and roadmap documentation.
- `{{TESTS_PATH}}` - Test suites.
- `{{SCRIPTS_PATH}}` - Development and operational scripts.
- `{{INFRA_PATH}}` - Infrastructure-as-code or deployment configuration.

## Technology Stack

- Frontend: `{{FRONTEND_STACK}}`
- Backend/API: `{{BACKEND_STACK}}`
- Database: `{{DATABASE_STACK}}`
- Infrastructure: `{{INFRA_STACK}}`
- Package manager: `{{PACKAGE_MANAGER}}`
- Test framework: `{{TEST_FRAMEWORK}}`
- Runtime versions: `{{RUNTIME_VERSIONS}}`

Use the existing stack unless the user explicitly requests evaluation or migration.

## Setup Commands

```bash
{{INSTALL_COMMAND}}
```

```bash
{{LOCAL_DEV_COMMAND}}
```

```bash
{{DATABASE_SETUP_OR_MIGRATION_COMMAND}}
```

Do not invent setup commands. If the command is unclear, inspect the repo first.

## Validation Commands

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

## LEAP Charter Rules

Use LEAP Charter when project direction, roadmap, source-truth status, documentation structure, implementation posture, or brownfield reconciliation is unclear.

Brownfield Charter policy:

```text
Canonicalize forward.
Archive backward.
Preserve traceability.
Never let stale docs compete with source-of-truth docs.
```

During Charter work:

- Identify canonical, supporting, stale, conflicting, duplicate, and archived docs.
- Compare docs against repo reality when applicable.
- Produce or update a gap register and prompt backlog.
- Preserve legacy docs in an archive when superseded.
- Avoid runtime implementation changes unless explicitly requested.
- Capture risky code, schema, API, UI, auth, workflow, or infrastructure work as follow-up LEAP Recon, LEAP Prompt, or LEAP LHS recommendations.

## Project Source of Truth

Use this order of truth:

1. Explicit user instruction for the current task.
2. Current repository code and tests.
3. This `AGENTS.md` and scoped `AGENTS.md` / `AGENTS.override.md` files.
4. Canonical product strategy and architecture docs.
5. Canonical layer/roadmap docs.
6. README and setup docs.
7. Existing issue/task text.
8. Archived docs, only when explicitly referenced by canonical docs.
9. Reasonable inference from nearby patterns.

If these conflict, call out the conflict and prefer the more specific, more recent, and safer source.

## Architecture Rules

Follow the project's existing architecture. Prefer incremental extension over replacement. Avoid broad rewrites unless the user requested a refactor.

Project-specific architecture constraints:

- `{{ARCHITECTURE_CONSTRAINT_1}}`
- `{{ARCHITECTURE_CONSTRAINT_2}}`
- `{{ARCHITECTURE_CONSTRAINT_3}}`

## Data and Migration Rules

Preserve existing data unless destructive changes are explicitly allowed. Inspect existing models and migrations before changing schemas, migrations, seed data, or persistence behavior.

Project-specific data rules:

- `{{DATA_RULE_1}}`
- `{{DATA_RULE_2}}`
- `{{DATA_RULE_3}}`

## API and Contract Rules

Preserve backward compatibility unless explicitly told otherwise. Update shared types, validation, tests, and docs together when contracts change.

Project-specific contract rules:

- `{{CONTRACT_RULE_1}}`
- `{{CONTRACT_RULE_2}}`

## UI/UX Rules

Follow existing component and styling patterns. Preserve user-entered data. Make loading, success, error, and empty states explicit.

Project-specific UX rules:

- `{{UX_RULE_1}}`
- `{{UX_RULE_2}}`
- `{{UX_RULE_3}}`

## AI / Automation Rules

Keep AI outputs reviewable by the user. Preserve traceability to source material where applicable. Do not fabricate facts or automate irreversible user-facing actions without review.

Project-specific AI rules:

- `{{AI_RULE_1}}`
- `{{AI_RULE_2}}`
- `{{AI_RULE_3}}`

## Security and Privacy Rules

Never commit secrets, weaken authentication, bypass validation, expose sensitive data, add third-party services without approval, or change security-sensitive behavior without calling it out.

Project-specific security/privacy rules:

- `{{SECURITY_RULE_1}}`
- `{{SECURITY_RULE_2}}`
- `{{SECURITY_RULE_3}}`

## Documentation Expectations

Update docs when changes affect product behavior, user workflows, API contracts, data models, setup, commands, environment variables, architecture, layer status, or roadmap assumptions.

Project-specific docs to keep aligned:

- `{{DOC_PATH_1}}`
- `{{DOC_PATH_2}}`
- `{{DOC_PATH_3}}`

## Stop Conditions

Stop and ask before:

- Destructive schema or data changes unless the project explicitly allows them.
- Changing auth/session/ownership rules.
- Changing public API contracts in a breaking way.
- Adding paid services or external integrations.
- Introducing new production dependencies.
- Removing major existing functionality.
- Replacing established architecture.
- Implementing unclear business rules with material product impact.
- Treating archived docs as current source truth.
- Weakening privacy, traceability, auditability, or security controls.

Project-specific stop conditions:

- `{{STOP_CONDITION_1}}`
- `{{STOP_CONDITION_2}}`
- `{{STOP_CONDITION_3}}`

## Completion Requirements

A task is complete when the requested behavior is implemented, relevant checks were run or explained, docs were updated if needed, risks and follow-ups are called out, and Validation/Handoff includes follow-up LEAP Recon, LEAP Prompt, or LEAP LHS recommendations when needed.

<!-- LEAP_MASTER_REPO_SECTION_END -->

<!-- LEAP_PROJECT_SECTION_END -->

<!-- LEAP_LOCAL_OVERRIDES_BEGIN -->

<!--
Optional local team or developer-specific notes go here.
Keep durable project guidance in the editable repository section above.
-->

<!-- LEAP_LOCAL_OVERRIDES_END -->
