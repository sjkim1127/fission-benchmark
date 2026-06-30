# Assembly Parity

Compares two instruction-listing providers for the same binary/function address.

Providers are command templates that must print JSON to stdout. The initial
schema expects a list of instruction objects:

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

Run example:

```bash
python -m benchmark.assembly_parity.run \
  --reference-command 'python tools/ref_asm.py {binary} {addr}' \
  --candidate-command 'python tools/fission_asm.py {binary} {addr}'
```
