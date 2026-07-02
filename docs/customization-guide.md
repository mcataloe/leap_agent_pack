# LEAP Agent Pack Customization Guide

Customize repository-level guidance so it reflects actual project evidence.

## Canonical templates

- Global reusable guidance: `templates/separated/global/AGENTS.md`
- Repository guidance: `templates/separated/repo/AGENTS.md`
- Combined local trial: `templates/combined/AGENTS.md`

## What belongs in repository guidance

- project name, Mission, users, and maturity
- source-truth entry point
- Project Charter or equivalent strategy
- Strategic Outcomes
- Initiative registry and active Initiative posture
- Roadmap path
- Domain map
- Architecture docs
- Delivery Unit and Build Unit paths
- legacy Layer docs requiring classification
- repository layout and technology stack
- setup and validation commands
- dependencies and contracts
- security, privacy, data, and ownership rules
- branch, PR, and commit conventions
- project-specific stop conditions

## What remains reusable global guidance

- lifecycle
- Materiality Gate behavior
- evidence-first repository inspection
- project-documentation terminology
- general planning-boundary rules
- general safety and validation expectations

Do not put project-specific facts in global instructions.

## Project-documentation customization

Use:

```text
Mission / Project Charter
  -> Strategic Outcome
    -> Initiative
      -> Delivery Unit
        -> Build Unit
```

Keep Roadmap, Domain Map, and Architecture separate.

Do not customize the model by:

- making Roadmap the permanent owner of Initiative identity
- treating temporary Initiatives as persistent Domains
- requiring Delivery Units for trivial work
- defining every Build Unit as independently deployable
- renaming all uses of `Layer`

A downstream project may retain legacy Layer docs. Record what each Layer actually represents and add canonical links before moving or renaming public paths.

## Keep guidance compact

Prefer links to canonical project docs over copying long content.

Good:

```text
Start with docs/00_start_here.md.
Strategic Outcomes: docs/02_strategy/01_strategic_outcomes.md
Initiative registry: docs/02_strategy/02_initiative_registry.md
Roadmap: docs/02_strategy/03_roadmap.md
Domain map: docs/03_domains/00_domain_map.md
Architecture: docs/04_architecture/00_architecture_overview.md
```

Avoid copying entire strategy, Roadmap, Domain, or Architecture documents into `AGENTS.md`.

## Baseline State

Keep Baseline State small. It is a Recon freshness signal, not a running status log.

When optional `leap.baseline.yaml` exists, use it as the canonical machine-readable record and keep `AGENTS.md` as a concise pointer.

Do not invent reconciliation dates or silently update baseline metadata during ordinary implementation.

## Modification notes

Record meaningful local edits in the hidden metadata block, for example:

```text
local_modification_notes: Added project source-truth paths and validation commands on 2026-07-01.
```

This distinguishes expected customization from accidental Agent Pack drift.
