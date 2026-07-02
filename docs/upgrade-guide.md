# LEAP Agent Pack Upgrade Guide

Use this guide to decide whether and how a downstream `AGENTS.md` should be updated.

Agent Pack updates are manual. Never overwrite project guidance automatically.

## Current canonical paths

| Scenario | Template | Population prompt |
|---|---|---|
| Separate global plus repository | `templates/separated/global/AGENTS.md` and `templates/separated/repo/AGENTS.md` | Both separated population prompts |
| Repository-only | `templates/separated/repo/AGENTS.md` | Repository population prompt |
| Combined local trial | `templates/combined/AGENTS.md` | Combined population prompt |

Older references to top-level `global/`, `repo/`, or `combined/` paths are documentation drift unless compatibility files are explicitly added later.

## Current model changes to review

The `0.2.0` candidate aligns guidance with:

```text
Mission / Project Charter
  -> Strategic Outcome
    -> Initiative
      -> Delivery Unit
        -> Build Unit
```

When upgrading, check whether the downstream file still:

- treats numbered Layers as the default sequential hierarchy
- combines Roadmap and Layer identity
- treats Domains as temporary workstreams
- defines Build Units as independently deployable
- lacks Delivery Unit collapse behavior
- uses Layer-based commit messages as the only convention

Preserve legitimate uses of:

- Layered Execution & Alignment Protocol
- Layered House Standard
- LEAP LHS
- qualified Architecture Layers
- legacy compatibility references

Classify legacy project Layer docs before migration.

## Compare versions

1. Read the hidden metadata in the downstream file.
2. Check `manifests/latest.json` and `manifests/compatibility.json`.
3. Compare the local managed guidance with the current template.
4. Identify project and local customizations.
5. Review Framework compatibility and migration notes.

## Safe update procedure

1. Back up or diff the downstream file.
2. Update only the Agent Pack-managed content.
3. Preserve project-specific sections and local overrides.
4. Preserve source-truth paths, commands, Architecture constraints, security rules, and stop conditions unless intentionally changed.
5. Reconcile Mission, Strategic Outcome, Initiative, Roadmap, Domain, Architecture, Delivery Unit, and Build Unit guidance.
6. Re-run the relevant population Prompt when project fields need reconciliation.
7. Verify that no legacy Layer was blindly renamed.
8. Validate section markers and links.
9. Record the Agent Pack version and meaningful local modifications.

## Update decision model

| Update type | Recommendation |
|---|---|
| PATCH | Optional unless it fixes a relevant defect. |
| MINOR | Recommended when the project uses the affected LEAP workflow or terminology. |
| MAJOR | Requires explicit review and migration planning. |

The hierarchy synchronization in the unreleased `0.2.0` candidate should be treated as a meaningful manual merge for projects actively using Layer-first planning guidance.
