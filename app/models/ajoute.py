from sqlalchemy import Column, Integer, JSON
from app.db.base import Base

class Ajoute(Base):
    __tablename__ = "ajoutes"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON, nullable=False)
