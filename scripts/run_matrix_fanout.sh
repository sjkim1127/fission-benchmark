#!/usr/bin/env bash
# Sequential full_matrix fan-out: run profile slices then merge envelopes.
#
# Usage:
#   ORACLE_ENDPOINT=http://localhost:8010 \
#     ./scripts/run_matrix_fanout.sh dev results/dev_latest.json
#
# Env:
#   RUN_MODE          smoke|local|official (default: smoke)
#   FANOUT_PROFILES   space-separated profiles (default: core set)
#   CORE_DECOMPILERS  decompilers for core_c_pe (default: fission,ghidra for speed)
#   SLICE_DECOMPILERS decompilers for lang_*/multi_isa (default: fission,ghidra)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

CORPUS="${1:-dev}"
OUTPUT="${2:-results/${CORPUS}_latest.json}"
RUN_MODE="${RUN_MODE:-smoke}"
FANOUT_PROFILES="${FANOUT_PROFILES:-core_c_pe lang_cpp lang_rust lang_go multi_isa}"
CORE_DECOMPILERS="${CORE_DECOMPILERS:-fission,ghidra}"
SLICE_DECOMPILERS="${SLICE_DECOMPILERS:-fission,ghidra}"
SLICE_DIR="results/slices"
mkdir -p "$SLICE_DIR"

echo "Fan-out corpus=$CORPUS mode=$RUN_MODE profiles=[$FANOUT_PROFILES]"
echo "  core decompilers:  $CORE_DECOMPILERS"
echo "  slice decompilers: $SLICE_DECOMPILERS"

inputs=()
labels=()
for profile in $FANOUT_PROFILES; do
  out="$SLICE_DIR/${CORPUS}_${profile}.json"
  if [ "$profile" = "core_c_pe" ]; then
    decs="$CORE_DECOMPILERS"
  else
    decs="$SLICE_DECOMPILERS"
  fi
  echo "==> profile=$profile decompilers=$decs → $out"
  ORACLE_ENDPOINT="${ORACLE_ENDPOINT:-}" \
    python runner/runner.py \
      --corpus "$CORPUS" \
      --profile "$profile" \
      --decompilers "$decs" \
      --run-mode "$RUN_MODE" \
      --output "$out"
  inputs+=("$out")
  labels+=("$profile")
done

# Always keep a pure core slice for publication ranking.
if [ -f "$SLICE_DIR/${CORPUS}_core_c_pe.json" ]; then
  cp "$SLICE_DIR/${CORPUS}_core_c_pe.json" "results/${CORPUS}_core_c_pe.json"
  echo "Wrote results/${CORPUS}_core_c_pe.json (publication ranking slice)"
fi

label_args=()
for lab in "${labels[@]}"; do
  label_args+=(--label "$lab")
done

python scripts/merge_envelopes.py "${inputs[@]}" \
  "${label_args[@]}" \
  -o "$OUTPUT"
echo "Merged fan-out → $OUTPUT"
