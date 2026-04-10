from sqlalchemy import Column, Integer, JSON
from app.db.base import Base

class Recu(Base):
    __tablename__ = "recus"

    id = Column(Integer, primary_key=True, index=True)
    payload = Column(JSON, nullable=False)
    response = Column(JSON, nullable=True)  # pour stocker réponse OpenClaw si besoin
