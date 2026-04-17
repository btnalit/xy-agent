from __future__ import annotations

import sys
from datetime import date, datetime, timezone
from pathlib import Path
from uuid import uuid4

try:
    from xianyu_schemas.read_models import (
        DailyReportAction,
        DailyReportData,
        DailyReportKpi,
        DailyReportResponse,
        DashboardData,
        DashboardResponse,
        ItemListData,
        ItemListResponse,
        ItemSummary,
        OrderListData,
        OrderListResponse,
        OrderSummary,
        ReplySuggestionData,
        ReplySuggestionResponse,
        UnreadChatListData,
        UnreadChatListResponse,
        UnreadChatThread,
    )
    from xianyu_schemas.tools import (
        DailyReportInput,
        ListItemsInput,
        ListOrdersInput,
        ListUnreadChatsInput,
        SuggestReplyInput,
    )
except ModuleNotFoundError:  # pragma: no cover - direct script fallback
    repo_root = Path(__file__).resolve().parents[4]
    schema_package = repo_root / "packages" / "xianyu-schemas"
    schema_path = str(schema_package)
    if schema_package.exists() and schema_path not in sys.path:
        sys.path.append(schema_path)

    from xianyu_schemas.read_models import (
        DailyReportAction,
        DailyReportData,
        DailyReportKpi,
        DailyReportResponse,
        DashboardData,
        DashboardResponse,
        ItemListData,
        ItemListResponse,
        ItemSummary,
        OrderListData,
        OrderListResponse,
        OrderSummary,
        ReplySuggestionData,
        ReplySuggestionResponse,
        UnreadChatListData,
        UnreadChatListResponse,
        UnreadChatThread,
    )
    from xianyu_schemas.tools import (
        DailyReportInput,
        ListItemsInput,
        ListOrdersInput,
        ListUnreadChatsInput,
        SuggestReplyInput,
    )


