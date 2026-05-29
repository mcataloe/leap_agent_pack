# LEAP Agent Pack Quickstart

Use this guide to install LEAP `AGENTS.md` templates into a local project.

## Prerequisites

- A local copy of this repository, for example `D:\Repos\leap_agent_pack`.
- A target project repository, for example `D:\Repos\my_project`.
- A coding agent that reads `AGENTS.md` instructions.

## Install The Repo-Level AGENTS.md

Copy the repo-level template into the target project:

```powershell
Copy-Item D:\Repos\leap_agent_pack\repo\AGENTS.md D:\Repos\my_project\AGENTS.md
```

Then open `D:\Repos\my_project\AGENTS.md` and populate the project-specific sections from actual repository evidence.

Do not invent commands, architecture, services, or deployment assumptions.

## Install The Global AGENTS.md

Use the global template only when you want LEAP guidance available across projects.

```powershell
Copy-Item D:\Repos\leap_agent_pack\global\AGENTS.md <your-global-agent-instructions-path>\AGENTS.md
```

The global template should stay reusable. Keep project commands and architecture rules in the repo-level `AGENTS.md`.

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

To pin a version, install from a release tag:

```powershell
git -C D:\Repos\leap_agent_pack checkout leap-agent-pack-v0.1.0
Copy-Item D:\Repos\leap_agent_pack\repo\AGENTS.md D:\Repos\my_project\AGENTS.md
```

Record local modifications in the hidden metadata block.

## Update Later

Check `manifests/latest.json` for the latest Agent Pack version. Follow `docs/upgrade-guide.md` before replacing any local `AGENTS.md` content.
