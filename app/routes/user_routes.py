# app/routes/user_routes.py
from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from flask import current_app as app

user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    user, token = UserService.authenticate_user(username, password)
    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    # Almacenar el token en la configuración de la aplicación
    app.config['TOKENS'].add(token)

    return jsonify({"access_token": token}), 200


@user_routes.route("/users", methods=["GET"])
def get_all_users():
    users = UserService.get_all_users()
    return jsonify(users), 200


@user_routes.route("/users/<user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = UserService.get_user_by_id(user_id)
    return jsonify(user), 200 if user else 404


@user_routes.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    print(request)
    if data is None or "username" not in data or "email" not in data or "password" not in data:
        return jsonify({"message": "Invalid data format"}), 400
    user = UserService.create_user(
        data["username"], data["email"], data["password"])
    return jsonify(user), 201


@user_routes.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = UserService.update_user(user_id, data.get(
        "username"), data.get("email"), data.get("password"))
    return jsonify(user), 200 if user else 404


@user_routes.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = UserService.delete_user(user_id)
    return jsonify(user), 200 if user else 404