class DemoReadFoundationProvider:
    """Read-only demo provider for MVP-1 foundation endpoints."""

    def __init__(self) -> None:
        self.account_id = "demo-account"
        self.shop_name = "闲鱼演示店铺"

        self._items = [
            ItemSummary(
                item_id="item-1001",
                title="复古机械键盘（87键）",
                status="on_sale",
                price=299.0,
                stock=4,
                views_today=128,
                favorites=22,
                updated_at=datetime(2026, 4, 17, 6, 50, tzinfo=timezone.utc),
            ),
            ItemSummary(
                item_id="item-1002",
                title="iPad Pro 11 保护壳",
                status="on_sale",
                price=69.0,
                stock=2,
                views_today=95,
                favorites=35,
                updated_at=datetime(2026, 4, 17, 6, 10, tzinfo=timezone.utc),
            ),
            ItemSummary(
                item_id="item-1003",
                title="Switch 游戏卡带合集",
                status="sold_out",
                price=188.0,
                stock=0,
                views_today=54,
                favorites=12,
                updated_at=datetime(2026, 4, 16, 14, 35, tzinfo=timezone.utc),
            ),
            ItemSummary(
                item_id="item-1004",
                title="二手显示器支架",
                status="on_sale",
                price=119.0,
                stock=1,
                views_today=63,
                favorites=9,
                updated_at=datetime(2026, 4, 17, 5, 20, tzinfo=timezone.utc),
            ),
        ]

        self._orders = [
            OrderSummary(
                order_id="order-9004",
                item_id="item-1004",
                item_title="二手显示器支架",
                buyer_name="王五",
                status="pending_payment",
                total_amount=119.0,
                unread_messages=1,
                created_at=datetime(2026, 4, 17, 7, 15, tzinfo=timezone.utc),
                updated_at=datetime(2026, 4, 17, 7, 20, tzinfo=timezone.utc),
            ),
            OrderSummary(
                order_id="order-9001",
                item_id="item-1001",
                item_title="复古机械键盘（87键）",
                buyer_name="张三",
                status="to_ship",
                total_amount=299.0,
                unread_messages=1,
                created_at=datetime(2026, 4, 17, 5, 40, tzinfo=timezone.utc),
                updated_at=datetime(2026, 4, 17, 5, 45, tzinfo=timezone.utc),
            ),
            OrderSummary(
                order_id="order-9002",
                item_id="item-1002",
                item_title="iPad Pro 11 保护壳",
                buyer_name="李四",
                status="shipping",
                total_amount=69.0,
                unread_messages=0,
                created_at=datetime(2026, 4, 16, 12, 5, tzinfo=timezone.utc),
                updated_at=datetime(2026, 4, 17, 2, 0, tzinfo=timezone.utc),
            ),
            OrderSummary(
                order_id="order-9003",
                item_id="item-1003",
                item_title="Switch 游戏卡带合集",
                buyer_name="赵六",
                status="finished",
                total_amount=188.0,
                unread_messages=0,
                created_at=datetime(2026, 4, 15, 10, 10, tzinfo=timezone.utc),
                updated_at=datetime(2026, 4, 16, 18, 30, tzinfo=timezone.utc),
            ),
        ]

        self._threads = [
            UnreadChatThread(
                thread_id="thread-7001",
                buyer_name="张三",
                item_id="item-1001",
                item_title="复古机械键盘（87键）",
                unread_count=1,
                last_message="可以今天发货吗？",
                last_message_at=datetime(2026, 4, 17, 7, 22, tzinfo=timezone.utc),
                priority="medium",
            ),
            UnreadChatThread(
                thread_id="thread-7002",
                buyer_name="王五",
                item_id="item-1004",
                item_title="二手显示器支架",
                unread_count=3,
                last_message="能包邮再便宜 10 块吗？",
                last_message_at=datetime(2026, 4, 17, 7, 28, tzinfo=timezone.utc),
                priority="high",
            ),
            UnreadChatThread(
                thread_id="thread-7003",
                buyer_name="周七",
                item_id="item-1002",
                item_title="iPad Pro 11 保护壳",
                unread_count=2,
                last_message="这个是原装材质吗？",
                last_message_at=datetime(2026, 4, 17, 6, 55, tzinfo=timezone.utc),
                priority="medium",
            ),
        ]

    def _meta(self, tool_name: str, evidence_refs: list[str]) -> dict[str, object]:
        return {
            "request_id": f"{tool_name}-{uuid4().hex[:12]}",
            "evidence_refs": evidence_refs,
            "generated_at": datetime.now(timezone.utc),
            "source": "demo-provider",
        }

    def get_dashboard(self, account_id: str = "demo-account") -> DashboardResponse:
        pending_orders = sum(
            order.status in {"pending_payment", "to_ship"} for order in self._orders
        )
        unread_threads = sum(thread.unread_count > 0 for thread in self._threads)
        low_stock_items = sum(
            item.status == "on_sale" and item.stock <= 2 for item in self._items
        )
        total_views = sum(item.views_today for item in self._items)

        alerts = [
            f"{pending_orders} 个订单待处理（含待付款/待发货）",
            f"{low_stock_items} 个在售商品库存低于等于 2",
            f"{unread_threads} 个未读会话待回复",
        ]

        data = DashboardData(
            account_id=account_id,
            shop_name=self.shop_name,
            snapshot_at=datetime.now(timezone.utc),
            pending_orders=pending_orders,
            unread_threads=unread_threads,
            low_stock_items=low_stock_items,
            today_views=total_views,
            conversion_rate=0.036,
            alerts=alerts,
        )

        return DashboardResponse(
            tool_name="xianyu_get_dashboard",
            data=data,
            **self._meta(
                "xianyu_get_dashboard",
                [
                    "demo://dashboard/snapshot",
                    "docs://runbooks/approval-policy#read-only-boundary",
                ],
            ),
        )

    def list_orders(self, query: ListOrdersInput) -> OrderListResponse:
        filtered_orders = self._orders
        if query.status:
            filtered_orders = [
                order for order in filtered_orders if order.status == query.status
            ]

        total = len(filtered_orders)
        start = (query.page - 1) * query.limit
        end = start + query.limit
        paginated_orders = filtered_orders[start:end]

        data = OrderListData(
            account_id=self.account_id,
            status_filter=query.status,
            page=query.page,
            limit=query.limit,
            total=total,
            orders=paginated_orders,
        )

        return OrderListResponse(
            tool_name="xianyu_list_orders",
            data=data,
            **self._meta(
                "xianyu_list_orders",
                [
                    "demo://orders/order-9001",
                    "demo://orders/order-9004",
                ],
            ),
        )

    def list_items(self, query: ListItemsInput) -> ItemListResponse:
        filtered_items = self._items

        if query.keyword:
            keyword = query.keyword.lower()
            filtered_items = [
                item for item in filtered_items if keyword in item.title.lower()
            ]

        if query.status:
            filtered_items = [
                item for item in filtered_items if item.status == query.status
            ]

        total = len(filtered_items)
        start = (query.page - 1) * query.limit
        end = start + query.limit
        paginated_items = filtered_items[start:end]

        data = ItemListData(
            account_id=self.account_id,
            keyword=query.keyword,
            status_filter=query.status,
            page=query.page,
            limit=query.limit,
            total=total,
            items=paginated_items,
        )

        return ItemListResponse(
            tool_name="xianyu_list_items",
            data=data,
            **self._meta(
                "xianyu_list_items",
                [
                    "demo://items/item-1001",
                    "demo://items/item-1004",
                ],
            ),
        )

    def list_unread_chats(self, query: ListUnreadChatsInput) -> UnreadChatListResponse:
        unread_threads = [thread for thread in self._threads if thread.unread_count > 0]
        total = len(unread_threads)
        start = (query.page - 1) * query.limit
        end = start + query.limit

        data = UnreadChatListData(
            account_id=self.account_id,
            page=query.page,
            limit=query.limit,
            total=total,
            threads=unread_threads[start:end],
        )

        return UnreadChatListResponse(
            tool_name="xianyu_list_unread_chats",
            data=data,
            **self._meta(
                "xianyu_list_unread_chats",
                [
                    "demo://chat/thread-7001",
                    "demo://chat/thread-7002",
                ],
            ),
        )

    def suggest_reply(self, query: SuggestReplyInput) -> ReplySuggestionResponse:
        thread = self._find_thread(query.thread_id)

        tone = query.tone or "professional_friendly"
        goal = query.goal or "推进成交并确认发货时效"

        suggested_reply = (
            f"你好 {thread.buyer_name}，这件“{thread.item_title}”目前库存在，"
            f"我这边可以在今天内安排发出。关于你提到的“{thread.last_message}”，"
            "我建议按平台规则给你最优方案，若你现在下单我会优先处理。"
        )

        data = ReplySuggestionData(
            thread_id=thread.thread_id,
            tone=tone,
            goal=goal,
            suggested_reply=suggested_reply,
            rationale=[
                "先确认库存与发货时效，降低买家不确定性",
                "引用买家最近问题，提升上下文相关性",
                "给出明确下一步动作，推进成交",
            ],
            confidence=0.84,
            approval_required_for_send=True,
            approval_boundary_note=(
                "当前接口仅返回回复草稿；真实发送属于写操作，"
                "必须走审批与审计流程。"
            ),
        )

        return ReplySuggestionResponse(
            tool_name="xianyu_suggest_reply",
            data=data,
            **self._meta(
                "xianyu_suggest_reply",
                [
                    f"demo://chat/{thread.thread_id}",
                    "docs://runbooks/approval-policy#must-approve",
                ],
            ),
        )

    def daily_report(self, query: DailyReportInput) -> DailyReportResponse:
        report_date = query.date or date.today()
        pending_orders = sum(
            order.status in {"pending_payment", "to_ship"} for order in self._orders
        )
        unread_threads = sum(thread.unread_count > 0 for thread in self._threads)
        on_sale_items = sum(item.status == "on_sale" for item in self._items)
        low_stock_items = sum(
            item.status == "on_sale" and item.stock <= 2 for item in self._items
        )

        kpis = DailyReportKpi(
            total_orders=len(self._orders),
            pending_orders=pending_orders,
            unread_threads=unread_threads,
            on_sale_items=on_sale_items,
            low_stock_items=low_stock_items,
            estimated_gmv=round(sum(order.total_amount for order in self._orders), 2),
        )

        actions = [
            DailyReportAction(
                action="优先回复高优先级未读会话",
                reason="可直接提升成交率并降低流失风险",
                priority="P0",
                requires_approval=False,
            ),
            DailyReportAction(
                action="补充低库存商品库存或调整可售状态",
                reason="避免意向买家下单后无法履约",
                priority="P1",
                requires_approval=True,
            ),
            DailyReportAction(
                action="整理待发货订单并批量打印面单",
                reason="缩短履约时效，减少催发货消息",
                priority="P1",
                requires_approval=True,
            ),
        ]

        summary = (
            f"截至 {report_date.isoformat()}，共 {len(self._orders)} 笔订单，"
            f"其中 {pending_orders} 笔待处理，"
            f"未读会话 {unread_threads} 个，在售商品 {on_sale_items} 个。"
        )

        data = DailyReportData(
            report_date=report_date,
            account_id=self.account_id,
            summary=summary,
            kpis=kpis,
            top_risks=[
                "低库存商品在促销时段可能缺货",
                "高优先级未读会话超过 30 分钟未响应",
            ],
            recommended_actions=actions,
            approval_boundary_note=(
                "本批次仅提供只读分析与建议；真实发送、改价、上/下架等写动作"
                "需审批后执行。"
            ),
        )

        return DailyReportResponse(
            tool_name="xianyu_daily_report",
            data=data,
            **self._meta(
                "xianyu_daily_report",
                [
                    "demo://reports/daily/2026-04-17",
                    "docs://architecture/mcp-tools#approval-boundary",
                ],
            ),
        )

    def _find_thread(self, thread_id: str) -> UnreadChatThread:
        for thread in self._threads:
            if thread.thread_id == thread_id:
                return thread
        raise KeyError(f"thread not found: {thread_id}")
