# IR Invariants

Checks Fission-internal IR/NIR/HIR invariants without requiring an external
reference provider.

The candidate command must print JSON to stdout:

```json
{
  "violations": [
    {"kind": "dangling_edge", "detail": "block 3 -> missing block 7"}
  ],
  "metrics": {"block_count": 10, "op_count": 42}
}
```

An empty `violations` list is a match. Any violation is a mismatch.
