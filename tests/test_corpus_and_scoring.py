from pathlib import Path

from runner.corpus import Corpus
from runner.scoring import FunctionScore, assign_consensus_ranks, extract_function_source, compute_correctness_score
from runner.test_wrappers import TEST_WRAPPERS


def test_manifest_preserves_variant_addr(tmp_path: Path) -> None:
    manifest = tmp_path / "manifest.json"
    manifest.write_text(
        """
        {
          "functions": [
            {
              "name": "foo",
              "source": "source/foo.c",
              "compiler_variants": [
                {"compiler": "gcc", "opt": "-O0", "binary": "binaries/foo", "addr": "0x401120"}
              ]
            }
          ]
        }
        """
    )

    corpus = Corpus.load(manifest)

    assert corpus.functions[0].compiler_variants[0].addr == "0x401120"


def test_extract_function_source_returns_requested_function_only() -> None:
    source = """
    int alpha(int x) {
        return x + 1;
    }

    int beta(int y) {
        if (y > 0) {
            return y;
        }
        return -y;
    }
    """

    extracted = extract_function_source(source, "beta")

    assert "int beta" in extracted
    assert "return -y;" in extracted
    assert "int alpha" not in extracted


def test_assign_ranks_preserves_intrinsics_flag() -> None:
    scores = [
        FunctionScore(
            decompiler="ghidra",
            function_name="foo",
            compiler_variant="gcc -O0",
            source_similarity=0.5,
            goto_count=0,
            nesting_depth=1,
            time_ms=10,
            decompiled_code="int foo(int x) { return __carry(x, 1); }",
        )
    ]

    ranked = assign_consensus_ranks(scores)

    assert ranked[0].uses_intrinsics is True


def test_crypto_functions_have_semantic_wrappers() -> None:
    for name in ("rc4_init", "rc4_crypt", "crc32"):
        assert name in TEST_WRAPPERS
        assert len(TEST_WRAPPERS[name]) >= 4


def test_assign_consensus_ranks_handles_ties_correctly() -> None:
    scores = [
        FunctionScore(
            decompiler="ghidra",
            function_name="foo",
            compiler_variant="gcc -O0",
            source_similarity=0.8,
            goto_count=0,
            nesting_depth=1,
            time_ms=10,
            semantic_score=1.0,
        ),
        FunctionScore(
            decompiler="angr",
            function_name="foo",
            compiler_variant="gcc -O0",
            source_similarity=0.8,
            goto_count=0,
            nesting_depth=1,
            time_ms=10,
            semantic_score=1.0,
        ),
        FunctionScore(
            decompiler="fission",
            function_name="foo",
            compiler_variant="gcc -O0",
            source_similarity=0.5,
            goto_count=0,
            nesting_depth=1,
            time_ms=10,
            semantic_score=1.0,
        ),
    ]

    ranked = assign_consensus_ranks(scores)
    # Group by name/variant to extract ranks
    ranks = {s.decompiler: s.consensus_rank for s in ranked}

    # ghidra and angr have the exact same score, so they must have the same rank (1)
    assert ranks["ghidra"] == 1
    assert ranks["angr"] == 1
    # fission has a lower score, so it must be ranked 3 (competition ranking: 1, 1, 3)
    assert ranks["fission"] == 3


def test_new_correctness_formula_happy_path() -> None:
    # Formula: sem * 0.50 + ast * 0.15 + read * 0.15 + sim * 0.10 + (1 - structural_penalty) * 0.10
    # Values: sem=0.8, ast=0.9, read=0.7, sim=0.6, sp=0.2
    # Expect: 0.8*0.50 + 0.9*0.15 + 0.7*0.15 + 0.6*0.10 + 0.8*0.10 = 0.40 + 0.135 + 0.105 + 0.06 + 0.08 = 0.78
    score = compute_correctness_score(
        semantic_score=0.8,
        source_similarity=0.6,
        structural_penalty=0.2,
        ast_score=0.9,
        readability_score=0.7,
    )
    assert score == 0.78


def test_ast_parsing_failures_map_to_zero_score() -> None:
    # If s.ast_similarity has available == False, ast_score must be 0.0.
    # We construct a FunctionScore with available = False but high similarity entries to verify they are ignored.
    scores = [
        FunctionScore(
            decompiler="fission",
            function_name="foo",
            compiler_variant="gcc -O0",
            source_similarity=1.0,
            goto_count=0,
            nesting_depth=1,
            time_ms=10,
            semantic_score=1.0,
            readability_proxy_score=1.0,
            ast_similarity={
                "available": False,
                "identifier_placeholder": {"similarity": 1.0},
                "type_erased": {"similarity": 1.0},
                "control_flow_normalized": {"similarity": 1.0},
            }
        )
    ]
    
    # Formula: sem * 0.50 + ast * 0.15 + read * 0.15 + sim * 0.10 + (1 - sp) * 0.10
    # With sp=0.1 (since nesting_depth=1, max_depth=1, delta=1, depth_pen=1/3, sp=0.3*1/3 = 0.1)
    # If ast_score is 0.0:
    # 1.0*0.50 + 0.0*0.15 + 1.0*0.15 + 1.0*0.10 + 0.9*0.10 = 0.50 + 0.0 + 0.15 + 0.10 + 0.09 = 0.84
    # If ast_score was 1.0 (from similarity entries):
    # 1.0*0.50 + 1.0*0.15 + 1.0*0.15 + 1.0*0.10 + 0.9*0.10 = 0.99
    ranked = assign_consensus_ranks(scores)
    assert ranked[0].correctness_score == 0.84


def test_semantic_failures_cap_correctness_score() -> None:
    # If semantic_score == 0.0, correctness_score must be capped at 0.15.
    # Let's set other components to 1.0:
    # raw = 0.0*0.50 + 1.0*0.15 + 1.0*0.15 + 1.0*0.10 + 1.0*0.10 = 0.50
    # Gated score must be min(0.50, 0.15) = 0.15
    score = compute_correctness_score(
        semantic_score=0.0,
        source_similarity=1.0,
        structural_penalty=0.0,
        ast_score=1.0,
        readability_score=1.0,
    )
    assert score == 0.15


def test_ast_similarity_robust_sub_key_lookup() -> None:
    # Verify that assign_consensus_ranks is robust to missing or None sub-keys in ast_similarity
    scores = [
        FunctionScore(
            decompiler="fission",
            function_name="foo",
            compiler_variant="gcc -O0",
            source_similarity=1.0,
            goto_count=0,
            nesting_depth=1,
            time_ms=10,
            semantic_score=1.0,
            readability_proxy_score=1.0,
            ast_similarity={
                "available": True,
                "identifier_placeholder": None,
                "type_erased": {"similarity": 0.9},
                # control_flow_normalized is missing completely
            }
        )
    ]

    # ast_score should be (0.0 + 0.9 + 0.0) / 3.0 = 0.3
    # Formula: sem * 0.50 + ast * 0.15 + read * 0.15 + sim * 0.10 + (1 - sp) * 0.10
    # With sp=0.1:
    # 1.0*0.50 + 0.3*0.15 + 1.0*0.15 + 1.0*0.10 + 0.9*0.10 = 0.50 + 0.045 + 0.15 + 0.10 + 0.09 = 0.885
    ranked = assign_consensus_ranks(scores)
    assert ranked[0].correctness_score == 0.885
