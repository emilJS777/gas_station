from . import CashBoxUserRepository
from src.CashBox import CashBoxServiceDb
from src.User import user_service_db
from src._response import response
from typing import List
from flask import g


# GET BY CASH BOX ID
def get_by_cash_box_id(cash_box_id: int = None) -> dict:
    cash_box_user: CashBoxUserRepository.CashBoxUser = CashBoxUserRepository.get_by_cash_box_id(cash_box_id)
    if not cash_box_user:
        return response(False, {'msg': 'cash box not found'}, 404)

    return response(True, {'id': cash_box_user.id,
                           'cash_box_id': cash_box_user.cash_box_id,
                           'user_id': cash_box_user.user_id}, 200)


# GET USER IDS BY CASH BOX ID
def get_users_by_cash_box_id(cash_box_id: int) -> dict:
    if not CashBoxServiceDb.get_by_id(cash_box_id):
        return response(False, {'msg': 'CashBox not found'}, 404)

    users: List[dict] = user_service_db.get_all_by_cash_box_id(cash_box_id)
    return response(True, users, 200)


# REQUEST CHANGE CASH BOX USER
def request_change_cash_box_user(user_id: int) -> dict:
    if not user_service_db.get_by_id_cash_box_id(user_id=user_id, cash_box_id=g.cash_box_id):
        return response(False, {'msg': 'cashier not found'}, 404)

    CashBoxUserRepository.request_update(
        user_id=g.user_id,
        next_user_id=user_id,
        cash_box_id=g.cash_box_id
    )
    return response(True, {'msg': 'change request successfully sent'}, 200)

