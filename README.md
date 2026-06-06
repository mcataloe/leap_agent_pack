# LEAP Agent Pack

LEAP Agent Pack provides the reusable `AGENTS.md` templates for using the LEAP Framework with Codex-style coding agents.

This repository is separate from [`leap_framework`](https://github.com/mcataloe/leap_framework) so users can pin stable agent instructions without updating local `AGENTS.md` files every time the LEAP methodology changes.

## What This Repo Owns

- Global `AGENTS.md` guidance for broad LEAP behavior.
- Repo-level `AGENTS.md` guidance for project-specific operating context.
- Combined local-trial `AGENTS.md` guidance for trying LEAP inside one repository before installing global instructions.
- Agent Pack versioning and compatibility manifests.
- Install, upgrade, and customization guidance for downstream users.

The LEAP Framework repo owns methodology, Charter, Recon, Prompt, LHS, examples, and framework roadmap docs.

## Current Version

```text
Agent Pack: 0.2.0 candidate
Release tag: none verified in this local repository
Compatible LEAP Framework: >=0.1.0 <1.0.0
Status: unreleased 0.2.0 candidate reconciliation in progress
```

## Files

| Path | Purpose |
| --- | --- |
| `global/AGENTS.md` | Global LEAP operating guidance. |
| `global/AGENTS_Population_Prompt.md` | Prompt for installing or verifying global LEAP guidance without adding project facts. |
| `repo/AGENTS.md` | Repo-level project adapter template. |
| `repo/AGENTS_Population_Prompt.md` | Prompt for populating a repo-level `AGENTS.md` from repository evidence. |
| `combined/AGENTS.md` | Combined local-trial template with locked global and editable repo sections. |
| `combined/AGENTS_Population_Prompt.md` | Prompt for populating the editable repo section in the combined template. |
| `templates/global-AGENTS.md` | Copy-friendly global template mirror. |
| `templates/repo-AGENTS.md` | Copy-friendly repo template mirror. |
| `templates/leap-*-AGENTS-file*/` | Compatibility paths for older LEAP AGENTS quickstart docs and links. |
| `manifests/latest.json` | Latest Agent Pack version record. |
| `manifests/template-inventory.json` | Machine-readable template and prompt inventory. |
| `manifests/compatibility.json` | LEAP Framework compatibility range. |
| `docs/quickstart.md` | Install guide. |
| `docs/LEAP_AGENTS_Quickstart.md` | Detailed historical quickstart for the combined local-trial workflow. |
| `docs/LEAP_AGENTS_Separate_Global_and_Repo_Method.md` | Detailed historical guide for separate global and repo files. |
| `docs/versioning.md` | Versioning model. |
| `docs/upgrade-guide.md` | Update decision guidance. |
| `docs/customization-guide.md` | Safe repo-level customization guidance. |

## Setup Scenarios

| Scenario | Use when | Install this AGENTS.md | Also install global? | Population / initialization prompt | Notes |
| --- | --- | --- | --- | --- | --- |
| Recommended Separate Global + Repo Method | You want LEAP behavior across multiple projects with per-repo rules. | `repo/AGENTS.md` in the project root | Yes, install `global/AGENTS.md` once | `global/AGENTS_Population_Prompt.md` for global verification; `repo/AGENTS_Population_Prompt.md` for project facts | Keep global reusable; put project commands, architecture, source truth, validation, and stop conditions in repo AGENTS. |
| Repo-Only Method | You only want LEAP inside one repository or cannot use global instructions. | `repo/AGENTS.md` in the project root | No | `repo/AGENTS_Population_Prompt.md` | Works standalone; global reusable behavior may need to come from the repo template or project instructions. |
| Combined Local-Trial Method | You want to test LEAP in one repository before installing global instructions. | `combined/AGENTS.md` in the project root | No | `combined/AGENTS_Population_Prompt.md` | Contains a Locked Global Section and Editable Repository Section; populate only the editable section. |
| Compatibility / Legacy Paths | Older docs, old links, or users already relying on historical paths. | `templates/global-AGENTS.md`, `templates/repo-AGENTS.md`, `templates/leap-repo-AGENTS-file/`, or `templates/leap-repo-AGENTS-file-complete/` | Depends on mapped scenario | Prompt paired in the compatibility path when present | Preserved for compatibility; prefer canonical paths above for new installs. |

## Install

For most projects, use the Recommended Separate Global + Repo Method. Install `global/AGENTS.md` once in the global instruction location used by your coding agent, then install the repo-level template in each project:

```powershell
Copy-Item D:\Repos\leap_agent_pack\repo\AGENTS.md D:\Repos\my_project\AGENTS.md
```

Use `global/AGENTS_Population_Prompt.md` to verify the global file stayed reusable, then use `repo/AGENTS_Population_Prompt.md` to populate the project-specific repo file.

To test LEAP in one repository before installing global instructions, use the Combined Local-Trial Method:

```powershell
Copy-Item D:\Repos\leap_agent_pack\combined\AGENTS.md D:\Repos\my_project\AGENTS.md
```

Then use `combined/AGENTS_Population_Prompt.md` to populate only the editable repository section.

For global LEAP behavior across projects, copy `global/AGENTS.md` to the Codex global instructions location used by your environment.

After copying, customize only the project-specific sections in the repo-level or combined `AGENTS.md`.

## Update Policy

Agent Pack updates are manual and notify-only. Do not overwrite a downstream `AGENTS.md` without reviewing local changes.

Use `docs/upgrade-guide.md` to compare versions and decide whether an update is worth applying.

## More

- [Quickstart](docs/quickstart.md)
- [Detailed combined quickstart](docs/LEAP_AGENTS_Quickstart.md)
- [Separate global and repo method](docs/LEAP_AGENTS_Separate_Global_and_Repo_Method.md)
- [Versioning](docs/versioning.md)
- [Upgrade guide](docs/upgrade-guide.md)
- [Customization guide](docs/customization-guide.md)
