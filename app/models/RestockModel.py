from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Restock(Base):
    __tablename__ = "restocks"  

    id = Column(Integer, primary_key=True, index=True)
    meat_id = Column(Integer, ForeignKey("meats.id")) 
    quantity_kg = Column(Float, nullable=False)  
    price_per_kg = Column(Float, nullable=False)  
    total_price = Column(Float, nullable=False)  
    date = Column(DateTime, default=datetime.utcnow)  

    # Relacionamento com a carne
    meat = relationship("Meat", back_populates="restocks")
