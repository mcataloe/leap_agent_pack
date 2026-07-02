# LEAP Agent Pack Versioning

LEAP Agent Pack is versioned independently from the LEAP Framework because users copy and customize `AGENTS.md` files in downstream repositories.

## When the Agent Pack version changes

Update the Agent Pack when distributable execution guidance changes, including:

- template behavior
- project-documentation terminology
- managed, project, or local section structure
- population Prompt behavior
- metadata or manifests
- compatibility posture
- update or customization guidance

Do not require an Agent Pack update for every Framework documentation edit. Update it when the change materially affects coding-agent behavior or downstream template correctness.

## Semantic versioning

- **PATCH:** wording, links, and non-behavioral corrections.
- **MINOR:** backward-compatible new behavior, fields, templates, planning guidance, or examples.
- **MAJOR:** breaking template structure, marker, compatibility, or execution behavior.

## Tags

```text
leap-agent-pack-vX.Y.Z
```

Do not claim a version is released until its tag or GitHub release exists.

## Current candidate

```text
Version: 0.2.0-candidate
Status: unreleased
Compatible LEAP Framework: >=0.1.0 <1.0.0
```

The candidate includes:

- separated and combined installation scenarios
- baseline freshness guidance
- dependency and contract Recon adaptation
- current command routing
- canonical template path reconciliation
- Mission / Project Charter -> Strategic Outcome -> Initiative -> Delivery Unit -> Build Unit guidance
- Roadmap, Domain, and Architecture separation
- Delivery Unit collapse behavior
- legacy Layer compatibility and classification guidance

This hierarchy synchronization is backward-compatible at the template-structure level but may require a meaningful manual merge for downstream files that still instruct agents to execute numbered Layers sequentially.

## Release preparation

Before tagging:

1. Validate canonical template paths.
2. Validate section markers.
3. Confirm metadata versions and dates.
4. Confirm manifests match actual repository files.
5. Review examples and population Prompts.
6. Review Framework compatibility.
7. Confirm migration and upgrade guidance.
8. Create the tag only after the candidate is approved.
