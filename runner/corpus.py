"""Corpus management with 80/20 holdout split for overfitting prevention."""
from __future__ import annotations

import hashlib
import json
import random
from dataclasses import dataclass, field
from pathlib import Path

CORPUS_ROOT = Path(__file__).parent.parent / "corpus"
HOLDOUT_SEED = 42          # Fixed seed — never change after initial split
HOLDOUT_RATIO = 0.20


@dataclass
class CompilerVariant:
    compiler: str           # "gcc", "clang", "msvc"
    opt: str                # "-O0", "-O2"
    binary: str             # relative path under corpus/


@dataclass
class FunctionEntry:
    name: str
    source: str             # relative path to C source
    compiler_variants: list[CompilerVariant]
    split: str = "dev"      # "dev" | "holdout"


@dataclass
class Corpus:
    functions: list[FunctionEntry] = field(default_factory=list)

    @classmethod
    def load(cls, manifest_path: Path) -> "Corpus":
        data = json.loads(manifest_path.read_text())
        functions = []
        for fn in data["functions"]:
            variants = [CompilerVariant(**v) for v in fn.get("compiler_variants", [])]
            functions.append(FunctionEntry(
                name=fn["name"],
                source=fn["source"],
                compiler_variants=variants,
            ))
        return cls(functions=functions)

    @classmethod
    def load_all(cls, split: str = "dev") -> "Corpus":
        """Load all manifests from corpus/{split}/manifests/."""
        assert split in ("dev", "holdout"), f"Invalid split: {split!r}"
        manifest_dir = CORPUS_ROOT / split / "manifests"
        all_functions: list[FunctionEntry] = []
        for manifest in sorted(manifest_dir.glob("*.json")):
            c = cls.load(manifest)
            for fn in c.functions:
                fn.split = split
                all_functions.append(fn)
        return cls(functions=all_functions)


def split_corpus_to_holdout(
    manifest_path: Path,
    out_dev: Path,
    out_holdout: Path,
    seed: int = HOLDOUT_SEED,
    holdout_ratio: float = HOLDOUT_RATIO,
) -> tuple[int, int]:
    """
    Deterministically split a manifest into dev/holdout by function unit.
    Holdout functions are locked — never use them during development.

    Returns: (n_dev, n_holdout)
    """
    corpus = Corpus.load(manifest_path)
    rng = random.Random(seed)

    # Deterministic shuffle by function name hash for reproducibility
    functions = sorted(corpus.functions, key=lambda f: hashlib.sha256(f.name.encode()).hexdigest())
    rng.shuffle(functions)

    n_holdout = max(1, int(len(functions) * holdout_ratio))
    holdout = functions[:n_holdout]
    dev = functions[n_holdout:]

    def serialize(fns: list[FunctionEntry]) -> dict:
        return {
            "functions": [
                {
                    "name": fn.name,
                    "source": fn.source,
                    "compiler_variants": [
                        {"compiler": v.compiler, "opt": v.opt, "binary": v.binary}
                        for v in fn.compiler_variants
                    ],
                }
                for fn in fns
            ]
        }

    out_dev.parent.mkdir(parents=True, exist_ok=True)
    out_holdout.parent.mkdir(parents=True, exist_ok=True)
    out_dev.write_text(json.dumps(serialize(dev), indent=2))
    out_holdout.write_text(json.dumps(serialize(holdout), indent=2))

    return len(dev), n_holdout
