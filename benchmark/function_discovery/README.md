# Function Discovery

Compares binary-level function discovery across providers.

Providers must print a JSON list to stdout:

```json
[
  {"address": "0x401000", "name": "main", "size": 64, "kind": "function"}
]
```

Rows are emitted once per unique binary/compiler/optimization variant rather
than once per manifest function.
