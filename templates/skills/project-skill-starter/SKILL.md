---
name: project-skill-starter
description: Template for creating a project-specific reusable agent Skill; not an operational workflow. Initialize and rename before installing for normal use.
---

# Project-specific Skill template

**Status:** Template; not ready for runtime use.
**Source:** LEAP Agent Pack.
**Portability:** Portable Agent Skills metadata.

## Purpose

TBD: Describe one reusable, specialized capability. Do not create Skills for one-off instructions.

## Use when

- TBD: Evidence-backed positive trigger.

## Do not use when

- A normal response or existing LEAP workflow is sufficient.
- TBD: Project-specific exclusions.

## Inputs and outputs

- Required inputs: TBD.
- Expected outputs/evidence: TBD.

## Preconditions and boundaries

- Source-truth paths: TBD.
- Allowed scope: TBD.
- Disallowed scope: No permission escalation or unrelated mutations.
- Tools: TBD; never assume availability.
- Permission ceiling: TBD; always subordinate to project AGENTS.md and governing Prompt.

## Procedure

1. Read relevant canonical project sources and existing implementation.
2. TBD: Add validated domain procedure steps.
3. Produce evidence and identify unresolved exceptions.

## Verification

- TBD: Observable checks needed before claiming success.
- Report not-run checks and remaining risk.

## Human approvals

- Ask first before destructive or high-impact changes, security/data/contracts, or unapproved architecture.
- Never treat Skill invocation as authorization for broader repository modification.

## Portability

- Installation target: .agents/skills/<name>/SKILL.md or .claude/skills/<name>/SKILL.md as documented by each platform.
- Optional vendor-specific adaptations: TBD. Keep portable core authoritative.
