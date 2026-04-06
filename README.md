# Transfert-de-taches-FastAPI
Cette API, utilisant Celery et Redis, permet de transférer des tâches reçu d'une requête, en format JSON, à une autre API qui sera chargé d'effectuer ces tâches. Elle se charge de maintenir les bases de données à jour avec toutes les informations qu'il faut. Aussi, cette API requiert des tokens d'authentification.
