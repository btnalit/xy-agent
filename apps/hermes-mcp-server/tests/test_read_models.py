from __future__ import annotations

from datetime import date, datetime, timezone

import pytest
from pydantic import ValidationError
from xianyu_schemas.read_models import (
    DailyReportData,
    DailyReportKpi,
    DailyReportResponse,
    ReplySuggestionData,
)


def test_reply_suggestion_confidence_validation() -> None:
    with pytest.raises(ValidationError):
        ReplySuggestionData(
            thread_id="thread-7001",
            tone="friendly",
            goal="test",
            suggested_reply="hello",
            rationale=["r1"],
            confidence=1.2,
            approval_required_for_send=True,
            approval_boundary_note="read-only",
        )


def test_daily_report_model_serialization() -> None:
    report = DailyReportResponse(
        request_id="xianyu_daily_report-0001",
        evidence_refs=["demo://reports/daily/2026-04-17"],
        generated_at=datetime(2026, 4, 17, 8, 0, tzinfo=timezone.utc),
        source="demo-provider",
        data=DailyReportData(
            report_date=date(2026, 4, 17),
            account_id="demo-account",
            summary="demo summary",
            kpis=DailyReportKpi(
                total_orders=4,
                pending_orders=2,
                unread_threads=3,
                on_sale_items=3,
                low_stock_items=2,
                estimated_gmv=675.0,
            ),
            top_risks=["risk"],
            recommended_actions=[],
            approval_boundary_note="write actions require approval",
        ),
    )

    dumped = report.model_dump(mode="json")
    assert dumped["tool_name"] == "xianyu_daily_report"
    assert dumped["data"]["kpis"]["pending_orders"] == 2
