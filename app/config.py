import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    MONGODB_URI = os.getenv("MONGODB_URI")
    MONGODB_DB = os.getenv("MONGODB_DB", "min")
    SECRET = os.getenv("SECRET")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "asd123")
    TOKENS = set()
