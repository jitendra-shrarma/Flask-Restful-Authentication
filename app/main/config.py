# import py modules
from os import path, getenv
from dotenv import load_dotenv


# base_dir path to load file from root directory
BASE_DIR = path.dirname(path.abspath(__name__))
# load environment variables from environment file
load_dotenv(BASE_DIR, ".flaskenv")


class Config(object):
    # default configuration class, it will work as the base class

    SECRET_KEY = getenv("SECRET_KEY")
    JWT_SECRET_KEY = SECRET_KEY
    JWT_TOKEN_LOCATION = "cookies"
    JWT_COOKIE_CSRF_PROTECT = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    # development configuration class

    FLASK_ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIR, "app_dev.db")


class ProductionConfig(Config):
    # production configuration class

    FLASK_ENV = "production"
    DEBUG = False
    JWT_COOKIE_CSRF_PROTECT = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIR, "app_prod.db")


# dictionary of (environment, environmentConfig), will be used to make easy configuration
config_by_name = dict({"dev": DevelopmentConfig, "prod": ProductionConfig})
