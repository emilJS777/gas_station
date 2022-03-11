from . import device_service
from flask import request
from src.auth import auth_middleware
from src.permission import permission_middleware
from src.client import client_middleware


@auth_middleware.check_authorize
@permission_middleware.check_permission("device_edit")
def create_device() -> dict:
    req: dict = request.get_json()
    res: dict = device_service.create_device(key=req['key'], name=req['name'],
                                             description=req['description'], client_id=req['client_id'])
    return res


@auth_middleware.check_authorize
@permission_middleware.check_permission("device_edit")
def update_device(device_id: int) -> dict:
    req: dict = request.get_json()
    res: dict = device_service.update_device(device_id=device_id, key=req['key'],
                                             name=req['name'], description=req['description'],
                                             parent_key=req['parent_key'])
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
