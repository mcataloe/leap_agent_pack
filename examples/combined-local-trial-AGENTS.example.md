<!--
LEAP_AGENT_PACK_TEMPLATE:
  template: combined-example
  version: 0.2.0-candidate
  compatible_leap_framework: ">=0.1.0 <1.0.0"
  source: https://github.com/mcataloe/leap_agent_pack
  last_updated: 2026-07-01
  local_modification_notes: Example only.
END_LEAP_AGENT_PACK_TEMPLATE
-->

# Example Combined Local-Trial AGENTS.md

This example shows the combined-file structure. The global section is reusable and locked; the repository section contains project facts.

<!-- LEAP_MASTER_GLOBAL_SECTION_START: DO NOT EDIT DURING REPO POPULATION -->

## Locked Global LEAP behavior

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

```text
Mission / Project Charter
  -> Strategic Outcome
    -> Initiative
      -> Delivery Unit
        -> Build Unit
```

Roadmap schedules and prioritizes. Domains are persistent boundaries. Architecture is technical structure.

Several Initiatives may run in parallel. Delivery Unit may collapse for small work. Build Unit is not necessarily independently deployable.

Generic project-planning `Layer` is legacy-compatible and deprecated. Preserve the LEAP name, Layered House Standard, LEAP LHS, qualified Architecture Layers, public paths, and compatibility references.

Before implementation, inspect repo reality, identify affected Domains and Architecture, perform Planning Boundary Review, define a bounded Build Unit, validate, and complete handoff.

<!-- LEAP_MASTER_GLOBAL_SECTION_END -->

<!-- LEAP_MASTER_REPO_SECTION_START: EDIT THIS SECTION ONLY DURING REPO POPULATION -->

## Example repository guidance

Project: `Example Verification Platform`

Source-truth entry point: `docs/00_start_here.md`

- Project Charter: `docs/01_charter/00_project_charter.md`
- Strategic Outcomes: `docs/02_strategy/01_strategic_outcomes.md`
- Initiative registry: `docs/02_strategy/02_initiative_registry.md`
- Roadmap: `docs/02_strategy/03_roadmap.md`
- Domain map: `docs/03_domains/00_domain_map.md`
- Architecture: `docs/04_architecture/00_architecture_overview.md`
- Delivery Units: `docs/05_delivery/`
- Build Units: `docs/06_build_units/`

Current work:

```text
SO-001 -> INIT-001 -> DU-001 -> BU-001
```

Validation:

```bash
npm run lint
npm run typecheck
npm test
npm run build
```

Stop for unapproved destructive data changes, auth changes, breaking contracts, unclear Initiative or Domain ownership, or ambiguous legacy Layer meaning.

<!-- LEAP_MASTER_REPO_SECTION_END -->
