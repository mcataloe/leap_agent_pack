<!--
LEAP_AGENT_PACK_TEMPLATE:
  template: repo-example
  version: 0.1.0
  compatible_leap_framework: ">=0.1.0 <1.0.0"
  source: https://github.com/mjcataldi/leap_agent_pack
  last_updated: 2026-05-29
  local_modification_notes: Record downstream edits here.
END_LEAP_AGENT_PACK_TEMPLATE
-->

<!-- LEAP_MANAGED_SECTION_BEGIN -->

# Repository AGENTS.md - LEAP Project Template

## Project Identity

This repository uses LEAP for agent-assisted software delivery.

LEAP work must be grounded in the repository's actual code, tests, documentation, architecture, and product intent. Do not treat prompts as permission to bypass established project rules.

Project name:

`{{PROJECT_NAME}}`

Project summary:

`{{ONE_PARAGRAPH_PROJECT_DESCRIPTION}}`

Current lifecycle:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

LEAP Charter establishes or reconciles project direction, source-of-truth docs, roadmap, and implementation posture.

LEAP LHS is a structured LEAP Prompt format for layered implementation work using the House Standard. It is not a mandatory lifecycle stage.

LEAP Prompt is the instruction artifact family. It includes Charter, Recon, standard implementation, fix, refactor, governance, validation, and LHS prompts. Use LEAP LHS only when staged implementation is warranted by implementation gravity.

<!-- LEAP_MANAGED_SECTION_END -->

<!-- LEAP_PROJECT_SECTION_BEGIN -->

## Documentation Starting Point

Start with `docs/00_start_here.md` when present.

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

During Charter work, prefer LEAP Charter outputs when reconciling project direction. Create LEAP Recon or LEAP Prompt recommendations instead of making risky implementation changes during Charter work.

Use LEAP Recon outputs for focused investigation findings. Use LEAP LHS only when the task needs staged implementation, commit boundaries, tests, docs, compatibility checks, rollback awareness, or multi-area coordination. Do not treat LHS as a mandatory stage after every LEAP Prompt.

Read the relevant docs before implementing layer, architecture, workflow, data model, or user-facing changes.

## Repository Layout

Update this section to match the actual repository.

- `{{FRONTEND_PATH}}` - Frontend application.
- `{{BACKEND_PATH}}` - API/backend service.
- `{{SHARED_PATH}}` - Shared types, schemas, utilities, or contracts.
- `{{DOCS_PATH}}` - Product, architecture, LEAP, and roadmap documentation.
- `{{TESTS_PATH}}` - Test suites.
- `{{SCRIPTS_PATH}}` - Development and operational scripts.
- `{{INFRA_PATH}}` - Infrastructure-as-code or deployment configuration.

If the repository structure changes, update this section.

## Technology Stack

Update this section to match the actual project.

- Frontend: `{{FRONTEND_STACK}}`
- Backend/API: `{{BACKEND_STACK}}`
- Database: `{{DATABASE_STACK}}`
- Infrastructure: `{{INFRA_STACK}}`
- Package manager: `{{PACKAGE_MANAGER}}`
- Test framework: `{{TEST_FRAMEWORK}}`
- Runtime versions: `{{RUNTIME_VERSIONS}}`

Use the existing stack unless the user explicitly requests evaluation or migration.

## Setup Commands

Use the repository's existing setup process.

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

Use the most relevant validation commands for the changed area.

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

If only part of the repo changed, prefer targeted checks first. Run broader checks when practical.

If a command is missing, broken, or too expensive to run, explain that in the final response.

## LEAP Project Rules

This repository should be implemented in bounded LEAP units.

When a task references a layer, phase, subsection, milestone, or roadmap item:

1. Locate the corresponding documentation.
2. Confirm the existing implementation state.
3. Identify affected models, routes, services, components, tests, and docs.
4. Implement only the requested layer/subsection unless a prerequisite is required.
5. Preserve compatibility with completed prior layers.
6. Update relevant tests and docs.
7. Complete Validation/Handoff with remaining gaps and follow-up prompt recommendations.

Do not skip ahead into later layers unless the user explicitly asks.

## Project Source of Truth

Use this order of truth when making decisions:

1. Explicit user instruction for the current task.
2. Current repository code and tests.
3. Repository `AGENTS.md` and scoped `AGENTS.md` / `AGENTS.override.md` files.
4. Canonical product strategy and architecture docs.
5. Canonical layer/roadmap docs.
6. README and setup docs.
7. Existing issue/task text.
8. Archived docs, only when explicitly referenced by canonical docs.
9. Reasonable inference from nearby patterns.

If these conflict, call out the conflict and prefer the more specific, more recent, and safer source.

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

## Architecture Rules

Follow the project's existing architecture.

Default expectations:

