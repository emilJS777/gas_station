from . import CashBoxDataService
from flask import request
from src.Auth import auth_middleware
from src.Client import client_middleware
from src.CashBox import CashBoxMiddleware
from src.Permission import permission_middleware


# CREATE
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@CashBoxMiddleware.check_cash_box(required=False)
@permission_middleware.check_permission('cash_box_data_edit')
def create_cash_box_data() -> dict:
    req: dict = request.get_json()
    res: dict = CashBoxDataService.create(
        salary=req['salary'],
        car_gas=req['car_gas'],
        payment_gas=req['payment_gas'],
        payment_electricity=req['payment_electricity'],
        harka=req['harka'],
        r=req['r'],
        s=req['s'],
        cash_box_id=req['cash_box_id']
    )
    return res


@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@CashBoxMiddleware.check_cash_box(required=False)
@permission_middleware.check_permission('cash_box_data_get')
def get_by_date() -> dict:
    res: dict = CashBoxDataService.get_by_date(
        cash_box_id=int(request.args.get('cash_box_id')),
        date=request.args.get('date')
    )
    return res
