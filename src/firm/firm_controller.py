from flask import request, g
from . import firm_service, firm_validator
from src.auth import auth_middleware
from src.permission import permission_middleware
from src.client import client_middleware
from flask_expects_json import expects_json


# CREATE NEW FIRM
@auth_middleware.check_authorize
@client_middleware.check_client(required=False)
@permission_middleware.check_permission("firm_edit")
@expects_json(firm_validator.firm_schema)
def firm_post():
    req_body = request.get_json()
    res = firm_service.firm_create(req_body=req_body)
    return res


# GET FIRM BY ID
@auth_middleware.check_authorize
@client_middleware.check_client(required=False)
@permission_middleware.check_permission("firm_get")
def firm_get_by_id(firm_id):
    res = firm_service.firm_get_by_id(firm_id=firm_id)
    return res


# GET ALL FIRM
@auth_middleware.check_authorize
@client_middleware.check_client(required=False)
@permission_middleware.check_permission("firm_get")
def firm_get():
    res = firm_service.firm_get_all()
    return res


# UPDATE FIRM BY ID
@auth_middleware.check_authorize
@client_middleware.check_client(required=False)
@permission_middleware.check_permission("firm_edit")
@expects_json(firm_validator.firm_schema)
def firm_update(firm_id):
    req_body = request.get_json()
    res = firm_service.firm_update(firm_id=firm_id, req_body=req_body)
    return res


# DELETE FIRM BY ID
@auth_middleware.check_authorize
@client_middleware.check_client(required=False)
@permission_middleware.check_permission("firm_edit")
def firm_delete(firm_id):
    res = firm_service.firm_delete(firm_id=firm_id)
    return res
