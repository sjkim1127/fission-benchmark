# Decode Parity

Compares decode fields (bytes, length, prefixes, ModRM/SIB when present).

**Default:** Ghidra (`/decode`) vs Fission (`/decode`) over Docker HTTP.

```bash
python -m benchmark.decode_parity.run --limit 5
```
