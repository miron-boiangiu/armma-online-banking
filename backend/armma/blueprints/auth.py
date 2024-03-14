from flask import Blueprint
from flask import g
from flask import redirect
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import get_jti
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_current_user

from ..db.db import get_db
from ..utils.response_formats import *


bp = Blueprint("auth", __name__)


@bp.route("/register", methods=["POST"])
def register():
    """Register a new user."""

    username = request.form["username"]
    password = request.form["password"]
    db = get_db()
    error = None

    if not username:
        error = "Username is required."
    elif not password:
        error = "Password is required."

    if error is None:
        try:
            db.execute(
                "INSERT INTO user (username, password) VALUES (?, ?)",
                (username, generate_password_hash(password)),
            )
            db.commit()
        except db.IntegrityError:
            # The username was already taken, which caused the
            # commit to fail. Show a validation error.
            error = f"User {username} is already registered."
        else:
            return success_response()

    return error_response(error, 409)


@bp.route("/login", methods=["POST"])
def login():
    """Log in a registered user by sending back a JWT token."""

    username = request.form["username"]
    password = request.form["password"]
    db = get_db()
    error = None
    user = db.execute(
        "SELECT * FROM user WHERE username = ?", (username,)
    ).fetchone()

    if user is None:
        error = "Incorrect username."
    elif not check_password_hash(user["password"], password):
        error = "Incorrect password."

    if error is None:
        access_token = create_access_token(identity=username)

        try:
            db.execute(
                "INSERT INTO token(jti) VALUES (?)",
                (get_jti(access_token),)
            )
            db.commit()
        except db.IntegrityError:
            # The username was already taken, which caused the
            # commit to fail. Show a validation error.
            error = f"User {username} is already registered."

        response = success_response()
        response["access_token"] = access_token
        return response

    return error_response(error, 401)


@bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    """Marks the access token as invalid."""
    db = get_db()

    db.execute(
    "UPDATE token SET expired = 1 WHERE jti = ?",
    (get_jwt()["jti"],))

    db.commit()

    return success_response()


@bp.route("/logged_in_check")
@jwt_required(optional=True)
def logged_in_test():
    """Checks whether the caller is logged in or not."""
    current_user = get_current_user()

    if get_current_user():
        response = success_response()
        response["user"] = current_user
        return response
    
    return error_response("You are not logged in.", 401)


@bp.route("/refresh", methods=["POST"])
@jwt_required()
def refresh():
    """Generates a new token to avoid being logged off."""
    db = get_db()

    current_user = get_current_user()
    access_token = create_access_token(identity=current_user)

    db.execute(
        "INSERT INTO token(jti) VALUES (?)",
        (get_jti(access_token),)
    )
    db.commit()

    response = success_response()
    response["access_token"] = access_token
    return response


def init_jwt(jwt):
    
    @jwt.user_lookup_loader
    def load_logged_in_user(jwt_header, jwt_data):
        """If the caller has a valid token, enables the use of get_current_user()."""
        user_id = jwt_data["sub"]
        return get_db().execute("SELECT * FROM user WHERE username = ?", (user_id,)).fetchone()["username"]
    
    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user
    