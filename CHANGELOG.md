# Changelog

All notable LEAP Agent Pack changes are documented here.

## 0.2.0-candidate.2 - Unreleased

Breaking template-structure change. See [Install, Upgrade, and Customize](docs/install-and-upgrade.md#from-020-candidate-or-earlier-to-020-candidate2).

### Changed

- Managed sections of the global and combined templates are now LEAP Core: about 600 words, embedded verbatim from the framework's `docs/leap-core.md`. LEAP Core adds the Materiality Gate with No Gate, the lightest-workflow ladder, Cleanup and Validation routing, and the four verification states. It drops the always-loaded planning hierarchy, Planning Boundary Review, E0–E4 tiers, and the 13-step work pattern.
- Repository template reduced from about 1,980 to 275 words of project-specific slots. Planning sources become one optional line, Baseline State becomes one line, and every stop condition names an approver.
- Combined template markers renamed to `LEAP_MANAGED_SECTION_*` / `LEAP_PROJECT_SECTION_*`, matching the separated templates. `LEAP_MASTER_*` markers are retired.
- Population prompts rewritten to match, with an 800-word budget for the project section.
- LEAP Core synced with the framework's current `docs/leap-core.md`: stop before changing (not only breaking) public contracts, APIs, schemas, or paths; stop before acting on an unclear business rule that would change the result; extend the existing implementation and add or update tests for changed behavior; `Failed` covers an unexplained out-of-scope change.
- Documentation collapsed into `README.md` (setups, per-tool table, macOS/Linux and Windows install), `docs/install-and-upgrade.md`, and `docs/skills-installation.md`.
- Manifests consolidated into `manifests/latest.json`.

### Added

- `scripts/check_pack.py` and a CI workflow: markers, metadata versus manifest, manifest-to-file consistency, LEAP Core drift (also against the framework), word budgets, links, and anchors.
- Per-tool setup table for Codex and Claude Code, and a "guardrails beyond instructions" section.

### Reconciled with `main` (#5–#9)

The work merged to `main` after #4 is kept and adapted to the slimmer structure:

- #5 advisory delivery estimates: the managed-section estimation rules give way to LEAP Core, which reaches the framework's `docs/team-delivery-estimation.md` on demand. The repository and combined project sections keep the work tracker pointer and gain an "allocation / capacity source" pointer. Population prompts record pointers only, never rosters, allocations, or accepted estimates.
- #6 template metadata dates: superseded by the `0.2.0-candidate.2` metadata.
- #7 `docs/native-delegation-adapters.md`, #8 `docs/optional-execution-roles.md` and role overlays, and #9 `docs/execution-continuity.md` and continuity templates: kept unchanged apart from links. All of `templates/execution/` is listed in `manifests/latest.json`, and the README links them under "Optional add-ons".
- Links that #5–#9 added to the removed quickstart, upgrade, customization, and versioning docs now live in the README and `docs/install-and-upgrade.md`.

### Removed

- `docs/quickstart.md`, `docs/LEAP_AGENTS_Quickstart.md`, `docs/LEAP_AGENTS_Separate_Global_and_Repo_Method.md`, `docs/upgrade-guide.md`, `docs/customization-guide.md`, `docs/versioning.md` (merged into the README and `docs/install-and-upgrade.md`).
- `manifests/template-inventory.json`, `manifests/compatibility.json` (merged into `manifests/latest.json`).
- `examples/global-AGENTS.example.md`, `examples/combined-local-trial-AGENTS.example.md` (identical to the templates).

## 0.2.0-candidate - Unreleased

### Added

- Added advisory delivery-capacity estimation rules to separated global/repo and combined templates, and external system-of-record pointers in editable project sections (#5).
- Extended population prompts to locate approved work-tracker and allocation sources without importing a live roster or individual activity history (#5).
- Added optional native multi-agent delegation adapters (#7), execution role overlays and context mapping (#8), and execution continuity templates (#9).

- Added optional native Skill installation, project Skill starter and evidence-based population prompt.
- Added minimal LEAP help and semantic routing behavior to global, combined and repository Agent Pack templates.
- Aligned missing LEAP Cleanup invocation in supported bootstrap tables.

- Added capability- and cost-aware execution routing to the global and combined templates.
- Added E0-E4 capability classes and the `Implemented — execution unverified` versus `Execution verified` distinction.
- Added distributed guidance for the current LEAP project-documentation model:

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

- Added explicit Roadmap, Domain Map, Architecture, Planning Boundary Review, Delivery Unit collapse, and legacy Layer classification guidance.
- Added parallel-Initiative and current traceability examples.
- Added migration notes to `manifests/latest.json` and compatibility details to `manifests/compatibility.json`.

### Changed

- Updated global, repository, and combined canonical templates.
- Required validation/capability analysis before execution-surface selection and prohibited cost optimization from weakening Definition of Done.
- Updated all three population Prompts.
- Replaced Layer-first sequential implementation guidance with Initiative, Delivery Unit, and bounded Build Unit behavior.
- Clarified that Roadmap is a scheduling and dependency view rather than permanent Initiative ownership.
- Clarified that Domains are persistent boundaries with many-to-many Initiative relationships.
- Clarified that Build Units are not necessarily independently deployable.
- Preserved the LEAP name, Layered House Standard, LEAP LHS, qualified Architecture Layers, public paths, and compatibility references.
- Updated examples, README, quickstart, upgrade, and customization guidance.
- Corrected manifests and navigation to use the repository's real canonical paths under `templates/separated/` and `templates/combined/`.
- Removed manifest claims that nonexistent top-level `global/`, `repo/`, `combined/`, or compatibility mirror files are canonical.

### Compatibility

- No release tag has been created.
- Existing downstream Layer-based guidance remains a supported migration input.
- Downstream updates remain manual and review-based.
- Project-specific and local-override sections must be preserved during updates.

### Previous unreleased candidate work

- Added setup-scenario guidance for separated, repository-only, and combined local-trial adoption.
- Added Agent Pack manifests and inventory.
- Added dependency and contract adapter guidance.
- Added LEAP Baseline State and Baseline Freshness Check guidance.
- Established the dedicated Agent Pack repository for distributable `AGENTS.md` templates.
