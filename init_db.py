# init_db.py

# Importa a engine síncrona do SQLAlchemy
from sqlalchemy import create_engine

# Importa as tabelas que você quer criar
from models.meatModel import Meat
from models.salesModel import Sale

# Importa a Base comum usada por todos os modelos
from database import Base

# Importa o .env para pegar a URL do banco
import os
from dotenv import load_dotenv

# Carrega o conteúdo do arquivo .env (como DATABASE_URL)
load_dotenv()

# Pega a string de conexão do arquivo .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Ajusta a URL de async para sync, porque create_all exige engine síncrona
SYNC_DATABASE_URL = DATABASE_URL.replace("postgresql+asyncpg", "postgresql")

# Cria engine síncrona para uso exclusivo neste script
engine = create_engine(SYNC_DATABASE_URL)

# Cria todas as tabelas definidas nas classes (Meat, Sale)
Base.metadata.create_all(bind=engine)

print("✅ Tabelas criadas com sucesso!")
