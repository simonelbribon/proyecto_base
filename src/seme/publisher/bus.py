import asyncio
import logging
from typing import Callable, Dict, List, Awaitable
from seme.publisher.event import Event

logger = logging.getLogger(__name__)

Handler = Callable[[dict], Awaitable[None]]

class AsyncEventBus:
    def __init__(self):
        self._handlers: Dict[str, List[Handler]] = {}

    def subscribe(self, event_type: str, handler: Handler):
        self._handlers.setdefault(event_type, []).append(handler)

    async def publish(self, event: Event):
        handlers = self._handlers.get(event.type, [])

        tasks = [
            self._safe_execute(handler, event.payload)
            for handler in handlers
        ]

        if tasks:
            await asyncio.gather(*tasks)

    async def _safe_execute(self, handler: Handler, payload: dict):
        try:
            await handler(payload)
        except Exception as e:
            logger.error(f"Handler failed: {handler.__name__} -> {e}")
