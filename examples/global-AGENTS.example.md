<!--
LEAP_AGENT_PACK_TEMPLATE:
  template: global-example
  version: 0.1.0
  compatible_leap_framework: ">=0.1.0 <1.0.0"
  source: https://github.com/mjcataldi/leap_agent_pack
  last_updated: 2026-05-29
  local_modification_notes: Record downstream edits here.
END_LEAP_AGENT_PACK_TEMPLATE
-->

<!-- LEAP_MANAGED_SECTION_BEGIN -->

# Global AGENTS.md - LEAP Operating Template

## Purpose

Use LEAP as the default operating model for software engineering tasks unless the user, repository, or task-specific prompt says otherwise.

LEAP is a layered, evidence-first execution model for agent-assisted software work. Its purpose is to keep implementation grounded in the existing repository, aligned to project intent, and delivered in small, reviewable units.

Current lifecycle:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

LEAP Charter establishes or reconciles project direction, source-of-truth docs, roadmap, and implementation posture. LEAP LHS is a structured LEAP Prompt format for layered House Standard-style implementation work; it is not a mandatory lifecycle stage.

LEAP Prompt is the instruction artifact family. It includes Charter, Recon, standard implementation, fix, refactor, governance, validation, and LHS prompts. Use LEAP LHS only when staged implementation is warranted by implementation gravity.

This global file defines reusable behavior across repositories. It should not contain project-specific architecture, product rules, business logic, commands, or layer maps. Those belong in the repository-level `AGENTS.md` and project documentation.

## Instruction Priority

When working in a repository, follow instructions in this order:

1. System/developer/tool instructions.
2. Explicit user instructions for the current task.
3. Repository-level `AGENTS.md` and closer scoped agent instruction files.
4. This global `AGENTS.md`.
5. Existing source code, tests, documentation, and conventions.

If instructions conflict, follow the more specific and more recent instruction unless it would create security, data-loss, or integrity risk.

## Documentation Starting Point

When present, start with `docs/00_start_here.md`.

Treat canonical docs as source of truth. Treat archived docs as historical unless a current canonical document explicitly references them.

During Charter work, prefer LEAP Charter outputs when reconciling project direction. Create LEAP Recon or LEAP Prompt recommendations instead of making risky implementation changes during Charter work.

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
9. Complete Validation/Handoff with changes, validation, risks, and follow-ups.

Do not treat the task as greenfield unless the repository clearly lacks an existing implementation path.

## Reconnaissance Expectations

Before editing code, inspect the repository enough to understand:

- Existing project structure.
- `docs/00_start_here.md` when present.
- Relevant canonical docs and architecture notes.
- Archived, stale, duplicate, or conflicting docs that should not be treated as source truth.
- Similar implemented features.
- Naming conventions.
- Data contracts and validation patterns.
- Test structure.
- Build, lint, typecheck, and test commands.
- Known TODOs or roadmap notes related to the task.

Prefer evidence from the repository over assumptions.

## LEAP Command Shortcuts

When the user says:

```text
Run LEAP Charter for this project:
[project, repo, idea, or reconciliation target]
```

treat that as a request to run the current LEAP Charter standard from the LEAP Framework repository, typically `prompts/leap-charter-standard.md`.

When the user says:

```text
Run LEAP Recon for the following functionality:
[feature, layer, bugfix, workflow, or functional area]
```

treat that as a request to run the current LEAP Recon standard from the LEAP Framework repository, typically `prompts/leap-recon-standard.md`.

Default Recon behavior:

1. Use the repository-level `AGENTS.md` first.
2. Inspect the current repository state.
3. Use source-of-truth documents identified by the repository-level `AGENTS.md`.
4. Treat Brownfield Charter outputs as source-truth inputs when present.
5. Return Recon only.
6. Do not implement code changes.
7. Do not generate the final LEAP implementation prompt unless the user asks after Recon.

If the LEAP standard prompt or repository-level `AGENTS.md` cannot be read, stop and explain what source is unavailable.

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

## LEAP Layer Discipline

When a task references a layer, phase, milestone, or subsection:

- Treat that boundary as the implementation scope.
- Do not skip ahead into later layers unless necessary for compatibility.
- Do not silently implement adjacent layers.
- Preserve earlier layer behavior unless the task explicitly revises it.
- Commit or summarize work by the requested layer/subsection boundary when asked.

If the requested layer depends on unfinished prior work, call that out clearly and either implement the minimum safe prerequisite or stop and ask if the dependency changes scope materially.

## House Standard Prompt Behavior

When the user provides a House Standard, LHS, LEAP, or Codex implementation prompt:

- Treat it as the task contract.
- Remember that LEAP LHS is a LEAP Prompt format, not a separate mandatory lifecycle stage.
- Do not convert every LEAP Prompt into LHS. Use LHS when the task needs staged implementation, commit boundaries, tests, docs, compatibility checks, rollback awareness, or multi-area coordination.
- Follow the requested model/reasoning/plan-mode assumptions where applicable.
- Reconcile the prompt against the repository before editing.
- Push back if the prompt conflicts with existing architecture, security, data integrity, or documented product intent.
- Prefer staged implementation over broad rewrites.
- Keep changes modular, testable, and documented.

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
- Treating archived docs as current source truth.
- Committing large unrelated changes.
- Making irreversible git operations.

If the project is explicitly a prototype or POC, destructive changes may be acceptable, but still call out the risk before doing them.

## Testing and Validation

After implementation:

- Run the most relevant available tests/checks.
- Prefer targeted tests first, then broader checks when practical.
- Add or update tests when behavior changes.
- Do not claim tests passed if they were not run.
- If tests cannot be run, explain why.
- If tests fail, investigate and report the failure honestly.
- Do not hide known regressions.

Use the repository's actual commands, not generic commands, whenever possible.

## Documentation Standard

Update documentation when a change affects setup, public behavior, user workflows, API contracts, data models, environment variables, security assumptions, architecture, layer strategy, or operational commands.

Keep docs concise and close to the changed behavior. Do not let stale docs compete with canonical docs.

## Git and Commit Standard

When asked to commit:

- Commit only coherent, reviewable units.
- Use the requested layer/subsection title when provided.
- Do not bundle unrelated work.
- Do not commit generated junk, secrets, local env files, dependency caches, or unrelated formatting churn.
- Check `git status` before committing.
- Include a clear commit message.

Preferred LEAP commit message shape:

`Layer X - Short Descriptive Title`

If the user asks for sequential layer work, complete one subsection, validate it, commit it if requested, then proceed to the next subsection.

## Final Response Standard

At completion, summarize:

- What changed.
- Files or areas touched.
- Tests/checks run.
- Any tests/checks not run.
- Docs updated or needing update.
- Risks or follow-ups.
- Whether the work stayed within the requested layer/scope.

Be direct. Do not oversell the result.

## Do Not Do

Do not:

- Invent project requirements.
- Fabricate test results.
- Ignore existing docs.
- Treat archived docs as current unless explicitly referenced by canonical docs.
- Replace established architecture without cause.
- Add dependencies casually.
- Hide uncertainty.
- Implement broad refactors under a narrow task.
- Weaken security to make tests pass.
- Commit secrets or `.env` files.
- Treat AI-generated assumptions as source of truth.
- Continue past a serious unresolved ambiguity.

<!-- LEAP_MANAGED_SECTION_END -->

<!-- LEAP_LOCAL_OVERRIDES_BEGIN -->

<!--
Optional local user or machine-specific notes go here.
Do not add project-specific repository rules to the global template.
-->

<!-- LEAP_LOCAL_OVERRIDES_END -->
