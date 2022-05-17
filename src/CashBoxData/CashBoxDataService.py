from . import CashBoxDataRepository
from src._response import response


def create(salary: float, car_gas: int, payment_gas: int, payment_electricity: int, harka: int, r: int, s: int, cash_box_id: int) -> dict:
    CashBoxDataRepository.create(
        salary=salary,
        car_gas=car_gas,
        payment_gas=payment_gas,
        payment_electricity=payment_electricity,
        harka=harka,
        r=r,
        s=s,
        cash_box_id=cash_box_id
    )
    return response(True, {'msg': 'cash box data successfully created'}, 200)


def get_by_date(cash_box_id: int, date) -> dict:
    cash_box_data: CashBoxDataRepository.CashBoxData = CashBoxDataRepository.get_by_date(
        cash_box_id=cash_box_id,
        date=date
    )
    if not cash_box_data:
        return response(False, {'msg': 'cash box data not found'}, 404)

    return response(True, {
        'id': cash_box_data.id,
        'salary': cash_box_data.salary,
        'car_gas': cash_box_data.car_gas,
        'payment_gas': cash_box_data.payment_gas,
        'payment_electricity': cash_box_data.payment_electricity,
        'harka': cash_box_data.harka,
        'r': cash_box_data.r,
        's': cash_box_data.s,
        'cash_box_id': cash_box_data.cash_box_id
    }, 200)
