#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def assert_contains(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label}: missing `{needle}`")


def test_required_files() -> None:
    required = [
        "SKILL.md",
        "agents/openai.yaml",
        "references/personal_context.md",
        "references/training_notes.md",
        "references/management_playbook.md",
        "references/reflection_log.md",
        "references/research_notes.md",
        "docs/spec_v1.md",
        "docs/plan_v1.md",
        "docs/task_v1.md",
        "docs/research_v1.md",
    ]
    for path in required:
        if not (ROOT / path).exists():
            raise AssertionError(f"required file missing: {path}")


def test_skill_frontmatter_and_trigger() -> None:
    skill = read("SKILL.md")
    if not skill.startswith("---\n"):
        raise AssertionError("SKILL.md must start with YAML frontmatter")
    assert_contains(skill, "name: management-growth-coach", "frontmatter")
    assert_contains(skill, "description:", "frontmatter")
    for phrase in [
        "management self-check",
        "team member",
        "upward reporting",
        "cross-team collaboration",
        "long-term management coaching",
    ]:
        assert_contains(skill, phrase, "trigger description")


def test_scene_protocol() -> None:
    skill = read("SKILL.md")
    for phrase in [
        "Classify the scene",
        "Identify likely blind spots",
        "Ask focused self-check questions",
        "Produce immediate actions",
        "Produce a growth log entry",
    ]:
        assert_contains(skill, phrase, "session protocol")
    for scene in [
        "task_delivery",
        "team_member",
        "upward_reporting",
        "cross_team_collaboration",
        "retrospective",
        "motivation",
        "delegation",
        "business_value",
        "learning_only",
    ]:
        assert_contains(skill, scene, "scene type")


def test_references_are_navigable() -> None:
    skill = read("SKILL.md")
    for ref in [
        "references/personal_context.md",
        "references/training_notes.md",
        "references/management_playbook.md",
        "references/reflection_log.md",
        "references/research_notes.md",
    ]:
        assert_contains(skill, ref, "reference navigation")


def test_disc_scenarios_have_guidance() -> None:
    skill = read("SKILL.md")
    training = read("references/training_notes.md")
    combined = f"{skill}\n{training}".lower()
    fixtures = json.loads(read("tests/scenario_fixtures.json"))
    for scenario in fixtures["disc_scenarios"]:
        assert_contains(combined, scenario["profile"].lower(), scenario["id"])
        assert_contains(combined, scenario["scene"].lower(), scenario["id"])
        for keyword in scenario["expected_keywords"]:
            assert_contains(combined, keyword.lower(), scenario["id"])


def test_six_month_usage_safeguards() -> None:
    skill = read("SKILL.md")
    playbook = read("references/management_playbook.md")
    log = read("references/reflection_log.md")
    combined = f"{skill}\n{playbook}\n{log}".lower()
    fixtures = json.loads(read("tests/scenario_fixtures.json"))
    sim = fixtures["six_month_simulation"]
    assert sim["weeks"] == 26
    assert sim["sessions_per_week"] in (1, 2)
    for safeguard in sim["expected_safeguards"]:
        assert_contains(combined, safeguard.lower(), "six-month simulation")


def test_growth_log_template_is_appendable() -> None:
    log = read("references/reflection_log.md")
    for field in [
        "Date",
        "Scene",
        "Facts",
        "Blind spot",
        "Decision",
        "Commitment",
        "Follow-up",
        "Playbook update",
    ]:
        assert_contains(log, field, "reflection log template")
    if not re.search(r"Append new entries", log, flags=re.IGNORECASE):
        raise AssertionError("reflection log must explicitly be appendable")


def test_disc_quality_contracts() -> None:
    skill = read("SKILL.md")
    training = read("references/training_notes.md")
    combined = f"{skill}\n{training}".lower()
    required_by_profile = {
        "d": ["escalation", "decision rights", "tradeoff", "stakeholder"],
        "i": ["relationship repair", "public feedback", "recognition", "belonging"],
        "s": ["silent resistance", "transition rhythm", "small step", "safety"],
        "c": ["quality concern", "definition of done", "decision record", "risk tier"],
    }
    for profile, phrases in required_by_profile.items():
        assert_contains(combined, profile, f"DISC {profile}")
        for phrase in phrases:
            assert_contains(combined, phrase, f"DISC {profile} quality")


def test_longitudinal_operating_rhythm() -> None:
    skill = read("SKILL.md")
    playbook = read("references/management_playbook.md")
    combined = f"{skill}\n{playbook}".lower()
    for phrase in [
        "weekly session opening",
        "monthly pattern review",
        "quarterly personal context refresh",
        "commitment follow-up",
        "playbook update criteria",
        "anti-repetition",
    ]:
        assert_contains(combined, phrase, "longitudinal rhythm")


def main() -> None:
    tests = [
        test_required_files,
        test_skill_frontmatter_and_trigger,
        test_scene_protocol,
        test_references_are_navigable,
        test_disc_scenarios_have_guidance,
        test_six_month_usage_safeguards,
        test_growth_log_template_is_appendable,
        test_disc_quality_contracts,
        test_longitudinal_operating_rhythm,
    ]
    for test in tests:
        test()
    print(f"{len(tests)} tests passed")


if __name__ == "__main__":
    main()
