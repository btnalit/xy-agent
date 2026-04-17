from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from app.adapters.read_providers.demo import DemoReadFoundationProvider
from xianyu_schemas.read_models import (
    DashboardResponse,
    ItemListResponse,
    OrderListResponse,
    ReplySuggestionResponse,
    UnreadChatListResponse,
    DailyReportResponse,
)
from xianyu_schemas.tools import (
    DailyReportInput,
    ListItemsInput,
    ListOrdersInput,
    ListUnreadChatsInput,
    SuggestReplyInput,
)


@dataclass(slots=True)
class PlaywrightH5AdapterSettings:
    offline_mode: bool = True
    browser_channel: str = 'chromium'
    locale: str = 'zh-CN'
    timezone_id: str = 'Asia/Shanghai'
    fixture_namespace: str = 'playwright_h5'


@dataclass(slots=True)
class BrowserSessionProfile:
    profile_name: str = 'xianyu-readonly-offline'
    headless: bool = True
    persist_storage_state: bool = False
    user_agent: str = 'Hermes-PlaywrightH5-Offline/1.0'


@dataclass(slots=True)
class PageAcquisitionPlan:
    page_type: str
    entrypoint: str
    wait_for: str
    parser_name: str
    fixture_ref: str


@dataclass(slots=True)
class PageCapture:
    plan: PageAcquisitionPlan
    captured_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    payload: dict[str, Any] = field(default_factory=dict)


class PlaywrightH5ReadFoundationAdapter(DemoReadFoundationProvider):
    """Offline/mock Playwright-H5 read-only adapter.

    This adapter intentionally does not touch the network or any real Xianyu account.
    It models the internal structure we will need later (session profile, page plans,
    acquisition hooks, extraction pipeline), but currently serves deterministic fixture-backed
    data through the existing response contracts.
    """

    provider_name = 'playwright_h5'

    def __init__(
        self,
        settings: PlaywrightH5AdapterSettings | None = None,
        session_profile: BrowserSessionProfile | None = None,
    ) -> None:
        super().__init__()
        self.settings = settings or PlaywrightH5AdapterSettings()
        self.session_profile = session_profile or BrowserSessionProfile()
        self._plans = {
            'dashboard': PageAcquisitionPlan(
                page_type='dashboard',
                entrypoint='/h5/dashboard',
                wait_for='[data-page="dashboard"]',
                parser_name='dashboard_summary',
                fixture_ref='fixture://playwright_h5/dashboard',
            ),
            'orders': PageAcquisitionPlan(
                page_type='orders',
                entrypoint='/h5/orders',
                wait_for='[data-page="orders"]',
                parser_name='orders_table',
                fixture_ref='fixture://playwright_h5/orders',
            ),
            'items': PageAcquisitionPlan(
                page_type='items',
                entrypoint='/h5/items',
                wait_for='[data-page="items"]',
                parser_name='items_grid',
                fixture_ref='fixture://playwright_h5/items',
            ),
            'unread_chats': PageAcquisitionPlan(
                page_type='unread_chats',
                entrypoint='/h5/chat',
                wait_for='[data-page="chat"]',
                parser_name='unread_threads',
                fixture_ref='fixture://playwright_h5/unread_chats',
            ),
        }

    def _meta(self, tool_name: str, evidence_refs: list[str]) -> dict[str, object]:
        return {
            'request_id': f'{tool_name}-{uuid4().hex[:12]}',
            'evidence_refs': evidence_refs,
            'generated_at': datetime.now(timezone.utc),
            'source': 'playwright-h5-offline',
        }

    def _capture_page(self, page_key: str) -> PageCapture:
        plan = self._plans[page_key]
        return PageCapture(
            plan=plan,
            payload={
                'offline_mode': self.settings.offline_mode,
                'profile': self.session_profile.profile_name,
                'entrypoint': plan.entrypoint,
                'parser': plan.parser_name,
            },
        )

    def get_dashboard(self, account_id: str = 'demo-account') -> DashboardResponse:
        capture = self._capture_page('dashboard')
        response = super().get_dashboard(account_id=account_id)
        data = response.model_dump(mode='python')
        data['evidence_refs'] = [capture.plan.fixture_ref, 'offline://playwright/session/dashboard']
        data['source'] = 'playwright-h5-offline'
        return DashboardResponse(**data)

    def list_orders(self, query: ListOrdersInput) -> OrderListResponse:
        capture = self._capture_page('orders')
        response = super().list_orders(query)
        data = response.model_dump(mode='python')
        data['evidence_refs'] = [capture.plan.fixture_ref, 'offline://playwright/session/orders']
        data['source'] = 'playwright-h5-offline'
        return OrderListResponse(**data)

    def list_items(self, query: ListItemsInput) -> ItemListResponse:
        capture = self._capture_page('items')
        response = super().list_items(query)
        data = response.model_dump(mode='python')
        data['evidence_refs'] = [capture.plan.fixture_ref, 'offline://playwright/session/items']
        data['source'] = 'playwright-h5-offline'
        return ItemListResponse(**data)

    def list_unread_chats(self, query: ListUnreadChatsInput) -> UnreadChatListResponse:
        capture = self._capture_page('unread_chats')
        response = super().list_unread_chats(query)
        data = response.model_dump(mode='python')
        data['evidence_refs'] = [capture.plan.fixture_ref, 'offline://playwright/session/unread_chats']
        data['source'] = 'playwright-h5-offline'
        return UnreadChatListResponse(**data)

    def suggest_reply(self, query: SuggestReplyInput) -> ReplySuggestionResponse:
        response = super().suggest_reply(query)
        data = response.model_dump(mode='python')
        data['evidence_refs'] = [f'fixture://playwright_h5/chat/{query.thread_id}', 'offline://playwright/session/reply_draft']
        data['source'] = 'playwright-h5-offline'
        return ReplySuggestionResponse(**data)

    def daily_report(self, query: DailyReportInput) -> DailyReportResponse:
        response = super().daily_report(query)
        data = response.model_dump(mode='python')
        data['evidence_refs'] = ['fixture://playwright_h5/daily_report', 'offline://playwright/session/report']
        data['source'] = 'playwright-h5-offline'
        return DailyReportResponse(**data)
