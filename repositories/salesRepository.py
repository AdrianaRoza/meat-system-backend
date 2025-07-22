from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.salesModel import Sale
from models.meatModel import Meat
from schemas.salesSchemas import SaleCreate
from sqlalchemy import delete

async def create_sale(db: AsyncSession, sale_data: SaleCreate):
    result = await db.execute(select(Meat).where(Meat.id == sale_data.meat_id))
    meat = result.scalar_one()

    total_price = sale_data.quantity_kg * meat.price_per_kg

    sale = Sale(
        meat_id=sale_data.meat_id,
        quantity_kg=sale_data.quantity_kg,
        total_price=total_price
    )

    db.add(sale)
    await db.commit()
    await db.refresh(sale)
    return sale

async def get_all_sales(db: AsyncSession):
    result = await db.execute(select(Sale))
    return result.scalars().all()

    # ✅ Deletar uma venda por ID
async def delete_sale(db: AsyncSession, sale_id: int):
        result = await db.execute(select(Sale).where(Sale.id == sale_id))
        sale = result.scalar_one_or_none()
        if sale:
            await db.delete(sale)
            await db.commit()
            return True
        return False
