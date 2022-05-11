from . import role_service, role_validator
from flask import request
from src.Permission import permission_middleware
from src.Auth import auth_middleware
from flask_expects_json import expects_json


@auth_middleware.check_authorize
@permission_middleware.check_permission("role_edit")
@expects_json(role_validator.role_schema)
def create_role():
    req = request.get_json()
    res = role_service.create_role(name=req['name'])
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("role_edit")
@expects_json(role_validator.role_schema)
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
