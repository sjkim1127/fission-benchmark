# CFG Parity

Compares basic-block and edge recovery for one function address.

Providers must print JSON to stdout:

```json
{
  "blocks": [{"start": "0x401000", "end": "0x401010"}],
  "edges": [{"source": "0x401000", "target": "0x401020", "kind": "branch"}]
}
```

This gate separates decode/lift correctness from control-flow recovery and
structuring failures.
