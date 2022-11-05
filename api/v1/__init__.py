from flask import Flask, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


api_v1 = Blueprint('api/v1', __name__)
db = SQLAlchemy()
ma = Marshmallow()
api = Api(api_v1)


from config import config_by_name
from api.v1.model.user import User
from api.v1.resource.user import UserResource


def createApp(environment):
    app = Flask(__name__)
    app.config.from_object(config_by_name[environment])
    db.init_app(app)
    ma.init_app(app)

    app.app_context().push()
    db.create_all()
    app.register_blueprint(api_v1, url_prefix="/api/v1")

    return app

api.add_resource(UserResource, "/user")
