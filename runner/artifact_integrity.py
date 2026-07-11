"""Integrity linkage for generated benchmark publication artifacts."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


MANIFEST_NAME = "artifact-manifest.json"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def write_artifact_manifest(
    output_root: Path,
    *,
    run_id: str,
    source_envelope_sha256: str,
    generated_from: str,
) -> Path:
    results_dir = output_root / "results"
    files = {
        "latest_json": results_dir / "latest.json",
        "latest_markdown": results_dir / "latest.md",
        "latest_summary": results_dir / "latest-summary.json",
        "dashboard": output_root / "docs" / "index.html",
    }
    missing = [str(path) for path in files.values() if not path.is_file() or path.stat().st_size == 0]
    if missing:
        raise ValueError("missing or empty publication artifacts: " + ", ".join(missing))
    manifest = {
        "schema_version": 1,
        "run_id": run_id,
        "source_envelope_sha256": source_envelope_sha256,
        "generated_from": generated_from,
        "files": {name: {"path": str(path.relative_to(output_root)), "sha256": sha256_file(path)} for name, path in files.items()},
    }
    path = results_dir / MANIFEST_NAME
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return path


def verify_artifact_manifest(output_root: Path) -> dict[str, Any]:
    manifest_path = output_root / "results" / MANIFEST_NAME
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    run_id = manifest.get("run_id")
    source_hash = manifest.get("source_envelope_sha256")
    if not run_id or not source_hash:
        raise ValueError("artifact manifest is missing run_id or source envelope hash")

    for entry in manifest.get("files", {}).values():
        path = output_root / entry["path"]
        if not path.is_file() or path.stat().st_size == 0:
            raise ValueError(f"artifact is missing or empty: {path}")
        if sha256_file(path) != entry.get("sha256"):
            raise ValueError(f"artifact hash mismatch: {path}")

    latest = json.loads((output_root / "results/latest.json").read_text(encoding="utf-8"))
    summary = json.loads((output_root / "results/latest-summary.json").read_text(encoding="utf-8"))
    if latest.get("run", {}).get("run_id") != run_id:
        raise ValueError("latest.json run_id does not match artifact manifest")
    if latest.get("artifact", {}).get("run_id") != run_id:
        raise ValueError("latest.json artifact run_id does not match artifact manifest")
    if latest.get("artifact", {}).get("source_envelope_sha256") != source_hash:
        raise ValueError("latest.json source hash does not match artifact manifest")
    if summary.get("run", {}).get("run_id") != run_id:
        raise ValueError("latest-summary.json run_id does not match artifact manifest")
    if summary.get("artifact", {}).get("source_envelope_sha256") != source_hash:
        raise ValueError("latest-summary.json source hash does not match artifact manifest")

    marker = f"run_id={run_id} source_envelope_sha256={source_hash}"
    if marker not in (output_root / "results/latest.md").read_text(encoding="utf-8"):
        raise ValueError("latest.md linkage marker mismatch")
    if marker not in (output_root / "docs/index.html").read_text(encoding="utf-8"):
        raise ValueError("dashboard linkage marker mismatch")
    return manifest
