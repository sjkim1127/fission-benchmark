"""Legacy entrypoint — delegates to build_matrix.py."""
from __future__ import annotations

import runpy
import sys
from pathlib import Path

if __name__ == "__main__":
    target = Path(__file__).with_name("build_matrix.py")
    sys.argv[0] = str(target)
    runpy.run_path(str(target), run_name="__main__")
