# Spec v3 - Multilingual and Management Library

## Purpose

Version 2 of the skill adds multilingual use, beginner-friendly structure, and a starter management knowledge library.

## Scope

The skill must support these languages:

- Chinese
- English
- Japanese
- German
- French
- Spanish
- Portuguese
- Russian

The skill must not duplicate the entire `SKILL.md` in every language. Instead:

- keep `SKILL.md` as the canonical operating protocol
- add a language policy reference
- add localized output field labels and style guidance
- keep reference file paths stable

## Beginner-Friendly Requirements

`SKILL.md` must be easy for first-time users to understand:

- brief "What this skill does"
- brief "When to use it"
- brief "Quick start"
- clear reference map
- clear session workflow
- clear memory behavior
- clear tests and installation note

## Management Library Requirements

Add a starter management library that classifies common management theory and tools by:

- historical development stage
- core school or stream
- application domain
- type: theory, methodology, philosophy, or tool

The library must include at least:

- classical management
- behavioral science
- modern management theory
- strategy management
- operations and quality management
- organization and HR management
- innovation and change management
- project/risk/communication/problem-solving tools
- contemporary frontier ideas

The skill must use the library as a selection guide, not as a theory dump.

## E2E User Simulation Requirements

Tests must simulate:

- different language users
- different management scenes
- different use frequencies
- different use durations
- beginner install and usage discovery
- management theory library navigation

The tests are deterministic file-based E2E contract tests. They verify that the skill has enough instructions to support the simulated user journeys.
