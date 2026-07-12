# Strip / no-symbol track

**Status:** active extension track — not MVP headline ranking.

## Goal

Measure function discovery (Ghidra inventory vs Fission) on stripped PE, with
manifest address recall for known functions from the unstripped parent.

## Layout

```
corpus/realworld/
  manifests/strip_from_dev.json
  binaries/*_strip.exe
```

Build from selected `dev` PEs:

```bash
python scripts/build_strip_corpus.py --sources control_flow,math
```

## Policy

- Does **not** enter headline layered rates until explicitly promoted.
- Empty corpus → one `skipped` row (`strip_corpus_empty`).
- Primary status uses inventory set equality (names ignored for presence).
- Extra metrics: `manifest_recall` (Fission), `manifest_ref_recall` (Ghidra).

## Commands

```bash
export FISSION_ENDPOINT=http://localhost:8007 GHIDRA_ENDPOINT=http://localhost:8001
python scripts/build_strip_corpus.py
python -m benchmark.strip_track.run
```
