# LEAP Agent Pack Customization Guide

Customize the repo-level `AGENTS.md` so it reflects the actual project.

## Setup Scenarios

| Scenario | Use when | Install this AGENTS.md | Also install global? | Population / initialization prompt | Notes |
| --- | --- | --- | --- | --- | --- |
| Recommended Separate Global + Repo Method | Reusable LEAP behavior belongs globally and project facts belong in each repo. | `repo/AGENTS.md` | Yes, `global/AGENTS.md` | `global/AGENTS_Population_Prompt.md` and `repo/AGENTS_Population_Prompt.md` | Customize only the repo file with project-specific facts. |
| Repo-Only Method | The project cannot or should not use global instructions. | `repo/AGENTS.md` | No | `repo/AGENTS_Population_Prompt.md` | Keep reusable LEAP behavior and project facts in the repo setup. |
| Combined Local-Trial Method | LEAP is being tested in one repo before global install. | `combined/AGENTS.md` | No | `combined/AGENTS_Population_Prompt.md` | Populate only the Editable Repository Section. |
| Compatibility / Legacy Paths | Older docs or downstream installs already use old paths. | Mapped compatibility template | Depends on mapped scenario | Paired compatibility prompt when present | Do not delete or rename compatibility paths. |

## What Belongs In Repo-Level AGENTS.md

- Local setup commands.
- Test, lint, typecheck, format, and build commands.
- Source-of-truth docs.
- LEAP Baseline State summary for Recon preflight.
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

Keep LEAP Baseline State small. It is a freshness signal for Recon, not a hard gate or running status log. If optional `leap.baseline.yaml` exists, treat that file as the canonical machine-readable baseline record and keep AGENTS.md as a short pointer/summary.
