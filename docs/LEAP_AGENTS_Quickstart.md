# LEAP AGENTS.md Combined Local-Trial Guide

Use this method to test LEAP inside one repository before installing separate global instructions.

For most long-term multi-repository use, prefer [`LEAP_AGENTS_Separate_Global_and_Repo_Method.md`](LEAP_AGENTS_Separate_Global_and_Repo_Method.md).

## Canonical files

- Combined template: `templates/combined/AGENTS.md`
- Combined population Prompt: `templates/combined/AGENTS_Population_Prompt.md`

Older references to top-level `combined/` or `templates/leap-repo-AGENTS-file-complete/` paths are not valid on the current branch unless compatibility files are explicitly added later.

## Structure

The combined file contains:

1. A Locked Global Section with reusable LEAP behavior.
2. An Editable Repository Section for project-specific facts.

During population:

- do not edit the Locked Global Section
- do not remove or rename boundary markers
- populate only the Editable Repository Section
- use repository evidence
- mark unsupported facts as `TBD`

## Current documentation model

```text
Mission / Project Charter
  -> Strategic Outcome
    -> Initiative
      -> Delivery Unit
        -> Build Unit
```

Roadmap is a planning view. Domains are persistent boundaries. Architecture is technical structure.

Several Initiatives may run in parallel. Delivery Unit may collapse for small work. Build Unit is not necessarily independently deployable.

Generic project-planning `Layer` is legacy-compatible and must be classified before migration.

## Install

```powershell
Copy-Item D:\Repos\leap_agent_pack\templates\combined\AGENTS.md D:\Repos\my_project\AGENTS.md
```

Then run:

```text
D:\Repos\leap_agent_pack\templates\combined\AGENTS_Population_Prompt.md
```

## Population expectations

The editable section should identify:

- project name, Mission, users, and maturity
- Strategic Outcomes and Initiative registry
- Roadmap, Domain map, and Architecture docs
- Delivery Unit and Build Unit paths
- legacy Layer classification candidates
- repository layout, technology stack, and commands
- source-truth status and baseline freshness
- contracts, dependencies, security, privacy, data, testing, and documentation rules
- branch, PR, commit, and stop-condition guidance

## First LEAP workflow

Run Charter when project direction, Strategic Outcomes, Initiative identity, Roadmap, Domains, Architecture, or source truth is unclear.

Run focused Recon when the baseline is sufficient and one Initiative, Delivery Unit, Build Unit, Domain, Architecture area, feature, dependency, contract, risk, or legacy Layer needs investigation.

## Moving beyond the trial

When LEAP becomes useful across several repositories:

1. Install `templates/separated/global/AGENTS.md` globally.
2. Install `templates/separated/repo/AGENTS.md` in each repository.
3. Move project-specific content from the combined Editable Repository Section into the repository template.
4. Do not copy project-specific facts into the global file.
