# String / constant recovery

**Status:** extension track (active).

Referenced string literals from Ghidra data xrefs. Fission currently returns an
empty set (`source=not_recovered`) so mismatches are expected until the product
emits xrefs — scored honestly, never faked.

```bash
python -m benchmark.string_recovery.run --limit 10
```
