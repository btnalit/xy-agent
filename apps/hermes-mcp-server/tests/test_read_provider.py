from app.services.read_foundation import DemoReadFoundationProvider
from xianyu_schemas.tools import DailyReportInput, ListOrdersInput, SuggestReplyInput


provider = DemoReadFoundationProvider()


def test_provider_orders_can_filter_by_status() -> None:
    response = provider.list_orders(ListOrdersInput(status="to_ship", limit=10, page=1))
    assert response.tool_name == "xianyu_list_orders"
    assert response.data.total >= 1
    assert all(order.status == "to_ship" for order in response.data.orders)


def test_provider_suggest_reply_contains_approval_boundary_note() -> None:
    response = provider.suggest_reply(
        SuggestReplyInput(thread_id="thread-7001", tone="friendly", goal="confirm shipping")
    )
    assert response.data.thread_id == "thread-7001"
    assert response.data.approval_required_for_send is True
    assert "审批" in response.data.approval_boundary_note


def test_provider_daily_report_contains_consistent_kpis() -> None:
    response = provider.daily_report(DailyReportInput())
    assert response.tool_name == "xianyu_daily_report"
    assert response.data.kpis.total_orders >= response.data.kpis.pending_orders
    assert response.data.kpis.unread_threads >= 0
