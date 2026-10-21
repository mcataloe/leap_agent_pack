# Global AGENTS.md Initialization Prompt

Use this after copying `templates/separated/global/AGENTS.md` into your coding agent's global instruction location (see the tool table in the [README](../../../README.md#tool-setup)).

```text
Verify the global LEAP AGENTS.md installation.

1. Confirm the file is loaded by the agent from its global location.
2. Confirm the managed section matches the current LEAP Core:
   https://github.com/mcataloe/leap_framework/blob/main/docs/leap-core.md
3. Report any project-specific content (paths, commands, business rules,
   repositories, credentials, environments) and recommend moving it to the
   repository AGENTS.md.
4. Do not install native Skills or edit any other file.

Return:
- Global file location and whether the agent loads it
- LEAP Core current: yes / no (differences)
- Project-specific content found
- Recommended next step
```
