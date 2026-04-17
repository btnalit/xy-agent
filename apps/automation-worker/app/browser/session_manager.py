from dataclasses import dataclass


@dataclass(slots=True)
class BrowserSession:
    account_id: str
    browser_profile_path: str
    proxy_id: str | None = None
    risk_level: str = "normal"
