<!--
LEAP_AGENT_PACK_TEMPLATE:
  template: repo
  version: 0.2.0-candidate.2
  compatible_leap_framework: ">=0.1.0 <1.0.0"
  source: https://github.com/mcataloe/leap_agent_pack
  last_updated: 2026-10-21
  local_modification_notes: Record downstream edits here.
END_LEAP_AGENT_PACK_TEMPLATE
-->

<!-- LEAP_MANAGED_SECTION_BEGIN -->

# Repository AGENTS.md

This repository uses LEAP. LEAP Core rules come from the global `AGENTS.md`. If that is not installed, use the combined template or read https://github.com/mcataloe/leap_framework/blob/main/docs/leap-core.md. Say `LEAP help` for the command list. Rules in this file take precedence over LEAP Core for this repository.

<!-- LEAP_MANAGED_SECTION_END -->

<!-- LEAP_PROJECT_SECTION_BEGIN -->

<!-- Keep this section under about 800 words. It loads every session. Link to docs/ for detail. Write TBD plus the exact owner question for anything evidence does not show. -->

## Project

- Name: `{{PROJECT_NAME}}`
- Summary: `{{ONE_PARAGRAPH_PROJECT_DESCRIPTION}}`
- Start here: `{{PATH_TO_SOURCE_TRUTH_ENTRYPOINT_OR_README}}`
- Work tracking / planning sources (if any): `{{JIRA_ADO_GITHUB_PROJECT_OR_DOC_PATHS_OR_NONE}}`
- Allocation / capacity source (if any): `{{ALLOCATION_OWNER_OR_SYSTEM_OR_NONE}}`

These are pointers only. Do not copy rosters, allocations, worklogs, or accepted estimates here. For effort or delivery estimates, follow [LEAP delivery estimation](https://github.com/mcataloe/leap_framework/blob/main/docs/team-delivery-estimation.md).

## Source truth

- Canonical docs: `{{CANONICAL_DOC_PATHS}}`
- Draft, archived, or do-not-use docs: `{{NON_CANONICAL_DOC_PATHS_OR_NONE}}`
- Last reconcile: `{{YYYY-MM-DD_OR_NEVER}}` via `{{Brownfield Charter / Governance / Manual}}`; known drift: `{{PATH_OR_NONE}}`

Do not invent reconcile history.

## Layout and stack

- `{{PATH}}`: `{{PURPOSE_AND_STACK}}`
- `{{PATH}}`: `{{PURPOSE_AND_STACK}}`

## Commands

```bash
{{INSTALL_COMMAND}}
{{TEST_COMMAND}}
{{LINT_OR_TYPECHECK_COMMAND}}
{{BUILD_COMMAND}}
```

Do not invent commands. Write `TBD` for unknown ones. Name any check that needs services, credentials, or a specific environment.

## Project rules

Rules that prevent a real failure in this repository: Architecture, data and migrations, contracts, security, UX, or AI behavior. Each rule should be concrete enough to check.

- `{{PROJECT_RULE_1}}`
- `{{PROJECT_RULE_2}}`

## Project stop conditions

- `{{STOP_CONDITION_1}}`: approver `{{OWNER_OR_ROLE}}`
- `{{STOP_CONDITION_2}}`: approver `{{OWNER_OR_ROLE}}`

## Branches and commits

- `{{BRANCH_PR_OR_COMMIT_RULE_OR_TBD}}`

<!-- LEAP_PROJECT_SECTION_END -->

<!-- LEAP_LOCAL_OVERRIDES_BEGIN -->
<!-- Optional local team or developer notes. Keep durable project guidance in the project section. -->
<!-- LEAP_LOCAL_OVERRIDES_END -->
