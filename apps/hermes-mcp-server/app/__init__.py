from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[3]
_SCHEMA_PACKAGE = _REPO_ROOT / "packages" / "xianyu-schemas"

if _SCHEMA_PACKAGE.exists():
    _schema_path = str(_SCHEMA_PACKAGE)
    if _schema_path not in sys.path:
        sys.path.append(_schema_path)
