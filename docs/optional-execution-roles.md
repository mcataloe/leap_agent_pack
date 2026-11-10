# Optional LEAP Execution Role Profiles and Context Packets

The templates in `templates/execution/` are a **portable, opt-in** way to adopt the responsibilities described by the [Framework agent execution roles contract](https://github.com/mcataloe/leap_framework/blob/main/docs/agent-execution-roles.md). That Framework contract is proposed in PR #25 until merged.

These profiles complement existing Agent Pack `AGENTS.md` guidance. They do not replace LEAP Charter/Recon/Prompt, create new lifecycle stages, set native models, enable delegation, or supply a coordinator runtime. Native Codex/Claude adapters are a separate concern (Agent Pack PR #7).

## Available overlays

| File | Use when |
|---|---|
| [Architect/coordinator](../templates/execution/architect.md) | Scoping and coordinating multiple bounded work items or independent review |
| [Implementor](../templates/execution/implementor.md) | Applying an approved Build Unit with clear scope and required evidence |
| [Independent reviewer](../templates/execution/reviewer.md) | A separate, evidence-grounded review is required or materially beneficial |
| [Example context manifest](../templates/execution/context-manifest.example.yaml) | Documenting which authoritative context sources a task packet should include |

## Adoption

1. Confirm the project-specific `AGENTS.md` and current approved LEAP Prompt remain the controlling instructions.
2. Select the smallest topology that satisfies risk and verification needs. Single-agent operation is the default; never require three sessions for small changes.
3. For a role that is actually assigned, provide its overlay as an **additional** context reference, not a replacement for project policy.
4. Build a task-specific packet from current sources and the approved Prompt; inspect revisions and dependencies before applying it. The YAML example is documentation only: no script or tool automatically processes it.
5. Use the project's existing issue/PR/handoff location for findings and evidence. Do not maintain duplicate project state just to support these templates.
6. On resume, reconcile material baseline changes and continue only from the next authorized step.
7. Validate observed behavior with native assistant sessions before relying on automatic routing or independent review.

## Distinctions

- **Agent execution profile:** tool-specific capability and failure modes; maintained by the Framework.
- **Execution role:** accountability for coordination, bounded implementation, review, or human approval.
- **Execution surface:** where work and verification can actually run.
- **Skill:** a reusable procedure for specialized work.
- **Build Unit:** the bounded responsibility being delivered.

A single session may perform architect and implementor responsibilities when appropriate, but never claim **independent** review from that same session. A role-specific overlay does not grant new tools, permissions, source-truth authority, or protected-action approval.

## Pilot checklist

Exercise: a small single-agent change; a consequential change that requires independent review; a stopped task caused by missing authorization; stale source/contract reinspection; interruption and handoff resumption; and a sequential fallback when native delegation is unavailable. Record what happened, including checks not run. Static template inspection is not proof of observed agent behavior.

## Customization and upgrade

Preserve managed `AGENTS.md` markers and downstream edits. Do not copy these instructions into locked global guidance. Adopt role overlays only for tasks that need them; replace example manifest paths with real current project sources. Verify compatibility with the installed Framework revision before depending on links to unmerged documents.
