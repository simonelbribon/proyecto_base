from pydantic import BaseModel


class TextRequest(BaseModel):
    text: str


class SemeResponse(BaseModel):
    input: str
    seme: str


class ProcessResponse(BaseModel):
    original: str
    processed: str


class PipelineResponse(BaseModel):
    input: str
    seme: str
    final: str
