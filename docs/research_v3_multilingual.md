# Research v3 - Multilingual and Management Library

## Skill Layout Reference

Effective skills should:

- keep frontmatter concise and trigger-oriented
- make the workflow obvious
- keep `SKILL.md` lean
- move detailed reference material to `references/`
- include enough quick-start guidance for first-time users
- use progressive disclosure so advanced content is loaded only when needed

## Multilingual Design

Use one canonical skill protocol and route output language dynamically.

Rules:

- detect preferred language from the latest user message
- if mixed, use the language of the actual request
- if unclear, ask a short preference question
- output questions, advice, scripts, and growth logs in the user's language
- use English source material when it is more authoritative, then summarize in the user's language
- cite sources regardless of language

## Management Library Design

The library should be useful for quick selection, not encyclopedic reading.

Each entry should indicate:

- stage
- school or domain
- type
- representative ideas or people
- when to use
- example tools

The skill should choose 1-3 relevant frameworks per session and explain why.
