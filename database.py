from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Carrega as variáveis do .env
load_dotenv()

# Lê a string de conexão do arquivo .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Cria o engine assíncrono
engine = create_async_engine(DATABASE_URL, echo=True)

# Cria sessão assíncrona
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base para os modelos
Base = declarative_base()
