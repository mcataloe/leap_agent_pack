# LEAP Project Skill Population Prompt

Use this prompt **only** when the user elects to create a new, project-specific Skill. Standard LEAP Skills, including the canonical LEAP navigator, are ready to install and MUST NOT be rewritten per project.

## Agent request

You are initializing a project-specific Skill from the LEAP Agent Pack template.

Goal: define one reusable specialized capability aligned with the project's current source truth; do not change application code or introduce a new lifecycle phase.

1. Inspect project AGENTS.md, current branch/worktree, canonical docs, existing Skills, tests and real tools.
2. Check whether ordinary instructions or an existing Skill already suffice. If so, recommend no new Skill.
3. Establish evidence-backed name and concise positive/negative trigger description; use lowercase kebab-case and valid YAML frontmatter keys name and description.
4. Populate Use when, Do not use when, inputs, outputs, preconditions, scope, tools, permission ceiling, Always/Ask first/Never, procedure, verification and optional references.
5. Mark unresolved project-specific content TBD with a precise owner question; never invent tool permissions, environment state or security policy.
6. Preserve one canonical body. Platform-specific installed copies must trace back to it; do not use symlinks as the only Windows installation method.
7. Propose an explicit path and explain how the intended Codex/Claude native discovery location will be populated. Do not overwrite an existing Skill without approval.
8. Verify YAML metadata, local references, negative trigger examples, the permission ceiling, and one positive and one negative selection example.
9. Stop before any application changes, deployment, auth/data/contract changes, or destructive operations.

Return the Skill file contents or exact created path, inspected evidence, remaining TBDs, validation evidence and next step. Do not claim native automatic invocation was tested unless actual runtime sessions were exercised.
