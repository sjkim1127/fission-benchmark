# Decode Parity

Compares instruction decoder output before assembly formatting or p-code lift.

Providers must print JSON to stdout. The expected shape is a list of decoded
instruction objects:

```json
[
  {
    "address": "0x401000",
    "bytes": "48895c2408",
    "length": 5,
    "mnemonic": "mov",
    "prefixes": ["rex.w"],
    "modrm": "0x5c",
    "sib": "0x24",
    "displacement": "0x08",
    "immediate": null
  }
]
```

This is the first gate: bytes must decode to the same instruction lengths and
operand fields before assembly or p-code parity failures can be interpreted.
