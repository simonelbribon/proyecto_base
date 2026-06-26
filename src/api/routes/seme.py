from src.seme.publisher.service import publish
from fastapi import APIRouter
from src.seme.core import SEME
from src.models.seme import SemeValidationResponse
router = APIRouter()

@router.get(
    "/validate",
    response_model=SemeValidationResponse
)
def validate():
    return SEME.validate()
@router.post("/publish")
def publish_endpoint(payload: dict):
    return publish(payload)
