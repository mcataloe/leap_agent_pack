# LEAP Agent Pack Upgrade Guide

Use this guide to decide whether a local `AGENTS.md` should be updated.

Agent Pack updates are manual. Do not overwrite local project guidance automatically.

## Setup Scenario Inventory

| Scenario | Use when | Install this AGENTS.md | Also install global? | Population / initialization prompt | Notes |
| --- | --- | --- | --- | --- | --- |
| Recommended Separate Global + Repo Method | LEAP should be available across multiple projects with project-specific repo rules. | `repo/AGENTS.md` | Yes, `global/AGENTS.md` | `global/AGENTS_Population_Prompt.md` and `repo/AGENTS_Population_Prompt.md` | Review both files independently during upgrades. |
| Repo-Only Method | LEAP is needed only inside one repository. | `repo/AGENTS.md` | No | `repo/AGENTS_Population_Prompt.md` | Upgrade only the repo template and preserve local project sections. |
| Combined Local-Trial Method | A user is testing LEAP locally before global install. | `combined/AGENTS.md` | No | `combined/AGENTS_Population_Prompt.md` | Preserve Locked Global Section and Editable Repository Section boundaries. |
| Compatibility / Legacy Paths | Existing users rely on older template paths. | Mapped compatibility template | Depends on mapped scenario | Paired compatibility prompt when present | Keep paths available; prefer canonical paths for new installs. |

## Compare Versions

1. Read the hidden metadata block in the local `AGENTS.md`.
2. Check `manifests/latest.json` in the Agent Pack repo.
3. Compare the local template version with the latest version.
4. Review local modifications before replacing managed guidance.

## Update Decision Model

| Update type | Recommendation |
| --- | --- |
| PATCH | Optional unless it fixes a known issue affecting the project. |
| MINOR | Recommended when users actively use the affected workflow or template. |
| MAJOR | Requires review before applying. Do not auto-merge. |

## Safe Update Procedure

1. Back up or diff the current local `AGENTS.md`.
2. Compare the current local file with the new Agent Pack template.
3. Preserve project-specific instructions.
4. Preserve local modification notes.
5. Apply only the template changes that are useful for the project.
6. Run a quick review to confirm setup, test, and stop-condition guidance still matches the repository.

If the local file has substantial custom guidance, create a manual merge plan instead of replacing it.
