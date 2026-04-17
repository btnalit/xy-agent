from __future__ import annotations

try:
    from app.services.read_provider_resolver import get_read_provider
except ModuleNotFoundError:  # pragma: no cover - direct script fallback
    from services.read_provider_resolver import get_read_provider


def build_demo_dashboard() -> dict:
    """Backward-compatible helper used by legacy `/demo/dashboard` endpoint."""
    return get_read_provider().get_dashboard().data.model_dump(mode="json")
