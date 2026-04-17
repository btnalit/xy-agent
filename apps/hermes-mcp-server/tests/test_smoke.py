from app.services.dashboard import build_demo_dashboard


def test_demo_dashboard_shape() -> None:
    payload = build_demo_dashboard()
    assert payload["account_id"] == "demo-account"
    assert payload["pending_orders"] >= 0
    assert isinstance(payload["alerts"], list)
