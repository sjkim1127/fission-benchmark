# Benchmark Infrastructure Known Issues

Status: infrastructure freeze, reliability fixes only.

This benchmark is now mature enough to act as a measuring instrument for
Fission quality work. New benchmark axes, new decompiler backends, and new
ranking formulas should be deferred unless they directly fix a trust problem in
existing results.

## Operating Policy

Allowed changes:

- Fix adapter errors, empty outputs, or broken health checks.
- Fix function boundary mismatches and whole-program output leakage.
- Add missing semantic wrappers for functions already present in the corpus.
- Keep CI/CD pulling the intended Fission release and publishing usable Pages
  artifacts.
- Correct misleading dashboard labels when the underlying metric semantics are
  already present.
- Add golden repros for confirmed Fission regressions found by the benchmark.

Deferred changes:

- Adding more decompilers to the default comparison set.
- Adding new composite rankings or weights.
- Treating readability proxies as a final readability score before the human
  comprehension study validates them.
- Expanding dashboard scope beyond result interpretation and triage.
- Using source similarity, AST similarity, or readability proxies as a
  substitute for semantic correctness.

## Current Trust Boundaries

- Correctness is based on semantic compile-and-run checks plus a small
  similarity and structural component.
- Readability proxy evidence is reported separately and is not a validated
  readability score.
- AST parse coverage means the readability parser accepted the decompiler
  output; proxy evidence coverage only means the row contains proxy fields.
- Function boundary diagnostics must be checked before interpreting a
  decompiler-quality row.
- Lower-level parity stages should be used before diagnosing Fission
  decompiler-output quality.

## Known Issues

### Adapter Reliability

Some backend adapters can still return invalid decompiler output while the HTTP
request itself succeeds. These rows must remain visible as adapter or boundary
diagnostics instead of being hidden behind output coverage.

Priority actions:

- Keep invalid-output diagnostics strict.
- Prefer marking bad rows invalid over normalizing suspicious output silently.
- Add golden repros when a bad adapter output pattern is confirmed.

### Function Boundary Fidelity

Whole-program or wrong-function output invalidates per-function comparisons even
if the output is large and parseable. Snowman, rev.ng, and older Boomerang paths
are the main risk areas because their tools are less naturally function-address
oriented.

Priority actions:

- Preserve direct-function, needs-normalization, boundary-mismatch, and
  whole-program counters.
- Treat repeated identical outputs across functions as suspicious.
- Do not use rows with boundary diagnostics as strong evidence for Fission
  quality decisions.

### Semantic Wrapper Coverage

Semantic correctness is only meaningful for functions with executable wrappers.
Missing wrappers should be handled as benchmark debt, not as decompiler failure.

Priority actions:

- Keep `no_wrapper` visible as a separate category.
- Add wrappers for existing corpus functions before adding new corpus breadth.
- Prefer focused wrapper tests over larger corpus expansion.

### Fission Release Tracking

The benchmark must test the intended Fission release. If CI or Docker cache keeps
an older `fission_cli`, benchmark numbers become stale even when CI is green.

Priority actions:

- Keep release-triggered benchmark runs wired to the Fission release pipeline.
- Verify `/health` exposes the expected Fission version in benchmark logs.
- Avoid relying on Docker cache as proof that the latest release is installed.
- CI must set `FISSION_SOURCE=release` and fail if `/health` reports `source=local`.
- Local current-build mounts (`docker-compose.local.yml`, `scripts/prepare_local_fission.sh`)
  are for quality-loop observation only; never promote `results/local_*.json` to
  Pages / `results/latest.*`.
- Focused local runs must pass `--no-publish`; use `--function NAME` to avoid
  running unrelated corpus rows while validating a semantic fix.

### Dashboard Semantics

The dashboard should explain evidence without implying unsupported conclusions.
The current split is intentional:

- Correctness: semantic-gated correctness score.
- Proxy Evidence: row contains readability proxy fields.
- AST Parse Coverage: parser accepted output for AST-based proxy extraction.
- Readability Proxy: unvalidated evidence only.

Priority actions:

- Keep correctness and readability separate.
- Do not add a final readability score before Phase 3 human validation.
- Keep generated dashboard artifacts reproducible from `results/latest.json`.

### Generated Result Conflicts

CI and local work can both update `docs/index.html`, `results/latest.json`, and
`results/latest.md`. Rebase conflicts in these files are expected when remote
benchmark results changed.

Priority actions:

- Rebase onto `origin/main`.
- Keep the newer remote benchmark data unless there is a clear reason to
  replace it.
- Regenerate reports with `python runner/render_report.py --input
  results/latest.json --corpus dev --update-latest`.

## Next Engineering Focus

The next useful work should happen in Fission itself, not by broadening the
benchmark. Use this repository to identify and preserve regressions, then move
the fixes into Fission 0.1.2 work.

Suggested Fission-side priorities:

- `checksum`, `crc32`, and `rc4_*` compile/runtime failures.
- `count_bits` parity mismatches and intrinsic-dependent codegen.
- `clamp` and simple conditional branch recovery regressions.
- Calling convention and parameter naming clarity that affects output review.
