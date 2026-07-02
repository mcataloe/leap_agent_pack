# LEAP AGENTS.md Setup - Separate Global + Repository Method

Use this recommended method when LEAP should be available across several repositories while each project retains its own source truth, commands, Architecture, planning, and stop conditions.

## Canonical paths

- Global template: `templates/separated/global/AGENTS.md`
- Global initialization Prompt: `templates/separated/global/AGENTS_Population_Prompt.md`
- Repository template: `templates/separated/repo/AGENTS.md`
- Repository population Prompt: `templates/separated/repo/AGENTS_Population_Prompt.md`

Older references to top-level `global/` or `repo/` paths are not valid in the current repository.

## What belongs globally

The global file owns reusable behavior:

- LEAP lifecycle
- Materiality Gate
- evidence-first inspection
- project-documentation terminology
- Planning Boundary Review
- general safety, validation, and handoff rules

It must not contain project-specific facts.

## What belongs in each repository

The repository file owns:

- project identity and Mission
- Strategic Outcomes
- Initiative registry
- Roadmap
- Domain map
- Architecture docs
- Delivery Unit and Build Unit records
- legacy Layer classification candidates
- source-truth status
- repository layout and technology stack
- commands, dependencies, contracts, security rules, and stop conditions

## Current project-documentation model

```text
Mission / Project Charter
  -> Strategic Outcome
    -> Initiative
      -> Delivery Unit
        -> Build Unit
```

Roadmap schedules and prioritizes. Domains are persistent responsibility boundaries. Architecture is technical structure.

Several Initiatives may run in parallel. Delivery Unit may collapse for small work. Build Unit is not necessarily independently deployable.

Generic project-planning `Layer` is legacy-compatible and deprecated. Preserve the LEAP name, Layered House Standard, LEAP LHS, qualified Architecture Layers, public paths, and compatibility references.

## Installation

1. Copy the global template to the coding agent's supported global instruction location.
2. Run the global initialization Prompt.
3. Copy the repository template to the project root as `AGENTS.md`.
4. Run the repository population Prompt inside the target repository.
5. Review every `TBD`, source-truth conflict, and legacy Layer classification.
6. Run Charter when project direction or documentation ownership is unclear.
7. Run focused Recon when the baseline is fresh enough.

## Update policy

Update global and repository files independently.

- Preserve project and local sections.
- Manually merge managed guidance.
- Do not overwrite source-truth paths, commands, or project rules blindly.
- Review Agent Pack manifests and Framework compatibility.
- Do not globally rename legacy Layer terms.

See [`upgrade-guide.md`](upgrade-guide.md).
