from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from loguru import logger
from typing import List

from app.db.session import SessionLocal
from app.schemas.recu import RecuCreate, RecuResponse
from app.repositories.recu_repository import (
    create_recu,
    update_recu,
    get_all_recus
)
from app.repositories.ajoute_repository import create_ajoute
from app.services.openclaw_service import send_to_openclaw
from app.workers.tasks import process_pipeline

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ POST
@router.post("/", response_model=RecuResponse)
def receive_recu(data: RecuCreate, db: Session = Depends(get_db)):
    recu = create_recu(db, data.payload)

    try:
        process_pipeline.delay(recu.id, data.payload)
        logger.info(f"Task envoyée à Celery pour recu {recu.id}")

        return {
            "id": recu.id,
            "payload": recu.payload,
            "response": None
        }

    except Exception as e:
        logger.error(f"Celery indisponible: {e}")
        logger.warning("Fallback en mode synchrone")

        result = send_to_openclaw(data.payload)

        update_recu(db, recu, result)

        if result.get("success") is True and isinstance(result.get("data"), dict):
            create_ajoute(db, result["data"])

        return {
            "id": recu.id,
            "payload": recu.payload,
            "response": result
        }


# ✅ GET
@router.get("/", response_model=List[RecuResponse])
def list_recus(db: Session = Depends(get_db)):
    return get_all_recus(db)
