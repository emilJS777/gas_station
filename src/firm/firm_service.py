from . import firm_service_db
from src.client import client_service_db
from src._response import response
from flask import g
from typing import List


# CREATE NEW FIRM
def firm_create(req_body):
    # GET CLIENT BY ID IND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not client_service_db.get_by_id(client_id=req_body['client_id']):
        return response(False, {'msg': 'client not found'}, 404)

    # IF FIND THIS FIRM TITLE RETURN RESPONSE CONFLICT
    if firm_service_db.get_by_title(title=req_body['title']):
        return response(False, {'msg': 'firm title is taken'}, 409)

    # ELSE FIRM BY THIS TITLE SAVE
    else:
        new_firm = firm_service_db.create(req_body=req_body)
        return response(True, {'msg': 'new firm by id {} successfully created'.format(new_firm.id)}, 200)


# FIRM GET BY ID
def firm_get_by_id(firm_id):
    # GET FIRM BY ID END VERIFY USER DOES IT EXIST. IF NO RETURN NOT FOUND
    firm = firm_service_db.get_by_id(firm_id=firm_id)
    if not firm:
        return response(False, {'msg': 'firm by this id not found'}, 404)

    # ELSE RETURN THIS FIRM AND STATUS OK
    return response(True, {'title': firm.title,
                           'activity_address': firm.activity_address}, 200)


# GET ALL FIRM
def firm_get_all():
    # GET ALL CLIENTS BY CLIENT ID
    firms_ids: List[int] = firm_service_db.get_all_ids()
    return response(True, firms_ids, 200)


# UPDATE FIRM
def firm_update(firm_id: int, req_body):
    # GET FIRM BY ID AND VERIFY DOES IT EXIST. IF NO RETURN NOT FOUND
    if not firm_service_db.get_by_id(firm_id=firm_id):
        return response(False, {'msg': 'firm by this id not found'}, 404)

    # VERIFY IF THERE IS A FIRM WITH THE SAME TITLE RETURN CONFLICT
    if firm_service_db.get_by_title_exclude_id(firm_id=firm_id, title=req_body['title']):
        return response(False, {'msg': 'firm by this title exist'}, 409)

    # ELSE CHANGE AND UPDATE DB AND RETURN RESPONSE OK
    firm_service_db.update(firm_id=firm_id, req_body=req_body)
    return response(True, {'msg': 'firm successfully update'}, 200)


# DELETE FIRM BY ID
def firm_delete(firm_id: int):
    # GET FIRM BY ID AND VERIFY DIES EXIST. IF NO RETURN NOT FOUND
    if not firm_service_db.get_by_id(firm_id=firm_id):
        return response(False, {"msg": "firm by this id not found"}, 404)

    # REMOVE THIS FIRM FROM DB
    firm_service_db.delete(firm_id=firm_id)
    return response(True, {'msg': "this firm successfully deleted"}, 200)

