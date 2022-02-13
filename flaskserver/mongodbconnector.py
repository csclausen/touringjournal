from mongoengine import connect
from flask import current_app

class Connection:
    """
        Wrapper to open and close a mongodb connection
        with Connection():
            do stuff with mongoengine models
    """

    def __enter__(self, **kwargs):
        self.conn = connect(host=current_app.config['MONGODB_HOST'])
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
