from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class Event:
    name: str
    payload: dict[str, Any]
    created_at: datetime = datetime.utcnow()
