from runner.report import generate_markdown
from runner.scoring import FunctionScore
from runner.run_validity import Coverage, RunValidity


def test_markdown_mvp_table_omits_similarity_column() -> None:
    scores = [
        FunctionScore(
            decompiler="fission",
            function_name="clamp",
            compiler_variant="gcc -O0",
            source_similarity=0.99,
            goto_count=0,
            nesting_depth=1,
            time_ms=12,
            semantic_score=1.0,
            correctness_score=1.0,
            fail_category="",
        ),
        FunctionScore(
            decompiler="ghidra",
            function_name="clamp",
            compiler_variant="gcc -O0",
            source_similarity=0.4,
            goto_count=0,
            nesting_depth=1,
            time_ms=40,
            semantic_score=0.5,
            correctness_score=0.5,
            fail_category="assertion_fail",
        ),
    ]
    cov = Coverage(attempted=2, clean=2, ratio=1.0)
    verdict = RunValidity(
        valid=True,
        publishable=False,
        fission=cov,
        overall=cov,
        reasons=(),
        publish_reasons=("non_official_run",),
    )
    md = generate_markdown(scores, "dev", verdict=verdict)
    assert "Semantic mean" in md
    assert "Fail taxonomy" in md
    assert "Adapter clean" in md
    # Similarity must not appear as an MVP summary column header
    assert "Avg Similarity" not in md
    assert "MVP Summary" in md
