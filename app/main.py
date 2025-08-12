from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import RouterMeat
from .routers import RouterSale
from .routers import RouterRestock


app = FastAPI()

# Permitir CORS para o frontend
origins = [
    "http://localhost:5173",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # quem pode acessar
    allow_credentials=True,
    allow_methods=["*"],        # métodos HTTP permitidos
    allow_headers=["*"],        # quais headers são permitidos
)
        
# Cria as tabelas se ainda não existirem
Base.metadata.create_all(bind=engine)

# Adiciona as rotas
app.include_router(RouterMeat.router)
app.include_router(RouterSale.router)
app.include_router(RouterRestock.router)

@app.get("/")
def home():
    return {"message": "Butcher Shop API is running!"}
