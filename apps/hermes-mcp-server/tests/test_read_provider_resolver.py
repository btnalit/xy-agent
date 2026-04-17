from __future__ import annotations

import pytest

from app.adapters.read_providers import (
    DemoReadFoundationProvider,
    PlaywrightH5ReadFoundationAdapter,
    ReadFoundationProvider,
    RealUpstreamReadFoundationAdapter,
)
from app.services.read_provider_resolver import (
    list_read_provider_keys,
    resolve_read_provider,
)


def test_demo_provider_implements_read_provider_protocol() -> None:
    provider = DemoReadFoundationProvider()
    assert isinstance(provider, ReadFoundationProvider)


def test_resolver_returns_demo_provider_by_default_name() -> None:
    provider = resolve_read_provider('demo')
    assert isinstance(provider, DemoReadFoundationProvider)


def test_resolver_exposes_playwright_h5_adapter() -> None:
    provider = resolve_read_provider('playwright_h5')
    assert isinstance(provider, PlaywrightH5ReadFoundationAdapter)


def test_resolver_exposes_real_upstream_slot() -> None:
    provider = resolve_read_provider('real_upstream')
    assert isinstance(provider, RealUpstreamReadFoundationAdapter)


def test_playwright_h5_adapter_is_offline_safe() -> None:
    provider = resolve_read_provider('playwright_h5')
    dashboard = provider.get_dashboard()
    assert dashboard.source == 'playwright-h5-offline'
    assert dashboard.evidence_refs


@pytest.mark.parametrize('provider_name', ['real_upstream'])
def test_placeholder_real_upstream_provider_is_not_ready(provider_name: str) -> None:
    provider = resolve_read_provider(provider_name)
    with pytest.raises(NotImplementedError):
        provider.get_dashboard()


def test_resolver_rejects_unknown_provider() -> None:
    with pytest.raises(ValueError):
        resolve_read_provider('unknown-provider')


def test_provider_keys_include_demo_and_future_slots() -> None:
    keys = set(list_read_provider_keys())
    assert {'demo', 'playwright_h5', 'real_upstream'}.issubset(keys)
