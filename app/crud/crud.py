from sqlalchemy.orm import Session
from app.schemas import MeatSchemas
from app.models import MeatModels


# Create meat
def create_meat(db: Session, meat_data: MeatSchemas.MeatCreate):
    new_meat = MeatModels.Meat(**meat_data.dict())
    db.add(new_meat)
    db.commit()
    db.refresh(new_meat)
    return new_meat

# Get all meats
def get_all_meats(db: Session):
    return db.query(MeatModels.Meat).all()

# Get one meat by ID
def get_meat_by_id(db: Session, meat_id: int):
    return db.query(MeatModels.Meat).filter(MeatModels.Meat.id == meat_id).first()

# Update meat
def update_meat(db: Session, meat_id: int, meat_data: MeatSchemas.MeatUpdate):
    meat = db.query(MeatModels.Meat).filter(MeatModels.Meat.id == meat_id).first()
    if meat:
        for field, value in meat_data.dict().items():
            setattr(meat, field, value)
        db.commit()
        db.refresh(meat)
    return meat

# Delete meat
def delete_meat(db: Session, meat_id: int):
    meat = db.query(MeatModels.Meat).filter(MeatModels.Meat.id == meat_id).first()
    if meat:
        db.delete(meat)
        db.commit()
    return meat
