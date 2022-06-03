from . import device_service, device_validator
from flask import request, g
from flask_expects_json import expects_json
from src.Auth import auth_middleware
from src.Permission import permission_middleware
from src.Client import client_middleware


@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@permission_middleware.check_permission("device_edit")
@expects_json(device_validator.device_create_schema)
def create_device() -> dict:
    req = request.get_json()
    res: dict = device_service.create_device(
        key=req['key'],
        name=req['name'],
        description=req['description'],
        error_after_minutes=req['error_after_minutes'],
        parent_ids=req['parent_ids'],
        client_ids=req['client_ids'],
        client_id=g.client_id)
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("device_edit")
@client_middleware.check_client(required=True)
@expects_json(device_validator.device_update_schema)
def update_device(device_id: int) -> dict:
    req: dict = request.get_json()
    res: dict = device_service.update_device(
        device_id=device_id,
        key=req['key'],
        name=req['name'],
        description=req['description'],
        error_after_minutes=req['error_after_minutes'],
        parent_ids=req['parent_ids'],
        client_ids=req['client_ids']
    )
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("device_edit")
@client_middleware.check_client(required=True)
def delete_device(device_id: int) -> dict:
    res: dict = device_service.delete_device(device_id=device_id)
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("device_get")
@client_middleware.check_client(required=True)
def get_devices() -> dict:
    res: dict = device_service.get_devices(
        page=int(request.args.get('page') or 0),
        per_page=int(request.args.get('per_page') or 0),
        client_id=int(request.args.get('client_id') or 0)
    )
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("device_get")
@client_middleware.check_client(required=True)
def get_device_by_id(device_id: int) -> dict:
    res: dict = device_service.get_device_by_id(device_id=device_id)
    return res
