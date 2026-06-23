from fastapi import APIRouter
from src.seme.core import SEME
from src.models.seme import SemeValidationResponse

router = APIRouter(prefix="/seme", tags=["SEME"])

@router.get(
    "/validate",
    response_model=SemeValidationResponse
)
def validate():
    return SEME.validate()
