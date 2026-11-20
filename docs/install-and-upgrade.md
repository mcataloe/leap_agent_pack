# Install, Upgrade, and Customize

First-time install steps are in the [README](../README.md#install). This page covers existing files, local changes, and versions.

## File structure

Every template uses the same markers:

| Marker pair | Owner | Edit during population? |
|---|---|---|
| `LEAP_MANAGED_SECTION_BEGIN` / `END` | Agent Pack (LEAP Core) | No; replace it wholesale on upgrade |
| `LEAP_PROJECT_SECTION_BEGIN` / `END` | Your repository | Yes |
| `LEAP_LOCAL_OVERRIDES_BEGIN` / `END` | An individual or team | Optional |

The hidden `LEAP_AGENT_PACK_TEMPLATE` comment at the top records the template, version, and `local_modification_notes`. Record meaningful local edits there so customization can be told apart from drift.

## Upgrade an existing AGENTS.md

Upgrades are manual. Never overwrite project guidance automatically.

1. Read the version in the downstream file's metadata comment and compare it with [`manifests/latest.json`](../manifests/latest.json). Check `breakingChanges` there.
2. Replace everything between the managed markers with the current template's managed section.
3. Keep the project section and local overrides. If the project section is long, move generic content out (LEAP Core now covers it) and keep only repository-specific facts and rules.
4. Update the metadata version and `last_updated`.
5. Ask the agent to quote the LEAP Core heading to confirm the file loads.

### From 0.2.0-candidate (or earlier) to 0.2.0-candidate.2

This is a breaking change to template structure.

- **Markers:** in combined files, rename `LEAP_MASTER_GLOBAL_SECTION_START` / `END` to `LEAP_MANAGED_SECTION_BEGIN` / `END`, and `LEAP_MASTER_REPO_SECTION_START` / `END` to `LEAP_PROJECT_SECTION_BEGIN` / `END`. Files that nest both schemes should keep only the new one.
- **Managed section:** replace with LEAP Core. The planning hierarchy, Planning Boundary Review, E0–E4 tiers, and the 13-step work pattern are no longer always loaded; they remain in the framework docs.
- **Project section:** the repository template now has seven short slots. Map old content as follows:

| Old section | New home |
|---|---|
| Project identity | Project |
| Strategic and planning sources | Project: one "work tracking / planning sources" line; detailed paths go in `docs/` |
| LEAP Baseline State table | Source truth: one "last reconcile" line |
| Repository layout, Technology stack | Layout and stack |
| Setup and validation commands | Commands |
| Architecture, data, contract, UX, AI, security rules | Project rules: keep only concrete, repository-specific rules |
| Stop conditions | Project stop conditions, each with an approver |
| Delivery system pointers, Advisory delivery estimates and source pointers | Project: "work tracking" and "allocation / capacity source" lines |
| Advisory delivery estimates (managed section) | Remove; the method is in the framework's [delivery estimation](https://github.com/mcataloe/leap_framework/blob/main/docs/team-delivery-estimation.md) doc |
| Generic testing, docs, completion, Charter, Recon rules | Remove; LEAP Core and the framework cover them |

When moving estimation guidance, keep the work tracker and allocation system authoritative. Fill the pointer lines only from verified sources; never move rosters, timesheets, or accepted estimates into `AGENTS.md`, and do not overwrite accepted estimates without separate authorization.

Keep the project section under about 800 words. Rules that are still `TBD` after population usually belong as open questions in `docs/`, not in a file every session loads.

## Customize safely

- Put project facts, paths, commands, and rules in the project section, never in the global file.
- Link to canonical docs instead of copying them into `AGENTS.md`.
- Each project rule should prevent a real failure and be concrete enough to check. Remove rules that never fire.
- Do not edit the managed section locally. Propose changes to [LEAP Core](https://github.com/mcataloe/leap_framework/blob/main/docs/leap-core.md) instead.
- Optional [execution role overlays](optional-execution-roles.md) and [continuity templates](execution-continuity.md) are extra context for tasks that need them. Do not copy them into the managed section.
- Native Skills: do not edit installed copies of the standard LEAP navigator. Write a separate project Skill with the [starter](../templates/skills/project-skill-starter/SKILL.md) instead.

## Versioning

The pack uses semantic versioning, independent of the framework.

- **Patch:** wording, links, and non-behavioral fixes.
- **Minor:** backward-compatible behavior, fields, or templates.
- **Major:** breaking marker, structure, compatibility, or behavior changes.

Every behavior change before a release bumps the candidate suffix (`0.2.0-candidate.2`, `.3`, and so on), so a downstream file can tell which revision it has. Tags use `leap-agent-pack-vX.Y.Z`. Do not call a version released until its tag exists.

Before tagging, run `python3 scripts/check_pack.py --framework ../leap_framework`. It checks markers, metadata versions and dates against the manifest, manifest-to-file consistency, links, size budgets, and LEAP Core drift.
