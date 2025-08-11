from sqlalchemy.orm import Session
from app.models.RestockModel import Restock
from app.models.MeatModels import Meat
from app.schemas.RestockSchema import RestockCreate

def create_restock(db: Session, restock_data: RestockCreate):
    meat = db.query(Meat).filter(Meat.id == restock_data.meat_id).first()
    if not meat:
        return None

    # Atualiza o estoque da carne somando a quantidade reabastecida
    meat.stock_kg += restock_data.quantity_kg

    new_restock = Restock(
        meat_id=restock_data.meat_id,
        quantity_kg=restock_data.quantity_kg
    )

    db.add(new_restock)
    db.commit()
    db.refresh(new_restock)
    return new_restock

def get_all_restocks(db: Session):
    return db.query(Restock).all()
