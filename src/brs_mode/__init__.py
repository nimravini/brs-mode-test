"""Deterministic Body Recomposition Scoring scaffold."""

from .formatting import render_brs
from .models import BRSResult
from .parser import load_brs_json
from .scoring import score_brs

__all__ = ["BRSResult", "load_brs_json", "render_brs", "score_brs"]
