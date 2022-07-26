# import default modules
from flask import Blueprint
from flask_restful import Api

# import resources to add in api
from app.main.resource.auth import (
    LoginResource,
    LogoutResource,
    RefreshTokenResource,
    RegistrationResource,
)

# create blueprint
blueprint = Blueprint("api.v1", __name__)
# create api to map resources with url
api = Api(blueprint)

# register resource methods = ['post'], return message and register user in database
api.add_resource(RegistrationResource, "/user/register")
# login resource methods = ['post'], return message with access_token and refresh_token
api.add_resource(LoginResource, "/user/login")
# logout resource methods = ['delete'], return message and remove access_token and refresh_token
api.add_resource(LogoutResource, "/user/logout")
# refresh token resource methods = ['put'], return message and update access_token
api.add_resource(RefreshTokenResource, "/user/refresh_token")
