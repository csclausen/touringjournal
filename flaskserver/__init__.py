import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_cors import CORS

from .views import auth, editor


def create_app(test_config=None):
    load_dotenv()
    secret_key = os.getenv('SECRET_KEY')
    mongodb_host = os.getenv('MONGODB_HOST')
    # create and configure app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=secret_key,
        MONGODB_HOST=mongodb_host
    )

    if test_config is None:
        # load instance config if not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/')
    def index():
        return render_template('base.html')

    # register blueprints
    app.register_blueprint(auth.bp) 
    app.register_blueprint(editor.bp)
    app.add_url_rule('/', endpoint='index')
    CORS(app)

    return app
