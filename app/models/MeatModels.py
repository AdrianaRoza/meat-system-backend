from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float
from ..database import Base

class Meat(Base):
    __tablename__ = "meats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    price_per_kg = Column(Float, nullable=False)
    stock_kg = Column(Float, nullable=False)


# Relacionamentos
    sales = relationship("Sale", back_populates="meat")
    restocks = relationship("Restock", back_populates="meat")
