# Docker
`docker-compose up -d` # For Linux
`docker compose up -d` # For Mac

# Virtualenv
`python3 -m virtualenv venv`
`source venv/bin/activate` # For Linux, Mac
`venv\Scripts\activate` # For Windows

# Celery
`celery -A celery_worker.celery worker --loglevel=info`

# Flask
`python run.py`