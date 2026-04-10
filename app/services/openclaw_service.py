import requests
import time

from app.core.config import OPENCLAW_URL, MAX_RETRIES, TIMEOUT, RETRY_DELAY, HEADERS
from app.services.parser import safe_parse


def send_to_openclaw(payload: dict) -> dict:
    prompt = {
        "instruction": (
            "Ajoute cet article (ou ces articles) au panier. "
            "Répond STRICTEMENT en JSON avec les clés: "
            "success (bool), message (string), data (object)."
        ),
        "input": payload
    }

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.post(
                OPENCLAW_URL,
                headers=HEADERS,
                json=prompt,
                timeout=TIMEOUT
            )
            response.raise_for_status()

            return safe_parse(response.text)

        except Exception as e:
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_DELAY)
            else:
                return {
                    "success": False,
                    "message": f"Retry failed: {str(e)}",
                    "data": None
                }
