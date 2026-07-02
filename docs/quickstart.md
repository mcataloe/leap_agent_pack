# LEAP Agent Pack Quickstart

Use this guide to install LEAP `AGENTS.md` guidance into a project.

## Prerequisites

- A local copy of `leap_agent_pack`.
- A target repository.
- A coding agent that reads `AGENTS.md` or equivalent instructions.

## Current template paths

| Scenario | Template | Population prompt |
|---|---|---|
| Separate global plus repository | `templates/separated/global/AGENTS.md` and `templates/separated/repo/AGENTS.md` | Both separated population prompts |
| Repository-only | `templates/separated/repo/AGENTS.md` | `templates/separated/repo/AGENTS_Population_Prompt.md` |
| Combined local trial | `templates/combined/AGENTS.md` | `templates/combined/AGENTS_Population_Prompt.md` |

Do not use nonexistent top-level `global/`, `repo/`, or `combined/` paths.

## Documentation model installed by the templates

```text
Mission / Project Charter
  -> Strategic Outcome
    -> Initiative
      -> Delivery Unit
        -> Build Unit
```

Roadmap schedules and prioritizes. Domains describe persistent responsibility boundaries. Architecture describes technical structure.

Several Initiatives may run in parallel. Delivery Unit may collapse for small work. Build Unit is not necessarily independently deployable.

Generic project-planning `Layer` is legacy-compatible and deprecated. Existing Layer docs should be classified before migration.

## Recommended: separate global plus repository method

Install global guidance once in the global instruction location supported by the coding agent:

```powershell
Copy-Item D:\Repos\leap_agent_pack\templates\separated\global\AGENTS.md <global-instruction-path>\AGENTS.md
```

Use:

```text
D:\Repos\leap_agent_pack\templates\separated\global\AGENTS_Population_Prompt.md
```

The global file must remain reusable and contain no project facts.

Then install repository guidance:

```powershell
Copy-Item D:\Repos\leap_agent_pack\templates\separated\repo\AGENTS.md D:\Repos\my_project\AGENTS.md
```

Populate it with:

```text
D:\Repos\leap_agent_pack\templates\separated\repo\AGENTS_Population_Prompt.md
```

## Repository-only method

Copy the repository template to the project root and run the repository population Prompt.

Use this when global instructions are unavailable or the user wants LEAP only in one project.

## Combined local-trial method

```powershell
Copy-Item D:\Repos\leap_agent_pack\templates\combined\AGENTS.md D:\Repos\my_project\AGENTS.md
```

Then use:

```text
D:\Repos\leap_agent_pack\templates\combined\AGENTS_Population_Prompt.md
```

Populate only the Editable Repository Section. Do not alter the Locked Global Section or its markers.

## What repository population should identify

- project name, purpose, users, and maturity
- repository layout and technology stack
- setup and validation commands
- source-truth entry point
- Project Charter or equivalent Mission
- Strategic Outcomes
- Initiative registry
- Roadmap
- Domain map
- Architecture docs
- Delivery Unit and Build Unit docs or active Prompts
- contracts and dependencies
- legacy Layer docs requiring classification
- baseline freshness metadata
- security, privacy, data, testing, documentation, branch, and stop-condition rules

Do not invent missing facts. Use `TBD`, `Never`, `None`, or `Not established` where appropriate.

## Pinning and updates

The current `0.2.0` candidate is unreleased. Do not assume a release tag exists.

Before updating a downstream file:

1. Read its hidden Agent Pack metadata.
2. Compare it with `manifests/latest.json`.
3. Review local project and local-override sections.
4. Manually merge useful managed-section changes.
5. Preserve project-specific content.

See [`upgrade-guide.md`](upgrade-guide.md).
