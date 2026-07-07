from __future__ import annotations

from .models import Entry, Result

ORDER = ("Sleep", "Kcal", "Protein", "Tonal")
DISPLAY_ORDER = ("Sleep", "Protein", "Kcal", "Tonal")


def validate(result: Result) -> None:
    if not result.date:
        raise ValueError("date is required")
    if not result.markers:
        raise ValueError("markers are required")

    names = {entry.name for entry in result.entries}
    required = set(DISPLAY_ORDER)
    missing = required - names
    extra = names - required
    if missing:
        raise ValueError("missing entries: " + ", ".join(sorted(missing)))
    if extra:
        raise ValueError("unknown entries: " + ", ".join(sorted(extra)))

    for entry in result.entries:
        if entry.maximum < 0:
            raise ValueError(f"{entry.name}: maximum cannot be negative")
        if entry.value < 0 or entry.value > entry.maximum:
            raise ValueError(f"{entry.name}: value must be between 0 and {entry.maximum}")

    if result.total < 0 or result.total > 100:
        raise ValueError("total must be between 0 and 100")


def ordered_entries(result: Result) -> list[Entry]:
    by_name = {entry.name: entry for entry in result.entries}
    return [by_name[name] for name in DISPLAY_ORDER]


def limiters(result: Result) -> list[str]:
    if result.total == 100:
        return []

    order_index = {name: index for index, name in enumerate(ORDER)}
    ranked = sorted(
        result.entries,
        key=lambda entry: (entry.maximum - entry.value, -order_index[entry.name]),
        reverse=True,
    )
    return [entry.name for entry in ranked if entry.maximum - entry.value > 0]


def score(result: Result) -> Result:
    validate(result)
    return result
