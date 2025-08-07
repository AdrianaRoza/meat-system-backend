from sqlalchemy.orm import Session
from . import models, schemas

# Create meat
def create_meat(db: Session, meat_data: schemas.MeatCreate):
    new_meat = models.Meat(**meat_data.dict())
    db.add(new_meat)
    db.commit()
    db.refresh(new_meat)
    return new_meat

# Get all meats
def get_all_meats(db: Session):
    return db.query(models.Meat).all()

# Get one meat by ID
def get_meat_by_id(db: Session, meat_id: int):
    return db.query(models.Meat).filter(models.Meat.id == meat_id).first()

# Update meat
def update_meat(db: Session, meat_id: int, meat_data: schemas.MeatUpdate):
    meat = db.query(models.Meat).filter(models.Meat.id == meat_id).first()
    if meat:
        for field, value in meat_data.dict().items():
            setattr(meat, field, value)
        db.commit()
        db.refresh(meat)
    return meat

# Delete meat
def delete_meat(db: Session, meat_id: int):
    meat = db.query(models.Meat).filter(models.Meat.id == meat_id).first()
    if meat:
        db.delete(meat)
        db.commit()
    return meat
