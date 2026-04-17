from __future__ import annotations

import sys
from pathlib import Path
from typing import Protocol, runtime_checkable

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


@runtime_checkable
class ReadFoundationProvider(Protocol):
    """Read-only provider abstraction for Xianyu data sources."""

    provider_name: str

    def get_dashboard(self, account_id: str = "demo-account") -> DashboardResponse:
        """Return dashboard snapshot envelope."""

    def list_orders(self, query: ListOrdersInput) -> OrderListResponse:
        """Return paginated orders envelope."""

    def list_items(self, query: ListItemsInput) -> ItemListResponse:
        """Return paginated items envelope."""

    def list_unread_chats(self, query: ListUnreadChatsInput) -> UnreadChatListResponse:
        """Return unread chat threads envelope."""

    def suggest_reply(self, query: SuggestReplyInput) -> ReplySuggestionResponse:
        """Return read-only reply suggestion envelope."""

    def daily_report(self, query: DailyReportInput) -> DailyReportResponse:
        """Return read-only daily report envelope."""
