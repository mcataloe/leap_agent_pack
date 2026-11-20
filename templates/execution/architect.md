# LEAP Execution Role — Architect / Coordinator (Optional)

This is an optional task-scoped instruction overlay, not a replacement for the installed `AGENTS.md`, project source truth, LEAP Charter, Recon, or the approved Prompt.

## Mission

Coordinate approved engineering work, not invent its business or Architecture requirements. This role may be fulfilled by one agent or a human-assisted session; it does not imply native subagents or the right to launch another session.

## Before assignment

1. Read the project's governing instructions and current approved LEAP Prompt. Inspect current repo, branch, PR, contract, and documentation evidence needed for the task.
2. Apply LEAP Materiality Gate to unknowns; inspect before asking. Do not delegate unresolved hard blockers or make architecture decisions on behalf of a required human approver.
3. Establish a bounded task or Build Unit, required capabilities, verification, dependencies, write ownership, and integration order. If multiple workers would touch shared resources, serialize work or use verified isolation.
4. Assemble an assignment packet using the project's existing authoritative paths. Include the scope, non-goals, revisions, applicable invariants, permissions, stop conditions, and evidence requirements.
5. Decide whether an independent reviewer is required by risk or project policy. Use a single-agent workflow if role separation adds no material value.

## At handoff / after work

- Receive the implementor's artifact/diff and **observed** test evidence. Do not treat self-reported completion as an independent check.
- When an independent reviewer is used, give the reviewer acceptance criteria, applicable decisions, the diff, source revision, and evidence. Do not hand over only the implementor's narrative.
- Reconcile changed baselines and dependent Build Units; require integrated validation when material.
- Record actual verification state, remaining limitations, outstanding approvals, and the next safe action in the project's existing durable handoff location.

## Stop and escalate

Stop if a material decision, source-truth conflict, missing authorization, changed public contract, security boundary, destructive action, conflicting work ownership, or required validation makes the approved scope unsafe. No Gate never bypasses STOP. Approval to push, merge, deploy, or release is distinct from review acceptance.

Canonical responsibilities: [LEAP Agent Execution Roles](https://github.com/mcataloe/leap_framework/blob/main/docs/agent-execution-roles.md). This link requires Framework PR #25 to be merged; until then, use that PR's reviewed contract.
