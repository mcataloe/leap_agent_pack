# LEAP Agent Pack Customization Guide

Customize the repo-level `AGENTS.md` so it reflects the actual project.

## What Belongs In Repo-Level AGENTS.md

- Local setup commands.
- Test, lint, typecheck, format, and build commands.
- Source-of-truth docs.
- Architecture constraints.
- Security, data, and privacy rules.
- Project-specific stop conditions.
- Branch, commit, and PR expectations.

## What Does Not Belong

- The full LEAP methodology.
- Long product docs that should live under `docs/`.
- Secrets, credentials, private tokens, or personal data.
- Guessed commands or unsupported architecture assumptions.

## Modification Notes

Record meaningful local edits in the hidden metadata block:

```md
local_modification_notes: Added project setup commands and source-of-truth docs on 2026-05-29.
```

This helps future update checks distinguish expected local customization from accidental drift.

## Keep Guidance Small

Prefer links to canonical project docs over duplicating long content.

Good:

```text
Start with docs/00_start_here.md and docs/architecture/overview.md.
```

Avoid copying entire architecture or roadmap documents into `AGENTS.md`.
