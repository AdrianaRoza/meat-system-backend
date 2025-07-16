from pydantic import BaseModel

# Dados que recebemos ao cadastrar carne
class MeatCreate(BaseModel):
    name: str
    type: str
    price_per_kg: float
    stock_kg: float

# Dados que retornamos da API
class MeatOut(MeatCreate):
    id: int

    class Config:
        orm_mode = True
