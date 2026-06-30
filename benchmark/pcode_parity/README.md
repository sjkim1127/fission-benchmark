# P-code Parity

Compares two raw p-code providers for the same binary/function address.

Providers are command templates that must print JSON to stdout. The initial
schema expects a list of p-code op objects:

```json
[
  {
    "seq": 0,
    "op": "INT_ADD",
    "output": {"space": "unique", "offset": "0x100", "size": 8},
    "inputs": [
      {"space": "register", "offset": "0x20", "size": 8},
      {"space": "const", "offset": "0x8", "size": 8}
    ]
  }
]
```

Use this stage as an admission gate before interpreting decompiler-similarity
numbers.
