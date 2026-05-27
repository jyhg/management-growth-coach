# Plan v5 - Web Research Assisted Learning

## Principles

- Documentation first: write spec, plan, task, research, and test docs before implementation.
- TDD first: add E2E contract tests and see them fail before implementation.
- Local-first: use local knowledge before web research.
- Privacy-first: sanitize web queries before browsing.
- No direct knowledge pollution: accepted web knowledge goes to `knowledge_inbox.md`, not directly to `management_library.md`.
- Git discipline: run tests and safety scans before commit and push.

## Steps

1. Add v5 documentation.
2. Add v5 E2E fixtures for simulated user journeys.
3. Extend test runner with v5 contract tests.
4. Run tests and confirm expected failure.
5. Implement `SKILL.md` web-research workflow.
6. Add `references/knowledge_inbox.md`.
7. Extend `references/research_notes.md`.
8. Update README with web-research and persistence notes.
9. Run all tests.
10. Run public safety scans.
11. Commit and push to GitHub.

## E2E Simulation Types

- Cross-team collaboration: local knowledge plus web stakeholder-alignment research.
- Feedback conversation: local feedback method plus credible external feedback model.
- Long-term use: accepted web knowledge goes to inbox, repeated items can later be curated.
- Sensitive scenario: private company/project details must be removed from web query and not persisted.
