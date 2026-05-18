# Transfert-de-taches-FastAPI
Cette API, utilisant Celery et Redis, permet de transférer des tâches reçu d'une requête, en format JSON, à une autre API qui sera chargé d'effectuer ces tâches. Elle se charge de maintenir les bases de données à jour avec toutes les informations qu'il faut. Aussi, cette API requiert des tokens d'authentification.

## Architecture

```
source/
│
├──app/
│   │
│   ├── core/
│   │   ├── celery_app.py
│   │   ├── security.py
│   │   └── config.py
│   │
│   ├── db/
│   │   ├── article_data.db
│   │   ├── base.py
│   │   └── session.py
│   │
│   ├── models/
│   │   ├── recu.py
│   │   └── ajoute.py
│   │
│   ├── schemas/
│   │   ├── ajoute.py
│   │   └── recu.py
│   │
│   ├── repositories/
│   │   ├── ajoute_repository.py
│   │   └── recu_repository.py
│   │
│   ├── services/
│   │   ├── parser.py
│   │   └── openclaw_service.py
│   │
│   ├── workers/
│   │   └── tasks.py
│   │
│   └── api/
│       ├── routes/
│  	    └── ajoutes.py
│           └── recus.py
│
└── main.py
```

## Lancer les services
1. Redis
redis-server

2. API
python (ou python3) main.py

3. Worker Celery
celery -A app.core.celery_app.celery_app worker --loglevel=info
