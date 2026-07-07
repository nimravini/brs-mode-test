from __future__ import annotations

import argparse

from .formatting import render
from .parser import load_json
from .scoring import score


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Render a deterministic BRS report from JSON input.")
    parser.add_argument("path", help="Path to a JSON input file")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = score(load_json(args.path))
    print(render(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
