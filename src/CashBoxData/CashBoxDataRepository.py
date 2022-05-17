from .CashBoxDataModel import CashBoxData
from flask import g


# CREATE
def create(salary: float, car_gas: int, payment_gas: int, payment_electricity: int,
           harka: int, r: int, s: int, cash_box_id: int) -> CashBoxData:

    cash_box_data: CashBoxData = CashBoxData(client_id=g.client_id)
    cash_box_data.salary = salary
    cash_box_data.car_gas = car_gas
    cash_box_data.payment_gas = payment_gas
    cash_box_data.payment_electricity = payment_electricity
    cash_box_data.harka = harka
    cash_box_data.r = r
    cash_box_data.s = s
    cash_box_data.cash_box_id = g.cash_box_id or cash_box_id

    cash_box_data.save_db()
    return cash_box_data


# GET CASH BOX DATA BY CASH BOX ID BY DATA
def get_by_date(cash_box_id: int, date) -> CashBoxData:
    if g.cash_box_id:
        cash_box_data: CashBoxData = CashBoxData.query.order_by(-CashBoxData.id).filter_by(client_id=g.client_id,
                                                                 cash_box_id=g.cash_box_id, creation_date=date).first()
    else:
        cash_box_data: CashBoxData = CashBoxData.query.order_by(-CashBoxData.id).filter_by(client_id=g.client_id, cash_box_id=cash_box_id,
                                                                 creation_date=date).first()

    return cash_box_data



