# ABI / calling-convention parity

**Status:** active adapter surface — extension stage (not MVP headline ranking).

## Goal

Compare recovered parameter locations (RCX/RDX/stack) and return register
against Ghidra for Windows PE subjects.

## Schema

```json
{
  "status": "ok",
  "address": "0x140001530",
  "convention": "windows_x64",
  "parameters": [
    {"index": 0, "location": "rcx", "size": 8},
    {"index": 1, "location": "rdx", "size": 8}
  ],
  "return": {"location": "rax", "size": 8}
}
```

## Adapters

- Ghidra `GET /abi` — Function parameters / return `VariableStorage` → register
  names or `stack+0xN` (via `ExportParity` mode `abi`).
- Fission `GET /abi` — decomp C signature arity + Windows PE default slots
  (`rcx,rdx,r8,r9` / stack; 32-bit stack slots). Source field:
  `decomp_signature+windows_default`.

When either side returns `not_implemented` / empty, the stage is **skipped**,
never matched. Location mismatches (e.g. Ghidra stack recovery at `-O0` vs
Windows defaults) are scored honestly as `abi_locations` / `abi_param_count`.

## Activation

```bash
export FISSION_ENDPOINT=http://localhost:8007 GHIDRA_ENDPOINT=http://localhost:8001
python -m benchmark.abi_parity.run --limit 12
```
