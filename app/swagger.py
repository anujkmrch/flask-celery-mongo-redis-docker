from flasgger import Swagger

def configure_swagger(app):
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec_1",
                "route": "/docs/swagger.json",  # JSON specification path
                "rule_filter": lambda rule: True,  # Include all routes
                "model_filter": lambda tag: True,  # Include all models
            }
        ],
        "static_url_path": "/docs/flasgger_static",  # Static files for Swagger UI
        "swagger_ui": True,
        "swagger_ui_url": "/docs",  # Swagger UI path
    }
    
    swagger_template={
        "swagger": "2.0",
        "info": {
            "title": "User API",
            "description": "API documentation for the User application",
            "version": "1.0.0"
        },
        "host": "localhost:5000",  # Change to your host
        "schemes": ["http"],
    }
    
    Swagger(
        app, 
        template=swagger_template,
        config=swagger_config
    )