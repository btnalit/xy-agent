from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
APP_PATH = REPO_ROOT / "apps" / "hermes-mcp-server"
SCHEMA_PATH = REPO_ROOT / "packages" / "xianyu-schemas"

for candidate in (APP_PATH, SCHEMA_PATH):
    candidate_str = str(candidate)
    if candidate.exists() and candidate_str not in sys.path:
        sys.path.insert(0, candidate_str)
