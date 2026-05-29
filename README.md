# LEAP Agent Pack

LEAP Agent Pack provides the reusable `AGENTS.md` templates for using the LEAP Framework with Codex-style coding agents.

This repository is separate from [`leap_framework`](https://github.com/mjcataldi/leap_framework) so users can pin stable agent instructions without updating local `AGENTS.md` files every time the LEAP methodology changes.

## What This Repo Owns

- Global `AGENTS.md` guidance for broad LEAP behavior.
- Repo-level `AGENTS.md` guidance for project-specific operating context.
- Agent Pack versioning and compatibility manifests.
- Install, upgrade, and customization guidance for downstream users.

The LEAP Framework repo owns methodology, Charter, Recon, Prompt, LHS, examples, and framework roadmap docs.

## Current Version

```text
Agent Pack: 0.1.0
Release tag: leap-agent-pack-v0.1.0
Compatible LEAP Framework: >=0.1.0 <1.0.0
Status: initial extraction / early version
```

## Files

| Path | Purpose |
| --- | --- |
| `global/AGENTS.md` | Global LEAP operating guidance. |
| `repo/AGENTS.md` | Repo-level project adapter template. |
| `templates/global-AGENTS.md` | Copy-friendly global template mirror. |
| `templates/repo-AGENTS.md` | Copy-friendly repo template mirror. |
| `manifests/latest.json` | Latest Agent Pack version record. |
| `manifests/compatibility.json` | LEAP Framework compatibility range. |
| `docs/quickstart.md` | Install guide. |
| `docs/versioning.md` | Versioning model. |
| `docs/upgrade-guide.md` | Update decision guidance. |
| `docs/customization-guide.md` | Safe repo-level customization guidance. |

## Install

For most projects, install the repo-level template:

```powershell
Copy-Item D:\Repos\leap_agent_pack\repo\AGENTS.md D:\Repos\my_project\AGENTS.md
```

For global LEAP behavior across projects, copy `global/AGENTS.md` to the Codex global instructions location used by your environment.

After copying, customize only the project-specific sections in the repo-level `AGENTS.md`.

## Update Policy

Agent Pack updates are manual and notify-only. Do not overwrite a downstream `AGENTS.md` without reviewing local changes.

Use `docs/upgrade-guide.md` to compare versions and decide whether an update is worth applying.

## More

- [Quickstart](docs/quickstart.md)
- [Versioning](docs/versioning.md)
- [Upgrade guide](docs/upgrade-guide.md)
- [Customization guide](docs/customization-guide.md)
