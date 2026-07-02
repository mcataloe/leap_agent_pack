# LEAP Agent Pack

LEAP Agent Pack provides reusable `AGENTS.md` templates for using the LEAP Framework with coding agents.

It is versioned separately from [`leap_framework`](https://github.com/mcataloe/leap_framework) so downstream repositories can pin agent instructions independently from methodology releases.

## What this repository owns

- Global reusable LEAP operating guidance.
- Repository-level project adapter guidance.
- Combined local-trial guidance.
- Population prompts.
- Agent Pack compatibility, inventory, install, customization, and upgrade guidance.

The LEAP Framework repository owns lifecycle doctrine, Charter, Recon, Prompt behavior, LHS, the project-documentation model, and framework examples.

## Current project-documentation model

Agent Pack templates align with:

```text
Mission / Project Charter
        ↓
Strategic Outcome
        ↓
Initiative
        ↓
Delivery Unit
        ↓
Build Unit
```

Supporting views remain separate:

```text
Roadmap      = timing, priority, milestones, dependencies, releases, status, parallelism
Domain Map   = persistent responsibility and ownership boundaries
Architecture = technical structure and qualified technical Layers
```

Several Initiatives may run in parallel. Delivery Unit may collapse for small work. Build Unit is not necessarily independently deployable.

Generic project-planning `Layer` is legacy-compatible and deprecated. Preserve the LEAP name, Layered House Standard, LEAP LHS, qualified Architecture Layers, public paths, and compatibility references.

## Current version

```text
Agent Pack: 0.2.0 candidate
Release tag: none verified
Compatible LEAP Framework: >=0.1.0 <1.0.0
Status: unreleased candidate
```

## Canonical files

The active repository structure is:

| Path | Purpose |
|---|---|
| `templates/separated/global/AGENTS.md` | Global reusable LEAP guidance. |
| `templates/separated/global/AGENTS_Population_Prompt.md` | Global initialization and verification prompt. |
| `templates/separated/repo/AGENTS.md` | Repository-level project adapter template. |
| `templates/separated/repo/AGENTS_Population_Prompt.md` | Repository population prompt. |
| `templates/combined/AGENTS.md` | Combined local-trial template. |
| `templates/combined/AGENTS_Population_Prompt.md` | Combined-template population prompt. |
| `examples/global-AGENTS.example.md` | Example global guidance. |
| `examples/repo-AGENTS.example.md` | Example populated repository guidance. |
| `examples/combined-local-trial-AGENTS.example.md` | Example combined local-trial file. |
| `manifests/latest.json` | Current candidate version and canonical path record. |
| `manifests/template-inventory.json` | Machine-readable template inventory. |
| `manifests/compatibility.json` | Framework compatibility range. |
| `docs/quickstart.md` | Primary install guide. |
| `docs/upgrade-guide.md` | Manual update guidance. |
| `docs/customization-guide.md` | Safe customization guidance. |

Older documentation may mention top-level `global/`, `repo/`, or `combined/` paths. Those paths do not exist in the current repository and should not be treated as canonical.

## Setup scenarios

| Scenario | Install | Population prompt |
|---|---|---|
| Separate global plus repository method | Install `templates/separated/global/AGENTS.md` globally and copy `templates/separated/repo/AGENTS.md` to the project root | Run both separated population prompts |
| Repository-only method | Copy `templates/separated/repo/AGENTS.md` to the project root | Run the repository population prompt |
| Combined local trial | Copy `templates/combined/AGENTS.md` to the project root | Run the combined population prompt |

## Installation examples

Separate repository template:

```powershell
Copy-Item D:\Repos\leap_agent_pack\templates\separated\repo\AGENTS.md D:\Repos\my_project\AGENTS.md
```

Combined local trial:

```powershell
Copy-Item D:\Repos\leap_agent_pack\templates\combined\AGENTS.md D:\Repos\my_project\AGENTS.md
```

Install the global template in the global instruction location supported by the coding-agent environment.

## Update policy

Updates are manual and notify-only.

Do not overwrite downstream `AGENTS.md` files without reviewing:

- Agent Pack-managed content
- project-specific edits
- local overrides
- current Framework compatibility
- migration notes

Use [`docs/upgrade-guide.md`](docs/upgrade-guide.md) before adopting a new Agent Pack candidate or release.

## More

- [Quickstart](docs/quickstart.md)
- [Versioning](docs/versioning.md)
- [Upgrade guide](docs/upgrade-guide.md)
- [Customization guide](docs/customization-guide.md)
