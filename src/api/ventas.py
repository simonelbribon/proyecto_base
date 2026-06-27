from pydantic import BaseModel

class VentaIn(BaseModel):
    id: int
    monto: float
