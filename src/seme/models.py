from dataclasses import dataclass, field
from typing import Any
from datetime import datetime
import uuid


@dataclass
class SEMEEvent:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    type: str = ""
    input: dict[str, Any] = field(default_factory=dict)
    output: dict[str, Any] = field(default_factory=dict)
    trace: list[dict[str, Any]] = field(default_factory=list)
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
