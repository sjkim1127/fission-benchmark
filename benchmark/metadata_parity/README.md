# Program metadata parity

This diagnostic stage compares Fission's typed `ProgramSnapshot` with Ghidra's
program database for the same binary. It runs once per binary, not once per
function.

Strict status requires equality of binary identity, memory block ranges and
permissions, function entries, symbol addresses, and relocation addresses. The
individual Jaccard rates remain available for triage. This stage is deliberately
non-publishable until the schemas and provenance filters stabilize.

```bash
export FISSION_HOST_PORT=8007
python -m benchmark.metadata_parity.run --corpus dev --limit 1
```
