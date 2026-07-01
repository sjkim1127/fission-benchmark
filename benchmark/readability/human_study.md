# Human Readability Validation Plan

This study validates which automatic readability proxies are actually useful.
It is required before any final readability composite is shown in the dashboard.

## Study Design

- Select 8-12 functions covering recursion, string handling, pointer arithmetic,
  table/data-structure use, and state-machine-like control flow.
- For each function, prepare Fission output and comparison outputs from the core
  decompiler set.
- Recruit 12-20 participants.
- Use a within-subject design: each participant reviews multiple functions, but
  output order is counterbalanced with a Latin-square schedule.

## Tasks

Use objective comprehension questions rather than Likert ratings:

- Multiple choice: "Under which condition does this function return zero?"
- Short answer: "How many iterations can this loop execute for input N?"
- Multiple choice: "Which buffer or field is modified?"
- Short answer: "What is the recursive base case?"

For selected pairs, also ask a forced-choice question:

- "Which version was faster to understand?"

## Measurements

- Correct answer rate.
- Response time.
- Pairwise forced-choice preference.
- Optional self-reported familiarity, recorded only as a covariate.

## Analysis

Use mixed-effects models rather than simple averages:

- Random effects: participant and function.
- Fixed effects: decompiler and each Phase 1 proxy.
- Outcomes: correctness, response time, and pairwise preference.

For each proxy, report:

- Correlation with correctness.
- Correlation with response time.
- Direction of effect.
- Significance and confidence interval.

Only proxies with useful, non-reversed relationships survive into Phase 4.
Non-significant or reversed proxies remain raw diagnostic fields only.

## Problem Set Draft

Initial candidate functions should be chosen from the existing dev/holdout
corpus after inspecting current benchmark output:

| Category | Candidate Question |
|---|---|
| Recursion | Identify the base case and recursive step. |
| Loop/counting | Compute the number of loop iterations for a concrete input. |
| String handling | Identify when a terminator or mismatch is detected. |
| Pointer arithmetic | Identify which memory element is read or written. |
| State machine | Identify which branch transitions to a terminal state. |

The final question set should be committed with function names, decompiler
outputs, correct answers, and Latin-square assignment sheets before data
collection starts.
