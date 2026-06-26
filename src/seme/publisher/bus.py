from typing import Callable, Dict, List, Any

from src.seme.publisher.event import Event


class AsyncEventBus:
    def __init__(self) -> None:
        self._handlers: Dict[str, List[Callable[[Event], Any]]] = {}

    def subscribe(self, event_name: str, handler: Callable[[Event], Any]) -> None:
        if event_name not in self._handlers:
            self._handlers[event_name] = []
        self._handlers[event_name].append(handler)

    def publish(self, event: Event) -> None:
        handlers = self._handlers.get(event.name, [])
        for handler in handlers:
            handler(event)
