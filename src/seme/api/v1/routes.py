# src/seme/api/v1/routes.py
from fastapi import APIRouter
from src.seme.publisher.service import publish

router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.post("/pipeline")
async def pipeline(payload: dict):
    return await publish(payload)

@router.post("/publish")
async def publish_endpoint(payload: dict):
    return await publish(payload)
