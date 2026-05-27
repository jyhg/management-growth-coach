# Research v5 - Design Notes

## Reasoning

Local management knowledge is stable, fast, and aligned with the skill's existing playbook. Web research adds freshness, source attribution, and broader public best practices.

The risk is knowledge pollution. A single accepted answer may be helpful in context but not suitable for the stable library. Therefore accepted web knowledge should first be stored in `knowledge_inbox.md`.

## Trust Model

Prefer sources such as:

- official institutions
- universities
- recognized management publications
- original framework authors or organizations
- reputable books or publisher pages
- established consulting or professional bodies when the claim is practical and non-sensitive

Avoid:

- unattributed blog summaries
- SEO listicles
- content farms
- forum claims unless explicitly treated as anecdotal
- sources that require private or confidential context

## Confirmation Model

At the end of an answer using web research, ask:

1. Do you accept this answer?
2. If yes, should the external knowledge be saved to the local candidate inbox?

Acceptance should not automatically write to the stable library.

## Public Safety

The skill must not send sensitive details to web search. It should use generic queries such as:

- cross-functional project collaboration stakeholder alignment management framework
- constructive feedback model manager employee missed deadline
- psychological safety team conflict leadership

It should not include organization, product, personal, customer, local path, or internal metric details.
