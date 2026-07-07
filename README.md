# BRS Mode Test

A deterministic scaffold for **Body Recomposition Scoring** workflows.

This repo exists to prove the boring bit: if a daily ChatGPT workflow needs fixed scoring, exact output, strict reconciliation, and no stale-canon swamp creatures, those rules should live in versioned code rather than an ever-lengthening chat thread.

## What this currently does

This first pass implements the parts visible from the public example snippet:

- fixed 100-point BRS total from four pillars
- fixed pillar order: Sleep, Protein, Kcal, Tonal
- limiter ranking by points lost
- limiter tie order: Sleep → Kcal → Protein → Tonal
- deterministic BRS first-line rendering
- fail-closed validation for missing or impossible values
- fixture tests for the two supplied examples

It deliberately **does not invent** the missing private canon for sleep scoring, protein bolus scoring, kcal scoring, Tonal scoring, nested formatting, or vacation overrides. Those need to be added as explicit rules before the tool should calculate from raw daily logs.

## Quick start

```bash
python -m pip install -e .
python -m brs_mode examples/april_01.json
python -m brs_mode examples/april_08.json
pytest
```

## Example

```text
4/8 38 (Sleep/Tonal/Kcal/Protein) 🎯🎯P4G3
• Sleep 13/35 (5h31)
• Protein 14/25 (Bolus 8/15 (2B); Grams 8/10 (145g); Gap adjustment)
• Kcal 11/25 (NET 1295)
• Tonal 0/15 (Skipped)
```

## Shape of the eventual beast

The useful split is:

- **ChatGPT:** parse messy user notes, explain trends, help amend canon, call the tool.
- **This tool:** calculate, validate, render, and refuse to guess.

One borb for language. One deterministic rat engine for numbers.
