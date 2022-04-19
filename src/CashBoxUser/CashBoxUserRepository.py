from .CashBoxUserModel import CashBoxUser
from flask import g
from datetime import datetime


# CREATE
def create(cash_box_id: int, client_id: int) -> CashBoxUser:
    cash_box_user: CashBoxUser = CashBoxUser(cash_box_id=cash_box_id, client_id=client_id)
    cash_box_user.save_db()
    return cash_box_user


# DELETE
def delete(cash_box_id: int) -> CashBoxUser:
    cash_box_user: CashBoxUser = CashBoxUser.query.filter_by(cash_box_id=cash_box_id).first()
    cash_box_user.delete_db()
    return cash_box_user


# UPDATE
def update(cash_box_id: int, user_id: int) -> CashBoxUser:
    cash_box_user: CashBoxUser = CashBoxUser.query.filter_by(cash_box_id=cash_box_id).first()
    cash_box_user.user_id = user_id
    cash_box_user.next_user_id = None
    cash_box_user.last_update = datetime.utcnow()
    cash_box_user.update_db()
    return cash_box_user


# REQUEST FOR UPDATE
def request_update(user_id: int, next_user_id: int, cash_box_id: int) -> CashBoxUser:
    cash_box_user: CashBoxUser = CashBoxUser.query.filter_by(
        cash_box_id=cash_box_id,
        user_id=user_id,
        client_id=g.client_id).first()
    cash_box_user.next_user_id = next_user_id
    cash_box_user.update_db()
    return cash_box_user


# GET BY NEXT USER ID
def get_by_next_user_id(next_user_id: int, cash_box_id: int) -> CashBoxUser:
    cash_box_user: CashBoxUser = CashBoxUser.query.filter_by(
        next_user_id=next_user_id,
        cash_box_id=cash_box_id).first()
    return cash_box_user


# GET BY CASH BOX ID
def get_by_cash_box_id(cash_box_id: int, client_id: int = None) -> CashBoxUser:
    client_id = client_id or g.client_id
    cas_box_user: CashBoxUser = CashBoxUser.query.filter_by(cash_box_id=cash_box_id, client_id=client_id).first()
    return cas_box_user


# GET BY CASH BOX ID EXCLUDE CLIENT
def get_by_cash_box_id_exclude_client(cash_box_id: int) -> CashBoxUser:
    cas_box_user: CashBoxUser = CashBoxUser.query.filter_by(cash_box_id=cash_box_id).first()
    return cas_box_user
