# routers/meat.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database import SessionLocal
from models.meatModel import Meat
from schemas.meatSchemas import MeatCreate, MeatOut

from repositories import meatRepository as meat_repo

router = APIRouter(prefix="/meats", tags=["Meats"])

#  Dependência para obter sessão do banco
async def get_db():
    async with SessionLocal() as session:
        yield session

# CREATE
@router.post("/", response_model=MeatOut)
async def create_meat(meat: MeatCreate, db: AsyncSession = Depends(get_db)):
    return await meat_repo.create_meat(meat, db)

# READ ALL
@router.get("/", response_model=list[MeatOut])
async def get_all_meats(db: AsyncSession = Depends(get_db)):
    return await meat_repo.list_all_meats(db)

# READ ID
@router.get("/{meat_id}", response_model=MeatOut)
async def get_meat(meat_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Meat).where(Meat.id == meat_id))
    meat = result.scalars().first()
    if meat is None:
        raise HTTPException(status_code=404, detail="Carne não encontrada")
    return meat

# UPDATE
@router.put("/{meat_id}", response_model=MeatOut)
async def update_meat(meat_id: int, meat_data: MeatCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Meat).where(Meat.id == meat_id))
    meat = result.scalars().first()
    if meat is None:
        raise HTTPException(status_code=404, detail="Carne não encontrada")

    meat.name = meat_data.name
    meat.type = meat_data.type
    meat.price_per_kg = meat_data.price_per_kg
    meat.stock_kg = meat_data.stock_kg

    await db.commit()
    await db.refresh(meat)
    return meat

# DELETE
@router.delete("/{meat_id}")
async def delete_meat(meat_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Meat).where(Meat.id == meat_id))
    meat = result.scalars().first()
    if meat is None:
        raise HTTPException(status_code=404, detail="Carne não encontrada")

    await db.delete(meat)
    await db.commit()
    return {"message": "Carne removida com sucesso"}
