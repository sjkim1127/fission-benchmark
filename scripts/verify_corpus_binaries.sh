#!/usr/bin/env bash
# Ensure dev (and holdout, when manifests exist) PE fixtures are present.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "[verify] cwd=$ROOT"

count="$(find corpus/dev/binaries -type f 2>/dev/null | wc -l | tr -d ' ')"
count="${count:-0}"
echo "[verify] corpus/dev/binaries files: ${count}"
if [ "${count}" -lt 1 ]; then
  echo "[verify] Cache empty — rebuilding dev corpus"
  docker compose --profile tools run --rm --build corpus-builder
  count="$(find corpus/dev/binaries -type f 2>/dev/null | wc -l | tr -d ' ')"
  count="${count:-0}"
  echo "[verify] after dev rebuild: ${count}"
fi
if [ "${count}" -lt 1 ]; then
  echo "[verify] ERROR: still no dev binaries" >&2
  exit 1
fi

# Soft address check: rebuild if many unset addrs (non-fatal if rebuild succeeds).
bad_addrs="$(
  python3 - <<'PY' || true
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
print(bad)
PY
)"
bad_addrs="${bad_addrs:-0}"
echo "[verify] unset/zero dev addrs: ${bad_addrs}"
if [ "${bad_addrs}" -gt 50 ]; then
  echo "[verify] Many unset addresses — re-running dev corpus-builder"
  docker compose --profile tools run --rm --build corpus-builder || {
    echo "[verify] WARN: dev re-sync failed; continuing" >&2
  }
fi

# Holdout PE fixtures (official publication needs these).
if find corpus/holdout/manifests -name '*.json' -print -quit 2>/dev/null | grep -q .; then
  hold_count="$(find corpus/holdout/binaries -type f 2>/dev/null | wc -l | tr -d ' ')"
  hold_count="${hold_count:-0}"
  echo "[verify] corpus/holdout/binaries files: ${hold_count}"

  missing="$(
    python3 - <<'PY' || echo 999
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
            if opt not in {"-O0", "-O2"}:
                continue
            if compiler not in {"gcc", "gcc-m32", "clang"}:
                continue
            checked += 1
            path = root / rel
            if not path.is_file():
                print(f"[verify] missing: {rel}", flush=True)
                missing += 1
print(missing, flush=True)
# also print summary to stderr so it always shows
import sys
print(f"[verify] holdout core checked={checked} missing={missing}", file=sys.stderr, flush=True)
PY
  )"
  # last line is the missing count
  missing="$(echo "${missing}" | tail -n1 | tr -d ' ')"
  missing="${missing:-999}"
  echo "[verify] holdout missing core binaries: ${missing}"

  if [ "${hold_count}" -lt 1 ] || [ "${missing}" -gt 0 ]; then
    echo "[verify] Building holdout corpus (CORPUS_SPLIT=holdout)"
    CORPUS_SPLIT=holdout docker compose --profile tools run --rm --build corpus-builder
    hold_count="$(find corpus/holdout/binaries -type f 2>/dev/null | wc -l | tr -d ' ')"
    hold_count="${hold_count:-0}"
    echo "[verify] after holdout rebuild: ${hold_count}"
    if [ "${hold_count}" -lt 1 ]; then
      echo "[verify] ERROR: holdout binaries still missing after rebuild" >&2
      # Official publish needs holdout; smoke can continue with a warning.
      if [ "${PUBLISH_RESULTS:-false}" = "true" ]; then
        exit 1
      fi
      echo "[verify] WARN: continuing without holdout (non-publish run)" >&2
    fi
  else
    echo "[verify] Holdout core PE fixtures present"
  fi
else
  echo "[verify] No holdout manifests; skipping holdout check"
fi

echo "[verify] OK corpus binary verification"
