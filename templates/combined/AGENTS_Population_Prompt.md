# LEAP Combined Local-Trial AGENTS.md Population Prompt

Use this after placing `templates/combined/AGENTS.md` at the repository root as `AGENTS.md`.

```text
You are helping adopt the current LEAP Framework using a combined local-trial AGENTS.md file.

Target file:
- AGENTS.md at the repository root.

Structure:
- Locked global section:
  <!-- LEAP_MASTER_GLOBAL_SECTION_START: DO NOT EDIT DURING REPO POPULATION -->
  <!-- LEAP_MASTER_GLOBAL_SECTION_END -->
- Editable repository section:
  <!-- LEAP_MASTER_REPO_SECTION_START: EDIT THIS SECTION ONLY DURING REPO POPULATION -->
  <!-- LEAP_MASTER_REPO_SECTION_END -->

Goal:
Populate only the editable repository section with verified project-specific
context. Preserve the locked global section and every boundary marker exactly.

Do not modify:
- the locked global section
- section markers
- application code
- tests
- product or strategy docs
- configuration
- any file other than root AGENTS.md unless separately approved

Before editing:
1. Inspect repository structure and current branch state.
2. Read the entire AGENTS.md file.
3. Treat the locked section as current reusable LEAP behavior.
4. Inspect README files, docs, package/build files, Architecture material,
   tests, schemas, CI, infrastructure, and other source-truth evidence.
5. Identify canonical, supporting, Draft, stale, archived, superseded,
   conflicting, and unknown sources.
6. Infer only what evidence supports.
7. Mark unsupported facts as TBD with the exact owner question.

Populate the editable section with:
- project name, purpose, type, maturity, users, and use cases
- repository layout and technology stack
- setup, development, format, lint, typecheck, test, and build commands
- infrastructure, data stores, queues, caches, and external dependencies
- LEAP Baseline State from evidence
- Mission / Project Charter path
- Strategic Outcomes path
- Initiative registry and active Initiative posture
- Roadmap path
- Domain map path
- Architecture docs path
- Delivery Unit and Build Unit documentation paths
- contract and schema paths
- legacy Layer docs requiring classification
- canonical and non-canonical document lists
- project Architecture, coding, data, contract, security, privacy,
  testing, documentation, branch, PR, and commit rules
- Recon and Planning Boundary Review expectations
- stop conditions requiring human review

Use this project-documentation model when material:

Mission / Project Charter
  -> Strategic Outcome
    -> Initiative
      -> Delivery Unit
        -> Build Unit

Treat Roadmap, Domain Map, and Architecture as separate views.

Rules:
- Several Initiatives may run in parallel.
- Roadmap placement does not permanently define Initiative identity.
- Initiatives and Domains are many-to-many.
- Delivery Unit may collapse for small work.
- Build Unit is not necessarily independently deployable.
- Generic project-planning Layer is legacy-compatible and deprecated.
- Preserve the LEAP name, Layered House Standard, LEAP LHS,
  qualified Architecture Layers, public paths, and compatibility references.
- Classify a legacy Layer before migration.

Baseline rules:
- Use only evidence-backed values.
- Use TBD, Never, None, or Not established when unknown.
- Do not invent reconciliation history.
- Do not claim a full reconcile unless this task performed one.
- Do not create leap.baseline.yaml unless explicitly authorized.
- Recommend machine-readable baseline tracking only when justified.
- An old date is not automatically a blocker; a recent date is not proof.

Editing rules:
- Preserve the combined-file structure.
- Preserve the locked section exactly.
- Keep the editable section concise and operational.
- Do not refactor application code.
- Do not create strategy docs during ordinary population.
- Do not blindly rename legacy Layer material.

After editing, return:
1. Confirmation that the locked section was unchanged.
2. Editable sections populated.
3. Evidence used.
4. Strategic and planning paths identified.
5. Unknowns left as TBD.
6. Contradictions, stale-doc risks, or legacy Layer classifications.
7. Recommended next Charter or Recon target.
8. Whether leap.baseline.yaml is recommended as follow-up.
```
