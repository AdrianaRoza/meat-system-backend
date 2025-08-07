from pydantic import BaseModel

class SaleBase(BaseModel):
    meat_id: int
    quantity_kg: float

class SaleCreate(SaleBase):
    pass

class SaleResponse(SaleBase):
    id: int
    total_price: float

    class Config:
        orm_mode = True
