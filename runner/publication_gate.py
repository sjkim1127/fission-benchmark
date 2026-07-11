"""Final evidence-linked publication gate for benchmark artifacts."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

try:
    from .run_validity import LoadedResult, evaluate_run, load_result_file
except ImportError:
    from run_validity import LoadedResult, evaluate_run, load_result_file

EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _candidate_reasons(label: str, loaded: LoadedResult) -> list[str]:
    verdict = evaluate_run(loaded)
    checks = {
        "execution": verdict.valid,
        "matrix": verdict.matrix_valid,
        "adapter_output": verdict.adapter_output_valid,
        "semantic_harness": verdict.semantic_harness_valid,
        "semantic_coverage": verdict.semantic_coverage_valid,
        "semantic_result": verdict.semantic_result_valid,
        "provenance": verdict.provenance_valid,
        "artifact": verdict.artifact_valid,
        "official_profile": verdict.official_profile_valid,
    }
    return [f"{label}_{name}_invalid" for name, valid in checks.items() if not valid]


def evaluate_publication(
    dev_path: Path,
    holdout_path: Path,
    overfitting_path: Path,
) -> dict[str, Any]:
    dev = load_result_file(dev_path)
    holdout = load_result_file(holdout_path)
    overfitting = json.loads(overfitting_path.read_text(encoding="utf-8"))
    dev_hash = sha256_file(dev_path)
    holdout_hash = sha256_file(holdout_path)

    reasons = _candidate_reasons("dev", dev) + _candidate_reasons("holdout", holdout)
    if not holdout.rows:
        reasons.append("holdout_empty")
    if holdout.envelope.get("run", {}).get("corpus") != "holdout":
        reasons.append("holdout_corpus_identity_invalid")
    if dev.envelope.get("run", {}).get("corpus_manifest_sha256") in (None, "", EMPTY_SHA256):
        reasons.append("dev_manifest_hash_missing")
    if holdout.envelope.get("run", {}).get("corpus_manifest_sha256") in (None, "", EMPTY_SHA256):
        reasons.append("holdout_manifest_hash_missing")
    if overfitting.get("dev_envelope_sha256") != dev_hash:
        reasons.append("overfitting_dev_hash_mismatch")
    if overfitting.get("holdout_envelope_sha256") != holdout_hash:
        reasons.append("overfitting_holdout_hash_mismatch")
    if overfitting.get("passed") is not True:
        reasons.append("overfitting_failed")

    reasons = list(dict.fromkeys(reasons))
    return {
        "schema_version": 1,
        "publishable": not reasons,
        "reasons": reasons,
        "dev": {
            "run_id": dev.envelope.get("run", {}).get("run_id"),
            "envelope_sha256": dev_hash,
            "manifest_sha256": dev.envelope.get("run", {}).get("corpus_manifest_sha256"),
        },
        "holdout": {
            "run_id": holdout.envelope.get("run", {}).get("run_id"),
            "envelope_sha256": holdout_hash,
            "manifest_sha256": holdout.envelope.get("run", {}).get("corpus_manifest_sha256"),
        },
        "overfitting_sha256": sha256_file(overfitting_path),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Evaluate final benchmark publication evidence")
    parser.add_argument("--dev", required=True, type=Path)
    parser.add_argument("--holdout", required=True, type=Path)
    parser.add_argument("--overfitting", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--github-env", type=Path)
    args = parser.parse_args(argv)

    try:
        verdict = evaluate_publication(args.dev, args.holdout, args.overfitting)
    except Exception as exc:
        print(f"::error::Publication evidence invalid: {exc}", file=sys.stderr)
        return 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(verdict, indent=2) + "\n", encoding="utf-8")
    if args.github_env:
        with args.github_env.open("a", encoding="utf-8") as handle:
            handle.write(f"RUN_PUBLISHABLE={'true' if verdict['publishable'] else 'false'}\n")
    if not verdict["publishable"]:
        print("NOT PUBLISHABLE: " + ", ".join(verdict["reasons"]))
        return 1
    print("PUBLISHABLE: dev, holdout, oracle, and overfitting evidence verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
