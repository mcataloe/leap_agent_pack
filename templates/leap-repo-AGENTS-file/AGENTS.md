# Repository AGENTS.md — LEAP Project Template

## Project Identity

This repository uses LEAP for agent-assisted software delivery.

LEAP work must be grounded in the repository’s actual code, tests, documentation, architecture, and product intent. Do not treat prompts as permission to bypass established project rules.

Project name:

`{{PROJECT_NAME}}`

Project summary:

`{{ONE_PARAGRAPH_PROJECT_DESCRIPTION}}`

## LEAP Baseline State

Use this section during LEAP Recon to decide whether the project baseline is fresh enough for focused investigation. This is a signal, not a hard gate.

| Item | Value |
| --- | --- |
| Baseline record | Inline in `AGENTS.md` |
| Last full reconcile | `{{YYYY-MM-DD_OR_NEVER}}` |
| Last reconcile mode | `{{Brownfield Charter / LEAP Governance / Manual / Never}}` |
| Current source-truth entry point | `{{PATH_TO_SOURCE_TRUTH_ENTRYPOINT}}` |
| Canonical docs location | `{{PATH_TO_CANONICAL_DOCS}}` |
| Archive location | `{{PATH_TO_ARCHIVE_DOCS_OR_NA}}` |
| Gap register / known drift | `{{PATH_TO_GAP_REGISTER_OR_NONE}}` |
| Baseline confidence | `{{High / Medium / Low / Unknown}}` |
| Reconcile triggers | `{{MAJOR_ROADMAP_CHANGE; ARCHITECTURE_PIVOT; SOURCE_TRUTH_CONFLICT; STALE_AGENTS_MD; LARGE_NEW_LAYER; ETC.}}` |

Update this section only after a full Brownfield Charter, LEAP Governance pass, major source-truth reconciliation, or intentional manual baseline update. Do not update it for every small feature or documentation edit.

If `leap.baseline.yaml` exists, use this compact pointer form instead and treat that file as the canonical machine-readable baseline record:

| Item | Value |
| --- | --- |
| Baseline record | `leap.baseline.yaml` |
| Last full reconcile | `{{YYYY-MM-DD_OR_NEVER}}` |
| Last reconcile mode | `{{Brownfield Charter / LEAP Governance / Manual / Never}}` |
| Current source-truth entry point | `{{PATH_TO_SOURCE_TRUTH_ENTRYPOINT}}` |
| Baseline confidence | `{{High / Medium / Low / Unknown}}` |
| Known drift | See `leap.baseline.yaml` |
| Reconcile triggers | See `leap.baseline.yaml` |

Primary product/architecture docs:

- `{{PATH_TO_PRIMARY_STRATEGY_DOC}}`
- `{{PATH_TO_ARCHITECTURE_DOCS}}`
- `{{PATH_TO_LAYER_OR_ROADMAP_DOCS}}`
- `{{PATH_TO_API_OR_DATA_CONTRACT_DOCS}}`

Read the relevant docs before implementing layer, architecture, workflow, data model, or user-facing changes.

---

## Repository Layout

Update this section to match the actual repository.

- `{{FRONTEND_PATH}}` — Frontend application.
- `{{BACKEND_PATH}}` — API/backend service.
- `{{SHARED_PATH}}` — Shared types, schemas, utilities, or contracts.
- `{{DOCS_PATH}}` — Product, architecture, LEAP, and roadmap documentation.
- `{{TESTS_PATH}}` — Test suites.
- `{{SCRIPTS_PATH}}` — Development and operational scripts.
- `{{INFRA_PATH}}` — Infrastructure-as-code or deployment configuration.

If the repository structure changes, update this section.

---

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

---

## Setup Commands

Use the repository’s existing setup process.

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

---

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

---

## LEAP Project Rules

This repository should be implemented in bounded LEAP units.

When a task references a layer, phase, subsection, milestone, or roadmap item:

1. Locate the corresponding documentation.
2. Confirm the existing implementation state.
3. Identify affected models, routes, services, components, tests, and docs.
4. Implement only the requested layer/subsection unless a prerequisite is required.
5. Preserve compatibility with completed prior layers.
6. Update relevant tests and docs.
7. Summarize remaining gaps.

