from sqlalchemy.orm import Session
from models.RestockModel import Restock
from models.MeatModels import Meat
from schemas.RestockSchema import RestockCreate

def create_restock(db: Session, restock_data: RestockCreate):
    # Calcula custo total
    total_cost = restock_data.quantity_kg * restock_data.price_per_kg

    # Cria registro de reabastecimento
    db_restock = Restock(
        meat_id=restock_data.meat_id,
        quantity_kg=restock_data.quantity_kg,
        price_per_kg=restock_data.price_per_kg,
        total_cost=total_cost
    )

    # Atualiza estoque da carne
    meat = db.query(Meat).filter(Meat.id == restock_data.meat_id).first()
    if meat:
        meat.stock_kg += restock_data.quantity_kg

    db.add(db_restock)
    db.commit()
    db.refresh(db_restock)

    return db_restock

def get_all_restocks(db: Session):
    return db.query(Restock).all()
