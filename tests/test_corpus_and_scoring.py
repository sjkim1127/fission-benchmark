from pathlib import Path

from runner.corpus import Corpus
from runner.scoring import FunctionScore, assign_consensus_ranks, extract_function_source
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
