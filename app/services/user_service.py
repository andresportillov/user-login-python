# app/services/user_service.py
from app.models.user import User
from flask_jwt_extended import create_access_token
from app.services.authentication import require_secret, require_token


class UserService:

    @require_secret
    @staticmethod
    def authenticate_user(username, password):
        user = User.objects(username=username, password=password).first()
        if user:
            # Autenticación exitosa
            token = create_access_token(identity=str(user.id))
            return user, token
        else:
            return {"message": "Invalid credentials"}, 401

    @require_secret
    @require_token
    @staticmethod
    def create_user(username, email, password):
        user = User(username=username, email=email, password=password)
        user.save()
        return user

    @require_token
    @require_secret
    @staticmethod
    def get_all_users():
        return User.objects()

    @require_secret
    @require_token
    @staticmethod
    def get_user_by_id(user_id):
        return User.objects(id=user_id).first()

    @require_secret
    @require_token
    @staticmethod
    def update_user(user_id, username=None, email=None, password=None):
        user = UserService.get_user_by_id(user_id)
        if user:
            if username:
                user.username = username
            if email:
                user.email = email
            if password:
                user.password = password
            user.save()
        return user

    @require_secret
    @require_token
    @staticmethod
    def delete_user(user_id):
        user = UserService.get_user_by_id(user_id)
        if user:
            user.delete()
        return user
