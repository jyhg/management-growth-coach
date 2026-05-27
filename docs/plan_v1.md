# management-growth-coach Plan v1

## Development Approach

Use documentation-driven TDD:

1. Write spec, plan, tasks, and research notes.
2. Write failing tests that define expected skill behavior.
3. Implement the skill and reference files.
4. Run tests.
5. Fix gaps until tests pass.
6. Record validation results in docs.

## Git Principles

The current project directory is not a git repository. Until the user asks to initialize git, follow these principles manually:

- Keep all new work inside `skill-src/`.
- Do not modify the original training documents.
- Make changes in small reviewable increments and document why each increment exists.

If git is initialized later:

- Commit documentation and tests before implementation.
- Keep unrelated changes out of commits.
- Use clear commit messages that describe behavior, not only files.

## Skill Shape

`skill-src/` will be a complete skill folder:

```text
skill-src/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── docs/
├── references/
└── tests/
```

## Implementation Notes

- Keep `SKILL.md` concise and procedural.
- Move detailed knowledge into `references/`.
- Use deterministic tests that inspect required content and run scenario simulations.
- Treat long-term memory as append-only user context unless the user asks to revise.

## Validation

Run:

```bash
python3 skill-src/tests/run_tests.py
```

Passing tests indicate structural completeness, not real coaching quality. The scenario tests are designed to catch obvious gaps before manual use.
