from pathlib import Path

from brs_mode.formatting import render
from brs_mode.parser import load_json

ROOT = Path(__file__).resolve().parents[1]


def test_april_01_fixture_renders_without_limiters() -> None:
    result = load_json(ROOT / "examples" / "april_01.json")

    assert render(result).splitlines()[0] == "4/1 100 🎯🎯P4G3 Impressive 🏖️"


def test_april_08_fixture_renders_ranked_limiters() -> None:
    result = load_json(ROOT / "examples" / "april_08.json")

    assert render(result).splitlines()[0] == "4/8 38 (Sleep/Tonal/Kcal/Protein) 🎯🎯P4G3"
