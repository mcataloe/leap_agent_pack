# Repository AGENTS.md Population Prompt

Use this with the separate global-plus-repository AGENTS method after placing the repository template at the project root.

```text
You are helping adopt the current LEAP Framework in this repository.

Target file:
- AGENTS.md at the repository root.

Framework source:
- https://github.com/mcataloe/leap_framework

Goal:
Populate the repository AGENTS.md with verified project-specific context so
future Charter, Recon, Prompt, implementation, and Validation/Handoff work is
source-grounded, bounded, and aligned with the current project-documentation model.

Scope:
- Update only the repository-level AGENTS.md unless another file is explicitly approved.
- Do not modify global instructions.
- Do not perform product implementation.
- Do not create or rewrite strategy docs during ordinary population.

Before editing:
1. Inspect repository structure and current branch state.
2. Read the full repository AGENTS.md template.
3. Inspect README files, docs, package/build files, Architecture material,
   schemas, tests, CI, infrastructure, and other source-truth evidence.
4. Identify canonical, supporting, Draft, stale, archived, superseded,
   conflicting, and unknown documents.
5. Infer only what repository evidence supports.
6. Mark unsupported facts as TBD with the exact owner question.

Use this project-documentation model when material:

Mission / Project Charter
  -> Strategic Outcome
    -> Initiative
      -> Delivery Unit
        -> Build Unit

Treat these as separate views:
- Roadmap: timing, priority, milestones, dependencies, releases, status, parallelism.
- Domain Map: persistent responsibility and ownership boundaries.
- Architecture: technical structure and qualified technical Layers.

Rules:
- Several Initiatives may run in parallel.
- Roadmap placement does not permanently define Initiative identity.
- Initiatives and Domains are many-to-many.
- Delivery Unit may collapse for small work.
- Build Unit is bounded implementation and is not necessarily independently deployable.
- Generic project-planning Layer is legacy-compatible and deprecated.
- Preserve the LEAP name, Layered House Standard, LEAP LHS,
  qualified Architecture Layers, public paths, and compatibility references.
- Classify legacy Layer docs as Initiative, Delivery Unit, Build Unit,
  Domain, Architecture Layer, Phase, or mixed / unclear before migration.

Populate or reconcile:
- Project name, purpose, type, maturity, users, and use cases.
- Repository layout and technology stack.
- Setup, development, test, lint, typecheck, format, and build commands.
- Infrastructure, database, storage, queue, cache, and external dependencies.
- LEAP Baseline State values from evidence.
- Mission / Project Charter path.
- Strategic Outcomes path.
- Initiative registry path and active Initiative posture.
- Roadmap path.
- Domain map path.
- Architecture docs path.
- Delivery Unit and Build Unit documentation paths, when present.
- API, event, schema, and data-contract paths.
- Legacy Layer docs requiring classification.
- Canonical and non-canonical document lists.
- Security, privacy, secrets, and data-handling rules.
- Coding, Architecture, contract, testing, branch, PR, and commit conventions.
- Recon expectations and planning-boundary behavior.
- Prompt and implementation handoff expectations.
- Stop conditions requiring human review.

Baseline rules:
- Populate values only from evidence.
- Use TBD, Never, None, or Not established when unknown.
- Do not invent reconciliation history.
- Do not claim a full reconcile unless this task performed one.
- Do not create leap.baseline.yaml unless explicitly authorized.
- Recommend optional machine-readable baseline tracking only when justified.
- An old date is not automatically a blocker; a recent date is not proof of correctness.

Editing rules:
- Preserve template intent and section markers.
- Keep the file concise and operationally useful.
- Remove or mark non-applicable placeholders only when evidence supports doing so.
- Do not refactor application code.
- Do not blindly rename legacy Layer material.
- Do not convert Roadmap lanes into permanent Initiative identity.

After editing, return:
1. Sections populated.
2. Evidence used.
3. Strategic and planning paths identified.
4. Unknowns left as TBD.
5. Contradictions, stale-doc risks, or legacy Layer classifications.
6. Recommended next Charter or Recon target.
7. Whether leap.baseline.yaml is recommended as follow-up.
```
