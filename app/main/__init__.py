# import default modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# import config_by_name for configuration environment
from .config import config_by_name


# create objects of database, bcrypt, jwt_manager
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt_manager = JWTManager()


# import user model after db to resolve looping
from app.main.model.user import User


# create_app with environment
def create_app(env):

    # create app
    app = Flask(__name__)

    # configure app with config_by_name[environment]
    app.config.from_object(config_by_name[env])

    # initialize database, bcrypt, jwt_manager with app
    db.init_app(app)
    bcrypt.init_app(app)
    jwt_manager.init_app(app)

    # push new app_context into app
    app.app_context().push()

    # create all models
    db.create_all()

    # return app
    return app
