# Benchmark Infrastructure Known Issues

Status: **Standard-set architecture** — public contract is MVP
(semantic / coverage / fail taxonomy / runtime + optional CFG secondary) with
extension tracks (holdout, cross-variant, human study, realworld-strip).
P0 reliability (original-binary oracle residual cases, official holdout
evidence, adapter boundary fidelity) still blocks publishable releases.

This benchmark tracks decompiler quality work. Infrastructure reliability fixes
take priority over new axes, composite rankings, or readability formula changes.

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

## Standard metric set

| Tier | Metric | Ranking? |
|------|--------|----------|
| MVP-1 | Semantic pass rate (`original_binary` when available) | **Yes — only** |
| MVP-2 | Coverage (attempted / adapter clean / boundary invalid / tested / no_wrapper) | Denominator |
| MVP-3 | Fail taxonomy (stable exclusive buckets) | Analysis |
| MVP-4 | CFG match (optional secondary from cfg_parity) | No |
| MVP-5 | Runtime (`time_ms`) | No |
| EXT-6 | Holdout + overfitting report | Release gate |
| EXT-7 | Cross-compiler / opt pivot | Analysis |
| EXT-8 | Human readability study | After validation |
| EXT-9 | Real-world strip suite (`corpus/realworld/`) | Separate track |

Envelope field: `summary.schema = "standard-set-v1"` from `runner/standard_summary.py`.

## Current Trust Boundaries

- Correctness rank uses **semantic evidence only** (test-case pass rate). Source
  similarity, structural penalty, AST similarity, and readability proxies are
  diagnostic axes and do not affect correctness or rank.
- Readability proxy evidence is reported separately and is not a validated
  readability score.
- AST parse coverage means the readability parser accepted the decompiler
  output; proxy evidence coverage only means the row contains proxy fields.
- Function boundary diagnostics must be checked before interpreting a
  decompiler-quality row. Whole-program / boundary-mismatch rows are treated as
  adapter-level failures via `invalid_output_reason`.
- Lower-level parity stages should be used before diagnosing Fission
  decompiler-output quality.
- Publication requires envelope v2 + official run mode + non-empty holdout +
  overfitting linkage + `oracle_subject: original_binary`. The runner now always
  sends corpus PE bytes + function address to the oracle so evidence is labeled
  `original_binary` when the PE map succeeds.

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

**Current status**: All 28 corpus functions (dev + holdout) have ≥5 semantic
wrappers in `runner/test_wrappers.py`, including string and memory-layout cases.

Priority actions:

- Keep `no_wrapper` visible as a separate category for future corpus additions.
- Prefer focused wrapper tests over larger corpus expansion.
- Add wrappers in the same PR that introduces new corpus functions.

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

### Benchmark-side (remaining P0)

1. **Original-binary oracle (implemented)** — Oracle maps the corpus PE under
   Wine and calls the function RVA as the reference side of the differential.
   Rebuild the oracle image after pull (`docker compose build oracle`).
   Residual risk: PE import/relocation edge cases on exotic binaries; keep
   fixture failures visible as `fixture_error`, not silent passes.
2. **Envelope-only official artifacts** — Migrate stale flat-list files with
   `scripts/migrate_legacy_results.py` for tooling; re-run the benchmark for
   real envelope v2 candidates. Never promote legacy migrations to Vercel.
3. **Holdout official run** — Holdout manifests are locked; CI executes holdout
   when manifests exist. Confirm a green official workflow produces
   `publication-verdict.json` with `publishable: true` before relying on Vercel.
4. **Adapter boundary fidelity** — Keep snowman / rev.ng / boomerang whole-program
   leakage marked invalid; prefer extraction fixes over silent normalization.

### Fission-side quality work

Use this repository to identify and preserve regressions, then move the fixes
into Fission releases.

Suggested priorities:

- `checksum`, `crc32`, and `rc4_*` compile/runtime failures.
- `count_bits` parity mismatches and intrinsic-dependent codegen.
- `clamp` and simple conditional branch recovery regressions.
- Calling convention and parameter naming clarity that affects output review.

---

## Additional Known Issues (filed 2026-07-11)

### Fission Adapter CLI Compatibility

The Fission adapter previously passed `--layer nir` unconditionally to
`fission_cli decomp`. CLI releases that do not support this flag rejected every
decompile request, causing all Fission rows to fail silently while CI still
published results and deployed to GitHub Pages.

**Fix in progress**: The adapter now probes `fission_cli decomp --help` at
startup and only adds optional flags (`--layer`, `--benchmark`, `--timeout-ms`)
when they are confirmed to be present. A CI validity gate was added to block
publication of runs where all Fission rows fail.

### Parity Runner Empty-Match False Positive

`run_parity.py` previously swallowed HTTP errors and timeouts, returning empty
arrays. Because comparators treat equal inputs as a match, a double-empty
response (both reference and candidate failed to fetch) was recorded as `match`.

**Fixed**: `fetch_parity_data()` returns typed `FetchResult`; empty pair guards
record `both_empty_invalid` / `*_empty`. Decode stage is **retired** until real
decoder fields exist.

### P-code space-selector policy

LOAD/STORE first input is a space *selector*. Ghidra and Fission encode table
ids differently. **Strict (CI primary)** abstracts selector offset to
`space_selector` while keeping space name + size. **Literal** dual metric keeps
raw ids for forensics. Never treat literal space-id mismatch alone as the only
reported rate.

### Incomplete extension stages

- `abi_parity` / `GET /abi`: scaffold (`not_implemented` → skip, never match).
- `strip_discovery` / `corpus/realworld`: scaffold until strip PE manifests land.
- Official `publication_gate` still requires real official holdout run +
  overfitting report (`scripts/check_publication_ready.py`).

### Holdout Corpus Lock

**Resolved (lock)**: `scripts/populate_holdout.py` applies a deterministic
80/20 function-level lock (`HOLDOUT_SEED=42`) and copies required sources and
binaries into `corpus/holdout/`. Dev manifests no longer contain locked
functions.

**Still open (evidence)**: Official publication still needs a real holdout
benchmark run (`results/holdout_latest.json` as envelope v2) plus a linked
overfitting report. Empty or legacy holdout results keep
`publication_gate` at `holdout_empty` / non-publishable.

### Summary Table Survivorship Bias

The previous summary table excluded error rows from the denominator, causing
decompilers with high failure rates to appear to have higher average scores
than they actually do.

**Fix in progress**: All attempted rows are now counted. The summary table
includes `Attempted`, `Valid`, `Adapter Fail`, and `Compile Fail` columns.
Decompilers where all attempts failed are marked with ⛔ instead of being
silently omitted from the ranking.
