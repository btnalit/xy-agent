from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_dashboard_endpoint_returns_envelope() -> None:
    response = client.get("/tools/xianyu_get_dashboard")
    assert response.status_code == 200
    payload = response.json()
    assert payload["tool_name"] == "xianyu_get_dashboard"
    assert payload["request_id"].startswith("xianyu_get_dashboard-")
    assert payload["evidence_refs"]


def test_list_orders_endpoint_supports_status_filter() -> None:
    response = client.get("/tools/xianyu_list_orders", params={"status": "to_ship"})
    assert response.status_code == 200
    payload = response.json()
    statuses = [order["status"] for order in payload["data"]["orders"]]
    assert statuses
    assert set(statuses) == {"to_ship"}


def test_list_items_endpoint_supports_keyword_filter() -> None:
    response = client.get("/tools/xianyu_list_items", params={"keyword": "键盘"})
    assert response.status_code == 200
    payload = response.json()
    assert payload["data"]["total"] >= 1
    assert all("键盘" in item["title"] for item in payload["data"]["items"])


def test_list_unread_chats_endpoint_returns_threads() -> None:
    response = client.get("/tools/xianyu_list_unread_chats", params={"limit": 2, "page": 1})
    assert response.status_code == 200
    payload = response.json()
    assert payload["tool_name"] == "xianyu_list_unread_chats"
    assert payload["data"]["threads"]
    assert all(thread["unread_count"] >= 1 for thread in payload["data"]["threads"])


def test_suggest_reply_endpoint_is_read_only() -> None:
    response = client.post(
        "/tools/xianyu_suggest_reply",
        json={"thread_id": "thread-7002", "tone": "friendly", "goal": "close deal"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["tool_name"] == "xianyu_suggest_reply"
    assert payload["data"]["approval_required_for_send"] is True


def test_suggest_reply_endpoint_returns_404_for_unknown_thread() -> None:
    response = client.post(
        "/tools/xianyu_suggest_reply",
        json={"thread_id": "thread-missing"},
    )
    assert response.status_code == 404


def test_daily_report_endpoint_supports_date_query() -> None:
    response = client.get("/tools/xianyu_daily_report", params={"date": "2026-04-17"})
    assert response.status_code == 200
    payload = response.json()
    assert payload["tool_name"] == "xianyu_daily_report"
    assert payload["data"]["report_date"] == "2026-04-17"