- Keep domain logic out of presentation-only code when possible.
- Keep API contracts explicit.
- Keep validation close to data boundaries.
- Reuse existing schema, type, and DTO patterns.
- Avoid duplicating model definitions.
- Preserve ownership and authorization boundaries.
- Keep persistence concerns isolated according to existing repository patterns.
- Prefer incremental extension over replacement.
- Avoid broad rewrites unless the user requested a refactor.

Project-specific architecture constraints:

- `{{ARCHITECTURE_CONSTRAINT_1}}`
- `{{ARCHITECTURE_CONSTRAINT_2}}`
- `{{ARCHITECTURE_CONSTRAINT_3}}`

## Data and Migration Rules

Before changing schemas, migrations, seed data, or persistence behavior:

- Inspect existing models and migrations.
- Determine whether the project is prototype, staging, or production-like.
- Preserve existing data unless destructive changes are explicitly allowed.
- Keep migrations reversible where practical.
- Update tests and docs for data model changes.
- Do not silently change identifiers, ownership semantics, or lifecycle states.

Project-specific data rules:

- `{{DATA_RULE_1}}`
- `{{DATA_RULE_2}}`
- `{{DATA_RULE_3}}`

## API and Contract Rules

When changing APIs, contracts, schemas, or shared types:

- Preserve backward compatibility unless explicitly told otherwise.
- Update shared types and validation together.
- Update API tests.
- Update docs or examples.
- Keep error responses consistent with existing patterns.
- Avoid creating parallel contract definitions.

Project-specific contract rules:

- `{{CONTRACT_RULE_1}}`
- `{{CONTRACT_RULE_2}}`

## UI/UX Rules

When changing UI:

- Follow existing component and styling patterns.
- Keep user flows calm, clear, and accessible.
- Prefer progressive disclosure over clutter.
- Preserve user-entered data.
- Make loading, success, error, and empty states explicit.
- Avoid large visual rewrites unless requested.
- Keep forms and validation behavior consistent.

Project-specific UX rules:

- `{{UX_RULE_1}}`
- `{{UX_RULE_2}}`
- `{{UX_RULE_3}}`

## AI / Automation Rules

If the project uses AI-assisted parsing, evaluation, generation, recommendations, or automation:

- Keep AI outputs reviewable by the user.
- Do not fabricate user facts, credentials, claims, experience, metrics, or decisions.
- Preserve traceability to source material where applicable.
- Distinguish generated drafts from reviewed or submitted artifacts.
- Make uncertainty visible.
- Do not automate irreversible user-facing actions without review.

Project-specific AI rules:

- `{{AI_RULE_1}}`
- `{{AI_RULE_2}}`
- `{{AI_RULE_3}}`

## Security and Privacy Rules

Never:

- Commit secrets, tokens, credentials, private keys, or `.env` files.
- Log sensitive user data unnecessarily.
- Weaken authentication or authorization.
- Bypass validation to make a test pass.
- Store sensitive data in client-visible locations.
- Add third-party services without approval.
- Change security-sensitive behavior without calling it out.

Project-specific security/privacy rules:

- `{{SECURITY_RULE_1}}`
- `{{SECURITY_RULE_2}}`
- `{{SECURITY_RULE_3}}`

## Testing Expectations

When behavior changes:

- Add or update tests.
- Prefer tests near the changed behavior.
- Cover success, failure, and edge cases where practical.
- Use existing test helpers and factories.
- Do not rewrite test infrastructure unless requested.
- Do not delete failing tests without explaining why.

## Documentation Expectations

Update docs when changes affect product behavior, user workflows, API contracts, data models, setup, commands, environment variables, architecture, layer status, or roadmap assumptions.

Project-specific docs to keep aligned:

- `{{DOC_PATH_1}}`
- `{{DOC_PATH_2}}`
- `{{DOC_PATH_3}}`

## Commit and Branch Expectations

When the user asks for commits:

- Keep commits scoped and reviewable.
- Use the layer/subsection name in the commit message when available.
- Do not combine unrelated layers.
- Check `git status` before committing.
- Include tests/docs in the same commit when they belong to the change.

Preferred LEAP commit message:

`{{LAYER_OR_PHASE}} - {{SUBSECTION_OR_FEATURE_TITLE}}`

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

A task is complete when:

- The requested behavior is implemented.
- The change follows existing project patterns.
- Relevant tests/checks were run or clearly explained.
- Docs were updated if needed.
- Risks and follow-ups are called out.
- The implementation stays within the requested LEAP layer/scope.
- Validation/Handoff includes follow-up LEAP Recon, LEAP Prompt, or LEAP LHS recommendations when needed.

Final response should include:

- Summary of changes.
- Files/areas changed.
- Tests/checks run.
- Tests/checks not run.
- Known risks or follow-ups.

<!-- LEAP_PROJECT_SECTION_END -->

<!-- LEAP_LOCAL_OVERRIDES_BEGIN -->

<!--
Optional local team or developer-specific notes go here.
Keep durable project guidance in the project section above.
-->

<!-- LEAP_LOCAL_OVERRIDES_END -->
