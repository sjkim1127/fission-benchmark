#!/usr/bin/env bash
# Official semantic profiles:
#   core  = fission,ghidra  (publication-proven)
#   full  = all configured adapters (wider matrix; may surface adapter residuals)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
PROFILE="${1:-core}"
export ORACLE_ENDPOINT="${ORACLE_ENDPOINT:-http://localhost:8010}"
export FISSION_ENDPOINT="${FISSION_ENDPOINT:-http://localhost:8007}"
export FISSION_HOST_PORT="${FISSION_HOST_PORT:-8007}"
case "$PROFILE" in
  core) DECS=fission,ghidra ;;
  full) DECS=fission,ghidra,boomerang,radare2,angr,snowman,revng,reko ;;
  *) echo "usage: $0 core|full"; exit 2 ;;
esac
echo "Official profile=$PROFILE decompilers=$DECS"
ORACLE_ENDPOINT="$ORACLE_ENDPOINT" python runner/runner.py \
  --corpus holdout --run-mode official --decompilers "$DECS" \
  --output results/holdout_latest.json
ORACLE_ENDPOINT="$ORACLE_ENDPOINT" python runner/runner.py \
  --corpus dev --run-mode official --decompilers "$DECS" \
  --output results/dev_latest.json
python runner/holdout_report.py \
  --dev results/dev_latest.json --holdout results/holdout_latest.json \
  --json-output results/overfitting_report.json
python -m runner.publication_gate \
  --dev results/dev_latest.json \
  --holdout results/holdout_latest.json \
  --overfitting results/overfitting_report.json \
  --output results/publication-verdict.json
