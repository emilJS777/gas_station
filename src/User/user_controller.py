from flask import request, g
from . import user_service
from src.Auth import auth_middleware
from flask_expects_json import expects_json
from src.User import user_validator
from src.Permission import permission_middleware
from src.Client import client_middleware
from src.CashBox import CashBoxMiddleware


# CREATE NEW USER OR REGISTRATION
@expects_json(user_validator.user_schema)
def create_user():
    req = request.get_json()
    res = user_service.create_user(
        ticket=req['ticket'],
        user_name=req['name'],
        password=req['password']
    )
    return res


# CREATE USER TICKET
@auth_middleware.check_authorize
@permission_middleware.check_permission("user_edit")
@client_middleware.check_client(required=False)
@CashBoxMiddleware.check_cash_box(required=False)
@expects_json(user_validator.user_ticket_schema)
def create_user_ticket():
    req: dict = request.get_json()
    res = user_service.create_user_ticket(creator_id=g.user_id,
                                          client_id=g.client_id,
                                          first_name=req['first_name'],
                                          last_name=req['last_name'],
                                          cash_box_id=g.cash_box_id or req['cash_box_id'],
                                          cashier=req['cashier'])
    return res


# DELETE USER BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("user_edit")
@client_middleware.check_client(required=False)
def user_delete(user_id):
    res = user_service.user_delete(user_id=user_id)
    return res


# GET USER BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("user_get")
@client_middleware.check_client(required=False)
def user_get_by_id(user_id):
    res = user_service.user_get_by_id(user_id=user_id)
    return res


# GET ALL USER
@auth_middleware.check_authorize
@permission_middleware.check_permission("user_get")
@client_middleware.check_client(required=False)
@CashBoxMiddleware.check_cash_box(required=False)
def user_get():
    res = user_service.user_get_all(
        page=int(request.args.get('page') or 0),
        per_page=int(request.args.get('per_page') or 0),
        client_id=int(request.args.get('client_id') or g.client_id)
    )
    return res


# UPDATE USER BY ID
@auth_middleware.check_authorize
@permission_middleware.check_permission("user_get")
@client_middleware.check_client(required=False)
@CashBoxMiddleware.check_cash_box(required=False)
@expects_json(user_validator.user_ticket_schema)
def user_update(user_id: int):
    req = request.get_json()
    res = user_service.user_update(user_id=user_id,
                                   first_name=req['first_name'],
                                   last_name=req['last_name'],
                                   cash_box_id=g.cash_box_id or req['cash_box_id'],
                                   cashier=req['cashier'])
    return res


