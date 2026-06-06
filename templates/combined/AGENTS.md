# Master Repo AGENTS.md — LEAP Local Trial Template

Use this single-file template when you want to test LEAP inside one local repository before installing a global AGENTS.md system-wide.

This file intentionally combines two scopes:

1. **Locked Global Section** — reusable LEAP operating behavior copied from the global AGENTS.md template.
2. **Editable Repository Section** — project-specific AGENTS.md content that should be populated from the current repository.

When this file is placed at the root of a repository as `AGENTS.md`, the code assistant should treat the locked global section as global LEAP behavior and the editable repository section as the repository-level AGENTS.md content.

## Local-Trial Editing Rules

- Do not edit the locked global section unless the user explicitly asks to revise LEAP global behavior.
- Do not remove or rename the section boundary markers.
- Populate only the editable repository section during repo onboarding.
- Preserve the overall two-section structure.
- If a rule in the locked global section refers to the repository-level `AGENTS.md`, interpret that as the editable repository section in this same file.
- If a rule in the editable repository section conflicts with the locked global section, prefer the repository section only for project-specific facts, commands, paths, architecture, and source-of-truth documents.
- If a conflict would create security, privacy, data-loss, or integrity risk, stop and ask.

---

<!-- LEAP_MASTER_GLOBAL_SECTION_START: DO NOT EDIT DURING REPO POPULATION -->

# Global AGENTS.md — LEAP Operating Template

## Purpose

Use LEAP as the default operating model for software engineering tasks unless the user, repository, or task-specific prompt says otherwise.

LEAP is a layered, evidence-first execution model for agent-assisted software work. Its purpose is to keep implementation grounded in the existing repository, aligned to project intent, and delivered in small, reviewable units.

This global file defines reusable behavior across repositories. It should not contain project-specific architecture, product rules, business logic, commands, or layer maps. Those belong in the repository-level `AGENTS.md` and project documentation.

---

## Instruction Priority

When working in a repository, follow instructions in this order:

1. System/developer/tool instructions.
2. Explicit user instructions for the current task.
3. Repository-level `AGENTS.md` and closer scoped agent instruction files.
4. This global `AGENTS.md`.
5. Existing source code, tests, documentation, and conventions.

If instructions conflict, follow the more specific and more recent instruction unless it would create security, data-loss, or integrity risk.

---

## Default LEAP Work Pattern

For non-trivial implementation tasks, use this sequence:

1. Understand the task.
2. Perform repository reconnaissance before editing.
3. Identify the relevant layer, subsystem, feature, route, component, service, data model, or workflow.
4. Locate existing patterns and contracts.
5. Make a concise implementation plan.
6. Implement the smallest coherent change.
7. Add or update relevant tests.
8. Run practical validation checks.
9. Summarize changes, validation, risks, and follow-ups.

Do not treat the task as greenfield unless the repository clearly lacks an existing implementation path.

---

## Reconnaissance Expectations

Before editing code, inspect the repository enough to understand:

- Existing project structure.
- Relevant docs and architecture notes.
- Similar implemented features.
- Naming conventions.
- Data contracts and validation patterns.
- Test structure.
- Build, lint, typecheck, and test commands.
- Known TODOs or roadmap notes related to the task.

Prefer evidence from the repository over assumptions.

---

## LEAP Command Shortcuts

When the user invokes a LEAP command, route it to current LEAP Framework behavior instead of responding generically. Use `docs/leap.md` as the lifecycle reference and the current prompt files when available.

