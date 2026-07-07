# Canon gaps

This repo only implements the visible example behaviour. The private scoring canon still needs to be supplied before this becomes a real calculator rather than a deterministic renderer.

## Known from snippets

- Total is 100 points.
- Component maximums are:
  - Sleep: 35
  - Protein: 25
  - Kcal: 25
  - Tonal: 15
- Limiter order is by points lost.
- Limiter tie order is Sleep → Kcal → Protein → Tonal.
- `Impressive` appears only at 100.

## Needed to calculate from raw logs

- Sleep points from sleep duration, target hits, timing, and any modifiers.
- Protein grams points.
- Protein bolus count points.
- Protein spacing/gap adjustment rules.
- Net kcal target band and partial-credit rules.
- Tonal points from workout data, rest days, vacation days, skips, hard sets, and tonnage.
- Exact nested formatting rules for sub-lines.

## Implementation rule

Do not guess these. Add them as versioned tests first, then implement the calculator.
