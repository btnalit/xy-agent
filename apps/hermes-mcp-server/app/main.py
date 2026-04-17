from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query

try:
    from app.services.dashboard import build_demo_dashboard
    from app.services.read_foundation import DemoReadFoundationProvider
except ModuleNotFoundError:  # pragma: no cover - direct script fallback
    from services.dashboard import build_demo_dashboard
    from services.read_foundation import DemoReadFoundationProvider

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
    repo_root = Path(__file__).resolve().parents[3]
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

app = FastAPI(title="xianyu-mcp-server", version="0.2.0")
provider = DemoReadFoundationProvider()


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok", "service": "hermes-mcp-server"}


@app.get("/demo/dashboard")
def demo_dashboard() -> dict:
    return build_demo_dashboard()


@app.get("/tools/xianyu_get_dashboard", response_model=DashboardResponse)
def xianyu_get_dashboard(account_id: str = "demo-account") -> DashboardResponse:
    return provider.get_dashboard(account_id=account_id)


@app.get("/tools/xianyu_list_orders", response_model=OrderListResponse)
def xianyu_list_orders(
    status: str | None = None,
    limit: int = Query(default=20, ge=1, le=100),
    page: int = Query(default=1, ge=1),
) -> OrderListResponse:
    payload = ListOrdersInput(status=status, limit=limit, page=page)
    return provider.list_orders(payload)


@app.get("/tools/xianyu_list_items", response_model=ItemListResponse)
def xianyu_list_items(
    keyword: str | None = None,
    status: str | None = None,
    limit: int = Query(default=20, ge=1, le=100),
    page: int = Query(default=1, ge=1),
) -> ItemListResponse:
    payload = ListItemsInput(keyword=keyword, status=status, limit=limit, page=page)
    return provider.list_items(payload)


@app.get("/tools/xianyu_list_unread_chats", response_model=UnreadChatListResponse)
def xianyu_list_unread_chats(
    limit: int = Query(default=20, ge=1, le=100),
    page: int = Query(default=1, ge=1),
) -> UnreadChatListResponse:
    payload = ListUnreadChatsInput(limit=limit, page=page)
    return provider.list_unread_chats(payload)


@app.post("/tools/xianyu_suggest_reply", response_model=ReplySuggestionResponse)
def xianyu_suggest_reply(payload: SuggestReplyInput) -> ReplySuggestionResponse:
    try:
        return provider.suggest_reply(payload)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@app.get("/tools/xianyu_daily_report", response_model=DailyReportResponse)
def xianyu_daily_report(
    report_date: date | None = Query(default=None, alias="date"),
) -> DailyReportResponse:
    payload = DailyReportInput(date=report_date)
    return provider.daily_report(payload)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
