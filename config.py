from os import path, getenv
from dotenv import load_dotenv


BASE_DIR = path.dirname(path.abspath(__file__))
load_dotenv(BASE_DIR, '.flaskenv')


class Config(object):
    BASE_DIR = BASE_DIR
    SECRET_KEY = getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIR, "app_dev.db")


class ProductionConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIR, "app_prod.db")


config_by_name = dict({"dev": DevelopmentConfig, "prod": ProductionConfig})