| Command | Route and behavior |
| --- | --- |
| `Run LEAP Charter` | Use `prompts/leap-charter-standard.md` to establish or reconcile project direction, source truth, roadmap, baseline assumptions, and implementation posture. |
| `Run LEAP Recon` | Use `prompts/leap-recon-standard.md` to investigate a focused feature, risk, layer, dependency, contract, repo area, or architecture question before implementation planning. |
| `Generate LEAP Prompt` | Use `prompts/leap-prompt-standard.md` only after source truth, repo reality, scope, validation, stop conditions, and execution configuration are clear enough. |
| `Run LEAP Prompt` | Execute or apply an already-approved LEAP Prompt according to its stated scope, constraints, validation, and stop conditions. |
| `Generate LEAP LHS` | Generate a staged LEAP Prompt format only when implementation gravity warrants Build Units; LHS is not a mandatory lifecycle phase. |
| `Run LEAP LHS` | Execute or apply an approved LHS prompt in Build Unit sequence with its validation and stop conditions. |
| `Run LEAP Governance` | Use `prompts/leap-governance-pass-standard.md` for source-truth, framework, prompt-library, adoption, terminology, or docs drift. |
| `Run LEAP Validation` | Verify completed work against scope, tests/checks, docs, acceptance criteria, and stop conditions. |
| `Run LEAP Handoff` | Summarize completed work, unresolved risks, validation status, deviations, and recommended follow-up. |

Default Recon behavior:

1. Use the repository-level `AGENTS.md` first.
2. Inspect the current repository state.
3. Use the current LEAP Recon Standard Operational Prompt from the LEAP framework repository:
   `/prompts/leap-recon-standard.md`
4. Use source-of-truth documents identified by the repository-level `AGENTS.md`.
5. Perform the Recon Baseline Freshness Check using repository AGENTS.md, baseline metadata if present, source-truth docs, and relevant repo reality.
6. Return Recon only.
7. Do not implement code changes.
8. Do not generate the final LEAP implementation prompt unless the user asks after Recon.

LEAP Charter is not required before every Recon. If the baseline is fresh enough, continue Recon. If minor drift exists, continue and disclose the limitation. If material drift exists, ask whether to run Brownfield Charter or LEAP Governance, continue with limited scope, or defer reconciliation. If source-truth conflict would make Recon unsafe or misleading, stop and recommend reconciliation.

If the LEAP standard prompt, `docs/leap.md`, or repository-level `AGENTS.md` cannot be read, stop and explain what source is unavailable.

The user should not need to paste full framework prompt standards when using standard AGENTS.md behavior.

---

## Planning Standard

For meaningful work, produce a short plan before implementation.

A useful plan should identify:

- The likely files or modules to inspect/change.
- The implementation sequence.
- Tests or checks to run.
- Compatibility concerns.
- Documentation updates.
- Stop conditions or decisions that require the user.

Avoid excessive planning for small, obvious changes.

---

## Implementation Standard

When changing code:

- Reuse existing patterns before introducing new ones.
- Keep changes scoped to the requested task.
- Prefer small, reviewable units.
- Preserve backward compatibility unless explicitly told otherwise.
- Do not rename public interfaces without a clear reason.
- Do not introduce new dependencies without justification.
- Do not mix unrelated refactors into feature work.
- Do not duplicate business logic, schemas, or validation rules.
- Prefer clear, boring, maintainable code over clever code.
- Keep behavior deterministic where practical.
- Handle errors explicitly.
- Preserve existing security, privacy, and auditability boundaries.

---

## LEAP Layer Discipline

When a task references a layer, phase, milestone, or subsection:

- Treat that boundary as the implementation scope.
- Do not skip ahead into later layers unless necessary for compatibility.
- Do not silently implement adjacent layers.
- Preserve earlier layer behavior unless the task explicitly revises it.
- Commit or summarize work by the requested layer/subsection boundary when asked.

If the requested layer depends on unfinished prior work, call that out clearly and either:

- implement the minimum safe prerequisite, or
- stop and ask if the dependency changes scope materially.

---

## House Standard Prompt Behavior

When the user provides a House Standard, LHS, LEAP, or Codex implementation prompt:

- Treat it as the task contract.
- Follow the requested model/reasoning/plan-mode assumptions where applicable.
- Reconcile the prompt against the repository before editing.
- Push back if the prompt conflicts with existing architecture, security, data integrity, or documented product intent.
- Prefer staged implementation over broad rewrites.
- Keep changes modular, testable, and documented.

