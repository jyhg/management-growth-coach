# Tests v5 - E2E Web Research Learning

## Simulated Journeys

### Local plus web answer

User asks a cross-project collaboration question. The skill must use local collaboration checklists first, then web research for public stakeholder-alignment knowledge.

Expected:

- local-first instruction
- sanitized web query
- credible source preference
- integrated answer structure
- source citation requirement

### Confirmation and persistence

User accepts the answer and asks to save it. The skill must write to `knowledge_inbox.md`, not directly to `management_library.md`.

Expected:

- explicit acceptance question
- explicit save question
- append-only inbox template
- no direct stable-library write

### Sensitive context

User includes private company, product, team, project, or path details.

Expected:

- sanitize before browsing
- do not persist sensitive details
- store only generalized question summary

### Long-term use

After repeated accepted web findings, the skill may suggest curating patterns into the stable library.

Expected:

- repeated-source or repeated-pattern criteria
- applicability boundary
- relation to local knowledge
