# Human readability study pack (scaffold)

This directory holds materials for the Phase 3 human comprehension study
described in `../human_study.md`.

**No final readability score is derived until the study is complete and
proxies are validated.**

## Planned contents

| Path | Purpose |
|------|---------|
| `functions.json` | Selected function names + category tags |
| `answer_key.json` | Ground-truth answers for objective questions |
| `latin_square.md` | Participant × condition assignment |
| `exports/` | Decompiled outputs per decompiler (generated) |

## Export (future)

```bash
# When implemented:
python scripts/export_study_pack.py \
  --input results/dev_latest.json \
  --functions benchmark/readability/study_pack/functions.json \
  --output benchmark/readability/study_pack/exports/
```

Do not commit large decompiled dumps unless they are part of a frozen study
revision.
