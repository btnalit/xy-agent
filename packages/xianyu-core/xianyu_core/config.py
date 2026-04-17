from pydantic import BaseModel


class AppSettings(BaseModel):
    app_name: str = "xianyu-agent-platform"
    environment: str = "development"
    require_approval_for_write_actions: bool = True
