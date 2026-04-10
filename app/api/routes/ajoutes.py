from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import SessionLocal
from app.schemas.ajoute import AjouteResponse
from app.repositories.ajoute_repository import get_all_ajoutes

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[AjouteResponse])
def list_ajoutes(db: Session = Depends(get_db)):
    return get_all_ajoutes(db)
