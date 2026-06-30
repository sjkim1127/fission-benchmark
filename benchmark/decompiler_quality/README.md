# Decompiler Quality

The current decompiler-output similarity benchmark lives in `runner/`.

This folder marks the top-level quality stage in the layered benchmark model:

1. assembly parity
2. raw p-code parity
3. telemetry gates
4. decompiler quality

Only rows that pass lower-level parity gates should be interpreted as meaningful
decompiler-quality comparisons.
