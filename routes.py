from fastapi import APIRouter
from src.seme.pipeline import run_pipeline

router = APIRouter(prefix="/v1")


@router.post("/process")
def process(record: dict):
    event = run_pipeline(record)
    return event.__dict__
