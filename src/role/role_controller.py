from . import role_service
from flask import request
from src.permission import permission_middleware
from src.auth import auth_middleware


@auth_middleware.check_authorize
@permission_middleware.check_permission("role_edit")
def create_role():
    req = request.get_json()
    res = role_service.create_role(name=req['name'])
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("role_edit")
def update_role(role_id: int):
    req = request.get_json()
    res = role_service.update_role(role_id=role_id, name=req['name'])
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("role_get")
def get_role_by_id(role_id: int):
    res = role_service.get_role_by_id(role_id=role_id)
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("role_get")
def get_roles():
    res = role_service.get_roles()
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("role_edit")
def delete_role(role_id: int):
    res = role_service.delete_role(role_id=role_id)
    return res
