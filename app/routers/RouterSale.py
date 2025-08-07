from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.SaleSchema import SaleCreate, SaleResponse
from app.crud.sale_crud import create_sale, get_all_sales
from app.database import SessionLocal

router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)

# Dependência de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SaleResponse)
def create_sale_route(sale: SaleCreate, db: Session = Depends(get_db)):
    result = create_sale(db, sale)
    if result is None:
        raise HTTPException(status_code=404, detail="Meat not found")
    if result == "not_enough_stock":
        raise HTTPException(status_code=400, detail="Not enough stock")
    return result

@router.get("/", response_model=list[SaleResponse])
def get_sales_route(db: Session = Depends(get_db)):
    return get_all_sales(db)
