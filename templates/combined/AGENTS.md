<!--
LEAP_AGENT_PACK_TEMPLATE:
  template: combined
  version: 0.2.0-candidate.2
  compatible_leap_framework: ">=0.1.0 <1.0.0"
  source: https://github.com/mcataloe/leap_agent_pack
  last_updated: 2026-10-21
  local_modification_notes: Record downstream edits here.
END_LEAP_AGENT_PACK_TEMPLATE
-->

# AGENTS.md - LEAP Combined Template

One file with LEAP Core and project guidance. Do not edit the managed section during population. Fill only the project section. Preserve all markers.

<!-- LEAP_MANAGED_SECTION_BEGIN -->

# LEAP Core

Canonical source: https://github.com/mcataloe/leap_framework/blob/main/docs/leap-core.md

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
- Reuse existing patterns. No unrelated cleanup.
- Do not invent product rules or decisions. Mark unknowns `TBD` with the exact question for the owner.
- Never weaken or delete tests to make them pass.
- Link the governing ticket, issue, or plan when one exists. Use the full LEAP planning model (Strategic Outcome, Initiative, Delivery Unit, Build Unit) only when the project already uses it.

## Hard stops

Stop and ask before:

- destructive or irreversible data changes, including edits to applied migrations
- auth, permission, security, privacy, billing, or identity changes
- breaking public contracts, APIs, schemas, or paths
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
- **Failed**: a required check failed, or the diff exceeds scope or crosses a hard stop.

Never call work complete when required checks did not run.

## Handoff

Report files changed, scope deviations, checks run with results, checks not run and why, verification state, stop conditions hit, and follow-ups. `Run LEAP Validation` is the full standard.

<!-- LEAP_MANAGED_SECTION_END -->

<!-- LEAP_PROJECT_SECTION_BEGIN -->

# Project Guidance

<!-- Keep this section under about 800 words. It loads every session. Link to docs/ for detail. Write TBD plus the exact owner question for anything evidence does not show. -->

## Project

- Name: `{{PROJECT_NAME}}`
- Summary: `{{ONE_PARAGRAPH_PROJECT_DESCRIPTION}}`
- Start here: `{{PATH_TO_SOURCE_TRUTH_ENTRYPOINT_OR_README}}`
- Work tracking / planning sources (if any): `{{JIRA_ADO_GITHUB_PROJECT_OR_DOC_PATHS_OR_NONE}}`
- Allocation / capacity source (if any): `{{ALLOCATION_OWNER_OR_SYSTEM_OR_NONE}}`

These are pointers only. Do not copy rosters, allocations, worklogs, or accepted estimates here. For effort or delivery estimates, follow [LEAP delivery estimation](https://github.com/mcataloe/leap_framework/blob/main/docs/team-delivery-estimation.md).

## Source truth

- Canonical docs: `{{CANONICAL_DOC_PATHS}}`
- Draft, archived, or do-not-use docs: `{{NON_CANONICAL_DOC_PATHS_OR_NONE}}`
- Last reconcile: `{{YYYY-MM-DD_OR_NEVER}}` via `{{Brownfield Charter / Governance / Manual}}`; known drift: `{{PATH_OR_NONE}}`

Do not invent reconcile history.

## Layout and stack

- `{{PATH}}`: `{{PURPOSE_AND_STACK}}`
- `{{PATH}}`: `{{PURPOSE_AND_STACK}}`

## Commands

```bash
{{INSTALL_COMMAND}}
{{TEST_COMMAND}}
{{LINT_OR_TYPECHECK_COMMAND}}
{{BUILD_COMMAND}}
```

Do not invent commands. Write `TBD` for unknown ones. Name any check that needs services, credentials, or a specific environment.

## Project rules

Rules that prevent a real failure in this repository: Architecture, data and migrations, contracts, security, UX, or AI behavior. Each rule should be concrete enough to check.

- `{{PROJECT_RULE_1}}`
- `{{PROJECT_RULE_2}}`

## Project stop conditions

- `{{STOP_CONDITION_1}}`: approver `{{OWNER_OR_ROLE}}`
- `{{STOP_CONDITION_2}}`: approver `{{OWNER_OR_ROLE}}`

## Branches and commits

- `{{BRANCH_PR_OR_COMMIT_RULE_OR_TBD}}`

<!-- LEAP_PROJECT_SECTION_END -->

<!-- LEAP_LOCAL_OVERRIDES_BEGIN -->
<!-- Optional local team or developer notes. Keep durable project guidance in the project section. -->
<!-- LEAP_LOCAL_OVERRIDES_END -->
