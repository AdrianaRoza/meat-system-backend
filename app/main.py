from fastapi import FastAPI
from .database import Base, engine
from .routers import RouterMeat
from .routers import RouterSale
from .routers import RouterRestock


app = FastAPI()
        
# Cria as tabelas se ainda não existirem
Base.metadata.create_all(bind=engine)

# Adiciona as rotas
app.include_router(RouterMeat.router)
app.include_router(RouterSale.router)
app.include_router(RouterRestock.router)

@app.get("/")
def home():
    return {"message": "Butcher Shop API is running!"}
