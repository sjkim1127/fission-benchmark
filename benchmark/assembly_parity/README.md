# Assembly Parity

Compares instruction listings for the same binary/function address.

**Default:** Ghidra (`/disasm`) vs Fission (`/disasm`) over Docker HTTP.

## Schema

```json
[
  {
    "address": "0x401000",
    "bytes": "48895c2408",
    "mnemonic": "mov",
    "operands": "[rsp + 8], rbx",
    "length": 5,
    "fallthrough": "0x401005",
    "branch_target": null
  }
]
```

Comparison normalizes hex bytes (strip spaces), addresses, and mnemonics; free-form
operands are ignored to avoid false mismatches.

## Run

```bash
export FISSION_HOST_PORT=8007   # if fission is not on 8000
python -m benchmark.assembly_parity.run --limit 5
```

Custom tools:

```bash
python -m benchmark.assembly_parity.run \
  --reference-command 'python tools/ref_asm.py {binary} {addr}' \
  --candidate-command 'python tools/cand_asm.py {binary} {addr}'
```
