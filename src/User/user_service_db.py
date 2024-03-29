from .user_model import User
from flask_bcrypt import generate_password_hash
from .user_helper import generate_ticket_code
from flask import g
from sqlalchemy import or_, and_
from typing import List
from src._general.parents import get_page_items


def create(ticket, name, password):
    # CREATE AND RETURN NEW USER
    new_user = User.query.filter_by(ticket=ticket).first()
    new_user.name = name
    new_user.password_hash = generate_password_hash(password)
    new_user.ticket = None
    new_user.update_db()
    return new_user


def create_ticket(creator_id: int = None,
                  role_id: int = None,
                  first_name: str = None,
                  last_name: str = None,
                  email_address: str = None,
                  cash_box_id: int = None,
                  cashier: bool = False,
                  client_id: int = None):
    # CREATE NEW USER AND TICKET
    user = User(ticket=generate_ticket_code())
    user.client_id = client_id if client_id else g.client_id
    user.first_name = first_name
    user.last_name = last_name
    user.role_id = role_id
    user.email_address = email_address
    user.cash_box_id = cash_box_id
    user.creator_id = creator_id
    user.cashier = cashier
    user.save_db()
    return user


def set_user_ticket(user_id):
    user = User.query.filter_by(id=user_id).first()
    ticket = generate_ticket_code()
    user.ticket = ticket
    user.update_db()
    return ticket


def update(user_id, role_id: int, first_name: str, last_name: str, email_address: str, cash_box_id: int, cashier: bool):
    # GET USER BY ID AND CREAtOR ID & UPDATE NAME
    user = User.query.filter_by(id=user_id).first()
    user.first_name = first_name
    user.last_name = last_name
    user.role_id = role_id
    user.email_address = email_address
    user.cash_box_id = cash_box_id
    user.cashier = cashier
    user.update_db()
    return user


def delete(user_id):
    # GET USER BY USER ID AND CREATOR ID & DELETE
    user = User.query.filter_by(id=user_id).first()
    user.delete_db()
    return user


def get_by_name(name):
    # GET USER BY NAME AND RETURN
    user = User.query.filter_by(name=name).first()
    return user


def get_by_email_address(email_address: str):
    user = User.query.filter_by(email_address=email_address).first()
    return user


def get_by_email_address_exclude_id(user_id: int, email_address: str):
    user = User.query.filter(User.id != user_id, User.email_address == email_address).first()
    return user


def get_by_id(user_id: int):
    user = User.query.filter_by(id=user_id, client_id=g.client_id).first()
    return user


def get_by_id_cash_box_id(user_id: int, cash_box_id: int) -> User:
    user = User.query.filter_by(id=user_id, cash_box_id=cash_box_id, client_id=g.client_id)
    return user


def get_by_ticket(ticket):
    # GET USER MODEL BY TICKET
    user = User.query.filter_by(ticket=ticket).first()
    return user


def get_by_id_creator_id(user_id, creator_id):
    # GET AND RETURN USER BY ID AND CREATOR ID
    user = User.query.filter_by(id=user_id, creator_id=creator_id).first()
    return user
#
#
# def get_by_id_client_id(user_id, client_id):
#     # GET AND RETURN USER BY FIRM ID
#     User = User.query.filter_by(id=user_id, client_id=client_id).first()
#     return User


def update_password(user_id: int, new_password: str):
    user = User.query.filter_by(id=user_id).first()
    user.password_hash = generate_password_hash(new_password)
    user.ticket = None
    user.update_db()


def get_first_by_creator_id(creator_id):
    # GET FIRST USER BY CREATOR ID
    user = User.query.filter_by(creator_id=creator_id).first()
    return user


# def get_all_by_creator_id(creator_id):
#     arr = []
#     # GET ALL USER BY CREATOR ID
#     # ITERATE OVER ONE AT A TIME AND INSERT THE USER OBJECT INTO THE ARRAY
#     users = User.query.filter_by(creator_id=creator_id).all()
#     for User in users:
#         arr.append({'id': User.id, 'name': User.name})
#
#     return arr

def get_all_by_cash_box_id(cash_box_id: int) -> List[dict]:
    arr: List[dict] = []
    # GET ALL USER BY CLIENT ID
    # ITERATE OVER ONE AT A TIME AND INSERT THE USER OBJECT INTO THE ARRAY
    users: List[User] = User.query.filter(User.cash_box_id == cash_box_id,
                                          User.id != g.user_id,
                                          User.client_id == g.client_id).all()

    for user in users:
        arr.append({'id': user.id,
                    'name': user.name,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'cashier': user.cashier})

    return arr


def get_all_by_client_id(client_id: int):
    # GE ALL BY CLIENT ID
    users: List[User] = User.query.filter_by(client_id=client_id).all()
    return users


def get_all(page: int, per_page: int, client_id: int) -> dict:
    # GET ALL USER BY CLIENT ID
    # ITERATE OVER ONE AT A TIME AND INSERT THE USER OBJECT INTO THE ARRAY
    if g.cash_box_id:
        users = User.query.filter_by(client_id=g.client_id, cash_box_id=g.cash_box_id)\
            .paginate(page=page, per_page=per_page)
    else:
        users = User.query.filter_by(client_id=client_id)\
            .paginate(page=page, per_page=per_page)

    return get_page_items(users)
