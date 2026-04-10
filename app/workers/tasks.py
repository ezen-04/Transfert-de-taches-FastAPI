from loguru import logger

from app.core.celery_app import celery_app
from app.db.session import SessionLocal

from app.repositories.recu_repository import get_recu, update_recu
from app.repositories.ajoute_repository import create_ajoute
from app.services.openclaw_service import send_to_openclaw


@celery_app.task(name="workers.tasks.process_pipeline", bind=True)
def process_pipeline(self, recu_id: int, payload: dict):
    db = SessionLocal()

    try:
        recu = get_recu(db, recu_id)

        if not recu:
            logger.error(f"Recu {recu_id} introuvable")
            return

        result = send_to_openclaw(payload)

        update_recu(db, recu, result)

        if result.get("success") is True:
            if isinstance(result.get("data"), dict):
                create_ajoute(db, result["data"])
                logger.info(f"Ajout réussi pour recu {recu_id}")
            else:
                logger.warning(f"Success=true mais data invalide pour recu {recu_id}")
        else:
            logger.info(f"Echec OpenClaw pour recu {recu_id}")

    except Exception as e:
        logger.error(f"Erreur worker: {str(e)}")
        raise e

    finally:
        db.close()
