# LEAP Agent Pack Versioning

LEAP Agent Pack is versioned independently from the LEAP Framework.

The LEAP Framework can change methodology, prompts, docs, and roadmap more often. Agent Pack versions should change deliberately because users copy `AGENTS.md` files into local projects and may customize them.

## Version Rule

Update the Agent Pack only when the Codex execution adapter changes:

- AGENTS template behavior.
- Template metadata.
- Managed/project/local section structure.
- Compatibility manifests.
- Update or customization guidance.

Do not force an Agent Pack update for every LEAP Framework documentation change.

## SemVer

- PATCH: wording fixes, clarifications, link fixes, and non-behavioral docs updates.
- MINOR: new optional guidance, new examples, backward-compatible metadata fields, or optional templates.
- MAJOR: breaking changes to template structure, metadata, managed sections, or execution expectations.

## Tags

Agent Pack tags use:

```text
leap-agent-pack-vX.Y.Z
```

The initial version is:

```text
0.1.0
```

The initial compatibility range is:

```text
>=0.1.0 <1.0.0
```

## Current Reconciliation Posture

The current setup-scenario reconciliation is tracked as an unreleased `0.2.0` candidate. It adds optional global initialization guidance, clearer template inventory metadata, command shortcut coverage, and Dependency & Contract Recon adapter guidance without creating a release tag.

Do not claim `0.2.0` is released unless a tag or release is created separately.
