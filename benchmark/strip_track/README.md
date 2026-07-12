# Strip / no-symbol track

**Status:** scaffold — separate extension track, not MVP headline ranking.

## Goal

Measure function discovery and (later) semantic drop when symbols are stripped,
matching real reverse-engineering conditions.

## Layout

```
corpus/realworld/
  manifests/     # subjects pointing at stripped PE/ELF
  binaries/      # gitignored large artifacts
  source/        # optional
```

## Policy

- Does **not** enter headline layered rates until explicitly promoted.
- Report `skipped_no_corpus` when no strip manifests/binaries exist.
- Prefer same sources as `dev` built with `strip` for controlled Δ metrics.

## Commands

```bash
python -m benchmark.strip_track.run --limit 5
# When corpus is populated:
# python runner/runner.py --corpus realworld --run-mode local
```