Do not skip ahead into later layers unless the user explicitly asks.

During LEAP Recon, perform a lightweight Baseline Freshness Check before focused investigation:

- Check the LEAP Baseline State table if present.
- If `leap.baseline.yaml` exists, use it as the canonical machine-readable baseline record and treat this table as a quick summary only.
- Do not treat an old date as an automatic blocker.
- Do not treat a recent date as proof that source truth is correct.
- Use baseline metadata as a signal, then inspect relevant repo/docs evidence.
- If baseline metadata is missing, continue normal source-truth inspection and recommend adding it when appropriate.
- Do not update the AGENTS.md Baseline State table or `leap.baseline.yaml` unless the task explicitly performs or confirms a full reconciliation, governance pass, or baseline update.
- If the baseline is fresh enough, continue Recon normally.
- If minor drift exists, continue Recon, disclose the limitation, and recommend follow-up cleanup if useful.
- If material drift exists, ask whether to run Brownfield Charter or LEAP Governance now, continue with limited scope/confidence, or defer reconciliation.
- If source-truth conflict would make Recon unsafe or misleading, stop and recommend reconciliation before proceeding.

---

## Project Source of Truth

Use this order of truth when making decisions:

1. Explicit user instruction for the current task.
2. Current repository code and tests.
3. Repository `AGENTS.md` and scoped `AGENTS.md` / `AGENTS.override.md` files.
4. Product strategy and architecture docs.
5. Layer/roadmap docs.
6. README and setup docs.
7. Existing issue/task text.
8. Reasonable inference from nearby patterns.

If these conflict, call out the conflict and prefer the more specific, more recent, and safer source.

---

## Architecture Rules

Follow the project’s existing architecture.

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

---

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

---

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

---

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

---

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

---

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

---

## Testing Expectations

When behavior changes:

- Add or update tests.
- Prefer tests near the changed behavior.
- Cover success, failure, and edge cases where practical.
- Use existing test helpers and factories.
- Do not rewrite test infrastructure unless requested.
- Do not delete failing tests without explaining why.

Testing priorities:

1. Contract/schema tests.
2. Service/domain logic tests.
3. API route tests.
4. UI behavior tests.
5. Regression tests for bugs.
6. Smoke tests for critical workflows.

---

## Documentation Expectations

Update docs when changes affect:

- Product behavior.
- User workflows.
- API contracts.
- Data models.
- Setup.
- Commands.
- Environment variables.
- Architecture.
- Layer status.
- Roadmap assumptions.

Project-specific docs to keep aligned:

- `{{DOC_PATH_1}}`
- `{{DOC_PATH_2}}`
- `{{DOC_PATH_3}}`

---

## Commit and Branch Expectations

When the user asks for commits:

- Keep commits scoped and reviewable.
- Use the layer/subsection name in the commit message when available.
- Do not combine unrelated layers.
- Check `git status` before committing.
- Include tests/docs in the same commit when they belong to the change.

Preferred LEAP commit message:

`{{LAYER_OR_PHASE}} — {{SUBSECTION_OR_FEATURE_TITLE}}`

Examples:

`Layer 4B — Application Timeline and Notes Workflow`

`Layer 6C — Versioning, Review, and Submitted-State Workflow`

---

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
- Weakening privacy, traceability, auditability, or security controls.

Project-specific stop conditions:

- `{{STOP_CONDITION_1}}`
- `{{STOP_CONDITION_2}}`
- `{{STOP_CONDITION_3}}`

---

## Completion Requirements

A task is complete when:

- The requested behavior is implemented.
- The change follows existing project patterns.
- Relevant tests/checks were run or clearly explained.
- Docs were updated if needed.
- Risks and follow-ups are called out.
- The implementation stays within the requested LEAP layer/scope.

Final response should include:

- Summary of changes.
- Files/areas changed.
- Tests/checks run.
- Tests/checks not run.
- Known risks or follow-ups.
