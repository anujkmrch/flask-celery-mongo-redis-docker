from flask import Flask
from celery import Celery
from mongoengine import connect

from app.swagger import configure_swagger

celery = None

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    # Initialize MongoEngine connection
    connect(
        db=app.config['MONGODB_NAME'],
        host=app.config['MONGODB_HOST'],
        port=app.config['MONGODB_PORT'],
    )
    
    # Configure Swagger
    configure_swagger(app)
    
    # Initialize Celery
    global celery
    celery = make_celery(app)

    with app.app_context():
        # Import routes to register them
        from app.routes import register_blueprints
        register_blueprints(app)

    return app


def make_celery(app):
    celery_instance = Celery(
        app.import_name,
        result_backend=app.config['RESULT_BACKEND_CELERY'],
        broker=app.config['CELERY_BROKER_URL'],
        broker_connection_retry_on_startup = True,
    )
    celery_instance.conf.update(app.config)
    return celery_instance
