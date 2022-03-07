from . import firm_user_service_db
from src.firm import firm_service_db
from src.user import user_service_db
from src._response import response
from typing import List


# CREATE BIND FIRM USER
def bind_firm_user(firm_id: int, user_id: int):
    # GET FIRM BY ID AND USER BY ID AND VERIFY IF USER OR FIRM NOT FOUND RETURN NOT FOUND
    if not firm_service_db.get_by_id(firm_id=firm_id) or not user_service_db.get_by_id(user_id=user_id):
        return response(False, {'msg': 'user and/or firm not found'}, 404)

    # ELSE BIND FIRM USER AND RETURN OK
    else:
        firm_user_service_db.bind_firm_user(firm_id=firm_id, user_id=user_id)
        return response(True, {'msg': 'binding done'}, 200)


# DELETE BIND FIRM USER
def unbind_firm_user(firm_id: int, user_id: int):
    # GET FIRM AND USER AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not firm_service_db.get_by_id(firm_id=firm_id) or not user_service_db.get_by_id(user_id=user_id):
        return response(False, {'msg': 'user and/or firm not found'}, 404)

    # ELSE UNBIND FIRM USER AND RETURN OK
    else:
        firm_user_service_db.unbind_firm_user(firm_id=firm_id, user_id=user_id)
        return response(True, {'msg': 'binding successfully deleted'}, 200)


# GET USER IDS BY FIRM ID
def get_user_ids_by_firm_id(firm_id: int):
    # GET FIRM BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not firm_service_db.get_by_id(firm_id=firm_id):
        return response(False, {'msg': 'firm not found'}, 404)

    # ELSE GET USER IDS BY FIRM ID AND RETURN OK
    else:
        user_ids: List[int] = firm_user_service_db.get_user_ids_by_firm_id(firm_id=firm_id)
        return response(True, user_ids, 200)
