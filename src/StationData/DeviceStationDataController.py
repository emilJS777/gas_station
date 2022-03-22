from . import DeviceStationDataService
from flask import request
from src.Auth import auth_middleware
from src.Permission import permission_middleware
from src.Client import client_middleware


# CREATE
def create_device_station_data() -> dict:
    res: dict = DeviceStationDataService.create(
        device_station_key=request.args['device_station_key'],
        weight=float(request.args['weight']),
        pressure=float(request.args['pressure']),
        price=float(request.args['price']),
        temperature=float(request.args['temperature'])
    )
    return res


# GET BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("device_station_get")
@client_middleware.check_client(required=False)
def device_station_data_get_by_id(device_station_data_id: int) -> dict:
    res: dict = DeviceStationDataService.get_by_id(device_station_data_id)
    return res


# GET ALL IDS
@auth_middleware.check_authorize
@permission_middleware.check_permission("device_station_get")
@client_middleware.check_client(required=False)
def device_station_data_get_all_ids() -> dict:
    res: dict = DeviceStationDataService.get_all_ids()
    return res

