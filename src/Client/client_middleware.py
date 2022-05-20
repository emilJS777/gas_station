from flask import g
from src._response import response
from functools import wraps
from . import client_service_db
from src.User import user_service_db


# CHECk CLIENT
# MIDDLEWARE FOR ASSIGNMENT g.client_id
def check_client(required: bool):
    def decoration(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            g.client_id = None
            # GET CLIENT ID FROM G USER ID
            client_id: int = user_service_db.User.query.filter_by(id=g.user_id).first().client_id

            # VERIFY IF CHECK CLIEnt ARG REQUIRED IS TRUE AND CLIENT ID NOT FOUND RETURN FORBIDDEN
            if required and not client_id or client_id and not client_service_db.Client.query.filter_by(id=client_id).first():
                return response(False, {'msg': 'Client not found'}, 403)

            # ELSE ASSIGN G CLIENT ID OR ASSIGN NONE AND NEXT
            else:
                g.client_id = client_id or None

            return f(*args, **kwargs)

        return decorated_function

    return decoration
