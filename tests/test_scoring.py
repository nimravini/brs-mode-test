import pytest

from brs_mode.models import Entry, Result
from brs_mode.scoring import limiters, validate


def test_limiter_order_uses_points_lost_then_tie_order() -> None:
    result = Result(
        date="1/1",
        markers="X",
        entries=(
            Entry("Protein", 20, 25),
            Entry("Kcal", 20, 25),
            Entry("Tonal", 10, 15),
            Entry("Sleep", 30, 35),
        ),
    )

    assert limiters(result) == ["Sleep", "Kcal", "Protein", "Tonal"]


def test_validation_fails_closed_for_missing_entry() -> None:
    result = Result(
        date="1/1",
        markers="X",
        entries=(
            Entry("Sleep", 35, 35),
            Entry("Protein", 25, 25),
            Entry("Kcal", 25, 25),
        ),
    )

    with pytest.raises(ValueError, match="missing entries"):
        validate(result)


def test_validation_rejects_impossible_value() -> None:
    result = Result(
        date="1/1",
        markers="X",
        entries=(
            Entry("Sleep", 36, 35),
            Entry("Protein", 25, 25),
            Entry("Kcal", 25, 25),
            Entry("Tonal", 15, 15),
        ),
    )

    with pytest.raises(ValueError, match="between"):
        validate(result)
