from flask import Blueprint, request, jsonify
from flasgger.utils import swag_from
from app.tasks import save_user_to_db

user_bp = Blueprint('users', __name__)

@user_bp.route('/add', methods=['POST'])
@swag_from({
    "tags": ["User Management"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "description": "JSON payload to create a user",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "email": {"type": "string"}
                },
                "required": ["name", "email"]
            }
        }
    ],
    "responses": {
        "202": {
            "description": "Task submitted"
        },
        "400": {
            "description": "Bad Request"
        }
    }
})
def add_user():
    data = request.json
    if not data or "name" not in data or "email" not in data:
        return jsonify({"message": "Bad Request"}), 400

    save_user_to_db.delay(data['name'], data['email'])
    return jsonify({"message": "Task submitted"}), 202
