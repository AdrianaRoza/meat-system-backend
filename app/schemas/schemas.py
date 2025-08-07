from pydantic import BaseModel
from typing import Optional

class MeatBase(BaseModel):
    name: str
    type: str
    price_per_kg: float
    stock_kg: float

class MeatCreate(MeatBase):
    pass

class MeatUpdate(MeatBase):
    pass

class MeatResponse(BaseModel):
    ...
    model_config = {
        "from_attributes": True
    }
