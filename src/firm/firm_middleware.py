from flask import g
from src._response import response
from functools import wraps
from . import firm_service_db
from src.user import user_service_db


# CHECk FIRM
# MIDDLEWARE FOR ASSIGNMENT g.firm_id
def check_firm(required: bool):
    def decoration(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # GET FIRM ID FROM G USER ID
            firm_id: int = user_service_db.get_by_id(user_id=g.user_id).firm_id

            # VERIFY IF CHECK FIRM ARG REQUIRED IS TRUE AND FIRM ID NOT FOUND RETURN FORBIDDEN
            if required and not firm_id or firm_id and not firm_service_db.get_by_id(firm_id=firm_id):
                return response(False, {'msg': 'client not found'}, 403)

            # ELSE ASSIGN G FIRM ID OR ASSIGN NONE AND NEXT
            else:
                g.firm_id = firm_id or None

            return f(*args, **kwargs)

        return decorated_function
    return decoration
