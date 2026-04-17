from __future__ import annotations

from app.adapters.read_providers import PlaywrightH5ReadFoundationAdapter
from xianyu_schemas.tools import ListItemsInput, ListOrdersInput, ListUnreadChatsInput


def test_playwright_h5_dashboard_offline_envelope() -> None:
    provider = PlaywrightH5ReadFoundationAdapter()
    response = provider.get_dashboard()
    assert response.source == 'playwright-h5-offline'
    assert response.tool_name == 'xianyu_get_dashboard'
    assert response.evidence_refs[0].startswith('fixture://playwright_h5/dashboard')


def test_playwright_h5_orders_offline_envelope() -> None:
    provider = PlaywrightH5ReadFoundationAdapter()
    response = provider.list_orders(ListOrdersInput(limit=5, page=1))
    assert response.source == 'playwright-h5-offline'
    assert response.data.orders
    assert response.evidence_refs[0].startswith('fixture://playwright_h5/orders')


def test_playwright_h5_items_offline_envelope() -> None:
    provider = PlaywrightH5ReadFoundationAdapter()
    response = provider.list_items(ListItemsInput(limit=5, page=1))
    assert response.source == 'playwright-h5-offline'
    assert response.data.items
    assert response.evidence_refs[0].startswith('fixture://playwright_h5/items')


def test_playwright_h5_unread_chats_offline_envelope() -> None:
    provider = PlaywrightH5ReadFoundationAdapter()
    response = provider.list_unread_chats(ListUnreadChatsInput(limit=5, page=1))
    assert response.source == 'playwright-h5-offline'
    assert response.data.threads
    assert response.evidence_refs[0].startswith('fixture://playwright_h5/unread_chats')
