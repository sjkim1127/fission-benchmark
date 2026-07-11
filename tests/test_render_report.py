import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "runner"))
from render_report import _normalise_scores

def test_legacy_correctness_fallback():
    # A legacy row without correctness_score
    legacy_row = {
        "decompiler": "fission",
        "function_name": "foo",
        "compiler_variant": "gcc",
        "semantic_score": 1.0,
        "source_similarity": 0.5,
        "structural_penalty": 0.0,
        "goto_count": 0,
        "nesting_depth": 0,
        "time_ms": 100,
    }
    
    # 0.9 * 1.0 + 0.1 * 0.5 = 0.95
    
    scores = _normalise_scores([legacy_row])
    
    # correctness_score must be computed instead of remaining 0.0
    assert scores[0].correctness_score == 0.95
