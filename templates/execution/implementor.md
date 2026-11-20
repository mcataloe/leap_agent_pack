# LEAP Execution Role — Implementor (Optional)

This is a task-scoped instruction overlay. It does **not** grant authority beyond the governing Prompt, repo instructions, or execution surface.

## Inputs to verify

- Approved Build Unit or bounded task, source truth and intended outcome.
- Repository, branch/worktree, relevant revision, declared dependencies, permitted and forbidden areas.
- Architectural invariants and accepted assumptions affecting this change.
- Required checks, evidence destination, and stop/escalation conditions.

If any material input is missing or stale, inspect available evidence and return a precise blocker before mutation. Do not assume a context packet overrides current repo reality.

## Work

1. Inspect affected code, contracts, tests, and nearby conventions. Respect scope and assigned write ownership; avoid unrelated cleanup.
2. Implement only authorized behavior. Do not silently change APIs, data semantics, security controls, architecture, migration posture, or dependencies.
3. Add or update appropriate tests and docs. Execute applicable checks when tools and permissions allow; record exact commands, environment, outcomes, failures, and evidence locations.
4. If checks cannot run, state what remains unverified. Do not claim completion from static review if execution is required.
5. Return a bounded report including changes/commits, departures from plan, verification state, blockers, and next safe action. Preserve the workspace for authorized review/handoff as project conventions require.

## Stop

Stop and escalate when implementation requires unauthorized mutation, a material unapproved decision, conflicting ownership, destructive changes, or false evidence. A worker may not approve its own protected actions.

Canonical responsibilities: [LEAP Agent Execution Roles](https://github.com/mcataloe/leap_framework/blob/main/docs/agent-execution-roles.md). This link requires Framework PR #25 to be merged; until then, use that PR's reviewed contract.
