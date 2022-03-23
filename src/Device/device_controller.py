from . import device_service, device_validator
from flask import request
from flask_expects_json import expects_json
from src.Auth import auth_middleware
from src.Permission import permission_middleware
from src.Client import client_middleware


@auth_middleware.check_authorize
@permission_middleware.check_permission("device_edit")
@expects_json(device_validator.device_create_schema)
def create_device() -> dict:
    req: dict = request.get_json()
    res: dict = device_service.create_device(
        key=req['key'],
        name=req['name'],
        description=req['description'],
        client_id=req['client_id'],
        cash_box_id=req['cash_box_id'])
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("device_edit")
@expects_json(device_validator.device_update_schema)
def update_device(device_id: int) -> dict:
    req: dict = request.get_json()
    res: dict = device_service.update_device(
        device_id=device_id,
        key=req['key'],
        name=req['name'],
        description=req['description'],
        parent_key=req['parent_key'],
        cash_box_id=req['cash_box_id']
    )
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("device_edit")
def delete_device(device_id: int) -> dict:
    res: dict = device_service.delete_device(device_id=device_id)
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("device_get")
@client_middleware.check_client(required=False)
def get_device_ids() -> dict:
    res: dict = device_service.get_device_ids()
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("device_get")
@client_middleware.check_client(required=False)
def get_device_by_id(device_id: int) -> dict:
    res: dict = device_service.get_device_by_id(device_id=device_id)
    return res