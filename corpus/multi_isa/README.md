# Multi-ISA track (scaffold)

**Status:** reserved — not active until Windows PE official path is the default
gate for the org’s releases.

Planned:

- `arm64` / ELF subjects with explicit oracle ABI profiles
- Separate manifests under `corpus/multi_isa/manifests/`
- Do not mix PE and ELF in one official matrix without `target_abi` tagging

Activation (future):

```bash
# python runner/runner.py --corpus multi_isa --run-mode local
```
