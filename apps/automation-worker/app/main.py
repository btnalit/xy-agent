try:
    from app.workers.sync import describe_worker_capabilities
except ModuleNotFoundError:  # pragma: no cover - direct script fallback
    from workers.sync import describe_worker_capabilities


if __name__ == "__main__":
    print(describe_worker_capabilities())
