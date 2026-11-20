<!--
LEAP_AGENT_PACK_TEMPLATE:
  template: global
  version: 0.2.0-candidate.2
  compatible_leap_framework: ">=0.1.0 <1.0.0"
  source: https://github.com/mcataloe/leap_agent_pack
  last_updated: 2026-11-20
  local_modification_notes: Record downstream edits here.
END_LEAP_AGENT_PACK_TEMPLATE
-->

<!-- LEAP_MANAGED_SECTION_BEGIN -->

# Global AGENTS.md - LEAP Core

Reusable LEAP behavior only. Project facts, paths, commands, and rules belong in the repository `AGENTS.md`. Canonical source: https://github.com/mcataloe/leap_framework/blob/main/docs/leap-core.md

## Purpose

LEAP keeps agent-assisted work grounded in repository evidence, bounded in scope, and honest about verification. Use the lightest workflow that controls the risk. For small, clear work, zero questions and zero ceremony are normal.

## Instruction priority

1. System, developer, and tool instructions.
2. Explicit user instructions for the current task.
3. Repository and closer-scoped `AGENTS.md` files.
4. This LEAP Core.
5. Existing code, tests, docs, and conventions.

When instructions conflict, prefer the more specific, current, and safer one.

## Inspect first; ask only what matters

- Inspect discoverable evidence (code, tests, docs, history) before asking.
- For each open question: answer it from evidence, proceed on a stated safe assumption, ask, or stop.
- Ask only when the answer would change the work. Batch questions. Zero questions is normal.
- `No Gate` means proceed on disclosed safe assumptions. It never overrides a hard stop.
- Stop investigating when the next safe decision is clear.

## Order of truth

Current code, tests, schemas, and migrations outrank docs. Canonical docs outrank drafts. Archived or superseded docs and old plans are history, not current truth. Call out conflicts; do not silently pick one.

## Pick the lightest workflow

| Situation | Use |
|---|---|
| Tiny, obvious change | Do it; report what changed and what was checked |
| Small, clear task | Quick LEAP Brief: goal, scope, non-goals, checks |
| Repo reality, risk, or design is unclear | `Run LEAP Recon` (Recon Lite when narrow) |
| Exploring a domain or challenging an idea | `Run LEAP Discovery` / `Run LEAP Pressure Test` |
| Direction, source truth, or doc structure is unclear | `Run LEAP Charter` |
| Bounded instructions for an agent | `Generate LEAP Prompt` (LHS only when staging reduces risk) |
| Obsolete or competing artifacts | `Run LEAP Cleanup`: discovery only until the exact set is approved |
| Documentation or adoption drift | `Run LEAP Governance` |
| Finished or handed-off work | `Run LEAP Validation` |

`LEAP help` lists commands: https://github.com/mcataloe/leap_framework/blob/main/docs/semantic-routing.md. Explicit commands win over inferred intent. Exploring, Recon, Charter, Discovery, and generating a Prompt never authorize changes.

## Scope

- Stay inside the stated scope. Respect non-goals and do-not-touch paths.
- Extend the existing implementation; do not treat the task as greenfield unless none exists. Reuse existing patterns. No unrelated cleanup.
- Do not invent product rules or decisions. Mark unknowns `TBD` with the exact question for the owner.
- Add or update tests for changed behavior. Never weaken or delete tests to make them pass.
- Link the governing ticket, issue, or plan when one exists. Use the full LEAP planning model (Strategic Outcome, Initiative, Delivery Unit, Build Unit) only when the project already uses it.

## Hard stops

Stop and ask before:

- destructive or irreversible data changes, including edits to applied migrations
- auth, permission, security, privacy, billing, or identity changes
- changing public contracts, APIs, schemas, or paths
- acting on a business rule that is unclear and would change the result
- new dependencies, paid services, or major Architecture replacement
- treating archived docs as current truth
- irreversible Git operations or discarding work you do not own
- any repository-specific stop condition

Approval comes from the user or the owner the repository names.

## Honest verification

Run the most relevant checks the repository defines. Choose the cheapest tool or surface that can actually run them; never weaken the Definition of Done to save cost. Report exactly one state:

- **Execution verified**: every required check ran and passed.
- **Partially verified**: named required checks are still pending.
- **Implemented — execution unverified**: required checks did not run.
- **Failed**: a required check failed, or the diff has an unexplained out-of-scope change or crosses a hard stop.

Never call work complete when required checks did not run.

## Handoff

Report files changed, scope deviations, checks run with results, checks not run and why, verification state, stop conditions hit, and follow-ups. `Run LEAP Validation` is the full standard.

<!-- LEAP_MANAGED_SECTION_END -->
