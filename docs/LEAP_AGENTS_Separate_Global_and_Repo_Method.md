# LEAP AGENTS.md Setup — Separate Global + Repo Method

Use this method when the user wants to install LEAP in the coding agent's global instruction location and maintain a separate repository-level `AGENTS.md` file per project.

For first-time evaluation inside one local repo, prefer the **Master Repo AGENTS.md local-trial method** from the main Quickstart. This separate method is best after the user is ready to make LEAP available across multiple repositories.

---

## Reference links

Primary framework reference:

- [LEAP Framework — main branch](/)

Template links:

- [Global AGENTS.md template](/templates/leap-global-AGENTS-file/AGENTS.md)
- [Repo AGENTS.md template](/templates/leap-repo-AGENTS-file/AGENTS.md)
- [Repository AGENTS.md Population Prompt](/templates/leap-repo-AGENTS-file/AGENTS_Population_Prompt.md)

---

## What the user does

This method uses two instruction files:

1. A global `AGENTS.md` file for reusable LEAP operating behavior.
2. A repo-level `AGENTS.md` file for one specific project.

### 1. Install the global AGENTS.md file

Download the global LEAP `AGENTS.md` template and place it in the global instruction location used by the coding agent.

Common locations:

| Agent / Tool | macOS / Linux | Windows |
|---|---|---|
| Codex-style AGENTS.md | `~/.codex/AGENTS.md` | `%USERPROFILE%\.codex\AGENTS.md` |
| Claude Code-style user memory | `~/.claude/CLAUDE.md` or tool-supported AGENTS import | `%USERPROFILE%\.claude\CLAUDE.md` or tool-supported AGENTS import |
| Other coding agents | Use the tool's documented global instruction location | Use the tool's documented global instruction location |

The global file should stay broad. It should explain LEAP behavior, source-of-truth discipline, Recon-first thinking, stop conditions, and safe agent handoff rules.

Do **not** put project-specific commands, architecture, secrets, or repo details in the global file.

---

### 2. Install the repo / project AGENTS.md file

Download the repo-level LEAP `AGENTS.md` template and place it at the root of the project repository:

```text
<repo-root>/AGENTS.md
```

The repo AGENTS.md file is where project-specific details belong, including:

- Project purpose.
- Tech stack.
- Local development commands.
- Test, lint, typecheck, format, and build commands.
- Source-of-truth docs.
- Architecture notes.
- Data model and API conventions.
- Security and secrets rules.
- Branch, worktree, and commit expectations.
- LEAP-specific repo workflow rules.

---

### 3. Populate the repo AGENTS.md file

Open the repository in the user's coding agent or code editor.

Then use this population prompt:

```text
templates/leap-repo-AGENTS-file/AGENTS_Population_Prompt.md
```

The prompt should update only the repository-level `AGENTS.md` file from actual repository evidence.

---

### 4. Run LEAP Recon

After the repo AGENTS.md file is populated, run Recon before asking the coding agent to implement anything.

Use the short launcher:

```text
Run LEAP Recon for the following functionality:

[DESCRIBE THE FEATURE, LAYER, BUGFIX, WORKFLOW, OR FUNCTIONAL AREA HERE]
```

The global and repo AGENTS files should provide the operating rules for Recon. The user should not need to paste the full Recon rules when using standard AGENTS.md behavior.

---

## Done state

The project is ready for normal LEAP use when:

- The global AGENTS.md or equivalent global instruction file is installed.
- The repo-level `AGENTS.md` file exists at the repository root.
- The repo-level `AGENTS.md` file has been populated from actual repo evidence.
- Unknowns are marked as `TBD`, not guessed.
- A LEAP Recon pass has been run for the first functionality target.
- The next implementation task has bounded scope, non-goals, validation expectations, and stop conditions.

---

## Short rule

```text
Global AGENTS.md teaches the agent how to think with LEAP.
Repo AGENTS.md teaches the agent how LEAP applies to this project.
Recon verifies reality before implementation.
Prompt only after Recon.
```
