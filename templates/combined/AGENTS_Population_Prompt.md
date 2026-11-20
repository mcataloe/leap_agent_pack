# Combined AGENTS.md Population Prompt

Use this after placing `templates/combined/AGENTS.md` at the repository root as `AGENTS.md`.

```text
You are populating a combined LEAP AGENTS.md.

Target: AGENTS.md at the repository root, between
<!-- LEAP_PROJECT_SECTION_BEGIN --> and <!-- LEAP_PROJECT_SECTION_END -->.
The managed section (<!-- LEAP_MANAGED_SECTION_BEGIN --> ...
<!-- LEAP_MANAGED_SECTION_END -->) is LEAP Core. Do not edit it.

Before editing:
1. Inspect repository structure, current branch, and worktree state.
2. Read the whole target file.
3. Inspect README files, docs, build and package files, CI, tests, schemas,
   migrations, and infrastructure.
4. Separate canonical docs from draft, stale, archived, or conflicting ones.
5. Use only what evidence supports. Write TBD plus the exact owner question
   for everything else.

Populate the project section:
- Project: name, summary, start-here path, work tracking or planning sources
  (Jira, Azure DevOps, GitHub Projects, or doc paths), or "none".
- Source truth: canonical docs, do-not-use docs, last reconcile, known drift.
  Do not invent reconcile history.
- Layout and stack: one line per meaningful top-level path.
- Commands: install, test, lint/typecheck, build. Copy them from CI or
  package scripts. Name checks that need services, credentials, or a
  specific environment.
- Project rules: only concrete rules that prevent a real failure here
  (identity keys, migration immutability, contract shapes, security
  boundaries, files not to split). Skip generic advice; LEAP Core covers it.
- Project stop conditions, each with an approver.
- Branch, PR, and commit conventions.

Editing rules:
- Edit only the project section. Preserve every marker exactly.
- Keep the project section under about 800 words. Link to docs/ for detail.
- Delete placeholder lines that do not apply instead of leaving them empty.
- Do not modify application code, tests, docs, or configuration.
- Do not install or overwrite native Skills.

After editing, return:
1. Sections populated and the evidence used.
2. Unknowns left as TBD, with owner questions.
3. Contradictions or stale-doc risks found.
4. Project-section word count.
5. Recommended next LEAP step, if any (often none).
```
