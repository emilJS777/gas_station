from . import CashBoxUserService
from flask import request
from src.Auth import auth_middleware


@auth_middleware.check_authorize
def get_by_cash_box_id(cash_box_id: int) -> dict:
    res: dict = CashBoxUserService.get_by_cash_box_id(cash_box_id=cash_box_id)
    return res
