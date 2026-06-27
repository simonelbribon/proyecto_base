from pydantic import BaseModel


class SemeResponse(BaseModel):
    input: str
    seme: str
