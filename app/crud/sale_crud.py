from sqlalchemy.orm import Session
from app.models.SaleModels import Sale
from app.models.MeatModels import Meat
from app.schemas.SaleSchema import SaleCreate

def create_sale(db: Session, sale_data: SaleCreate):
    meat = db.query(Meat).filter(Meat.id == sale_data.meat_id).first()
    if not meat:
        return None

    if meat.stock_kg < sale_data.quantity_kg:
        return "not_enough_stock"

    total_price = sale_data.quantity_kg * meat.price_per_kg

    new_sale = Sale(
        meat_id=sale_data.meat_id,
        quantity_kg=sale_data.quantity_kg,
        total_price=total_price
    )

    meat.stock_kg -= sale_data.quantity_kg  # atualiza o estoque

    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)
    return new_sale


def get_all_sales(db: Session):
    return db.query(Sale).all()
