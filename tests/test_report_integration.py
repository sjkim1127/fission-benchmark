"""Integration tests for report generation and runner CLI contract (P0.6.2)."""
import json
import sys
import subprocess
from pathlib import Path
import hashlib

sys.path.insert(0, str(Path(__file__).parent.parent / "runner"))
import run_validity as rv
from report import generate_report
from scoring import FunctionScore


RUNNER_DIR = Path(__file__).parent.parent / "runner"


def _make_score(decompiler="fission", fn="foo", variant="gcc -O0",
                semantic=1.0, similarity=0.8, correctness=0.92):
    return FunctionScore(
        decompiler=decompiler,
        function_name=fn,
        compiler_variant=variant,
        source_similarity=similarity,
        goto_count=0,
        nesting_depth=0,
        time_ms=100,
        semantic_score=semantic,
        correctness_score=correctness,
    )


def _make_verdict(valid=True, publishable=True):
    from run_validity import Coverage, RunValidity
    cov = Coverage(attempted=1, clean=1, ratio=1.0)
    return RunValidity(
        valid=valid,
        publishable=publishable,
        fission=cov,
        overall=cov,
        reasons=(),
        publish_reasons=() if publishable else ("non_official_run",),
    )


def test_generate_report_writes_markdown_and_html(tmp_path, monkeypatch):
    """generate_report() must write both latest.md and docs/index.html."""
    import report
    monkeypatch.setattr(report, "RESULTS_DIR", tmp_path / "results")
    monkeypatch.setattr(report, "DOCS_DIR", tmp_path / "docs")

    scores = [_make_score()]
    verdict = _make_verdict()
    generate_report(
        scores,
        corpus_split="dev",
        verdict=verdict,
        results_dir=tmp_path / "results",
        docs_dir=tmp_path / "docs",
    )

    assert (tmp_path / "results" / "latest.md").exists(), "latest.md not written"
    assert (tmp_path / "docs" / "index.html").exists(), "index.html not written"
    assert (tmp_path / "results" / "latest.md").stat().st_size > 0, "latest.md is empty"
    assert (tmp_path / "docs" / "index.html").stat().st_size > 0, "index.html is empty"


def test_html_and_markdown_share_verdict(tmp_path, monkeypatch):
    """HTML and Markdown must embed the same valid/publishable state."""
    import report
    monkeypatch.setattr(report, "RESULTS_DIR", tmp_path / "results")
    monkeypatch.setattr(report, "DOCS_DIR", tmp_path / "docs")

    scores = [_make_score()]
    verdict = _make_verdict(valid=True, publishable=False)
    generate_report(
        scores,
        corpus_split="dev",
        verdict=verdict,
        results_dir=tmp_path / "results",
        docs_dir=tmp_path / "docs",
    )

    md = (tmp_path / "results" / "latest.md").read_text()
    html = (tmp_path / "docs" / "index.html").read_text()

    # Both must contain the smoke/unpublishable banner text
    assert "VALID" in md
    assert "NOT PUBLISHABLE" in md or "SMOKE" in md
    # HTML must NOT say VALID RUN as publishable
    assert "\"publishable\": false" in html or '"publishable":false' in html


def test_runner_accepts_corpus_option():
    """runner.py --help must list --corpus as an option (not positional)."""
    import os
    env = {**os.environ, "NO_COLOR": "1", "TERM": "dumb"}
    result = subprocess.run(
        [sys.executable, str(RUNNER_DIR / "runner.py"), "--help"],
        capture_output=True, text=True, env=env,
    )
    assert result.returncode == 0
    # Strip any residual ANSI escape codes before searching
    import re
    plain = re.sub(r"\x1b\[[0-9;]*m", "", result.stdout)
    assert "--corpus" in plain, f"--corpus option not found in help. Got:\n{plain}"


def test_render_cli_preserves_input_hash(tmp_path):
    """render_report.py must not mutate the input JSON file."""
    rows = [
        {"decompiler": "fission", "function_name": "foo", "compiler_variant": "gcc -O0",
         "error": None, "semantic_score": 1.0, "source_similarity": 0.8,
         "correctness_score": 0.92, "correctness_rank": None,
         "structural_penalty": 0.0, "cases_passed": 1, "cases_total": 1,
         "goto_count": 0, "nesting_depth": 0, "time_ms": 100}
    ]
    envelope = rv.build_envelope(rows, run_meta={"official": False})
    in_file = tmp_path / "input.json"
    in_file.write_text(json.dumps(envelope), encoding="utf-8")

    before_hash = hashlib.sha256(in_file.read_bytes()).hexdigest()

    # render_report without --update-latest should not touch the input file
    output_dir = tmp_path / "rendered"
    result = subprocess.run(
        [sys.executable, str(RUNNER_DIR / "render_report.py"),
         "--input", str(in_file), "--corpus", "dev",
         "--output-dir", str(output_dir)],
        capture_output=True, text=True, cwd=str(RUNNER_DIR.parent)
    )
    assert result.returncode == 0, result.stderr

    after_hash = hashlib.sha256(in_file.read_bytes()).hexdigest()
    assert before_hash == after_hash, "render_report mutated the input file"
    assert (output_dir / "results/artifact-manifest.json").is_file()


def test_report_renders_no_wrapper_as_unmeasured(tmp_path):
    score = _make_score()
    score.semantic_score = None
    score.correctness_score = None
    score.correctness_rank = None
    score.fail_category = "no_wrapper"

    generate_report(
        [score],
        corpus_split="dev",
        verdict=_make_verdict(valid=True, publishable=False),
        results_dir=tmp_path / "results",
        docs_dir=tmp_path / "docs",
    )
    markdown = (tmp_path / "results/latest.md").read_text(encoding="utf-8")
    assert "n/a" in markdown
    assert "no_test" in markdown


def test_linked_publication_verdict_marks_isolated_artifact_publishable(tmp_path):
    rows = [{
        "decompiler": "fission", "function_name": "foo", "compiler_variant": "gcc -O0",
        "error": None, "semantic_score": 1.0, "source_similarity": 0.8,
        "correctness_score": 1.0, "correctness_rank": 1,
        "structural_penalty": 0.0, "cases_passed": 1, "cases_total": 1,
        "goto_count": 0, "nesting_depth": 0, "time_ms": 1,
    }]
    envelope = rv.build_envelope(rows, run_meta={"official": False})
    input_path = tmp_path / "candidate.json"
    input_path.write_text(json.dumps(envelope), encoding="utf-8")
    source_hash = hashlib.sha256(input_path.read_bytes()).hexdigest()
    verdict_path = tmp_path / "publication.json"
    verdict_path.write_text(json.dumps({
        "publishable": True,
        "dev": {"envelope_sha256": source_hash},
    }), encoding="utf-8")
    output_dir = tmp_path / "published"

    result = subprocess.run(
        [
            sys.executable, str(RUNNER_DIR / "render_report.py"),
            "--input", str(input_path), "--corpus", "dev",
            "--output-dir", str(output_dir),
            "--publication-verdict", str(verdict_path),
        ],
        capture_output=True, text=True, cwd=str(RUNNER_DIR.parent),
    )

    assert result.returncode == 0, result.stderr
    latest = json.loads((output_dir / "results/latest.json").read_text(encoding="utf-8"))
    assert latest["validity"]["publishable"] is True
    assert latest["publication"]["dev"]["envelope_sha256"] == source_hash
