# Native Delegation Adapters (Optional)

This guide implements the [LEAP Framework native delegation policy](https://github.com/mcataloe/leap_framework/blob/main/docs/native-agent-delegation.md) on supported agent runtimes. It is an **opt-in** overlay: existing templates and installations continue working unchanged.

## Installation posture

1. Read the framework policy and your project's actual runtime capabilities and restrictions.
2. Manually merge the shared policy below into the appropriate *editable* project guidance or local override. Do **not** overwrite locked global markers, downstream customizations, or existing `AGENTS.md`/`CLAUDE.md`.
3. Configure native agent enablement using the **installed version's official documentation**, not guesses or copied version-dependent flags. Enable only if permitted by the organization and environment.
4. Test one read-only task, one independent two-worker task, and the sequential fallback before using implementation workers. Record the observed models, effort settings, concurrency, permissions, cost, and validation state.

## Shared policy snippet (for AGENTS.md and/or CLAUDE.md)

```markdown
### LEAP Native Agent Delegation (opt-in)
Default to sequential work. When the runtime exposes native subagents,
delegate only independently bounded work with a demonstrable advantage.
Respect approved Build Units, dependency order, disjoint file ownership,
permissions, data restrictions, stop conditions, and human approval gates.
The coordinator owns final integration and verification. Worker claims
are not proof of executed validation.

Select roles, models, and reasoning effort according to verified runtime
capabilities and task risk; prefer medium for bounded implementation,
high for consequential review, low for mechanical tasks when available.
Never assume a particular model/effort combination exists.
If unavailable or unsafe, continue sequentially without reducing
acceptance criteria. Report the fallback and validation evidence.
```

This is an instruction policy, **not** a native enablement switch, an access-control mechanism, or a guarantee that the coordinator will select a different model.

## Codex adapter

- Use `AGENTS.md` for project governance, and the installed Codex version's supported user/project configuration and agent-definition facilities for execution settings.
- Keep per-worker roles narrowly scoped: e.g., architecture reviewer (read-only), implementation worker (approved Build Unit), test reviewer (independent results), documentation worker.
- Check the current [Codex documentation](https://developers.openai.com/codex/) for the exact configuration keys, allowed reasoning settings, and agent spawning API in **your** release. Do not presume that API agent-session `multi_agent` settings are interchangeable with Codex CLI `config.toml` flags.
- A separate OpenAI Agents API integration can enable `agent.multi_agent.enabled` on session creation; that is an **API-specific** feature, not a substitute for configuring the local Codex CLI. See [Agents API multi-agent documentation](https://developers.openai.com/api/docs/guides/agents-api/multi-agent).

## Claude Code adapter

- Use `CLAUDE.md` for project governance and `.claude/agents/` for optional role-specific subagent definitions when supported by your installed version.
- Choose model and effort values only from currently supported Claude Code settings; do not assume invocation-time effort override mirrors Codex behavior.
- Distinguish ordinary delegated subagents from experimental agent teams, where available. Verify rollout status, enablement, worktree/isolation behavior, and organization policy before adopting either.
- Consult the [official Claude Code documentation](https://code.claude.com/docs/en/sub-agents) and [settings reference](https://code.claude.com/docs/en/settings) before writing executable configuration.

## Worker contract

For every delegated task capture: approved Build Unit or bounded scope; source truth and inputs; deliverable; prerequisites; allowed tools and paths; no-touch files; reasoning requirement (not an invented SKU); tests/evidence; stop/escalation criteria; integration owner.

Worker result: changed files / observations; tests actually executed with results; failures; conflicts; outstanding risks; verification state. The parent validates and integrates in dependency order.

## No-regression trial

1. **Recon:** two independent read-only investigations; no mutations.
2. **Implementation:** two independent, disjoint areas under an explicitly approved Build Unit; verify integration and tests.
3. **Negative:** same-file edits, unknown authorization, missing subagent capability, and unsupported model effort must **not** silently proceed as parallel authorized work.
4. Compare accepted outcomes, retries, wall time, and full token/inference/human review cost against sequential baseline.

## Lifecycle and release boundaries

This guide adds no new lifecycle phase, dependency, background scheduler, required service, or default paid plan. It intentionally does not modify the locked global LEAP section, version numbers, compatibility markers, or existing downstream files. Any future default enablement or schema change requires separate review and versioning.
