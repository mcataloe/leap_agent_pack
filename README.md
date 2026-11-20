# LEAP Agent Pack

`AGENTS.md` templates that put [LEAP](https://github.com/mcataloe/leap_framework) in front of coding agents. The pack is versioned separately from the framework, so downstream repositories can pin their agent instructions.

What loads every session is deliberately small:

- **LEAP Core** (~600 words): inspect first, ask only what matters, order of truth, the lightest-workflow ladder, scope, hard stops, honest verification, handoff. Canonical text: [`docs/leap-core.md`](https://github.com/mcataloe/leap_framework/blob/main/docs/leap-core.md) in the framework.
- **Your project section**: the rules that only apply to your repository, kept under about 800 words.

Everything else in LEAP (Charter, Recon, Prompt, LHS, Cleanup, Skills, routing) is loaded on demand.

## Current version

```text
Agent Pack: 0.2.0-candidate.2 (unreleased; no tag)
Compatible LEAP Framework: >=0.1.0 <1.0.0
```

Machine-readable record: [`manifests/latest.json`](manifests/latest.json).

## Choose a setup

| Setup | Files | When |
|---|---|---|
| Separated (recommended) | `templates/separated/global/AGENTS.md` in your agent's global location + `templates/separated/repo/AGENTS.md` at the repository root | You use LEAP in several repositories |
| Combined | `templates/combined/AGENTS.md` at the repository root | One repository, a trial, or a tool with no global instruction file |

After copying, run the matching population prompt next to the template (`AGENTS_Population_Prompt.md`). It fills only the project section, from repository evidence, and marks unknowns `TBD`.

## Tool setup

| Tool | Global LEAP Core | Repository file |
|---|---|---|
| OpenAI Codex | `~/.codex/AGENTS.md` (or `$CODEX_HOME/AGENTS.md`) | `AGENTS.md` at the repository root |
| Claude Code | `~/.claude/CLAUDE.md` containing the global template, or a line `@~/.codex/AGENTS.md` to share Codex's copy | `AGENTS.md` is read when the repository has no `CLAUDE.md`; otherwise add `@AGENTS.md` to `CLAUDE.md` |
| Other tools that read `AGENTS.md` | Use the combined template | `AGENTS.md` at the repository root |

Confirm the agent actually loaded the file (for example, `/context` in Claude Code, or ask the agent to quote the LEAP Core heading). An instruction file that does not load is not a guardrail.

## Install

macOS / Linux:

```bash
PACK=~/src/leap_agent_pack        # your clone of this repository
REPO=~/src/my_project             # the repository adopting LEAP

# Separated: global core for Codex, shared with Claude Code
mkdir -p ~/.codex ~/.claude
cp -i "$PACK/templates/separated/global/AGENTS.md" ~/.codex/AGENTS.md
grep -qxF '@~/.codex/AGENTS.md' ~/.claude/CLAUDE.md 2>/dev/null || echo '@~/.codex/AGENTS.md' >> ~/.claude/CLAUDE.md
cp -i "$PACK/templates/separated/repo/AGENTS.md" "$REPO/AGENTS.md"

# Or combined, one file
cp -i "$PACK/templates/combined/AGENTS.md" "$REPO/AGENTS.md"
```

Windows (PowerShell):

```powershell
$Pack = 'D:\Repos\leap_agent_pack'
$Repo = 'D:\Repos\my_project'

New-Item -ItemType Directory -Force "$HOME\.codex", "$HOME\.claude" | Out-Null
Copy-Item "$Pack\templates\separated\global\AGENTS.md" "$HOME\.codex\AGENTS.md" -Confirm
Add-Content "$HOME\.claude\CLAUDE.md" '@~/.codex/AGENTS.md'
Copy-Item "$Pack\templates\separated\repo\AGENTS.md" "$Repo\AGENTS.md" -Confirm

# Or combined
Copy-Item "$Pack\templates\combined\AGENTS.md" "$Repo\AGENTS.md" -Confirm
```

`cp -i` and `-Confirm` stop you from overwriting an existing file. For an existing `AGENTS.md`, follow [Upgrade and customize](docs/install-and-upgrade.md).

## Guardrails beyond instructions

Instructions are requests; enforced checks are guardrails. Pair the templates with:

- the [LEAP pull request template](https://github.com/mcataloe/leap_framework/blob/main/templates/leap-pull-request-template.md) for scope, verification state, and checks not run
- CODEOWNERS or branch protection on paths your project stop conditions name
- CI checks for rules that can be tested (for example, "applied migrations are immutable")
- agent permission deny-rules or hooks for paths that must never be edited (Claude Code permission rules and `PreToolUse` hooks, Codex sandbox and approval settings)

## Optional add-ons

Opt-in guidance. None of it changes the managed section, enables native delegation, or replaces the project's work tracker. Small tasks need none of it.

- [Execution role overlays](docs/optional-execution-roles.md): architect, implementor, and independent-reviewer overlays plus an example context manifest, for work split across roles or sessions.
- [Execution continuity](docs/execution-continuity.md): cross-session handoffs, independent review evidence, and lesson promotion.
- [Native delegation adapters](docs/native-delegation-adapters.md): Codex and Claude Code subagent policy. Validate against the installed runtime before relying on it.

## Repository contents

| Path | Purpose |
|---|---|
| `templates/separated/global/` | Global LEAP Core template and initialization prompt |
| `templates/separated/repo/` | Repository template (project slots only) and population prompt |
| `templates/combined/` | Single-file template and population prompt |
| `templates/skills/` | Optional starter for project-specific native Skills |
| `templates/execution/` | Optional role overlays, context manifest example, handoff, report, review, and lesson templates |
| `examples/repo-AGENTS.example.md` | A populated repository file |
| `docs/install-and-upgrade.md` | Upgrade, customization, and versioning |
| `docs/skills-installation.md` | Optional native LEAP Skill install for Codex and Claude Code |
| `docs/optional-execution-roles.md`, `docs/execution-continuity.md`, `docs/native-delegation-adapters.md` | Optional add-ons (see above) |
| `manifests/latest.json` | Version, compatibility, and file inventory |
| `scripts/check_pack.py` | Markers, metadata, manifest, links, and size budgets |

## Maintainer check

```bash
python3 scripts/check_pack.py                                   # pack only
python3 scripts/check_pack.py --framework ../leap_framework     # plus LEAP Core drift
```

Standard library only. CI runs it on every push and pull request.
