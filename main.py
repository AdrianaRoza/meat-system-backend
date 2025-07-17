from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import meatRouter

app = FastAPI(title="Meat-system")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui as rotas da aplicação
app.include_router(meatRouter.router)
