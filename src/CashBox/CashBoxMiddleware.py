from flask import g
from src._response import response
from functools import wraps
from src.User import user_service_db


# CHECk CLIENT
# MIDDLEWARE FOR ASSIGNMENT g.client_id
def check_cash_box(required: bool):
    def decoration(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            g.cash_box_id = None
            # GET CASH BOX ID FROM G USER ID
            cash_box_id: int = user_service_db.get_by_id(user_id=g.user_id).cash_box_id

            # VERIFY IF CHECK CLIEnt ARG REQUIRED IS TRUE
            if required and not cash_box_id:
                return response(False, {'msg': 'cash box not found'}, 403)

            # ELSE ASSIGN G CASH BOX ID OR ASSIGN NONE AND NEXT
            else:
                g.cash_box_id = cash_box_id or None

            return f(*args, **kwargs)

        return decorated_function

    return decoration
