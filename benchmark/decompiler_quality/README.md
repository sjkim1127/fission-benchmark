# Decompiler Quality

The current decompiler-output similarity benchmark lives in `runner/`.

This folder marks the top-level quality stage in the layered benchmark model:

1. assembly parity
2. decode parity
3. raw p-code parity
4. CFG parity
5. function discovery
6. IR invariants
7. golden repros
8. telemetry gates
9. decompiler quality

Only rows that pass lower-level parity gates should be interpreted as meaningful
decompiler-quality comparisons.
