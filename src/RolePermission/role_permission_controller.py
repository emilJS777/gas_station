from . import role_permission_service
from flask import request
from src._response import response
from src.Auth import auth_middleware
from src.Permission import permission_middleware


@auth_middleware.check_authorize
@permission_middleware.check_permission("role_edit")
def create_bind():
    req = request.get_json()
    res = role_permission_service.create_bind(role_id=req['role_id'], permission_ids=req['permission_ids'])
    return res


# @auth_middleware.check_authorize
# @permission_middleware.check_permission("role_edit")
# def delete_bind():
#     req = request.get_json()
#     res = role_permission_service.delete_bind(role_id=req['role_id'], permission_ids=req['permission_ids'])
#     return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("role_get")
def get_permissions_by_role_id(role_id: int):
    res = role_permission_service.get_permissions_by_role_id(role_id=role_id)
    return res

