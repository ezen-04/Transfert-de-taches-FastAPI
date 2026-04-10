OPENCLAW_URL = "http://127.0.0.1:18789/v1/chat/completions"

access_token = "b3652addc3fc34f3be6628200e9310fa874dc239ab3eb7fe"

HEADERS = {"Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"}

MAX_RETRIES = 3
TIMEOUT = 10
RETRY_DELAY = 2

# Celery
CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

API_TOKEN = {"a2zd528grfngvbdzSEGRTHGYXTC2ef-f_MLkihgbJ?!ha",
            "vdegffgjyik258g5y55bdg45ZEZHAGc8g8ZRAet8!!f71dp"}

