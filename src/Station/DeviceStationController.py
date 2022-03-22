from . import DeviceStationService
from . import DeviceStationValidator
from flask import request
from src.Auth import auth_middleware
from src.Permission import permission_middleware
from flask_expects_json import expects_json
from src.Client import client_middleware
from src.CashBox import CashBoxMiddleware


# CREATE
@auth_middleware.check_authorize
@permission_middleware.check_permission("device_station_edit")
@client_middleware.check_client(required=False)
@expects_json(DeviceStationValidator.device_create_schema)
def create_device_station() -> dict:
    req: dict = request.get_json()
    res: dict = DeviceStationService.create(
        key=req['key'],
        name=req['name'],
        description=req['description'],
        cash_box_id=req['cash_box_id'],
        client_id=req['client_id']
    )
    return res


# UPDATE
@auth_middleware.check_authorize
@permission_middleware.check_permission("device_station_edit")
@client_middleware.check_client(required=False)
@expects_json(DeviceStationValidator.device_update_schema)
def update_device_station(device_id: int) -> dict:
    req: dict = request.get_json()
    res: dict = DeviceStationService.update(
        device_id,
        key=req['key'],
        name=req['name'],
        description=req['description'],
        cash_box_id=req['cash_box_id']
    )
    return res


# DELETE
@auth_middleware.check_authorize
@permission_middleware.check_permission("device_station_edit")
@client_middleware.check_client(required=False)
def delete_device_station(device_id: int) -> dict:
    res: dict = DeviceStationService.delete(device_id)
    return res


# GET BY ID
@auth_middleware.check_authorize
# @permission_middleware.check_permission("device_station_get")
@client_middleware.check_client(required=False)
@CashBoxMiddleware.check_cash_box(required=False)
def device_station_get_by_id(device_id: int) -> dict:
    res: dict = DeviceStationService.get_by_id(device_id)
    return res


# GET ALL IDS
@auth_middleware.check_authorize
# @permission_middleware.check_permission("device_station_get")
@client_middleware.check_client(required=False)
@CashBoxMiddleware.check_cash_box(required=False)
def device_station_get_all_ids() -> dict:
    res: dict = DeviceStationService.get_all_ids()
    return res
