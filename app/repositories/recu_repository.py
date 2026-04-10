from sqlalchemy.orm import Session
from app.models.recu import Recu


def create_recu(db: Session, payload: dict):
    recu = Recu(payload=payload)
    db.add(recu)
    db.commit()
    db.refresh(recu)
    return recu


def get_recu(db: Session, recu_id: int):
    return db.query(Recu).filter(Recu.id == recu_id).first()


def get_all_recus(db: Session):
    return db.query(Recu).all()


def update_recu(db: Session, recu: Recu, response: dict):
    recu.response = response
    db.commit()
    db.refresh(recu)
