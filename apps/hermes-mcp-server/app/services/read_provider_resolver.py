from __future__ import annotations

import os
from collections.abc import Callable
from functools import lru_cache

try:
    from app.adapters.read_providers import (
        DemoReadFoundationProvider,
        PlaywrightH5ReadFoundationAdapter,
        ReadFoundationProvider,
        RealUpstreamReadFoundationAdapter,
    )
except ModuleNotFoundError:  # pragma: no cover - direct script fallback
    from adapters.read_providers import (  # type: ignore[no-redef]
        DemoReadFoundationProvider,
        PlaywrightH5ReadFoundationAdapter,
        ReadFoundationProvider,
        RealUpstreamReadFoundationAdapter,
    )

ReadProviderFactory = Callable[[], ReadFoundationProvider]

ENV_READ_PROVIDER = "XIANYU_READ_PROVIDER"
DEFAULT_READ_PROVIDER = "demo"

_PROVIDER_FACTORIES: dict[str, ReadProviderFactory] = {
    "demo": DemoReadFoundationProvider,
    "playwright_h5": PlaywrightH5ReadFoundationAdapter,
    "real_upstream": RealUpstreamReadFoundationAdapter,
}


def list_read_provider_keys() -> tuple[str, ...]:
    return tuple(sorted(_PROVIDER_FACTORIES.keys()))


def resolve_read_provider(provider_name: str | None = None) -> ReadFoundationProvider:
    selected_provider = (
        provider_name or os.getenv(ENV_READ_PROVIDER, DEFAULT_READ_PROVIDER)
    ).strip().lower()

    factory = _PROVIDER_FACTORIES.get(selected_provider)
    if factory is None:
        supported = ", ".join(list_read_provider_keys())
        raise ValueError(
            f"unknown read provider '{selected_provider}', supported: {supported}"
        )

    return factory()


@lru_cache(maxsize=1)
def get_read_provider() -> ReadFoundationProvider:
    """Singleton resolver used by HTTP handlers and service helpers."""

    return resolve_read_provider()


def reset_read_provider_cache() -> None:
    get_read_provider.cache_clear()
