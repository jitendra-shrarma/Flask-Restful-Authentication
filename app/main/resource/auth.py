# import default modules
from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    jwt_refresh_token_required,
    create_refresh_token,
    get_jwt_identity,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
)

# import custom modules
from app.main import db, jwt_manager
from app.main.model.user import User


class RegistrationResource(Resource):
    def __init__(self):
        # parser to parse_args, required arguments are email and password
        self.parser = reqparse.RequestParser(bundle_errors=True)
        self.parser.add_argument(
            "first_name", type=str, help="user's first name", location="json"
        )
        self.parser.add_argument(
            "last_name", type=str, help="user's last name", location="json"
        )
        self.parser.add_argument(
            "username", type=str, help="user's username", location="json"
        )
        self.parser.add_argument(
            "email", type=str, required=True, help="user's email", location="json"
        )
        self.parser.add_argument(
            "password", type=str, required=True, help="user's password", location="json"
        )

    def saveChanges(self, user):
        db.session.add(user)
        db.session.commit()

    def post(self):
        args = self.parser.parse_args()
        first_name = args["first_name"]
        last_name = args["last_name"]
        username = args["username"]
        email = args["email"]
        password = args["password"]

        # get first user with this email
        user = User.query.filter_by(email=email).first()

        # if user found, return status
        if user:
            return make_response(jsonify({"status": False, "message": "user exists with this email"}), 400)

        # username is not provided
        if not username:
            username = first_name or "user"
            username += last_name or str(User.query.count())

        else:
            # check if there is a user with this username already
            user = User.query.filter_by(username=username).first()

            # if user found, return status
            if user:
                return make_response(jsonify({'status': False, 'message': f'user exists with this {username}'}),400)

        # create user with given arguments
        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
        )
        user.set_password(password)
        self.saveChanges(user)
        # return response, with username
        return make_response(jsonify({'status': True, 'message': f'{username} added successfully'}), 201)


# login resouce with post method
# create access token and refresh token with passed credentials(email, password)
# parse credentials, to make login successful
class LoginResource(Resource):
    def __init__(self):
        # parser to parse_args, arguments are email and password only
        self.parser = reqparse.RequestParser(bundle_errors=True)
        self.parser.add_argument(
            "email", type=str, required=True, help="user's email", location="json"
        )
        self.parser.add_argument(
            "password", type=str, required=True, help="user's password", location="json"
        )

    def post(self):
        # get args after parsering with required conditions
        args = self.parser.parse_args()
        email = args["email"]
        password = args["password"]

        # get first user with this email
        user = User.query.filter_by(email=email).first()

        # if no user found, return error
        if not user:
            return make_response(
                jsonify({"status": False, "error": "invalid email"}), 400
            )

        # if password does not match, return error
        if not user.check_password(password):
            return make_response(
                jsonify({"status": False, "error": "invalid password"}), 400
            )

        # create access token and refresh_token with user username
        access_token = create_access_token(identity=user.user_id)
        refresh_token = create_refresh_token(identity=user.user_id)

        # return response with access token and refresh token
        response = jsonify({"status": True, "message": "login successful"})
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return make_response(response, 201)


# refresh token resource with put method
# refresh token required to refresh access token and authenticate
class RefreshTokenResource(Resource):

    # check cookies for refresh token
    @jwt_refresh_token_required
    def put(self):

        # get current user identity
        current_user = get_jwt_identity()

        # create new access token with current user's identity
        access_token = create_access_token(identity=current_user)

        # return response with access token
        response = jsonify({"status": True, "message": "token refreshed successfully"})
        set_access_cookies(response, access_token)
        return make_response(response, 201)


# logout resource with delete method
# access token authentication required to perform logout
class LogoutResource(Resource):

    # required access token to perform operation
    @jwt_required
    def delete(self):

        # return response and reset access token
        response = jsonify({"status": True, "message": "logout successful"})
        unset_jwt_cookies(response)
        return make_response(response, 200)
