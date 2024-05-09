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


bp = Blueprint("transactions", __name__)


@bp.route("/add_balance", methods=["POST"])
@jwt_required()
def add_balance():
    """Add balance to chosen account."""

    account_id = None
    if "account_id" in request.json:
        account_id = request.json["account_id"]

    amount = None
    if "amount" in request.json:
        amount = request.json["amount"]

    db = get_db()
    current_user = get_current_user()

    error = None

    if not account_id:
        return error_response("Field account_id missing from request.", 400)

    if amount is None:
        return error_response("Field amount missing from request.", 400)

    try:
        account = db.execute(
            "SELECT account_name, user_id from banking_account WHERE user_id=? AND id=? AND is_closed=0 and is_frozen=0",
            (current_user["id"], account_id)
        ).fetchone()
        
        if account is None:
            error = "Account either doesn't exist or operation is not permitted."
            return error_response(error, 400)

        db.execute(
            "UPDATE banking_account SET balance=balance+? WHERE id=?",
            (amount, account_id),
        )
        db.commit()
    except db.IntegrityError:
        error = f"Operation failed."
    else:
        return success_response()

    return error_response(error, 400)

@bp.route("/transfer_balance", methods=["POST"])
@jwt_required()
def transfer_balance():
    """Transfer balance from an acconut to another."""

    from_account = None
    if "from_account" in request.json:
        from_account = request.json["from_account"]
    
    to_account = None
    if "to_account" in request.json:
        to_account = request.json["to_account"]
    
    amount = None
    if "amount" in request.json:
        amount = request.json["amount"]

    db = get_db()
    current_user = get_current_user()

    error = None

    if not from_account:
        return error_response("Field from_account missing from request.", 400)
    
    if not to_account:
        return error_response("Field to_account missing from request.", 400)
    
    if amount is None:
        return error_response("Field amount missing from request.", 400)

    try:
        from_account_check = db.execute(
            "SELECT account_name, user_id, balance from banking_account WHERE user_id=? AND id=? AND is_closed=0 and is_frozen=0",
            (current_user["id"], from_account)
        ).fetchone()
        
        if from_account_check is None:
            error = "Account either doesn't exist or operation is not permitted."
            return error_response(error, 400)

        if from_account_check["balance"] < amount:
            error = "Not enough funds for this transfer."
            return error_response(error, 406)
        
        to_account_check = db.execute(
            "SELECT account_name, user_id, balance from banking_account WHERE id=? AND is_closed=0 and is_frozen=0",
            (to_account,)
        ).fetchone()

        if to_account_check is None:
            error = "Receiving account does not exist."
            return error_response(error, 404)

        db.execute(
            "UPDATE banking_account SET balance=balance-? WHERE id=?",
            (amount, from_account),
        )

        db.execute(
            "UPDATE banking_account SET balance=balance+? WHERE id=?",
            (amount, to_account),
        )

        db.execute(
            "INSERT INTO bank_transaction (from_banking_account_id, to_banking_account_id, amount) VALUES (?, ?, ?)",
            (from_account, to_account, amount),
        )

        db.commit()
    except db.IntegrityError:
        error = f"Operation failed."
    else:
        return success_response()

    return error_response(error, 400)

@bp.route("/transactions", methods=["GET"])
@jwt_required()
def transactions():  # TODO: Paginate this
    """List transactions of this user."""

    db = get_db()
    current_user = get_current_user()

    error = None

    try:
        transactions = db.execute(
            "SELECT * from bank_transaction where from_banking_account_id in (select id from banking_account where user_id=?) or to_banking_account_id in (select id from banking_account where user_id=?)",
            (current_user["id"], current_user["id"])
        ).fetchall()

        return success_message_response([dict(x) for x in transactions])
    except db.IntegrityError:
        error = f"Operation failed."

    return error_response(error, 400)
