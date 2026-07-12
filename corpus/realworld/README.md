# Real-world / multi-TU track

**Status:** active extension (not MVP ranking).

## Contents

| Fixture | Path | Notes |
|---------|------|-------|
| Strip-from-dev | `scripts/build_strip_corpus.py` | controlled Δ vs unstripped dev |
| Multi-TU util app | `source/util_*.c` → `binaries/util_app_*` | multi-object PE + strip twin |
| Manifests | `manifests/util_multi_tu.json`, `strip_from_dev.json` | |

```bash
python scripts/build_extension_corpora.py
python scripts/build_strip_corpus.py
python -m benchmark.strip_track.run
```

Policy: does not feed headline correctness until promoted. Prefer redistributable fixtures.
