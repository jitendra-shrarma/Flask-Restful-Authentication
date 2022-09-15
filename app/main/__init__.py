from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from .config import config_by_name

# initialize SQLAlchemy object for model and resource access
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt_manager = JWTManager()

from app.main.model.user import User

def create_app(env):
    """ create app with configuration by the 'env' name given as argument from config.py file """

    # create app
    app = Flask(__name__)

    # configure app with config_by_name[environment]
    app.config.from_object(config_by_name[env])

    # initialize database with app
    db.init_app(app)
    bcrypt.init_app(app)
    jwt_manager.init_app(app)

    # push new app_context into app
    app.app_context().push()

    # create all models
    db.create_all()

    # return app
    return app
