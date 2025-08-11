from pydantic import BaseModel
from datetime import datetime

class RestockBase(BaseModel):
    meat_id: int
    quantity_kg: float
    price_per_kg: float

class RestockCreate(RestockBase):
    pass  # usamos o mesmo que o base

class RestockResponse(RestockBase):
    id: int
    total_cost: float
    date: datetime

    class Config:
        orm_mode = True
