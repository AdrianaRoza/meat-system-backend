from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.meatModel import Meat
from schemas.meatSchemas import MeatCreate

# Criar uma nova carne
async def create_meat(meat_data: MeatCreate, db: AsyncSession) -> Meat:
    new_meat = Meat(**meat_data.dict())
    db.add(new_meat)
    await db.commit()
    await db.refresh(new_meat)
    return new_meat

# Listar todas as carnes
async def list_all_meats(db: AsyncSession):
    result = await db.execute(select(Meat))
    meats = result.scalars().all()
    return meats
