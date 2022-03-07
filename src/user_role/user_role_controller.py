from . import user_role_service
from flask import request
from src.auth import auth_middleware
from src.permission import permission_middleware


@auth_middleware.check_authorize
@permission_middleware.check_permission("user_edit")
@permission_middleware.check_permission("role_edit")
def user_role_bind():
    req = request.get_json()
    res = user_role_service.create_bind(user_id=req['user_id'], role_id=req['role_id'])
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("user_edit")
@permission_middleware.check_permission("role_edit")
def user_role_unbind():
    req = request.get_json()
    res = user_role_service.delete_bind(user_id=req['user_id'], role_id=req['role_id'])
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("user_get")
@permission_middleware.check_permission("role_get")
def get_role_ids_by_user_id(user_id: int):
    res = user_role_service.get_role_ids_by_user_id(user_id=user_id)
    return res

