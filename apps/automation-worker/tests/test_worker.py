from app.workers.sync import describe_worker_capabilities


def test_worker_capabilities_contains_sync_orders() -> None:
    assert "sync_orders" in describe_worker_capabilities()
