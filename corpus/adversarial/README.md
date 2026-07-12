# Adversarial / obfuscation suite

**Status:** active extension fixture — **never** default publication gate.

## Fixture

| Name | Source | Binary |
|------|--------|--------|
| CFF toy | `source/cff_toy.c` | `binaries/cff_toy_gcc_O0.exe` |

```bash
python scripts/build_extension_corpora.py
# structural stages only unless wrappers added:
# python -m runner.run_parity --corpus …  # not wired as default corpus
```

Policy: label `track=adversarial`; do not mix into MVP semantic denominators.
