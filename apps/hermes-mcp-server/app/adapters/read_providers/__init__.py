from __future__ import annotations

from .base import ReadFoundationProvider
from .demo import DemoReadFoundationProvider
from .playwright_h5 import PlaywrightH5ReadFoundationAdapter
from .real_upstream import RealUpstreamReadFoundationAdapter

__all__ = [
    "ReadFoundationProvider",
    "DemoReadFoundationProvider",
    "PlaywrightH5ReadFoundationAdapter",
    "RealUpstreamReadFoundationAdapter",
]
