# app/services/authentication.py
from functools import wraps
from flask import request, abort
from app.config import Config
from flask import current_app as app


def require_secret(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        secret = request.headers.get('Secret')

        if not secret or secret != Config.SECRET:
            abort(401, 'Unauthorized: Missing or incorrect secret.')

        return func(*args, **kwargs)

    return wrapper


def require_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('TOKEN')

        if not token or not token.startswith('Bearer '):
            abort(401, 'Unauthorized: Missing or invalid token.')

        token = token.split('Bearer ')[1]

        # Validar la existencia del token en el contexto de la aplicación
        print(app.config['TOKENS'])
        if token not in app.config['TOKENS']:
            abort(401, 'Unauthorized: Invalid token.')

        return func(*args, **kwargs)

    return wrapper
