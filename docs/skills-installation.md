# Install LEAP native Skills (project scope)

Project-level Skills are optional. No root SKILLS.md is required. Existing LEAP AGENTS.md commands still work without them.

## Authority and prerequisites

The canonical LEAP navigator is maintained in [Framework skills/leap/SKILL.md](https://github.com/mcataloe/leap_framework/blob/main/skills/leap/SKILL.md). The Agent Pack distributes it; it does not maintain a second copy. Use a pinned Framework commit or release when repeatable installation matters, and record it in your project's adoption notes.

OpenAI Codex currently discovers project Skills under .agents/skills/<skill-name>/SKILL.md. Claude Code discovers them under .claude/skills/<skill-name>/SKILL.md. Both use YAML name and description metadata for discovery.

- Codex: https://learn.chatgpt.com/docs/build-skills
- Claude Code: https://code.claude.com/docs/en/skills

## Install from a local checkout

From the target project root, with the LEAP Framework cloned alongside. Install only the destination for the assistant you use.

macOS / Linux:

```bash
SRC=../leap_framework/skills/leap/SKILL.md
for DEST in .agents/skills/leap/SKILL.md .claude/skills/leap/SKILL.md; do
  if [ -e "$DEST" ]; then echo "Review existing $DEST before overwriting"; continue; fi
  mkdir -p "$(dirname "$DEST")" && cp "$SRC" "$DEST"
done
```

Windows (PowerShell):

```powershell
$Source = '..\leap_framework\skills\leap\SKILL.md'
foreach ($Destination in @('.agents\skills\leap\SKILL.md', '.claude\skills\leap\SKILL.md')) {
    if (Test-Path $Destination) { throw "Review existing Skill before overwrite: $Destination" }
    New-Item -ItemType Directory -Force (Split-Path $Destination) | Out-Null
    Copy-Item $Source $Destination
}
```

The installed files are copies of one canonical source, not separately maintained definitions. Plain copies work; symlinks are not required.

`AGENTS.md` loading per tool is covered in the [README tool table](../README.md#tool-setup).

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
