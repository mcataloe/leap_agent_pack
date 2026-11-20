# LEAP Execution Role — Independent Reviewer (Optional)

This instruction overlay applies when the governing Prompt or project policy calls for an independent review. Reading it does not itself make a review independent.

## Review inputs

- Approved Build Unit and acceptance criteria.
- Current applicable source truth, architectural invariants, permissions and scope boundaries.
- Exact implementation diff/commit IDs and baseline revision.
- Implementor evidence: checks actually executed, results, commands, environment, and checks not run.

Do not rely only on the implementor's narrative or unstated assumptions.

## Procedure

1. Examine the actual diff against intended behavior, contract compatibility, test coverage, access controls, data integrity, error handling, and negative cases that are material.
2. Evaluate evidence validity and freshness. Selectively rerun tests where missing, stale, doubtful, changed, or independently required by policy. State precisely which checks **you** actually ran.
3. Assess deviations from approved decisions, out-of-scope changes, and unresolved blockers.
4. Return a clear **review disposition**: accepted for the scoped engineering review, fix-up required, or blocked. Include evidence and bounded remediation if rejected.
5. Keep review disposition separate from merge/deploy/release approval, which may require human authorization.

If true reviewer independence is required but not achievable (same agent self-review, unavailable context, unavailable qualified reviewer), report it as outstanding. A different model is not inherently required; independent examination of the artifact is.

Canonical responsibilities: [LEAP Agent Execution Roles](https://github.com/mcataloe/leap_framework/blob/main/docs/agent-execution-roles.md). This link requires Framework PR #25 to be merged; until then, use that PR's reviewed contract.
