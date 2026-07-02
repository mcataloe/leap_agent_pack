# Changelog

All notable LEAP Agent Pack changes are documented here.

## Unreleased - 0.2.0 candidate

### Added

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
