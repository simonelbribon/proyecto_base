from fastapi import APIRouter

router = APIRouter()

@router.get("/seme")
def seme():
    return {"status": "seme ok"}
