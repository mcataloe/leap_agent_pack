<!--
LEAP_AGENT_PACK_TEMPLATE:
  template: global
  version: 0.2.0-candidate
  compatible_leap_framework: ">=0.1.0 <1.0.0"
  source: https://github.com/mcataloe/leap_agent_pack
  last_updated: 2026-07-01
  local_modification_notes: Record downstream edits here.
END_LEAP_AGENT_PACK_TEMPLATE
-->

<!-- LEAP_MANAGED_SECTION_BEGIN -->

# Global AGENTS.md - LEAP Operating Template

## Purpose

Use LEAP as the default operating model for software-engineering work unless the user, repository, or task-specific Prompt says otherwise.

LEAP is evidence-first and documentation-aware. It keeps implementation grounded in repository reality, project intent, explicit planning boundaries, and verifiable completion.

Current lifecycle:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

LEAP LHS is the Layered House Standard Prompt format for staged implementation. It is not a lifecycle phase and does not define a project's strategic hierarchy.

## Canonical project-documentation model

Use this hierarchy when strategic context is material:

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

Treat these as separate supporting views:

```text
Roadmap      = timing, priority, milestones, dependencies, release targets, status, parallelism
Domain Map   = persistent business, responsibility, ownership, or technical boundaries
Architecture = technical structure and qualified technical Layers
```

Rules:

- Several Initiatives may run in parallel.
- A Roadmap schedules and prioritizes work; it does not permanently own Initiative identity.
- Initiatives and Domains have a many-to-many relationship.
- A Delivery Unit is a releasable, deployable, enabled, adoptable, or demonstrable increment.
- Delivery Unit may be collapsed for small work when one Build Unit delivers the complete Initiative outcome.
- A Build Unit is bounded implementation that can be implemented, tested, reviewed, and usually committed independently.
- A Build Unit is not necessarily independently deployable or independently valuable to an end user.

Generic unqualified project-planning `Layer` is legacy-compatible and deprecated as the preferred planning level.

Preserve:

- Layered Execution & Alignment Protocol
- Layered House Standard
- LEAP LHS
- qualified Architecture Layers
- public paths
- historical and compatibility references

Classify a legacy Layer before migration as Initiative, Delivery Unit, Build Unit, Domain, Architecture Layer, Phase, or mixed / unclear.

## Global-versus-repository boundary

This global file contains reusable behavior only.

Do not add project-specific:

- product facts
- repositories
- source-truth paths
- architecture decisions
- setup commands
- validation commands
- business rules
- environment details
- credentials or secrets
- Initiative, Roadmap, Domain, Delivery Unit, or Build Unit records

Those belong in the repository-level `AGENTS.md` and project documentation.

## Instruction priority

Follow instructions in this order:

1. System, developer, and tool instructions.
2. Explicit user instructions for the current task.
3. Repository-level `AGENTS.md` and closer-scoped agent instruction files.
4. This global `AGENTS.md`.
5. Existing source code, tests, documentation, and conventions.

When instructions conflict, prefer the more specific, current, and safer instruction. Stop when the conflict materially affects source truth, product behavior, Architecture, data, security, compatibility, or validation.

## Documentation starting point

When present, start with `docs/00_start_here.md`.

Treat canonical docs as source truth. Treat Draft, stale, archived, superseded, and do-not-use docs according to repository guidance.

During Charter work, establish or reconcile Mission, Strategic Outcomes, Initiative identity, Roadmap posture, Domains, Architecture, source truth, and implementation readiness.

During Recon, inspect repository reality before implementation planning.

## Default work pattern

For non-trivial work:

1. Understand the requested outcome.
2. Inspect repository and documentation evidence before editing.
3. Identify Strategic Outcome and Initiative when material.
4. Identify Roadmap placement only as planning context.
5. Identify affected Domains and Architecture areas.
6. Determine whether the task is Initiative-sized, Delivery-Unit-sized, Build-Unit-sized, Domain-oriented, Architecture-oriented, a Phase, or an ambiguous legacy Layer.
7. Define a bounded Build Unit or task.
8. Make the smallest coherent change.
9. Add or update relevant tests and docs.
10. Run practical validation.
11. Complete Validation/Handoff.

Do not treat work as greenfield unless repository evidence supports that conclusion.

## Reconnaissance expectations

Inspect enough evidence to understand:

- repository structure
- canonical and supporting docs
- Strategic Outcomes and Initiative registry, when present
- active Roadmap
- Domain map
- Architecture docs
- Delivery Unit and Build Unit records
- legacy Layer docs requiring classification
- similar implemented behavior
- APIs, schemas, events, data models, and contracts
- tests and validation commands
- branches, worktrees, and pull requests
- dependency and contract evidence
- known drift or stale assumptions

Prefer evidence over inference. Label material assumptions.

## LEAP command routing

