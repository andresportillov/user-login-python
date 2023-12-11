from mongoengine import Document, StringField
import uuid


class User(Document):
    id = StringField(primary_key=True, default=str(
        uuid.uuid4()), required=True)
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
