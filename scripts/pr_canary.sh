#!/usr/bin/env bash
# PR-local differential canary: golden repros + short parity + extension smoke.
# Intended for Fission PR CI / local pre-push. Not an official publication path.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

export FISSION_HOST_PORT="${FISSION_HOST_PORT:-8007}"
export FISSION_ENDPOINT="${FISSION_ENDPOINT:-http://localhost:${FISSION_HOST_PORT}}"
export GHIDRA_ENDPOINT="${GHIDRA_ENDPOINT:-http://localhost:8001}"
export PARITY_CANONICALIZE_MODE="${PARITY_CANONICALIZE_MODE:-strict}"

LIMIT="${CANARY_LIMIT:-8}"

echo "== golden_repros =="
python -m benchmark.golden_repros.run || true

echo "== parity smoke (limit=${LIMIT}) =="
python -m runner.run_parity --corpus dev --limit "${LIMIT}" --decompilers fission,ghidra

echo "== extension stages (limit=${LIMIT}) =="
python -m runner.run_extensions --corpus dev --limit "${LIMIT}"

echo "== reliability gate on telemetry =="
python scripts/check_reliability.py results/telemetry/latest.json

echo "PR canary complete."
