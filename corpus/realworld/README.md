# Real-world strip suite (extension track)

**Status:** scaffold only — not part of the MVP public ranking.

This track is reserved for stripped third-party / multi-TU binaries evaluated
**separately** from the synthetic `dev` / `holdout` function suite.

## Policy

- Does **not** feed `correctness` ranking for the synthetic standard set until
  explicitly promoted.
- Prefer PE/ELF targets matching the oracle ABI in use.
- Prefer publicly redistributable binaries with clear licenses.
- Strip symbols (`strip`) is the default evaluation mode for this track.
- Semantic wrappers may be incomplete; report `no_wrapper` honestly.

## Layout

```
corpus/realworld/
  manifests/   # one JSON per subject family (empty until cases land)
  source/      # optional ground-truth sources when available
  binaries/    # built or vendored binaries (gitignored if large)
```

## Activation

```bash
# Reserved: will work once manifests are populated
python runner/runner.py --corpus realworld --run-mode local
```

Populate cases only after MVP surfaces (semantic/coverage/taxonomy/runtime) and
P0 original-binary + holdout publication paths are green.
