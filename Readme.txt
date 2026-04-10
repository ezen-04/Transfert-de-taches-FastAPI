▶️ Lancer les services
1. Redis
redis-server

2. API
python (ou python3) main.py

3. Worker Celery
celery -A app.core.celery_app.celery_app worker --loglevel=info
