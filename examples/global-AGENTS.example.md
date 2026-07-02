<!--
LEAP_AGENT_PACK_TEMPLATE:
  template: global-example
  version: 0.2.0-candidate
  compatible_leap_framework: ">=0.1.0 <1.0.0"
  source: https://github.com/mcataloe/leap_agent_pack
  last_updated: 2026-07-01
  local_modification_notes: Example only.
END_LEAP_AGENT_PACK_TEMPLATE
-->

<!-- LEAP_MANAGED_SECTION_BEGIN -->

# Example Global AGENTS.md - LEAP Operating Guidance

Use LEAP as the default operating model for software work unless more specific instructions apply.

## Lifecycle

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

LEAP LHS is the Layered House Standard Prompt format for staged execution, not a lifecycle phase.

## Project-documentation model

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

Roadmap schedules and prioritizes. Domains describe persistent responsibility boundaries. Architecture describes technical structure.

Several Initiatives may run in parallel. Delivery Unit may collapse for small work. Build Unit is not necessarily independently deployable.

Generic project-planning `Layer` is legacy-compatible and deprecated. Preserve the LEAP name, Layered House Standard, LEAP LHS, qualified Architecture Layers, public paths, and compatibility references.

## Default behavior

- Inspect repository evidence before editing.
- Identify Strategic Outcome and Initiative when material.
- Treat Roadmap placement as planning context, not permanent identity.
- Identify affected Domains and Architecture areas.
- Perform Planning Boundary Review.
- Implement only a bounded Build Unit or task.
- Run relevant validation and report checks not run.
- Stop rather than inventing product, Architecture, data, security, or compatibility decisions.

## Commit guidance

Prefer one Build Unit per commit where practical. Use Initiative, Delivery Unit, Build Unit, or task identifiers when available.

<!-- LEAP_MANAGED_SECTION_END -->
