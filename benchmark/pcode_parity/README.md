# P-code Parity

Compares raw p-code op sequences for one function address.

**Default:** Ghidra (`/pcode`) vs Fission (`/pcode`) over Docker HTTP.

## Schema

```json
[
  {
    "seq": 0,
    "op": "COPY",
    "output": {"space": "unique", "offset": "0x100", "size": 8},
    "inputs": [{"space": "register", "offset": "0x0", "size": 8}]
  }
]
```

Ops are compared primarily by opcode sequence after normalization:

- **Opcode names:** Ghidra `INT_SUB` and Fission `IntSub` both become `INTSUB`
  (underscore / CamelCase insensitive).
- **LOAD/STORE space id:** first input is an address-space selector whose const
  encoding differs across tools; it is stubbed out so pointer/value varnodes
  still compare.

Mismatch kinds: `op_kind` / `op_count` / `varnode` / `op_sequence`.

## Run

```bash
python -m benchmark.pcode_parity.run --limit 5
```
