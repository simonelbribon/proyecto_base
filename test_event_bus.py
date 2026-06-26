from src.seme.publisher.service import bus, publish


def handler(event):
    print(f"EVENTO RECIBIDO: {event.name} -> {event.payload}")


bus.subscribe("venta_creada", handler)

publish("venta_creada", {"id": 1, "monto": 100})
