# ABI / calling-convention parity

**Status:** scaffold — not yet a headline quality stage.

## Goal

Compare recovered parameter locations (RCX/RDX/stack) and return register
against Ghidra for Windows PE subjects.

## Schema (target)

```json
{
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

- `GET /abi?binary=...&addr=...` — until implemented, returns
  `{"status":"not_implemented"}` and the stage is **skipped**, never matched.

## Activation

```bash
# When adapters implement /abi:
python -m benchmark.abi_parity.run --limit 5
```
