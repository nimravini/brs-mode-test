from dataclasses import dataclass


@dataclass(frozen=True)
class Entry:
    name: str
    value: int
    maximum: int
    note: str = ""


@dataclass(frozen=True)
class Result:
    date: str
    markers: str
    entries: tuple[Entry, ...]
    label: str = ""

    @property
    def total(self) -> int:
        return sum(entry.value for entry in self.entries)