---

## Questions and Stop Conditions

Ask a question before proceeding only when moving forward would create meaningful risk.

Stop and ask before:

- Destructive production-like data changes.
- Dropping or overwriting user data.
- Weakening authentication or authorization.
- Exposing secrets or credentials.
- Adding paid external services.
- Adding major production dependencies.
- Changing public API contracts without migration.
- Replacing major architecture instead of extending it.
- Guessing business rules that materially affect user-facing behavior.
- Implementing a security-sensitive shortcut.
- Committing large unrelated changes.
- Making irreversible git operations.

If the project is explicitly a prototype or POC, destructive changes may be acceptable, but still call out the risk before doing them.

---

## Testing and Validation

After implementation:

- Run the most relevant available tests/checks.
- Prefer targeted tests first, then broader checks when practical.
- Add or update tests when behavior changes.
- Do not claim tests passed if they were not run.
- If tests cannot be run, explain why.
- If tests fail, investigate and report the failure honestly.
- Do not hide known regressions.

Common validation categories:

- Unit tests.
- Integration/API tests.
- Typecheck.
- Lint.
- Build.
- Formatting.
- Migration checks.
- Manual smoke test notes.

Use the repository’s actual commands, not generic commands, whenever possible.

---

## Documentation Standard

Update documentation when a change affects:

- Setup or local development.
- Public behavior.
- User workflows.
- API contracts.
- Data models.
- Environment variables.
- Security assumptions.
- Architecture.
- Layer strategy.
- Operational commands.

Keep docs concise and close to the changed behavior.

---

## Git and Commit Standard

When asked to commit:

- Commit only coherent, reviewable units.
- Use the requested layer/subsection title when provided.
- Do not bundle unrelated work.
- Do not commit generated junk, secrets, local env files, dependency caches, or unrelated formatting churn.
- Check `git status` before committing.
- Include a clear commit message.

Preferred LEAP commit message shape:

`Layer X — Short Descriptive Title`

Examples:

`Layer 6C — Versioning, Review, and Submitted-State Workflow`

`Layer 8A — Integration Provider Contracts`

If the user asks for sequential layer work, complete one subsection, validate it, commit it if requested, then proceed to the next subsection.

---

## Final Response Standard

At completion, summarize:

- What changed.
- Files or areas touched.
- Tests/checks run.
- Any tests/checks not run.
- Risks or follow-ups.
- Whether the work stayed within the requested layer/scope.

Be direct. Do not oversell the result.

---

## Do Not Do

Do not:

- Invent project requirements.
- Fabricate test results.
- Ignore existing docs.
- Replace established architecture without cause.
- Add dependencies casually.
- Hide uncertainty.
- Implement broad refactors under a narrow task.
- Weaken security to make tests pass.
- Commit secrets or `.env` files.
- Treat AI-generated assumptions as source of truth.
- Continue past a serious unresolved ambiguity.


<!-- LEAP_MASTER_GLOBAL_SECTION_END -->

---

<!-- LEAP_MASTER_REPO_SECTION_START: EDIT THIS SECTION ONLY DURING REPO POPULATION -->

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

## Dependency & Contract Recon Adapter

During LEAP Recon, inspect dependency and contract evidence when the task touches integrations, APIs, SDKs, generated clients, packages, platform services, events, identity, payments, or infrastructure dependencies.

Relevant evidence can include `leap.dependencies.yaml`, OpenAPI, AsyncAPI, protobuf, GraphQL schemas, provider repo URLs, docs URLs, SDKs, generated clients, package manifests, integration tests, mocks, Pact or WireMock files, infrastructure service dependencies, event topics, queues, identity providers, and payment providers.

Dependency tracking is not mandatory for tiny projects. If `leap.dependencies.yaml` is missing, treat that as a limitation and possible follow-up, not an automatic blocker. Do not claim ownership of provider repos or external contracts; report incomplete evidence instead of guessing.

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


<!-- LEAP_MASTER_REPO_SECTION_END -->
