# Optional Execution Continuity, Review Evidence, and Lessons

Purpose: preserve a verifiable handoff across separate agent sessions and turn successful corrections into reusable guidance **without creating a second source of project truth**.

This optional guidance builds on existing LEAP [execution routing](https://github.com/mcataloe/leap_framework/blob/main/docs/execution-routing.md) and the proposed [execution roles contract](https://github.com/mcataloe/leap_framework/blob/main/docs/agent-execution-roles.md) (Framework PR #25). It complements optional Agent Pack role overlays proposed separately in PR #8. It does not require Mission Control software, native agent teams, a message inbox, or new project status names.

## Four separate kinds of information

| Kind | Source of authority | Template | Keep / update |
|---|---|---|---|
| **Active handoff** | Existing work tracker or project handoff | [active-handoff.md](../templates/execution/active-handoff.md) | Current work, next action, blockers, actual state |
| **Execution evidence** | Commands, diffs, logs, CI, tests | [implementation-report.md](../templates/execution/implementation-report.md) | What actually changed and what ran |
| **Independent review** | Reviewer inspection and any rerun evidence | [independent-review.md](../templates/execution/independent-review.md) | Findings and scoped disposition, not merge approval |
| **Reusable lessons** | Verified cases and existing project policy | [lesson-candidate.md](../templates/execution/lesson-candidate.md) | Candidate improvement, evidence and review decision |

Use existing project conventions when they already cover these needs. Do not copy canonical decisions, roadmaps, architecture, or contracts into handoffs; link to the authoritative version. Keep completed tasks in the existing history/issue/PR record. No arbitrary filename or directory is required.

## Handoff rule

Before a session ends or execution passes to another role, record the approved scope, current source revision, work completed, observed verification, open decisions, outstanding approvals, next owner, and next safe action. On resumption, inspect the current baseline, reconcile material changes, and use LEAP Materiality Gate to ask only questions that change the next safe decision.

A missing or stale handoff may require Recon, not automatic continuation. The receiver never treats a summary as permission to mutate.

## Review and correction loop

1. Implementor submits the diff and an evidence report.
2. Reviewer independently reads the diff and governing acceptance criteria, checks evidence, and selectively executes missing/doubtful/risk-required checks.
3. Reviewer records accepted / fix-up required / blocked with concrete findings.
4. For fix-up, coordinator issues a **bounded correction**: observed failure, expected behavior, files/areas, authority, required validation, and ownership.
5. After correction, verify the changed scope and integration effects, then update the active handoff and actual LEAP verification state.

No automatic approval of protected changes is implied. Avoid duplicative reruns when evidence is sufficient, but do not sacrifice independent validation when policy or risk requires it.

## Lesson promotion: evidence before new rules

1. Record a candidate from a real observed correction or repeated friction.
2. Determine whether its impact is task-only, project-wide, or broadly portable.
3. Search existing instructions for overlap or contradiction; revise or consolidate rather than accumulate.
4. Require adequate evidence and a responsible approver before promoting to project `AGENTS.md`, canonical docs, shared Agent Pack, or Framework doctrine.
5. Preserve supersession or migration notes when a public path or managed instruction changes. Do not overwrite downstream customizations without review.

Static acceptance checks can verify template structure and references. Actual recoverability, review independence, and lesson effectiveness require agent-session trials with recorded outcomes. Do not claim those behaviors from documents alone.

## Small pilot

Use a bounded task with an actual implementation artifact and separate reviewer when risk justifies it. Interrupt after implementation, resume from a new session, reconcile source state, request a targeted fix-up, and verify that required approvals remain outstanding. Record the manual overhead. If a single-agent task is simpler, skip these templates.
