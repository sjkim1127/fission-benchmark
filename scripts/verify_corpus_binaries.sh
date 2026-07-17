#!/usr/bin/env bash
# Ensure dev (and holdout, when manifests exist) PE fixtures are present.
# corpus-builder defaults to CORPUS_SPLIT=dev — holdout must be built explicitly.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

count="$(find corpus/dev/binaries -type f 2>/dev/null | wc -l | tr -d ' ')"
echo "corpus/dev/binaries files: ${count}"
if [ "${count}" -lt 1 ]; then
  echo "Cache empty or incomplete — rebuilding corpus (dev)"
  docker compose --profile tools run --rm --build corpus-builder
  count="$(find corpus/dev/binaries -type f 2>/dev/null | wc -l | tr -d ' ')"
  echo "after rebuild: ${count}"
fi
test "${count}" -ge 1

# Safety net: unset addresses after partial cache restore.
if ! python3 - <<'PY'
import json
from pathlib import Path
bad = 0
for man in Path("corpus/dev/manifests").glob("*.json"):
    data = json.loads(man.read_text())
    for fn in data.get("functions", []):
        for var in fn.get("compiler_variants", []):
            addr = (var.get("addr") or "").strip().lower()
            if not addr or addr in {"0x0", "0", "0x00"}:
                bad += 1
raise SystemExit(1 if bad else 0)
PY
then
  echo "Manifest addresses look unset — re-running corpus-builder (dev)"
  docker compose --profile tools run --rm --build corpus-builder
fi

# Holdout PE fixtures for official publication.
if find corpus/holdout/manifests -name '*.json' -print -quit | grep -q .; then
  hold_count="$(find corpus/holdout/binaries -type f 2>/dev/null | wc -l | tr -d ' ')"
  echo "corpus/holdout/binaries files: ${hold_count}"
  need_holdout=0
  if [ "${hold_count}" -lt 1 ]; then
    need_holdout=1
  elif ! python3 - <<'PY'
import json
from pathlib import Path

root = Path("corpus/holdout")
missing = 0
checked = 0
for man in (root / "manifests").glob("*.json"):
    data = json.loads(man.read_text())
    for fn in data.get("functions", []):
        for var in fn.get("compiler_variants", []):
            rel = var.get("binary") or ""
            if not rel:
                continue
            opt = (var.get("opt") or "").strip()
            compiler = (var.get("compiler") or "").strip()
            # Match core_c_pe slice used for official ranking.
            if opt not in {"-O0", "-O2"}:
                continue
            if compiler not in {"gcc", "gcc-m32", "clang"}:
                continue
            checked += 1
            path = root / rel
            if not path.is_file():
                print(f"missing holdout binary: {rel}")
                missing += 1
print(f"holdout core paths checked={checked} missing={missing}")
raise SystemExit(1 if missing else 0)
PY
  then
    need_holdout=1
  fi

  if [ "${need_holdout}" = "1" ]; then
    echo "Building holdout corpus binaries (CORPUS_SPLIT=holdout)"
    CORPUS_SPLIT=holdout docker compose --profile tools run --rm --build corpus-builder
    hold_count="$(find corpus/holdout/binaries -type f 2>/dev/null | wc -l | tr -d ' ')"
    echo "after holdout rebuild: ${hold_count}"
    test "${hold_count}" -ge 1
  else
    echo "Holdout core PE fixtures present"
  fi
else
  echo "No holdout manifests; skipping holdout binary check"
fi

echo "OK corpus binary verification"
