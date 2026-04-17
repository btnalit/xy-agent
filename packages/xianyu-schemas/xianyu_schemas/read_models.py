from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, Field

OrderStatus = Literal[
    "pending_payment",
    "to_ship",
    "shipping",
    "finished",
    "refund_requested",
]
ItemStatus = Literal["on_sale", "off_shelf", "sold_out"]
ChatPriority = Literal["high", "medium", "low"]


class ToolResponseEnvelope(BaseModel):
    request_id: str = Field(min_length=8)
    evidence_refs: list[str] = Field(default_factory=list)
    generated_at: datetime
    source: str = "demo-provider"


class DashboardData(BaseModel):
    account_id: str
    shop_name: str
    snapshot_at: datetime
    pending_orders: int = Field(ge=0)
    unread_threads: int = Field(ge=0)
    low_stock_items: int = Field(ge=0)
    today_views: int = Field(ge=0)
    conversion_rate: float = Field(ge=0.0, le=1.0)
    alerts: list[str] = Field(default_factory=list)


class DashboardResponse(ToolResponseEnvelope):
    tool_name: Literal["xianyu_get_dashboard"] = "xianyu_get_dashboard"
    data: DashboardData


class OrderSummary(BaseModel):
    order_id: str
    item_id: str
    item_title: str
    buyer_name: str
    status: OrderStatus
    total_amount: float = Field(gt=0)
    unread_messages: int = Field(ge=0)
    created_at: datetime
    updated_at: datetime


class OrderListData(BaseModel):
    account_id: str
    status_filter: str | None = None
    page: int = Field(ge=1)
    limit: int = Field(ge=1, le=100)
    total: int = Field(ge=0)
    orders: list[OrderSummary] = Field(default_factory=list)


class OrderListResponse(ToolResponseEnvelope):
    tool_name: Literal["xianyu_list_orders"] = "xianyu_list_orders"
    data: OrderListData


class ItemSummary(BaseModel):
    item_id: str
    title: str
    status: ItemStatus
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    views_today: int = Field(ge=0)
    favorites: int = Field(ge=0)
    updated_at: datetime


class ItemListData(BaseModel):
    account_id: str
    keyword: str | None = None
    status_filter: str | None = None
    page: int = Field(ge=1)
    limit: int = Field(ge=1, le=100)
    total: int = Field(ge=0)
    items: list[ItemSummary] = Field(default_factory=list)


class ItemListResponse(ToolResponseEnvelope):
    tool_name: Literal["xianyu_list_items"] = "xianyu_list_items"
    data: ItemListData


class UnreadChatThread(BaseModel):
    thread_id: str
    buyer_name: str
    item_id: str
    item_title: str
    unread_count: int = Field(ge=1)
    last_message: str
    last_message_at: datetime
    priority: ChatPriority


class UnreadChatListData(BaseModel):
    account_id: str
    page: int = Field(ge=1)
    limit: int = Field(ge=1, le=100)
    total: int = Field(ge=0)
    threads: list[UnreadChatThread] = Field(default_factory=list)


class UnreadChatListResponse(ToolResponseEnvelope):
    tool_name: Literal["xianyu_list_unread_chats"] = "xianyu_list_unread_chats"
    data: UnreadChatListData


class ReplySuggestionData(BaseModel):
    thread_id: str
    tone: str
    goal: str
    suggested_reply: str = Field(min_length=1, max_length=2000)
    rationale: list[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0)
    approval_required_for_send: bool = True
    approval_boundary_note: str


class ReplySuggestionResponse(ToolResponseEnvelope):
    tool_name: Literal["xianyu_suggest_reply"] = "xianyu_suggest_reply"
    data: ReplySuggestionData


class DailyReportKpi(BaseModel):
    total_orders: int = Field(ge=0)
    pending_orders: int = Field(ge=0)
    unread_threads: int = Field(ge=0)
    on_sale_items: int = Field(ge=0)
    low_stock_items: int = Field(ge=0)
    estimated_gmv: float = Field(ge=0)


class DailyReportAction(BaseModel):
    action: str
    reason: str
    priority: Literal["P0", "P1", "P2"]
    requires_approval: bool = False


class DailyReportData(BaseModel):
    report_date: date
    account_id: str
    summary: str
    kpis: DailyReportKpi
    top_risks: list[str] = Field(default_factory=list)
    recommended_actions: list[DailyReportAction] = Field(default_factory=list)
    approval_boundary_note: str


class DailyReportResponse(ToolResponseEnvelope):
    tool_name: Literal["xianyu_daily_report"] = "xianyu_daily_report"
    data: DailyReportData
