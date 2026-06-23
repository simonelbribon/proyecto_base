from src.seme.publisher import EventPublisher
from src.seme.models import SEMEEvent


class MemoryPublisher(EventPublisher):
    def __init__(self):
        self.events = []

    def publish(self, event: SEMEEvent) -> None:
        self.events.append(event)
