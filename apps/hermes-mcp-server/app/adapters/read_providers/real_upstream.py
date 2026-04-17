from __future__ import annotations

import sys
from pathlib import Path

try:
    from xianyu_schemas.read_models import (
        DailyReportResponse,
        DashboardResponse,
        ItemListResponse,
        OrderListResponse,
        ReplySuggestionResponse,
        UnreadChatListResponse,
    )
    from xianyu_schemas.tools import (
        DailyReportInput,
        ListItemsInput,
        ListOrdersInput,
        ListUnreadChatsInput,
        SuggestReplyInput,
    )
except ModuleNotFoundError:  # pragma: no cover - direct script fallback
    repo_root = Path(__file__).resolve().parents[5]
    schema_package = repo_root / "packages" / "xianyu-schemas"
    schema_path = str(schema_package)
    if schema_package.exists() and schema_path not in sys.path:
        sys.path.append(schema_path)

    from xianyu_schemas.read_models import (
        DailyReportResponse,
        DashboardResponse,
        ItemListResponse,
        OrderListResponse,
        ReplySuggestionResponse,
        UnreadChatListResponse,
    )
    from xianyu_schemas.tools import (
        DailyReportInput,
        ListItemsInput,
        ListOrdersInput,
        ListUnreadChatsInput,
        SuggestReplyInput,
    )


class RealUpstreamReadFoundationAdapter:
    """Placeholder for future real-upstream read-only adapter."""

    provider_name = "real_upstream"

    def _not_ready(self) -> NotImplementedError:
        return NotImplementedError(
            "real_upstream adapter is scaffolded only and intentionally disabled in MVP-0"
        )

    def get_dashboard(self, account_id: str = "demo-account") -> DashboardResponse:
        raise self._not_ready()

    def list_orders(self, query: ListOrdersInput) -> OrderListResponse:
        raise self._not_ready()

    def list_items(self, query: ListItemsInput) -> ItemListResponse:
        raise self._not_ready()

    def list_unread_chats(self, query: ListUnreadChatsInput) -> UnreadChatListResponse:
        raise self._not_ready()

    def suggest_reply(self, query: SuggestReplyInput) -> ReplySuggestionResponse:
        raise self._not_ready()

    def daily_report(self, query: DailyReportInput) -> DailyReportResponse:
        raise self._not_ready()
