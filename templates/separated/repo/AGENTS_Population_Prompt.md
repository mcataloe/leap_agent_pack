# Repository AGENTS.md Population Prompt

Repository path:

```text
templates/leap-repo-AGENTS-file/AGENTS_Population_Prompt.md
```

Use this prompt when using the **separate global AGENTS.md + repo AGENTS.md method**.

This prompt assumes:

1. The global LEAP `AGENTS.md` file has already been installed in the coding agent's global instruction location.
2. The repository-level LEAP `AGENTS.md` template has already been placed at the root of the target repository.
3. The code assistant has access to the target repository and can inspect its files.

Copy/paste the prompt below into the code assistant for the target repository.

```text
You are helping adopt the LEAP Framework in this repository using a separate repository-level AGENTS.md file.

Target file:
- AGENTS.md at the repository root.

Framework reference:
- Use the LEAP Framework main branch as the stable reference:
  /

Goal:
Populate this repository's AGENTS.md file with project-specific operating context so future LEAP Recon and LEAP Prompt work can be accurate, bounded, and source-grounded.

Scope:
- Update only the repository-level AGENTS.md file unless I explicitly approve another file change.
- Do not modify any global AGENTS.md file or system-wide instruction file.
- Do not perform product implementation work.

Before editing:
1. Inspect the existing repository structure.
2. Read the existing repository-level AGENTS.md template.
3. Identify available source-of-truth documents, such as README files, docs, architecture notes, package files, build files, compose files, infrastructure files, test configuration, and CI files.
4. Infer only what the repository evidence supports.
5. Do not invent commands, architecture, services, credentials, environments, workflows, business rules, or deployment assumptions.

Populate the AGENTS.md file with:
- Project name and purpose.
- Application type and current maturity, if discoverable.
- Primary users or use cases, if documented.
- Tech stack and major frameworks.
- Repository layout.
- Local setup commands.
- Development commands.
- Test, lint, typecheck, format, and build commands.
- Database, storage, queue, cache, or external service dependencies.
- Infrastructure and deployment notes.
- Source-of-truth documents and their status if known.
- Known stale, draft, archived, or conflicting documents if discoverable.
- LEAP Baseline State table values from repo evidence.
- Security, secrets, and data-handling rules.
- Coding conventions and architectural constraints.
- Branch, worktree, PR, and commit conventions.
- LEAP Recon expectations for this repo.
- LEAP Prompt / implementation handoff expectations for this repo.
- Stop conditions requiring human review.

Rules:
- Preserve the intent of the LEAP repository AGENTS.md template.
- Keep the file concise, practical, and useful to a coding agent.
- Prefer verified repository evidence over assumptions.
- If something is unknown, mark it as TBD and include the exact question the project owner should answer.
- For LEAP Baseline State, populate fields from evidence when available. If unknown, use TBD, Never, None, or Not established.
- Do not invent reconcile history.
- Do not claim a full reconcile happened unless this prompt actually performed one.
- Do not create `leap.baseline.yaml` during normal AGENTS.md population unless explicitly authorized or the prompt includes an authorized baseline setup pass.
- If the repo clearly needs machine-readable baseline tracking, recommend optional `leap.baseline.yaml` as follow-up.
- Do not treat an old baseline date as an automatic blocker or a recent baseline date as proof that source truth is correct.
- Do not refactor application code.
- Do not create new strategic docs unless I explicitly approve that separately.
- Do not remove useful template sections unless they clearly do not apply.

After editing, return a short completion report with:
1. Sections populated.
2. Evidence used.
3. Unknowns left as TBD.
4. Any contradictions or stale-doc risks found.
5. Recommended next LEAP Recon target.
6. Whether optional `leap.baseline.yaml` is recommended as follow-up.
```
