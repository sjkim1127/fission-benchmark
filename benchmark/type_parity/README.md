# Type recovery parity

**Status:** extension track (active).

Compare recovered return/parameter type *names* (Ghidra DataType vs Fission
decomp-signature types). Not a layout IoU yet — field-level struct recovery is
a follow-on tightening of this surface.

```bash
python -m benchmark.type_parity.run --limit 10
# or
python -m runner.run_extensions --limit 10
```
