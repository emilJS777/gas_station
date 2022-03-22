from . import CashBoxUserRepository
from src._response import response


# GET BY CASH BOX ID
def get_by_cash_box_id(cash_box_id: int = None) -> dict:
    cash_box_user: CashBoxUserRepository.CashBoxUser = CashBoxUserRepository.get_by_cash_box_id(cash_box_id)
    if not cash_box_user:
        return response(False, {'msg': 'cash box not found'}, 404)

    return response(True, {'id': cash_box_user.id,
                           'cash_box_id': cash_box_user.cash_box_id,
                           'user_id': cash_box_user.user_id}, 200)
