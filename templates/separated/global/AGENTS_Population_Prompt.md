# Global AGENTS.md Initialization Prompt

Use this after copying `templates/separated/global/AGENTS.md` into the coding agent's global instruction location.

## Goal

Install or verify reusable LEAP behavior without adding project-specific facts.

## Instructions

1. Confirm the global LEAP file is installed in the intended global instruction location.
2. Verify that it remains reusable across repositories.
3. Confirm it includes the current lifecycle:

   ```text
   LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
   ```

4. Confirm it recognizes the preferred project-documentation model:

   ```text
   Mission / Project Charter
     -> Strategic Outcome
       -> Initiative
         -> Delivery Unit
           -> Build Unit
   ```

5. Confirm it treats Roadmap, Domain Map, and Architecture as separate supporting views.
6. Confirm it allows Delivery Unit collapse for small work and does not define Build Units as necessarily independently deployable.
7. Confirm it treats generic project-planning `Layer` as legacy-compatible while preserving the LEAP name, Layered House Standard, LEAP LHS, qualified Architecture Layers, public paths, and compatibility references.
8. Do not add project-specific Architecture, commands, source-truth paths, business rules, repositories, Strategic Outcomes, Initiatives, Roadmaps, Domains, Delivery Units, Build Units, credentials, environments, or validation commands.
9. Direct project-specific content to the repository-level template and population Prompt.
10. For a one-repository trial, direct the user to the combined template and combined population Prompt.
11. If project-specific content is already present in the global file, report it and recommend moving it to repository guidance.

## Output

```text
Global AGENTS.md Initialization Summary
- Global file present:
- Current LEAP lifecycle present:
- Current project-documentation model present:
- Reusable guidance preserved:
- Project-specific content found:
- Recommended repository-level next step:
- Combined local-trial alternative needed:
```
