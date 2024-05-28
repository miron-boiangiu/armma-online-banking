from flask import Blueprint
from flask import g
from flask import redirect
from flask import request
from flask import session
from flask import url_for
import random
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import get_jti
from flask_jwt_extended import jwt_required
import string
from flask import jsonify
from flask_jwt_extended import get_current_user

from ..db.db import get_db
from ..utils.response_formats import *


bp = Blueprint("accounts", __name__)


@bp.route("/create_banking_account", methods=["POST"])
@jwt_required()
def create_banking_account():
    """Create a new banking account."""

    account_name = None
    if "account_name" in request.json:
        account_name = request.json["account_name"]

    db = get_db()
    current_user = get_current_user()

    error = None

    if not account_name:
        return error_response("Field account_name missing from request.", 400)

    def generate_iban():
        country_code = "RO"
        check_digits = f"{random.randint(10, 99)}"  # Two digits
        bank_code = "BANK"  # Example bank code
        account_identifier = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        return f"{country_code}{check_digits}{bank_code}{account_identifier}"

    iban = generate_iban()

    try:
        db.execute(
            "INSERT INTO banking_account (user_id, account_name, iban) VALUES (?, ?, ?)",
            (current_user["id"], account_name, iban),
        )
        db.commit()
    except db.IntegrityError:
        error = f"Operation failed."
    else:
        return jsonify({"message": "Account created successfully", "iban": iban}), 201

    return error_response(error, 406)


@bp.route("/accounts", methods=["GET"])
@jwt_required()
def accounts():  # TODO: Paginate this
    """List accounts of this user."""

    db = get_db()
    current_user = get_current_user()

    error = None

    try:
        accounts = db.execute(
            "SELECT * from banking_account where user_id=? AND is_closed=0",
            (current_user["id"],)
        ).fetchall()

        return success_message_response([dict(x) for x in accounts])
    except db.IntegrityError:
        error = f"Operation failed."

    return error_response(error, 400)

@bp.route("/inspect_banking_account", methods=["POST"])
@jwt_required()
def inspect_banking_account():
    """Inspect a banking account."""

    account_id = None
    if "account_id" in request.json:
        account_id = request.json["account_id"]

    db = get_db()
    current_user = get_current_user()

    error = None

    if not account_id:
        return error_response("Field account_id missing from request.", 400)

    try:
        res = db.execute(
            "SELECT * from banking_account where user_id=? AND id=?",
            (current_user["id"], account_id),
        ).fetchone()

        if res:
            return success_message_response(dict(res))

    except db.IntegrityError:
        error = f"User doesn't own an account with this name."
    else:
        return success_response()

    return error_response(error, 406)

@bp.route("/close_banking_account", methods=["POST"])
@jwt_required()
def close_banking_account():
    """Close a banking account."""

    account_id = None
    if "account_id" in request.json:
        account_id = request.json["account_id"]

    db = get_db()
    current_user = get_current_user()

    error = None

    if not account_id:
        return error_response("Field account_id missing from request.", 400)

    try:
        db.execute(
            "UPDATE banking_account SET is_closed=1 WHERE user_id=? AND id=?",
            (current_user["id"], account_id),
        )
        db.commit()
    except db.IntegrityError:
        error = f"User doesn't own an account with this name."
    else:
        return success_response()

    return error_response(error, 406)