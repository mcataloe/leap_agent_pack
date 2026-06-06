# LEAP Agent Pack Quickstart

Use this guide to install LEAP `AGENTS.md` templates into a local project.

## Prerequisites

- A local copy of this repository, for example `D:\Repos\leap_agent_pack`.
- A target project repository, for example `D:\Repos\my_project`.
- A coding agent that reads `AGENTS.md` instructions.

## Setup Scenarios

| Scenario | Use when | Install this AGENTS.md | Also install global? | Population / initialization prompt | Notes |
| --- | --- | --- | --- | --- | --- |
| Recommended Separate Global + Repo Method | You want LEAP behavior across multiple projects with per-repo rules. | `repo/AGENTS.md` | Yes, install `global/AGENTS.md` once | `global/AGENTS_Population_Prompt.md` and `repo/AGENTS_Population_Prompt.md` | Keep global reusable; put source truth, commands, validation, and stop conditions in repo AGENTS. |
| Repo-Only Method | You only want LEAP inside one repository or cannot use global instructions. | `repo/AGENTS.md` | No | `repo/AGENTS_Population_Prompt.md` | Works standalone; project instructions may need to provide any missing reusable LEAP behavior. |
| Combined Local-Trial Method | You want to test LEAP in one repository before installing global instructions. | `combined/AGENTS.md` | No | `combined/AGENTS_Population_Prompt.md` | Populate only the Editable Repository Section. |
| Compatibility / Legacy Paths | Older docs, old links, or users already relying on historical paths. | Compatibility path matching the scenario | Depends on mapped scenario | Paired compatibility prompt when present | Preserved, but not the primary recommendation for new installs. |

## Recommended: Install Global + Repo AGENTS.md

Install global LEAP behavior once:

```powershell
Copy-Item D:\Repos\leap_agent_pack\global\AGENTS.md <your-global-agent-instructions-path>\AGENTS.md
```

Then use:

```text
D:\Repos\leap_agent_pack\global\AGENTS_Population_Prompt.md
```

The global template should stay reusable. Keep project commands and architecture rules in the repo-level `AGENTS.md`.

Then copy the repo-level template into the target project:

```powershell
Copy-Item D:\Repos\leap_agent_pack\repo\AGENTS.md D:\Repos\my_project\AGENTS.md
```

For project-specific population, use:

```text
D:\Repos\leap_agent_pack\repo\AGENTS_Population_Prompt.md
```

## Repo-Only AGENTS.md

Copy the repo-level template into the target project:

```powershell
Copy-Item D:\Repos\leap_agent_pack\repo\AGENTS.md D:\Repos\my_project\AGENTS.md
```

Then open `D:\Repos\my_project\AGENTS.md` and populate the project-specific sections from actual repository evidence.

Do not invent commands, architecture, services, or deployment assumptions.

For a guided population prompt, use:

```text
D:\Repos\leap_agent_pack\repo\AGENTS_Population_Prompt.md
```

## Combined Local-Trial AGENTS.md

Use the combined template when you want to test LEAP in one repository before installing global instructions.

```powershell
Copy-Item D:\Repos\leap_agent_pack\combined\AGENTS.md D:\Repos\my_project\AGENTS.md
```

Then use the combined population prompt:

```text
D:\Repos\leap_agent_pack\combined\AGENTS_Population_Prompt.md
```

The combined template contains a locked global LEAP section and an editable repository section. Populate only the editable repository section.

## Recommended Workspace Layout

```text
D:\Repos\
  leap_framework\
  leap_agent_pack\
  my_project\
```

Cross-platform users can use the same layout idea with their normal home or workspace directory.

## Customize Repo Instructions

In the repo-level `AGENTS.md`, fill in:

- Project name and purpose.
- Source-of-truth docs.
- Repository layout.
- Setup and validation commands.
- Security, data, architecture, and stop-condition rules.

Prefer links to project docs over copying long documentation into `AGENTS.md`.

## Pin A Version

To pin a released version, install from a release tag after verifying the tag exists:

```powershell
git -C D:\Repos\leap_agent_pack tag --list
git -C D:\Repos\leap_agent_pack checkout <release-tag>
Copy-Item D:\Repos\leap_agent_pack\repo\AGENTS.md D:\Repos\my_project\AGENTS.md
```

The current reconciliation is an unreleased `0.2.0` candidate. Do not use a `0.2.0` tag unless it is created separately.

Record local modifications in the hidden metadata block.

## Update Later

Check `manifests/latest.json` for the latest Agent Pack version. Follow `docs/upgrade-guide.md` before replacing any local `AGENTS.md` content.

## Detailed Guides

- `docs/LEAP_AGENTS_Quickstart.md` covers the combined local-trial workflow.
- `docs/LEAP_AGENTS_Separate_Global_and_Repo_Method.md` covers the separate global and repo-file workflow.
