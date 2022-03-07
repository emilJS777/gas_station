from src.firm.firm_model import Firm
from sqlalchemy import not_
from flask import g
from typing import List


def create(req_body):
    # CREATE NEW FIRM AND RETURN
    new_firm = Firm(req_body['title'], req_body['activity_address'], client_id=req_body['client_id'])
    new_firm.save_db()
    return new_firm


def update(firm_id, req_body):
    # GET FIRM BY ID AND UPDATE & RETURN
    firm = Firm.query.filter_by(id=firm_id).first()
    firm.title = req_body['title']
    firm.activity_address = req_body['activity_address']
    firm.update_db()
    return firm


def delete(firm_id):
    # GET FIRM BY ID AND CLIENT ID. DELETE AND RETURN
    firm = Firm.query.filter_by(id=firm_id).first()
    firm.delete_db()
    return firm


def get_by_title(title):
    # GET FIRM BY TITLE AND CLIENT ID & RETURN
    firm = Firm.query.filter_by(title=title).first()
    return firm


def get_by_id(firm_id):
    # GET FIRM BY ID AND CLIENT ID & RETURN
    firm: Firm = Firm.query.filter_by(id=firm_id, client_id=g.client_id).first() \
        if g.client_id else \
        Firm.query.filter_by(id=firm_id).first()
    return firm


def get_all_ids():
    firms_arr: List[int] = []
    # GET ALL FIRM BY THIS USER CLIENT ID
    # ITERATE OVER ONE AT A TIME AND INSERT THE FIRM OBJECT INTO THE ARRAY
    firms: List[Firm] = Firm.query.filter_by(client_id=g.client_id).all() if g.client_id else Firm.query.all()
    for firm in firms:
        firms_arr.append(firm.id)
    return firms_arr


def get_by_title_exclude_id(firm_id, title):
    # GET FIRM BY CLIENT ID TITLE, AND EXCLUDE FIRM ID
    firm = Firm.query.filter(Firm.id != firm_id, Firm.title == title).first()
    return firm
