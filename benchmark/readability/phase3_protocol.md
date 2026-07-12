# Human readability study — Phase 3 protocol

**Status:** ready for pilot (composite still **forbidden** until correlations land).

## Goal

Measure whether decompiler output helps humans recover:

1. Function purpose (free text → graded)
2. Correct I/O examples (multiple choice / write-in)
3. Bug localization time (seconds)

## Materials

- Function shortlist: `study_pack/functions.json`
- Exports: `python scripts/export_study_pack.py` → `study_pack/exports/`
- Answer sheet schema: `study_pack/answer_sheet.schema.json`
- Analysis: `python scripts/analyze_readability_study.py study_pack/responses/*.json`

## Design

- Within-subject: each participant sees **Ghidra** and **Fission** on **different** functions (counterbalanced).
- Between-subject arm optional for single-tool baseline.
- Time box: 8 minutes per function max.
- N target pilot: ≥12 participants; full: ≥30.

## Metrics (pre-registered)

| Metric | Definition |
|--------|------------|
| accuracy | fraction of graded items correct |
| time_sec | wall time until submit |
| confidence | 1–5 Likert |
| preference | forced choice Ghidra vs Fission after paired items |

**No composite score** is published until Spearman ρ with accuracy is estimated and documented in `composite_decision.md`.

## Ethics / ops

- No personal identifiers in response JSON (use participant_id tokens).
- Store raw responses under `study_pack/responses/` (gitignored recommended).
- Pilot must be labeled `pilot=true` in analysis output.
