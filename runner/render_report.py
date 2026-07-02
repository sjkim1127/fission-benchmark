"""Render benchmark report artifacts from a saved JSON result file."""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import fields
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from report import generate_report
from scoring import FunctionScore


def load_scores(path: Path) -> list[FunctionScore]:
    data = json.loads(path.read_text(encoding="utf-8"))
    score_fields = {field.name for field in fields(FunctionScore)}
    return [FunctionScore(**{k: v for k, v in row.items() if k in score_fields}) for row in data]


def main() -> None:
    parser = argparse.ArgumentParser(description="Render benchmark dashboard from saved results")
    parser.add_argument("--input", required=True, type=Path, help="Input JSON results file")
    parser.add_argument("--corpus", required=True, help="Corpus label to show in the report")
    parser.add_argument(
        "--update-latest",
        action="store_true",
        help="Also copy the input JSON to results/latest.json",
    )
    args = parser.parse_args()

    scores = load_scores(args.input)
    generate_report(scores, corpus_split=args.corpus)

    if args.update_latest:
        latest_path = Path("results/latest.json")
        latest_path.parent.mkdir(exist_ok=True)
        latest_path.write_text(args.input.read_text(encoding="utf-8"), encoding="utf-8")

    print(f"Rendered {len(scores)} rows from {args.input} as corpus {args.corpus!r}")


if __name__ == "__main__":
    main()
