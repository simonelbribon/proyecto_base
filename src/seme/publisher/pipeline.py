from src.seme.models import SEMEEvent
from src.seme.publisher import EventPublisher


def run_pipeline(record: dict, publisher: EventPublisher) -> SEMEEvent:
    event = SEMEEvent(
        type=record.get("type", "unknown"),
        input=record,
    )

    # ───────── normalize ─────────
    normalized = {
        "type": event.type.lower(),
        "payload": record.get("payload", {})
    }

    event.trace.append({"stage": "normalize", "data": normalized})

    # ───────── classify ─────────
    if normalized["type"] == "sale":
        category = "revenue_event"
    elif normalized["type"] == "inventory_event":
        category = "stock_event"
    else:
        category = "unknown"

    event.trace.append({"stage": "classify", "data": category})

    # ───────── output ─────────
    event.output = {
        "category": category,
        "id": event.id
    }

    # 💥 EMIT EVENT (sin saber dónde va)
    publisher.publish(event)

    return event
