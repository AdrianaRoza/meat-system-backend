from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Carrega as variáveis do .env
load_dotenv()

# Pega a string do banco
DATABASE_URL = os.getenv("DATABASE_URL")

# Cria o engine de conexão
engine = create_engine(DATABASE_URL)

# Sessão do banco (para executar comandos)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base para criar os modelos
Base = declarative_base()
