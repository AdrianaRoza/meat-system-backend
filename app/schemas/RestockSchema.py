from pydantic import BaseModel

class RestockBase(BaseModel):
    meat_id: int
    quantity_kg: float

class RestockCreate(RestockBase):
    pass

class RestockResponse(RestockBase):
    id: int

    class Config:
        orm_mode = True
