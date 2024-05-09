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


bp = Blueprint("accounts", __name__)


@bp.route("/create_banking_account", methods=["POST"])
@jwt_required()
def create_banking_account():
    """Create a new banking account."""

    account_name = request.json["account_name"]

    db = get_db()
    current_user = get_current_user()

    error = None

    if not account_name:
        return error_response("Field account_name missing from request.", 400)

    try:
        
        db.execute(
            "INSERT INTO banking_account (user_id, account_name) VALUES (?, ?)",
            (current_user["id"], account_name),
        )
        db.commit()
    except db.IntegrityError:
        error = f"User already has an account with this name."
    else:
        return success_response()

    return error_response(error, 406)

@bp.route("/close_banking_account", methods=["POST"])
@jwt_required()
def close_banking_account():
    """Close a banking account."""

    account_name = request.json["account_name"]

    db = get_db()
    current_user = get_current_user()

    error = None

    if not account_name:
        return error_response("Field account_name missing from request.", 400)

    try:
        
        db.execute(
            "UPDATE banking_account SET is_closed=1 WHERE user_id=? AND account_name=?",
            (current_user["id"], account_name),
        )
        db.commit()
    except db.IntegrityError:
        error = f"User doesn't own an account with this name."
    else:
        return success_response()

    return error_response(error, 406)
