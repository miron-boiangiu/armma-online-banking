import os

from flask_jwt_extended import JWTManager
from flask import Flask
from datetime import timedelta
from .db import db
from .blueprints import auth


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        JWT_SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "armma.sqlite"),
        JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    )

    jwt = JWTManager(app)
    auth.init_jwt(jwt)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register the database commands
    db.prepare_db(app)

    # apply the blueprints to the app
    app.register_blueprint(auth.bp)

    return app
