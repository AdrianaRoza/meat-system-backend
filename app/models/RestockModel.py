from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Restock(Base):
    __tablename__ = "restocks"

    id = Column(Integer, primary_key=True, index=True)
    meat_id = Column(Integer, ForeignKey("meats.id"), nullable=False)
    quantity_kg = Column(Float, nullable=False)

    meat = relationship("Meat")
