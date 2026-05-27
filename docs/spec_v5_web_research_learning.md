# Spec v5 - Web Research Assisted Learning

## Goal

Add a controlled web-research workflow to the management growth coach.

The skill should answer with both:

- local initialized management knowledge
- public, credible web knowledge when useful

It must also ask the user whether the answer is accepted. If the user accepts and explicitly wants to save the new public knowledge, the skill should add it to a candidate knowledge inbox instead of directly modifying the stable management library.

## Core Workflow

1. Search local references first.
2. Classify the management scene.
3. Decide whether web research is needed.
4. Sanitize the web query before browsing.
5. Browse credible public sources.
6. Integrate local and web knowledge in one answer.
7. Cite external sources.
8. Ask whether the user accepts the answer.
9. If accepted and the user asks to save it, append a structured item to `references/knowledge_inbox.md`.
10. Periodically curate high-value inbox items into `references/management_library.md`.

## When To Browse

Browse when:

- the user explicitly requests web research
- the user asks for current or source-backed management knowledge
- local knowledge is insufficient for the scenario
- a specific framework needs authoritative clarification
- the answer would benefit from public best practices

Do not browse when:

- the user asks for a private internal judgment only
- the user explicitly says not to browse
- the query would expose personal, company, team, project, customer, or confidential details

## Sanitization

Before web search, rewrite the query into a generic management question.

The web query must remove:

- company names
- product names
- personal names
- internal project names
- team-specific details
- private metrics
- local file paths
- credentials or tokens

## Answer Structure

When web research is used, answer with:

- 场景判断
- 本地知识命中
- 外部可信资料补充
- 融合判断
- 下一步动作
- 可沉淀知识
- 确认问题

## Knowledge Persistence

Do not write directly to `management_library.md` after one accepted answer.

Use `references/knowledge_inbox.md` as an intermediate queue:

- Date
- Scene
- User question summary
- Sanitized web query
- Source title and URL
- Key insight
- Applicability boundary
- Relation to local knowledge
- User acceptance
- Suggested library action

## Acceptance Criteria

- v5 docs exist.
- E2E tests cover local-first search, sanitized web query, credible source use, integrated answer, user confirmation, and inbox persistence.
- `SKILL.md` explains the web-research workflow.
- `references/research_notes.md` explains source quality and query sanitization.
- `references/knowledge_inbox.md` exists and is append-only.
- Safety tests prevent sensitive terms from being stored in public docs.
