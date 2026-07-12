# Decode Parity — **RETIRED**

**Status: retired from the active benchmark suite.**

Adapters currently only synthesize “decode” from disasm with null
`modrm` / `sib` / `displacement` / `immediate` fields. Emitting a scored
stage would invent false quality signal.

## Policy (conservative)

- `runner.run_parity` **does not** write `results/decode_parity/` rows.
- Dashboard excludes decode from headline tables.
- CI fails if any decode **match** rows reappear under stub policy.
- Re-activate only when Ghidra **and** Fission export real decode fields.

## Manual / research only

```bash
# Optional research CLI (not part of CI or headline rates)
python -m benchmark.decode_parity.run --limit 5
```

When re-enabling, require:

1. Non-null structural fields on both adapters
2. Unit tests that stub payloads are **not** scored as match
3. Golden canaries for known decode gaps
