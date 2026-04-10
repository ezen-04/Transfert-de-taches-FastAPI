from sqlalchemy.orm import Session
from app.models.ajoute import Ajoute


def create_ajoute(db: Session, data: dict):
    ajoute = Ajoute(data=data)
    db.add(ajoute)
    db.commit()
    db.refresh(ajoute)
    return ajoute


def get_all_ajoutes(db: Session):
    return db.query(Ajoute).all()
