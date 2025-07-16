from fastapi import FastAPI
from routers import meatRouter

app = FastAPI(title="Meat-system")

# Inclui as rotas da aplicação
app.include_router(meatRouter.router)
