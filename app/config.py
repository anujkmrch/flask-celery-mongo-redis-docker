class Config:
    SECRET_KEY = 'your-secret-key'
    MONGODB_NAME='your_db_name'
    MONGODB_HOST='localhost'
    MONGODB_PORT=27017
    
    CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
    RESULT_BACKEND_CELERY = "mongodb://127.0.0.1:27017/your_db_name"
    SWAGGER_URL = '/api/docs'

    
