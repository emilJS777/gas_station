from . import user_role_service
from flask import request
from src.Auth import auth_middleware
from src.Permission import permission_middleware
from src.Client import client_middleware


@auth_middleware.check_authorize
@permission_middleware.check_permission("user_edit")
@permission_middleware.check_permission("role_edit")
@client_middleware.check_client(required=True)
def user_role_bind():
    req = request.get_json()
    res = user_role_service.create_bind(user_id=req['user_id'], role_id=req['role_id'])
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("user_edit")
@permission_middleware.check_permission("role_edit")
@client_middleware.check_client(required=True)
def user_role_unbind():
    req = request.get_json()
    res = user_role_service.delete_bind(user_id=req['user_id'], role_id=req['role_id'])
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("user_get")
@permission_middleware.check_permission("role_get")
@client_middleware.check_client(required=True)
def get_roles_by_user_id(user_id: int):
    res = user_role_service.get_roles_by_user_id(user_id=user_id)
    return res

