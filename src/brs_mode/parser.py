from __future__ import annotations

import json
from pathlib import Path

from .models import Entry, Result


def load_json(path: str | Path) -> Result:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    entries = tuple(
        Entry(
            name=item["name"],
            value=int(item["value"]),
            maximum=int(item["maximum"]),
            note=item.get("note", ""),
        )
        for item in data["entries"]
    )
    return Result(
        date=data["date"],
        markers=data["markers"],
        entries=entries,
        label=data.get("label", ""),
    )
