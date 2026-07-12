"""Build benchmark subjects from existing corpus manifests."""
from __future__ import annotations

from pathlib import Path

# Prefer package import so we never put runner/ on sys.path (that shadows
# the `runner` package name and breaks `import runner.*` elsewhere).
try:
    from runner.corpus import CORPUS_ROOT, Corpus
except ImportError:  # pragma: no cover
    import sys

    ROOT = Path(__file__).resolve().parents[2]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from runner.corpus import CORPUS_ROOT, Corpus

from benchmark.common.schema import BenchmarkSubject


def _infer_arch(compiler: str, binary: str) -> str:
    name = f"{compiler} {binary}".lower()
    if "m32" in name or "i686" in name or "x86_32" in name:
        return "x86"
    return "x86_64"


def load_subjects(split: str) -> list[BenchmarkSubject]:
    corpus = Corpus.load_all(split=split)
    subjects: list[BenchmarkSubject] = []
    for fn in corpus.functions:
        for variant in fn.compiler_variants:
            subjects.append(
                BenchmarkSubject(
                    binary=str(CORPUS_ROOT / split / variant.binary),
                    function=fn.name,
                    addr=variant.addr,
                    arch=_infer_arch(variant.compiler, variant.binary),
                    compiler=variant.compiler,
                    opt=variant.opt,
                    corpus_split=split,
                )
            )
    return subjects
