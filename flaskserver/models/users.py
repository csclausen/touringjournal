import datetime
from mongoengine import *
from flaskserver.mongodbconnector import Connection


# MongoDB Schema
class User(Document):
    username = StringField(max_length=21, required=True, unique=True)
    email = EmailField(max_length=320, required=True, unique=True)
    password = StringField(required=True)
    date_created = DateTimeField(default=datetime.datetime.utcnow)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)


class UserModelManager:

    def create_user(self, **kwargs):
        with Connection():
            new_user = User(**kwargs)
            new_user.save()
        
        return new_user

    def get_user(self, **kwargs):
        with Connection():
            user = User.objects(**kwargs)
        
        return user
        