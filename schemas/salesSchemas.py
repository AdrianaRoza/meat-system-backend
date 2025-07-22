from pydantic import BaseModel

class SaleCreate(BaseModel):
    meat_id: int
    quantity_kg: float

class SaleResponse(SaleCreate):
    id: int
    total_price: float

    class Config:
        orm_mode = True
