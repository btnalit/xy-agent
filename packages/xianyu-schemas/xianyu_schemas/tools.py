from __future__ import annotations

from datetime import date as date_type

from pydantic import BaseModel, Field


class ListOrdersInput(BaseModel):
    status: str | None = None
    limit: int = Field(default=20, ge=1, le=100)
    page: int = Field(default=1, ge=1)


class ListItemsInput(BaseModel):
    keyword: str | None = None
    status: str | None = None
    limit: int = Field(default=20, ge=1, le=100)
    page: int = Field(default=1, ge=1)


class ListUnreadChatsInput(BaseModel):
    limit: int = Field(default=20, ge=1, le=100)
    page: int = Field(default=1, ge=1)


class SuggestReplyInput(BaseModel):
    thread_id: str
    tone: str | None = None
    goal: str | None = None


class DailyReportInput(BaseModel):
    date: date_type | None = None


class SendReplyInput(BaseModel):
    thread_id: str
    message: str = Field(min_length=1, max_length=2000)
    require_approval: bool = True
