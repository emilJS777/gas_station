from . import CashBoxServiceDb
from src.Client import client_service_db
from src._response import response
from typing import List


# CREATE
def create(client_id: int, name: str, description: str) -> dict:
    client = client_service_db.get_by_id(client_id)
    if not client:
        return response(False, {'msg': 'client not found'}, 404)

    CashBoxServiceDb.create(
        client_id=client.id,
        name=name,
        description=description
    )
    return response(True, {'msg': 'cash box successfully created'}, 200)


# UPDATE
def update(cash_box_id: int, name: str, description: str) -> dict:
    if not CashBoxServiceDb.get_by_id(cash_box_id):
        return response(False, {'msg': 'cash box and/or firm not found'}, 404)

    CashBoxServiceDb.update(
        cash_box_id=cash_box_id,
        name=name,
        description=description
    )
    return response(True, {'msg': 'cash box successfully updated!'}, 200)


# DELETE
def delete(cash_box_id: int) -> dict:
    if not CashBoxServiceDb.get_by_id(cash_box_id):
        return response(False, {'msg': 'cash box not found'}, 404)

    CashBoxServiceDb.delete(cash_box_id)
    return response(True, {'msg': 'cash box successfully deleted'}, 200)


# GET BY ID
def get_by_id(cash_box_id: int) -> dict:
    cash_box: CashBoxServiceDb.CashBox = CashBoxServiceDb.get_by_id(cash_box_id)
    if not cash_box:
        return response(False, {'msg': 'cash box not found'}, 404)

    return response(True, {'id': cash_box.id,
                           'name': cash_box.name,
                           'description': cash_box.description,
                           'client_id': cash_box.client_id}, 200)


# GET ALL IDS
def get_all_ids() -> dict:
    cash_box_ids: List[int] = CashBoxServiceDb.get_all_ids()
    return response(True, cash_box_ids, 200)


