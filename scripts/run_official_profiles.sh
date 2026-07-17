#!/usr/bin/env bash
# Official semantic profiles:
#   core       = core_c_pe × fission,ghidra  (publication-proven)
#   full       = core_c_pe × all adapters
#   full_matrix= fan-out core_c_pe + lang_cpp + lang_rust + lang_go + multi_isa
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
PROFILE="${1:-core}"
export ORACLE_ENDPOINT="${ORACLE_ENDPOINT:-http://localhost:8010}"
export FISSION_ENDPOINT="${FISSION_ENDPOINT:-http://localhost:8007}"
export FISSION_HOST_PORT="${FISSION_HOST_PORT:-8007}"

case "$PROFILE" in
  core)
    DECS=fission,ghidra
    MATRIX=core_c_pe
    echo "Official profile=core matrix=$MATRIX decompilers=$DECS"
    ORACLE_ENDPOINT="$ORACLE_ENDPOINT" python runner/runner.py \
      --corpus holdout --profile "$MATRIX" --run-mode official --decompilers "$DECS" \
      --output results/holdout_latest.json
    ORACLE_ENDPOINT="$ORACLE_ENDPOINT" python runner/runner.py \
      --corpus dev --profile "$MATRIX" --run-mode official --decompilers "$DECS" \
      --output results/dev_latest.json
    cp results/dev_latest.json results/dev_publish.json
    ;;
  full)
    DECS=fission,ghidra,boomerang,radare2,angr,snowman,revng,reko,retdec
    MATRIX=core_c_pe
    echo "Official profile=full matrix=$MATRIX decompilers=$DECS"
    ORACLE_ENDPOINT="$ORACLE_ENDPOINT" python runner/runner.py \
      --corpus holdout --profile "$MATRIX" --run-mode official --decompilers "$DECS" \
      --output results/holdout_latest.json
    ORACLE_ENDPOINT="$ORACLE_ENDPOINT" python runner/runner.py \
      --corpus dev --profile "$MATRIX" --run-mode official --decompilers "$DECS" \
      --output results/dev_latest.json
    cp results/dev_latest.json results/dev_publish.json
    ;;
  full_matrix)
    echo "Official profile=full_matrix (fan-out)"
    chmod +x scripts/run_matrix_fanout.sh
    # Holdout: core ranking only (holdout is C-centric).
    ORACLE_ENDPOINT="$ORACLE_ENDPOINT" python runner/runner.py \
      --corpus holdout --profile core_c_pe --run-mode official \
      --decompilers fission,ghidra \
      --output results/holdout_latest.json
    CORE_DECOMPILERS="${CORE_DECOMPILERS:-fission,ghidra}" \
    SLICE_DECOMPILERS=fission,ghidra \
    RUN_MODE=official \
      ./scripts/run_matrix_fanout.sh dev results/dev_latest.json
    cp results/dev_core_c_pe.json results/dev_publish.json
    ;;
  *)
    echo "usage: $0 core|full|full_matrix"
    exit 2
    ;;
esac

python runner/holdout_report.py \
  --dev results/dev_publish.json --holdout results/holdout_latest.json \
  --json-output results/overfitting_report.json
python -m runner.publication_gate \
  --dev results/dev_publish.json \
  --holdout results/holdout_latest.json \
  --overfitting results/overfitting_report.json \
  --output results/publication-verdict.json
