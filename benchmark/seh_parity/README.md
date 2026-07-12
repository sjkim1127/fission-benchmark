# SEH / unwind surface

**Status:** extension track (flags-only surface).

Compares thunk/no-return flags and program EH-symbol counts. Full
`RUNTIME_FUNCTION` parsing is future work; Fission returns
`seh_surface=not_recovered`.

```bash
python -m benchmark.seh_parity.run --limit 10
```
