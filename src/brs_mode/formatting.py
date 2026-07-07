from __future__ import annotations

from .models import Result
from .scoring import limiters, ordered_entries, validate


TWO_EM_SPACES = "\u2003\u2003"


def render(result: Result) -> str:
    validate(result)

    ranked = limiters(result)
    limiter_text = ""
    if ranked:
        limiter_text = " (" + "/".join(ranked) + ")"

    label_text = f" {result.label}" if result.label else ""
    lines = [f"{result.date} {result.total}{limiter_text} {result.markers}{label_text}".rstrip()]

    for entry in ordered_entries(result):
        lines.append(f"• {entry.name} {entry.value}/{entry.maximum}" + (f" ({entry.note})" if entry.note else ""))

    return "\n".join(lines)
