# Plan v3 - Multilingual Iteration

## Principles

1. Documentation first: write spec, plan, task, research, and test docs before implementation.
2. TDD first: add E2E scenario tests and see them fail before implementation.
3. Git discipline: keep changes scoped, test before commit, and commit coherent increments.

## Steps

1. Add v3 spec, plan, task, and research docs.
2. Add multilingual E2E scenario fixtures.
3. Extend the test runner with v3 E2E contract tests.
4. Run tests and confirm expected failure.
5. Refactor `SKILL.md` for beginner-friendly layout.
6. Add `references/language_policy.md`.
7. Add `references/language_templates.md`.
8. Add `references/management_library.md`.
9. Update existing references if needed.
10. Run tests.
11. Fix gaps.
12. Commit v3.

## Git Notes

- Do not touch files outside `skill-src`.
- Keep generated local files ignored.
- Commit the baseline, then commit v3 docs/tests, then implementation if practical.
