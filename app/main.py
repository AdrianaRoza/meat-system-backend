from fastapi import FastAPI
from .database import Base, engine
from .models import models
from .routers import meat


app = FastAPI()

# Cria as tabelas se ainda não existirem
Base.metadata.create_all(bind=engine)

# Adiciona as rotas
app.include_router(meat.router)

@app.get("/")
def home():
    return {"message": "Butcher Shop API is running!"}
