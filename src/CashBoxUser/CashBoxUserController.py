from . import CashBoxUserService
from flask import request
from src.Auth import auth_middleware
from src.Client import client_middleware
from src.CashBox import CashBoxMiddleware


@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
def get_by_cash_box_id(cash_box_id: int) -> dict:
    res: dict = CashBoxUserService.get_by_cash_box_id(cash_box_id=cash_box_id)
    return res


@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
def get_users_by_cash_box_id(cash_box_id: int) -> dict:
    res: dict = CashBoxUserService.get_users_by_cash_box_id(cash_box_id=cash_box_id)
    return res


@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@CashBoxMiddleware.check_cash_box(required=True)
def request_change_cash_box_user(user_id: int) -> dict:
    res: dict = CashBoxUserService.request_change_cash_box_user(user_id)
    return res
