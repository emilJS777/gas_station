from . import ExpenseServiceDb
from src._response import response
from typing import List


# CREATE
def create(name: str, description: str, price: float, cash_box_id: int) -> dict:
    ExpenseServiceDb.create(
        name=name,
        description=description,
        price=price,
        cash_box_id=cash_box_id
    )
    return response(True, {'msg': 'expense successfully created'}, 200)


# GET BY ID
def get_by_id(expense_id: int) -> dict:
    expense: ExpenseServiceDb.Expense = ExpenseServiceDb.get_by_id(expense_id)
    if not expense:
        return response(False, {'msg': 'expense not found'}, 404)

    return response(True, {
        'id': expense.id,
        'name': expense.name,
        'description': expense.description,
        'price': expense.price,
        'creator_id': expense.creator_id,
        'cash_box_id': expense.cash_box_id
    }, 200)


# GET ALL
def get_all(date, cash_box_id) -> dict:
    expenses: List[dict] = ExpenseServiceDb.get_all(date=date, cash_box_id=cash_box_id)
    return response(True, expenses, 200)
