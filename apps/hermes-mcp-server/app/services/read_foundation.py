from __future__ import annotations

"""Backward-compatible provider exports.

The concrete demo provider now lives under `app.adapters.read_providers`.
This module stays to keep existing imports stable.
"""

try:
    from app.adapters.read_providers import DemoReadFoundationProvider, ReadFoundationProvider
except ModuleNotFoundError:  # pragma: no cover - direct script fallback
    from adapters.read_providers import (  # type: ignore[no-redef]
        DemoReadFoundationProvider,
        ReadFoundationProvider,
    )

__all__ = ["DemoReadFoundationProvider", "ReadFoundationProvider"]
