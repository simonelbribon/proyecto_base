from fastapi import APIRouter

from src.api.schemas.ventas import VentaIn

router = APIRouter()


@router.get("/ventas")
def get_ventas():
    return {"status": "ventas ok"}


@router.post("/ventas")
def crear_venta(venta: VentaIn):
    return {"recibido": venta.model_dump()}
