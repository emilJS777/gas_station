from . import ExpenseService, ExpenseValidator
from flask import request
from src.Auth import auth_middleware
from src.Client import client_middleware
from src.CashBox import CashBoxMiddleware
from src.Permission import permission_middleware
from flask_expects_json import expects_json


# CREATE
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@CashBoxMiddleware.check_cash_box(required=False)
@permission_middleware.check_permission("expense_edit")
@expects_json(ExpenseValidator.expense_create_schema)
def create_expense() -> dict:
    req: dict = request.get_json()
    res = ExpenseService.create(
        name=req['name'],
        description=req['description'],
        price=req['price'],
        cash_box_id=req['cash_box_id']
    )
    return res


# GET BY ID
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@CashBoxMiddleware.check_cash_box(required=False)
@permission_middleware.check_permission("expense_get")
def get_by_id_expense(expense_id) -> dict:
    res: dict = ExpenseService.get_by_id(expense_id=expense_id)
    return res


# GET ALL
@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
@CashBoxMiddleware.check_cash_box(required=False)
@permission_middleware.check_permission("expense_get")
def get_all_expense() -> dict:
    res: dict = ExpenseService.get_all(date=request.args.get('date'), cash_box_id=request.args.get('cash_box_id'))
    return res


