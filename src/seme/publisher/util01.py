import json
from src.seme.publisher import EventPublisher
from src.seme.models import SEMEEvent


class FilePublisher(EventPublisher):
    def __init__(self, path: str):
        self.path = path

    def publish(self, event: SEMEEvent) -> None:
        with open(self.path, "a") as f:
            f.write(json.dumps(event.__dict__) + "\n")
