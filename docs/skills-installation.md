# Install LEAP native Skills (project scope)

Project-level Skills are optional. No root SKILLS.md is required. Existing LEAP AGENTS.md commands still work without them.

## Authority and prerequisites

The canonical LEAP navigator is maintained in [Framework skills/leap/SKILL.md](https://github.com/mcataloe/leap_framework/blob/main/skills/leap/SKILL.md). The Agent Pack distributes it; it does not maintain a second copy. Use a pinned Framework commit or release when repeatable installation matters, and record it in your project's adoption notes.

OpenAI Codex currently discovers project Skills under .agents/skills/<skill-name>/SKILL.md. Claude Code discovers them under .claude/skills/<skill-name>/SKILL.md. Both use YAML name and description metadata for discovery.

- Codex: https://learn.chatgpt.com/docs/build-skills
- Claude Code: https://code.claude.com/docs/en/skills

## Install from local checkout (PowerShell)

From the target project root, with a separately cloned LEAP Framework repository:

~~~powershell
$Source = 'D:\Repos\leap_framework\skills\leap\SKILL.md'
$Codex = '.agents\skills\leap\SKILL.md'
$Claude = '.claude\skills\leap\SKILL.md'
if (!(Test-Path $Source)) { throw 'Canonical LEAP Skill source not found' }
foreach ($Destination in @($Codex, $Claude)) {
    if (Test-Path $Destination) { throw "Review existing Skill before overwrite: $Destination" }
    New-Item -ItemType Directory -Force (Split-Path $Destination) | Out-Null
    Copy-Item $Source $Destination
}
~~~

If you only use one assistant, install only its destination. These are copied artifacts of one canonical source, not competing manually maintained definitions. For Windows, ordinary file copies are supported; symlinks are not required.

## AGENTS.md and Claude Code

Install the Agent Pack repository AGENTS.md as usual, or use separated global and repo guidance. The repository-level file contains project-specific facts; the global or combined file contains reusable LEAP routing.

Claude Code normally loads CLAUDE.md. Where it does not automatically load the existing AGENTS.md, create a small CLAUDE.md wrapper using Claude's supported import syntax:

~~~markdown
@AGENTS.md
~~~

Confirm the wrapper loads your local AGENTS.md in the actual Claude environment and retains project-specific permissions. Do not duplicate or manually synchronize full LEAP instructions into CLAUDE.md.

## The three supported Agent Pack setups

- **Separated:** global AGENTS.md plus repository AGENTS.md; install optional native Skill after population.
- **Repository-only:** project AGENTS.md contains minimal LEAP help/routing fallback; install optional native Skill for richer discovery.
- **Combined local trial:** combined template includes routing, then optional Skill installation.

## Project-specific Skills

Use [project-skill-starter/SKILL.md](../templates/skills/project-skill-starter/SKILL.md) and [Project Skill Population Prompt](../templates/skills/Project_Skill_Population_Prompt.md) only for NEW project-specific capabilities. Rename the template before installing. The standard LEAP navigator must not be repopulated with project facts.

## Upgrade / rollback

Never overwrite customized AGENTS.md or existing SKILL.md without inspection and approval. Upgrade by comparing pinned Framework and Agent Pack versions, reviewing the diff, and copying the canonical Skill body after approval. Roll back by restoring the previously committed copy or removing the newly installed optional Skill; legacy AGENTS.md invocation remains usable.

## Verification

- Confirm the native SKILL.md file is present, with YAML name and description.
- Run explicit LEAP help, one Discovery and one Recon request.
- Run an unrelated trivial task and confirm LEAP does not intrude.
- Test destructive cleanup and No Gate scenarios for approval gates.
- Record Codex and Claude results independently; file existence is not proof of native implicit invocation.
