# Data-flow sink parity

**Status:** extension track (active).

Compares compact RETURN/STORE sink keys from Ghidra p-code vs Fission raw p-code.
Use with golden canaries for “CFG match but wrong value” triage.

```bash
python -m benchmark.dataflow_parity.run --limit 10
```
