from . import CashBoxService
from flask import request
from src.Auth import auth_middleware
from src.Permission import permission_middleware
from src.Client import client_middleware


# CREATE
@auth_middleware.check_authorize
@permission_middleware.check_permission("cash_box_edit")
@client_middleware.check_client(required=False)
def create() -> dict:
    req: dict = request.get_json()
    res: dict = CashBoxService.create(
        client_id=req['client_id']
    )
    return res


# UPDATE
@auth_middleware.check_authorize
@permission_middleware.check_permission("cash_box_edit")
@client_middleware.check_client(required=False)
def update(cash_box_id: int) -> dict:
    req: dict = request.get_json()
    res = CashBoxService.update(
        cash_box_id=cash_box_id
    )
    return res


# DELETE
@auth_middleware.check_authorize
@permission_middleware.check_permission("cash_box_edit")
@client_middleware.check_client(required=False)
def delete(cash_box_id: int) -> dict:
    res = CashBoxService.delete(
        cash_box_id=cash_box_id
    )
    return res


# GET BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("cash_box_get")
@client_middleware.check_client(required=False)
def get_by_id(cash_box_id: int) -> dict:
    res = CashBoxService.get_by_id(
        cash_box_id=cash_box_id
    )
    return res


# GET ALL IDS
@auth_middleware.check_authorize
@permission_middleware.check_permission("cash_box_get")
@client_middleware.check_client(required=False)
def get_all_ids() -> dict:
    res = CashBoxService.get_all_ids()
    return res
