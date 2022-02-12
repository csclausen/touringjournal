from mongoengine import connect
from flask import app

class Connection:
    """
        Wrapper to open and close a mongodb connection
        with Connection():
            do stuff with mongoengine models
    """

    def __enter__(self):
        self.conn = connect(host=app.config.MONGODB_HOST)
        return self.conn

    def __exit__(self):
        self.conn.close()
