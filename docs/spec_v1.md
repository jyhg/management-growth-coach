# management-growth-coach Spec v1

## Goal

Create a Codex skill that acts as a management growth coach for recurring self-check, reflection, learning, and memory building.

The skill must help the user:

- inspect management situations with the training notes from this project
- use external management knowledge when current or precise support is useful
- identify blind spots before giving advice
- convert reflection into concrete next actions
- save core learning as durable context for future sessions

## Source Context

The project provides two source documents:

- `../远航培训总结.md`
- `../1V1沟通汇报稿.md`

The skill should preserve the user's current growth themes:

- move from governance-only thinking to business value thinking
- move from after-the-fact handling to early risk sensing
- move from explaining reasons to giving plans, commitments, and closure
- pay attention to people, responsibility boundaries, pressure, and delivery risk
- turn one-off delivery into repeatable mechanisms and talent development

## Trigger

Use this skill when the user asks for:

- management self-check
- team member reflection
- 1:1 preparation or follow-up
- upward reporting preparation
- cross-team collaboration diagnosis
- project delivery review
- leadership learning and growth record
- long-term management coaching

## Required Interaction Protocol

The skill must not jump directly to advice. It should first classify the situation and ask for missing critical facts when needed.

Every session should follow this loop:

1. Classify the scene.
2. Identify likely blind spots.
3. Ask focused self-check questions.
4. Produce immediate actions.
5. Produce communication or reporting language when useful.
6. Produce a growth log entry for durable memory.

## Scene Types

The skill must support these scene types:

- task_delivery
- team_member
- upward_reporting
- cross_team_collaboration
- retrospective
- motivation
- delegation
- business_value
- learning_only

## DISC-Aware Coaching

The skill must adapt its prompts and advice for DISC-style behavioral tendencies.

Required member profiles:

- D: direct, fast, result-oriented, may resist long emotional processing
- I: expressive, relationship-oriented, may be sensitive to recognition and atmosphere
- S: stable, harmony-oriented, may avoid conflict or change
- C: analytical, quality-oriented, may need clarity, standards, and evidence

The skill must avoid stereotyping. DISC is a working hypothesis, not a label. It should ask for observed behavior before drawing conclusions.

## Long-Term Use

The skill is expected to be used 1-2 times per week for six months.

It must prevent these degradation risks:

- repetitive generic advice
- excessive logging without behavior change
- stale personal context
- confirmation bias from old reflections
- failure to follow up prior commitments
- over-indexing on one management framework

Each session should check for previous open commitments when the user references ongoing work. The skill should periodically summarize patterns and update the user's management playbook.

## External Research Boundary

The skill may browse the web when the user requests current knowledge, frameworks, references, or when the question would benefit from source attribution.

Research must:

- prefer primary or authoritative sources
- cite sources in the final answer
- convert theory into concrete management action
- avoid dumping broad management theory

## Persistent References

Required reference files:

- `references/personal_context.md`
- `references/training_notes.md`
- `references/management_playbook.md`
- `references/reflection_log.md`
- `references/research_notes.md`

## Acceptance Criteria

- Skill has valid `SKILL.md` frontmatter.
- Skill references all required durable context files.
- Skill instructs the agent to save growth log entries.
- Skill supports all required scene types.
- Skill includes DISC-aware coaching safeguards.
- Tests include multiple DISC profiles and management scenes.
- Tests include a six-month recurring-use simulation.
- Tests pass with a local deterministic test runner.
