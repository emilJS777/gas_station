from flask import request
from . import client_user_service, client_user_validator
from src.Auth import auth_middleware
from src.Permission import permission_middleware
from flask_expects_json import expects_json


# # GET USER IDS BY CLIENT ID
# @auth_middleware.check_authorize
# @permission_middleware.check_permission("user_get")
# @permission_middleware.check_permission("client_get")
# def get_users_by_client_id():
#     res = client_user_service.get_users_by_client_id(
#         client_id=int(request.args.get('client_id') or None),
#         page=int(request.args.get('page') or None),
#         per_page=int(request.args.get('per_page') or None)
#     )
#     return res


# BIND LINK CLIENT AND USER BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("user_edit")
@permission_middleware.check_permission("client_edit")
@expects_json(client_user_validator.client_user_schema)
def bind_client_user():
    req = request.get_json()
    res = client_user_service.bind_client_user(client_id=req['client_id'], user_id=req['user_id'])
    return res


# UNBIND CLIENT USER
@auth_middleware.check_authorize
@permission_middleware.check_permission("user_edit")
@permission_middleware.check_permission("client_edit")
@expects_json(client_user_validator.client_user_schema)
def unbind_client_user():
    req = request.get_json()
    res = client_user_service.unbind_client_user(client_id=req['client_id'], user_id=req['user_id'])
    return res
