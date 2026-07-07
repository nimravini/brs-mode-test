"""Deterministic BRS scaffold."""

from .formatting import render
from .models import Entry, Result
from .parser import load_json
from .scoring import score

__all__ = ["Entry", "Result", "load_json", "render", "score"]
