from flask import jsonify
from flask_restful import Resource

from . import db
from api.v1.model.user import User


class UserResource(Resource):
    def get(self):
        return {"message":"hi"}