| Command | Expected behavior |
|---|---|
| `Run LEAP Charter` | Establish or reconcile Mission, Strategic Outcomes, Initiative identity, Roadmap, Domains, Architecture, source truth, and implementation posture. |
| `Run LEAP Recon` | Investigate a focused Strategic Outcome, Initiative, Delivery Unit, Build Unit, Domain, Architecture area, feature, dependency, contract, risk, or legacy Layer. |
| `Generate LEAP Prompt` | Create an agent-ready Prompt only after source truth, repo reality, planning boundary, scope, validation, stop conditions, and execution configuration are clear. |
| `Run LEAP Prompt` | Execute an approved Prompt according to its traceability, scope, constraints, validation, and stop conditions. |
| `Generate LEAP LHS` | Create a staged Prompt when an Initiative or Delivery Unit contains several Build Units or integration checkpoints. |
| `Run LEAP LHS` | Execute an approved LHS Prompt in its defined Delivery Unit and Build Unit sequence. |
| `Run LEAP Governance` | Reconcile framework, project-documentation model, Prompt library, source truth, Agent Pack, terminology, or adoption drift. |
| `Run LEAP Validation` | Verify completed work against scope, acceptance criteria, tests, docs, and stop conditions. |
| `Run LEAP Handoff` | Summarize changes, validation, deviations, risks, and follow-up work. |

## Baseline Freshness Check

LEAP Recon should perform a lightweight Baseline Freshness Check using repository guidance, baseline metadata, source-truth docs, and relevant repo reality.

Possible outcomes:

- Fresh enough
- Minor drift
- Material drift
- Unsafe source-truth conflict

An old date is not automatically a blocker. A recent date is not proof of correctness.

## Planning-boundary discipline

Before implementation, determine the actual boundary:

- Initiative
- Delivery Unit
- Build Unit
- Domain concern
- Architecture concern
- Phase
- legacy Layer requiring classification

Do not:

- treat Roadmap order as permanent hierarchy
- assume numbered work must be sequential
- confuse Domain ownership with temporary Initiative ownership
- define Build Units as independently deployable without evidence
- globally replace `Layer`
- skip required dependencies or human decisions

## Implementation standard

When changing code or docs:

- reuse existing patterns before introducing new ones
- keep changes within the approved Build Unit or bounded task
- preserve compatibility unless approved otherwise
- avoid unrelated cleanup
- do not invent product or Architecture decisions
- do not add dependencies without justification and permission
- do not weaken tests
- keep behavior deterministic and errors explicit where practical
- preserve security, privacy, data, auditability, and ownership boundaries

## LHS behavior

Use LHS when staged execution reduces risk, including:

- several Build Units
- several system or documentation areas
- dependency or merge order
- tests and docs
- phased commits
- rollback or compatibility risk
- Architecture, data-contract, or workflow changes
- cross-repository coordination
- explicit integration checkpoints

Do not convert every LEAP Prompt into LHS.

## Questions and stop conditions

Apply Materiality Gate:

1. Inspect discoverable evidence.
2. Proceed on stated safe assumptions.
3. Ask only unresolved material questions.
4. Stop when proceeding would create meaningful risk.

Stop before:

- destructive or irreversible data changes
- auth, permission, security, privacy, billing, or identity changes without approval
- breaking public contracts without migration approval
- major Architecture replacement
- adding paid services or major production dependencies
- inventing material business rules
- treating archived docs as current source truth
- proceeding with unclear Initiative, Domain, Architecture, Delivery Unit, or Build Unit ownership
- interpreting an ambiguous legacy Layer without sufficient evidence
- irreversible Git operations

## Testing and validation

After implementation:

- run the most relevant available checks
- prefer targeted tests first, then broader checks when practical
- add or update tests when behavior changes
- report checks not run and why
- do not claim success for checks that were not run
- do not hide regressions

Use repository commands rather than generic commands whenever possible.

## Documentation standard

Update docs when changes affect:

- Mission, Strategic Outcomes, or Initiative status
- Roadmap timing, priority, dependencies, or releases
- Domain ownership or contracts
- Architecture
- Delivery Unit or Build Unit status
- setup or operational commands
- public behavior
- user workflows
- APIs, events, schemas, or data models
- environment variables
- security assumptions

Do not let stale docs compete with canonical docs.

## Git and commit standard

When asked to commit:

- commit coherent, reviewable units
- prefer one Build Unit per commit where feasible
- use Initiative, Delivery Unit, Build Unit, or task identifiers when available
- do not bundle unrelated work
- check repository status before committing
- do not commit secrets, local environment files, caches, or generated junk

Preferred message shapes:

```text
INIT-001 - Short descriptive title
DU-001 - Short descriptive title
BU-001 - Short descriptive title
Task - Short descriptive title
```

## Final response standard

At completion, report:

- summary of changes
- Strategic Outcome / Initiative / Delivery Unit / Build Unit traceability when material
- files or areas changed
- tests and checks run
- checks not run and why
- deviations and assumptions
- documentation updates
- risks and follow-up LEAP work

<!-- LEAP_MANAGED_SECTION_END -->
