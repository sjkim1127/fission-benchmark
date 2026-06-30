from pathlib import Path

from runner.corpus import Corpus
from runner.scoring import extract_function_source


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
