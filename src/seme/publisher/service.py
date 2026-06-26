from src.seme.publisher.bus import AsyncEventBus
from src.seme.publisher.event import Event

bus = AsyncEventBus()


def publish(name: str, payload: dict) -> None:
    event = Event(name=name, payload=payload)
    bus.publish(event)
