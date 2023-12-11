# app/__init__.py
from app.routes.user_routes import user_routes
from flask import Flask
from flask_mongoengine import MongoEngine
from app.config import Config
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
db = MongoEngine(app)
jwt = JWTManager(app)


app.register_blueprint(user_routes)

if __name__ == "__main__":
    app.run(debug=True)
