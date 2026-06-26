from fastapi import APIRouter
from seme.publisher.service import publish

router = APIRouter()

@router.get("/ping")
def ping():
    return {"ok": True}

@router.post("/pipeline")
def pipeline(payload: dict):
    return publish(payload)

@router.post("/publish")
def publish_endpoint(payload: dict):
    return publish(payload)
