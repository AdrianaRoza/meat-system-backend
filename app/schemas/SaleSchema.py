from pydantic import BaseModel

class MeatInSale(BaseModel):
    id: int
    name: str
    price_per_kg: float

    class Config:
        orm_mode = True

class SaleBase(BaseModel):
    meat_id: int
    quantity_kg: float

class SaleCreate(SaleBase):
    pass

class SaleResponse(SaleBase):
    id: int
    total_price: float
    meat: MeatInSale  # adiciona a relação

    class Config:
        orm_mode = True
