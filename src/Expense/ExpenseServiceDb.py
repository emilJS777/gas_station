from .ExpenseModel import Expense
from flask import g
from typing import List


# CREATE
def create(name: str, description: str, price: float, cash_box_id: int) -> Expense:
    expense: Expense = Expense(
        name=name,
        description=description,
        price=price,

        cash_box_id=g.cash_box_id if g.cash_box_id else cash_box_id,
        client_id=g.client_id,
        creator_id=g.user_id
    )
    expense.save_db()
    return expense


# GET BY ID
def get_by_id(expense_id: int) -> Expense:
    expense: Expense = Expense.query.filter_by(id=expense_id, client_id=g.client_id).first()
    return expense


# GET ALL
def get_all(date, cash_box_id: int) -> List[dict]:
    if g.cashier:
        expenses: List[Expense] = Expense.query.filter_by(client_id=g.client_id,
                                                          creator_id=g.user_id,
                                                          cash_box_id=g.cash_box_id,
                                                          creation_date=date).all()
    elif g.cash_box_id:
        expenses: List[Expense] = Expense.query.filter_by(client_id=g.client_id,
                                                          cash_box_id=g.cash_box_id,
                                                          creation_date=date).all()
    else:
        expenses: List[Expense] = Expense.query.filter_by(client_id=g.client_id,
                                                          cash_box_id=cash_box_id,
                                                          creation_date=date).all()

    expense_list: List[dict] = []
    for expense in expenses:
        expense_list.append({'id': expense.id,
                             'name': expense.name,
                             'description': expense.description,
                             'price': expense.price,
                             'cash_box_id': expense.cash_box_id,
                             'creation_date': expense.creation_date,
                             'creator_id': expense.creator_id})

    print(cash_box_id)

    return expense_list
