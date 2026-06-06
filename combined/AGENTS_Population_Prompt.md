# LEAP Master Repo AGENTS.md Population Prompt

Use this prompt inside a code assistant after placing the combined master `AGENTS.md` file at the root of a repository.

Copy/paste the prompt below into the code assistant for that repository.

```text
You are helping adopt the LEAP Framework in this repository using a combined local-trial AGENTS.md file.

Target file:
- `AGENTS.md` at the repository root.

Important structure:
- The file contains a locked global LEAP section and an editable repository section.
- The locked global section is delimited by:
  - `<!-- LEAP_MASTER_GLOBAL_SECTION_START: DO NOT EDIT DURING REPO POPULATION -->`
  - `<!-- LEAP_MASTER_GLOBAL_SECTION_END -->`
- The editable repository section is delimited by:
  - `<!-- LEAP_MASTER_REPO_SECTION_START: EDIT THIS SECTION ONLY DURING REPO POPULATION -->`
  - `<!-- LEAP_MASTER_REPO_SECTION_END -->`

Goal:
Populate only the editable repository section so this repo has accurate project-specific LEAP operating context.

Do not modify:
- The locked global section.
- The section boundary markers.
- Application code.
- Tests.
- Product docs.
- Configuration files.
- Any file other than the root `AGENTS.md`, unless I explicitly approve a separate change.

Before editing:
1. Inspect the existing repository structure.
2. Read the full root `AGENTS.md` file.
3. Treat the locked global section as read-only LEAP behavior.
4. Treat the editable repository section as the repo-specific AGENTS.md template to populate.
5. Identify available source-of-truth documents, such as README files, docs, architecture notes, package files, build files, compose files, infrastructure files, test configuration, and CI files.
6. Infer only what the repository evidence supports.
7. Do not invent commands, architecture, services, credentials, environments, workflows, business rules, or deployment assumptions.

Update only the editable repository section with:
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
- Preserve the combined master AGENTS.md structure.
- Preserve the locked global section exactly.
- Preserve all section boundary markers exactly.
- Keep the repo section concise, practical, and useful to a coding agent.
- Prefer verified repository evidence over assumptions.
- If something is unknown, mark it as `TBD` and include the exact question the project owner should answer.
- For LEAP Baseline State, populate fields from evidence when available. If unknown, use `TBD`, `Never`, `None`, or `Not established`.
- Do not invent reconcile history.
- Do not claim a full reconcile happened unless this prompt actually performed one.
- Do not create `leap.baseline.yaml` during normal AGENTS.md population unless explicitly authorized or the prompt includes an authorized baseline setup pass.
- If the repo clearly needs machine-readable baseline tracking, recommend optional `leap.baseline.yaml` as follow-up.
- Do not treat an old baseline date as an automatic blocker or a recent baseline date as proof that source truth is correct.
- Do not perform product implementation work.
- Do not refactor application code.
- Do not create new strategic docs unless I explicitly approve that separately.
- Do not remove useful repo-template sections unless they clearly do not apply.

After editing, return a short completion report with:
1. Confirmation that the locked global section was not changed.
2. Sections populated in the editable repo section.
3. Evidence used.
4. Unknowns left as `TBD`.
5. Any contradictions or stale-doc risks found.
6. Recommended next LEAP Recon target.
7. Whether optional `leap.baseline.yaml` is recommended as follow-up.
```
