# Global AGENTS.md Initialization Prompt

Use this prompt after copying `global/AGENTS.md` into the global instruction location used by Codex or another coding agent.

## Goal

Install or verify reusable LEAP operating guidance without adding project-specific facts.

## Instructions for Codex

1. Confirm that `global/AGENTS.md` or equivalent global instructions are installed in the user's intended global instruction location.
2. Verify that the global file stays reusable across projects.
3. Do not add project-specific architecture, commands, source-truth docs, business rules, repositories, secrets, credentials, environment details, or validation commands to the global file.
4. If project-specific facts are needed, direct the user to install `repo/AGENTS.md` in the project root and run `repo/AGENTS_Population_Prompt.md`.
5. If the user wants to test LEAP in only one repository before installing global guidance, direct the user to use `combined/AGENTS.md` and `combined/AGENTS_Population_Prompt.md` instead.
6. If the global file contains project-specific content, report the issue and recommend moving that content into the repo-level AGENTS file.

## Output

Return:

```text
Global AGENTS.md Initialization Summary
- Global file present:
- Reusable guidance preserved:
- Project-specific content found:
- Recommended repo-level next step:
- Local-trial alternative needed:
```
