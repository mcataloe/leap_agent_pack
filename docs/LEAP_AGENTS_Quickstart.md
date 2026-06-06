# LEAP AGENTS.md Quickstart

Use this compatibility guide for the historical combined local-trial setup. For new installs, prefer `docs/quickstart.md`, which lists all canonical setup scenarios.

This historical Quickstart defaults to the **Master Repo AGENTS.md local-trial method**. The canonical current path for that scenario is `combined/AGENTS.md`; the older compatibility path remains `templates/leap-repo-AGENTS-file-complete/AGENTS.md`. This method uses one repository-root `AGENTS.md` file that contains both:

1. A locked global LEAP operating section.
2. An editable repository-specific section.

This lets users test LEAP inside one local repository before installing anything system-wide.

For users who prefer the recommended separate global + repo approach, see:

- [Separate Global + Repo AGENTS.md Method](/docs/LEAP_AGENTS_Separate_Global_and_Repo_Method.md)

# User Actions

There are two setup actions, then one first-use action.

### 1. Install the Master Repo AGENTS.md file

For new installs, copy `combined/AGENTS.md`. The compatibility mirror is [Master Repo AGENTS.md local-trial template](/templates/leap-repo-AGENTS-file-complete/AGENTS.md). Place the selected file at the root of the project repository:

```text
<repo-root>/AGENTS.md
```

This file intentionally combines two scopes:

1. **Locked Global Section** — reusable LEAP operating behavior.
2. **Editable Repository Section** — project-specific AGENTS.md content that should be populated from the current repository.

This is the recommended starter method because it lets the user test LEAP in one repository without changing global system behavior.

---

### 2. Populate the editable repo section

Open the repository in the user's coding agent or code editor.

Then use `combined/AGENTS_Population_Prompt.md`. The compatibility mirror is [Master Repo AGENTS.md population prompt](/templates/leap-repo-AGENTS-file-complete/AGENTS_Population_Prompt.md):

The prompt instructs the code assistant to:

- Preserve the locked global section.
- Preserve the section boundary markers.
- Update only the editable repository section.
- Populate project-specific values from actual repository evidence.
- Mark unknowns as `TBD` instead of guessing.

The output of this step should be a populated repository-root `AGENTS.md` file.

---

### 3. Run LEAP Recon on the functionality

After the editable repo section is populated, run a Recon pass before asking the coding agent to implement anything.

Use this short launcher:

```text
Run LEAP Recon for the following functionality:

[DESCRIBE THE FEATURE, LAYER, BUGFIX, WORKFLOW, OR FUNCTIONAL AREA HERE]
```

The Master Repo AGENTS.md file provides the operating rules for Recon. The user should not need to paste the full Recon rules when using standard AGENTS.md behavior.

Only after Recon is accepted should the user generate a final LEAP Prompt for implementation.

---

## Done state

The project is ready for normal LEAP use when:

- The Master Repo `AGENTS.md` file exists at the repository root.
- The locked global section is still intact.
- The editable repository section has been populated from actual repo evidence.
- Unknowns are marked as `TBD`, not guessed.
- A LEAP Recon pass has been run for the first functionality target.
- The next implementation task has bounded scope, non-goals, validation expectations, and stop conditions.

---

## Short rule

```text
Master Repo AGENTS.md lets users test LEAP locally before installing global instructions.
The locked global section teaches the agent how to think with LEAP.
The editable repo section teaches the agent how LEAP applies to this project.
Recon verifies reality before implementation.
Prompt only after Recon.
```

---

## LEAP reference links

Primary framework reference:

- [LEAP Framework — main branch](/)

Useful starting points:

- [Start Here](/docs/00_start_here.md)
- [LEAP for Humans](/docs/leap-for-humans.md)
- [Quick LEAP Brief](/docs/quick-leap-brief.md)
- [Current LEAP Framework Document](/docs/leap.md)
- [LEAP Recon Template](/templates/leap-recon-template.md)
- [LEAP Prompt Template](/templates/leap-prompt-template.md)

AGENTS.md local-trial template links:

- Canonical local-trial template: `combined/AGENTS.md`
- Canonical local-trial population prompt: `combined/AGENTS_Population_Prompt.md`
- [Master Repo AGENTS.md local-trial template](/templates/leap-repo-AGENTS-file-complete/AGENTS.md)
- [Master Repo AGENTS.md population prompt](/templates/leap-repo-AGENTS-file-complete/AGENTS_Population_Prompt.md)

Optional advanced setup:

- [Separate Global + Repo AGENTS.md Method](/docs/LEAP_AGENTS_Separate_Global_and_Repo_Method.md)

---
