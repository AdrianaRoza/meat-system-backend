from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.RestockSchema import RestockCreate, RestockResponse
from app.crud.restock_crud import create_restock, get_all_restocks
from app.database import SessionLocal

router = APIRouter(
    prefix="/restocks",
    tags=["Restocks"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=RestockResponse)
def create_restock_route(restock: RestockCreate, db: Session = Depends(get_db)):
    result = create_restock(db, restock)
    if result is None:
        raise HTTPException(status_code=404, detail="Meat not found")
    return result

@router.get("/", response_model=list[RestockResponse])
def get_restocks_route(db: Session = Depends(get_db)):
    return get_all_restocks(db)
