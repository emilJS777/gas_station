from .CashBoxModel import CashBox
from typing import List
from flask import g


# CREATE
def create(client_id: int, name: str, description: str) -> CashBox:
    cash_box: CashBox = CashBox(client_id=client_id)
    cash_box.name = name
    cash_box.description = description
    cash_box.save_db()
    return cash_box


# UPDATE
def update(cash_box_id: int, name: str, description: str) -> CashBox:
    cash_box: CashBox = CashBox.query.filter_by(id=cash_box_id).first()
    cash_box.name = name
    cash_box.description = description
    cash_box.update_db()
    return cash_box


# DELETE
def delete(cash_box_id: int) -> CashBox:
    cash_box: CashBox = CashBox.query.filter_by(id=cash_box_id).first()
    cash_box.delete_db()
    return cash_box


# GET BY ID
def get_by_id(cash_box_id: int) -> CashBox:
    # # FOR FIRM ID
    # if g.firm_id:
    #     cash_box: CashBox = CashBox.query.filter_by(id=cash_box_id, firm_id=g.firm_id).first()
    # # FOR CLIENT ID
    # elif g.client_id:
    #     cash_box: CashBox = CashBox.query.filter_by(id=cash_box_id, client_id=g.client_id).first()
    # # FOR ADMIN
    # else:
    #     cash_box: CashBox = CashBox.query.filter_by(id=cash_box_id).first()

    cash_box: CashBox = \
        CashBox.query.filter_by(id=cash_box_id, client_id=g.client_id).first() \
        if g.client_id else \
        CashBox.query.filter_by(id=cash_box_id).first()

    return cash_box


# # GET BY FIRM ID
# def get_by_firm_id(firm_id: int) -> CashBox:
#     cash_box: CashBox = CashBox.query.filter_by(firm_id=firm_id).first()
#     return cash_box


# GET ALL BY CLIENT ID
def get_all_ids() -> List[int]:
    # # FOR FIRM ID
    # if g.firm_id:
    #     cash_boxes: List[CashBox] = CashBox.query.filter_by(firm_id=g.firm_id).all()
    # # FOR CLIENT ID
    # elif g.client_id:
    #     cash_boxes: List[CashBox] = CashBox.query.filter_by(client_id=g.client_id).all()
    # # FOR ADMIN
    # else:
    #     cash_boxes: List[CashBox] = CashBox.query.all()

    cash_boxes: List[CashBox] = \
        CashBox.query.filter_by(client_id=g.client_id).all() \
        if g.client_id else \
        CashBox.query.all()

    cash_box_ids: List[int] = []
    for cash_box in cash_boxes:
        cash_box_ids.append(cash_box.id)

    return cash_box_ids
