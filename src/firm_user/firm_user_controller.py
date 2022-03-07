from . import firm_user_service, firm_user_validator
from flask import request
from src.auth import auth_middleware
from src.client import client_middleware
from src.permission import permission_middleware
from flask_expects_json import expects_json


# CREATE BIND FIRM USER
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@permission_middleware.check_permission("firm_edit")
@permission_middleware.check_permission("user_edit")
@expects_json(firm_user_validator.firm_user_schema)
def bind_firm_user():
    req = request.get_json()
    res = firm_user_service.bind_firm_user(firm_id=req['firm_id'], user_id=req['user_id'])
    return res


# DELETE BIND FIRM USER
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@permission_middleware.check_permission("firm_edit")
@permission_middleware.check_permission("user_edit")
@expects_json(firm_user_validator.firm_user_schema)
def unbind_firm_user():
    req = request.get_json()
    res = firm_user_service.unbind_firm_user(firm_id=req['firm_id'], user_id=req['user_id'])
    return res


# GET USER IDS BY FIRM ID
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@permission_middleware.check_permission("firm_get")
@permission_middleware.check_permission("user_get")
def get_user_ids_by_firm_id(firm_id: int):
    res = firm_user_service.get_user_ids_by_firm_id(firm_id=firm_id)
    return res
