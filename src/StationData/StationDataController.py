from . import StationDataService
from flask import request
from src.Auth import auth_middleware
from src.Permission import permission_middleware
from src.Client import client_middleware
from src.CashBox import CashBoxMiddleware


# CREATE
def create_station_data() -> dict:
    res: dict = StationDataService.create(
        station_key=request.args['station_key'],
        weight=float(request.args.get('weight')),
        pressure=float(request.args.get('pressure')),
        price=float(request.args.get('price')),
        temperature=float(request.args.get('temperature'))
    )
    return res


# GET BY ID
@auth_middleware.check_authorize
# @permission_middleware.check_permission("station_get")
@client_middleware.check_client(required=False)
@CashBoxMiddleware.check_cash_box(required=False)
def station_data_get_by_id(device_station_data_id: int) -> dict:
    res: dict = StationDataService.get_by_id(device_station_data_id)
    return res


# GET ALL IDS
@auth_middleware.check_authorize
# @permission_middleware.check_permission("station_get")
@client_middleware.check_client(required=False)
@CashBoxMiddleware.check_cash_box(required=False)
def station_data_get_all_ids() -> dict:
    date = request.args.get('date')
    res: dict = StationDataService.get_all_ids(date=date)
    return res


# GET ALL IDS BY CASH BOX ID
@auth_middleware.check_authorize
# @permission_middleware.check_permission("station_get")
@client_middleware.check_client(required=False)
@CashBoxMiddleware.check_cash_box(required=False)
def get_all_ids_by_cash_box_id() -> dict:
    res: dict = StationDataService.get_all_ids_by_cash_box_id(
        cash_box_id=int(request.args.get('cash_box_id')),
        date=request.args.get('date')
    )
    return res
