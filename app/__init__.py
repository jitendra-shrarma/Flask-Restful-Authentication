from flask import Blueprint
from flask_restful import Api

from app.main.resource.auth import (
    LoginResource,
    LogoutResource,
    RefreshTokenResource,
    RegistrationResource,
)

api_bp = Blueprint("api/v1", __name__)
api = Api(api_bp)

api.add_resource(LoginResource, "/user/login")
api.add_resource(LogoutResource, "/user/logout")
api.add_resource(RefreshTokenResource, "/user/refresh_token")
api.add_resource(RegistrationResource, "/user/register")
