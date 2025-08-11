from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.RestockSchema import RestockCreate, RestockResponse
from crud import restock_crud
from typing import List

router = APIRouter(prefix="/restocks", tags=["Restocks"])

@router.post("/", response_model=RestockResponse)
def create_restock(restock: RestockCreate, db: Session = Depends(get_db)):
    return restock_crud.create_restock(db, restock)

@router.get("/", response_model=List[RestockResponse])
def list_restocks(db: Session = Depends(get_db)):
    return restock_crud.get_all_restocks(db)
