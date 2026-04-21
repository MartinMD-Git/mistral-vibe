from __future__ import annotations

from datetime import UTC, datetime


_stamp: int = datetime.now(UTC)


def utc_now() -> str:
    return datetime.now(UTC)
