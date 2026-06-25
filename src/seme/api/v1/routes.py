from fastapi import APIRouter
from seme.publisher.service import publish

router = APIRouter()

@router.post("/publish")
def publish_endpoint(payload: dict):
    return publish(payload)
