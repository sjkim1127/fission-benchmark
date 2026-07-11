import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "runner"))
from artifact_integrity import verify_artifact_manifest, write_artifact_manifest


def _write_artifacts(root: Path) -> None:
    (root / "results").mkdir(parents=True)
    (root / "docs").mkdir(parents=True)
    marker = "run_id=run-1 source_envelope_sha256=abc123"
    (root / "results/latest.json").write_text(
        json.dumps({
            "run": {"run_id": "run-1"},
            "artifact": {"run_id": "run-1", "source_envelope_sha256": "abc123"},
        }),
        encoding="utf-8",
    )
    (root / "results/latest.md").write_text(f"<!-- {marker} -->", encoding="utf-8")
    (root / "results/latest-summary.json").write_text(
        json.dumps({
            "run": {"run_id": "run-1"},
            "artifact": {"source_envelope_sha256": "abc123"},
        }),
        encoding="utf-8",
    )
    (root / "docs/index.html").write_text(f"<!-- {marker} -->", encoding="utf-8")


def test_artifact_manifest_links_all_publication_outputs(tmp_path: Path) -> None:
    _write_artifacts(tmp_path)
    write_artifact_manifest(
        tmp_path,
        run_id="run-1",
        source_envelope_sha256="abc123",
        generated_from="candidate.json",
    )
    manifest = verify_artifact_manifest(tmp_path)
    assert manifest["run_id"] == "run-1"


def test_artifact_manifest_rejects_tampering(tmp_path: Path) -> None:
    _write_artifacts(tmp_path)
    write_artifact_manifest(
        tmp_path,
        run_id="run-1",
        source_envelope_sha256="abc123",
        generated_from="candidate.json",
    )
    (tmp_path / "results/latest.md").write_text("tampered", encoding="utf-8")
    with pytest.raises(ValueError, match="hash mismatch"):
        verify_artifact_manifest(tmp_path)
