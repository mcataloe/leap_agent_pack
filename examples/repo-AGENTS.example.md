<!--
LEAP_AGENT_PACK_TEMPLATE:
  template: repo-example
  version: 0.2.0-candidate
  compatible_leap_framework: ">=0.1.0 <1.0.0"
  source: https://github.com/mcataloe/leap_agent_pack
  last_updated: 2026-07-01
  local_modification_notes: Example only.
END_LEAP_AGENT_PACK_TEMPLATE
-->

<!-- LEAP_MANAGED_SECTION_BEGIN -->

# Example Repository AGENTS.md - Sample Project

## Project identity

Project: `Example Verification Platform`

Purpose: Help organizations submit verification requests and receive traceable eligibility results.

## Lifecycle and documentation model

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

Roadmap is a scheduling view. Domains are persistent responsibility boundaries. Architecture is technical structure.

## Baseline State

| Item | Value |
|---|---|
| Baseline record | `leap.baseline.yaml` |
| Last full reconcile | `2026-07-01` |
| Last reconcile mode | `Brownfield Charter` |
| Current source-truth entry point | `docs/00_start_here.md` |
| Baseline confidence | `High` |
| Known drift | See `leap.baseline.yaml` |

## Strategic and planning sources

- Project Charter: `docs/01_charter/00_project_charter.md`
- Strategic Outcomes: `docs/02_strategy/01_strategic_outcomes.md`
- Initiative registry: `docs/02_strategy/02_initiative_registry.md`
- Roadmap: `docs/02_strategy/03_roadmap.md`
- Domain map: `docs/03_domains/00_domain_map.md`
- Architecture: `docs/04_architecture/00_architecture_overview.md`
- Delivery plans: `docs/05_delivery/`
- Build Units and Prompts: `docs/06_build_units/` and `docs/08_prompts/`

Current example:

```text
Strategic Outcome: SO-001 - Reduce manual verification work
Initiative: INIT-001 - Self-Service Organization Verification
Delivery Unit: DU-001 - Submit and track verification request
Build Unit: BU-001 - Verification request data model
Affected Domains: Verification; Organization Records
Affected Architecture: API, persistence, and frontend workflow
```

## Project rules

- Several Initiatives may run in parallel.
- Do not treat Roadmap order as permanent hierarchy.
- One Initiative may touch several Domains.
- Build Units are implementation boundaries, not necessarily deployable releases.
- Classify legacy Layer docs before migration.
- Prefer one Build Unit per commit where practical.

## Stop conditions

Stop for unapproved schema destruction, auth changes, breaking contracts, unclear Domain ownership, unclear Initiative scope, or ambiguous legacy Layer meaning.

<!-- LEAP_MANAGED_SECTION_END -->

<!-- LEAP_PROJECT_SECTION_BEGIN -->

## Example project-specific commands

```bash
npm install
npm run lint
npm run typecheck
npm test
npm run build
```

## Example completion report

Report changes, traceability, files changed, validation, documentation updates, deviations, risks, and follow-up LEAP work.

<!-- LEAP_PROJECT_SECTION_END -->
