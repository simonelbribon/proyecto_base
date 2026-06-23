from pydantic import BaseModel


class SemeValidationResponse(BaseModel):
    simple: bool
    stable: bool
    modular: bool
    elegant: bool
    status: str
