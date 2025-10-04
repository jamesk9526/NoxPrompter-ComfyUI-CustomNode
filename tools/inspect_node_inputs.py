from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import noxprompter.nodes as nodes  # noqa: E402


def collect_input_keys() -> Dict[str, Dict[str, list[str]]]:
    summary: Dict[str, Dict[str, list[str]]] = {}
    for cls in nodes.NODE_CLASSES:
        if not hasattr(cls, "INPUT_TYPES"):
            continue
        input_types = cls.INPUT_TYPES()
        normalized: Dict[str, list[str]] = {}
        for bucket, mapping in input_types.items():
            normalized[bucket] = list(mapping.keys())
        summary[cls.__name__] = normalized
    return summary


def main() -> None:
    summary = collect_input_keys()
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
