from fastapi import APIRouter

router = APIRouter()

@router.get("/ventas")
def get_ventas():
    return {"status": "ventas ok"}
