from . import ClientDeviceService
from flask import request
from src.Auth import auth_middleware
from src.Client import client_middleware
from src.Permission import permission_middleware


@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@permission_middleware.check_permission('device_edit')
@permission_middleware.check_permission('client_edit')
def client_device_bind():
    req = request.get_json()
    res = ClientDeviceService.create_bind(
        client_id=req['client_id'],
        device_id=req['device_id']
    )
    return res


@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@permission_middleware.check_permission('device_edit')
@permission_middleware.check_permission('client_edit')
def client_device_unbind():
    req = request.get_json()
    res = ClientDeviceService.delete_bind(
        client_id=req['client_id'],
        device_id=req['device_id']
    )
    return res


@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@permission_middleware.check_permission('device_get')
@permission_middleware.check_permission('client_get')
def get_devices_by_client_id():
    res = ClientDeviceService.get_devices_by_client_id(
        client_id=int(request.args.get('client_id') or 0)
    )
    return res
