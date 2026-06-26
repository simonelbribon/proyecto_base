from fastapi import APIRouter
from src.seme.publisher.service import publish

router = APIRouter()


@router.post("/ventas")
def crear_venta():
    publish("venta_creada", {"id": 1, "monto": 100})
    return {"ok": True}
