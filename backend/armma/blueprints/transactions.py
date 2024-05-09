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

    account_name = request.json["account_name"]
    amount = request.json["amount"]

    db = get_db()
    current_user = get_current_user()

    error = None

    if not account_name:
        return error_response("Field account_name missing from request.", 400)

    if amount is None:
        return error_response("Field amount missing from request.", 400)

    try:
        account = db.execute(
            "SELECT account_name, user_id from banking_account WHERE user_id=? AND account_name=? AND is_closed=0 and is_frozen=0",
            (current_user["id"], account_name)
        ).fetchone()
        
        if account is None:
            error = "Account either doesn't exist or operation is not permitted."
            return error_response(error, 400)

        db.execute(
            "UPDATE banking_account SET balance=balance+? WHERE user_id=? AND account_name=?",
            (int(amount), current_user["id"], account_name),
        )
        db.commit()
    except db.IntegrityError:
        error = f"Operation failed."
    else:
        return success_response()

    return error_response(error, 400)
