<!--
LEAP_AGENT_PACK_TEMPLATE:
  template: repo-example
  version: 0.2.0-candidate.2
  compatible_leap_framework: ">=0.1.0 <1.0.0"
  source: https://github.com/mcataloe/leap_agent_pack
  last_updated: 2026-10-21
  local_modification_notes: Example only.
END_LEAP_AGENT_PACK_TEMPLATE
-->

<!-- LEAP_MANAGED_SECTION_BEGIN -->

# Repository AGENTS.md

This repository uses LEAP. LEAP Core rules come from the global `AGENTS.md`. If that is not installed, use the combined template or read https://github.com/mcataloe/leap_framework/blob/main/docs/leap-core.md. Say `LEAP help` for the command list. Rules in this file take precedence over LEAP Core for this repository.

<!-- LEAP_MANAGED_SECTION_END -->

<!-- LEAP_PROJECT_SECTION_BEGIN -->

## Project

- Name: Example Verification Platform
- Summary: Organizations submit verification requests and receive traceable eligibility results.
- Start here: `docs/00_start_here.md`
- Work tracking / planning sources: Jira project `VER`; Strategic Outcomes and Initiatives in `docs/02_strategy/`

## Source truth

- Canonical docs: `docs/00_start_here.md`, `docs/04_architecture/`, `api/openapi.yaml`
- Draft, archived, or do-not-use docs: `docs/archive/`, `docs/drafts/`
- Last reconcile: 2026-07-01 via Brownfield Charter; known drift: `docs/gap-register.md`

## Layout and stack

- `web/`: React + TypeScript frontend
- `api/`: Node 20 + Express API, PostgreSQL via Knex
- `api/migrations/`: Knex migrations
- `infra/`: Terraform for AWS

## Commands

```bash
npm ci
npm test                 # unit tests; no services needed
npm run test:integration # needs local Postgres (docker compose up db)
npm run lint && npm run typecheck
npm run build
```

## Project rules

- Never edit a migration that has been applied; add a new one.
- `verification_request.id` and `org_id` are external identifiers. Do not change their format or generation.
- Keep every SQL query parameterized. No string-built SQL.
- `api/openapi.yaml` is the API contract. Update it in the same change as the handler.

## Project stop conditions

- Any change under `infra/` or to IAM policies: approver platform lead
- Any change to eligibility rules in `api/src/eligibility/`: approver product owner

## Branches and commits

- Branch from `main` as `VER-<ticket>-short-name`; one ticket per PR; squash merge.

<!-- LEAP_PROJECT_SECTION_END -->
