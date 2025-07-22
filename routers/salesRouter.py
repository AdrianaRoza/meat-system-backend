# routers/salesRouter.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import SessionLocal
from schemas.salesSchemas import SaleCreate, SaleResponse
from repositories.salesRepository import (
    create_sale,
    get_all_sales,
    delete_sale
)

router = APIRouter(prefix="/sales", tags=["Sales"])

async def get_db():
    async with SessionLocal() as session:
        yield session

# 🟢 POST /sales - já existente
@router.post("/", response_model=SaleResponse)
async def register_sale(
    sale: SaleCreate,
    db: AsyncSession = Depends(get_db)
):
    return await create_sale(db, sale)

# ✅ GET /sales - listar todas as vendas
@router.get("/", response_model=list[SaleResponse])
async def list_sales(db: AsyncSession = Depends(get_db)):
    return await get_all_sales(db)

# ✅ DELETE /sales/{id} - excluir venda por ID
@router.delete("/{sale_id}", status_code=204)
async def remove_sale(sale_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_sale(db, sale_id)
    if not success:
        raise HTTPException(status_code=404, detail="Venda não encontrada")
