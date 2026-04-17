from __future__ import annotations

try:
    from app.services.read_foundation import DemoReadFoundationProvider
except ModuleNotFoundError:  # pragma: no cover - direct script fallback
    from services.read_foundation import DemoReadFoundationProvider

_provider = DemoReadFoundationProvider()


def build_demo_dashboard() -> dict:
    """Backward-compatible helper used by legacy `/demo/dashboard` endpoint."""
    return _provider.get_dashboard().data.model_dump(mode="json")
