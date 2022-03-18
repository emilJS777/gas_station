from flask import request
from . import client_service, client_validator
from src.Auth import auth_middleware
from src.Permission import permission_middleware
from flask_expects_json import expects_json


# CREATE NEW CLIENT
@auth_middleware.check_authorize
@permission_middleware.check_permission("client_edit")
@expects_json(client_validator.client_schema)
def client_post():
    req = request.get_json()
    res = client_service.client_create(client_name=req['name'], client_description=req["description"])
    return res


# UPDATE CLIENT BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("client_edit")
@expects_json(client_validator.client_schema)
def client_update(client_id):
    req = request.get_json()
    res = client_service.client_update(client_id=client_id,
                                       client_name=req['name'],
                                       client_description=req["description"])
    return res


# DELETE CLIENT BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("client_edit")
def client_delete(client_id):
    res = client_service.client_delete(client_id=client_id)
    return res


# GET CLIENT BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("client_get")
def client_get_by_id(client_id):
    res = client_service.client_get_by_id(client_id=client_id)
    return res


# GET ALL CLIENT
@auth_middleware.check_authorize
@permission_middleware.check_permission("client_get")
def client_get():
    res = client_service.client_get_all()
    return res



