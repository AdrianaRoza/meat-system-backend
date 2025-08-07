from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas
from app import crud
from ..database import SessionLocal

router = APIRouter(
    prefix="/meats",
    tags=["Meats"]
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create new meat
@router.post("/", response_model=schemas.MeatResponse)
def create_meat(meat: schemas.MeatCreate, db: Session = Depends(get_db)):
    return crud.create_meat(db, meat)

# Get all meats
@router.get("/", response_model=list[schemas.MeatResponse])
def get_all_meats(db: Session = Depends(get_db)):
    return crud.get_all_meats(db)

# Get one meat by ID
@router.get("/{meat_id}", response_model=schemas.MeatResponse)
def get_meat(meat_id: int, db: Session = Depends(get_db)):
    meat = crud.get_meat_by_id(db, meat_id)
    if not meat:
        raise HTTPException(status_code=404, detail="Meat not found")
    return meat

# Update meat
@router.put("/{meat_id}", response_model=schemas.MeatResponse)
def update_meat(meat_id: int, updated_data: schemas.MeatUpdate, db: Session = Depends(get_db)):
    meat = crud.update_meat(db, meat_id, updated_data)
    if not meat:
        raise HTTPException(status_code=404, detail="Meat not found")
    return meat

# Delete meat
@router.delete("/{meat_id}", response_model=schemas.MeatResponse)
def delete_meat(meat_id: int, db: Session = Depends(get_db)):
    meat = crud.delete_meat(db, meat_id)
    if not meat:
        raise HTTPException(status_code=404, detail="Meat not found")
    return meat
