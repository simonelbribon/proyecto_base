from seme.publisher.bus import AsyncEventBus
from seme.publisher.event import Event
from seme.publisher.handlers import handle_publish

bus = AsyncEventBus()

bus.subscribe("publish", handle_publish)

async def publish(data: dict):
    await bus.publish(Event(type="publish", payload=data))
    return {"status": "dispatched"}
