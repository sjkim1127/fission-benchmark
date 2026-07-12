# CFG Parity

Compares basic-block and edge recovery for one function address.

**Default:** Ghidra (`/cfg`) vs Fission (`/cfg`) over Docker HTTP.

## Schema

```json
{
  "blocks": [{"start": "0x401000", "end": "0x401010"}],
  "edges": [{"source": "0x401000", "target": "0x401020", "kind": "branch"}]
}
```

Mismatch kinds: `block_count`, `edge_count`, `block_set`, `edge_set`, `cfg_shape`.

## Run

```bash
python -m benchmark.cfg_parity.run --limit 5
```
