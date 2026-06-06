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
