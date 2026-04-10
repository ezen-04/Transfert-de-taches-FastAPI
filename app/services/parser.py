import json
import re

def extract_json(text: str) -> dict:
    """
    Extrait le JSON même s'il est entouré de texte
    """
    try:
        return json.loads(text)
    except:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except:
                pass

    return None


def safe_parse(response_text: str) -> dict:
    data = extract_json(response_text)

    if not data or not isinstance(data, dict):
        return {
            "success": False,
            "message": "Invalid JSON from OpenClaw",
            "data": None
        }

    return {
        "success": bool(data.get("success", False)),
        "message": str(data.get("message", "")),
        "data": data.get("data")
    }
