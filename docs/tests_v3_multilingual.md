# Tests v3 - E2E Simulations

## Multilingual Simulations

The E2E tests simulate eight users:

- Chinese manager preparing upward reporting
- English new manager giving feedback
- Japanese manager preparing 1:1
- German project manager diagnosing delivery risk
- French manager reflecting on motivation
- Spanish manager handling cross-team conflict
- Portuguese manager delegating a task
- Russian manager doing retrospective

Expected contract:

- language is recognized
- output language policy exists
- localized growth log labels exist
- scene type is supported
- suggested wording is required in the user's language

## Frequency and Duration Simulations

The tests simulate:

- one-off quick use
- weekly use
- twice-weekly use
- one-month pattern review
- six-month coaching cycle

Expected contract:

- weekly opening
- monthly pattern review
- quarterly context refresh
- anti-repetition
- open commitment follow-up

## Beginner Journey Simulation

The tests simulate a first-time user asking:

- what this skill does
- when to use it
- how to start
- where memory is stored
- how to install or validate it

Expected contract:

- `SKILL.md` has beginner sections
- test command is documented
- restart Codex after installation is mentioned

## Management Library Simulation

The tests simulate a user asking:

- "What management method should I use for this problem?"

Expected contract:

- management library exists
- it is classified by stage, stream/domain, application domain, and type
- it includes classical, behavioral, modern, contemporary, strategy, operations, HR, change, project, risk, communication, and problem-solving categories
