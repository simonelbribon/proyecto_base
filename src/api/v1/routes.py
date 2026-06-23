from fastapi import APIRouter
from src.seme.pipeline import run_pipeline

router = APIRouter(prefix="/v1")


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/pipeline")
def pipeline(payload: dict):
    text = payload.get("text", "")
    return run_pipeline(text)
