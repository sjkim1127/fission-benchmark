"""Build benchmark subjects from existing corpus manifests."""
from __future__ import annotations

from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[2]
RUNNER_DIR = ROOT / "runner"
if str(RUNNER_DIR) not in sys.path:
    sys.path.insert(0, str(RUNNER_DIR))

from corpus import CORPUS_ROOT, Corpus  # noqa: E402
from benchmark.common.schema import BenchmarkSubject  # noqa: E402


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
                    arch="unknown",
                    compiler=variant.compiler,
                    opt=variant.opt,
                    corpus_split=split,
                )
            )
    return subjects
