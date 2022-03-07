from src.user.user_model import User
from flask import g
from typing import List


# CREATE FIRM USER BIND
def bind_firm_user(firm_id: int, user_id: int) -> User:
    user: User = User.query.filter_by(id=user_id, client_id=g.client_id).first()
    user.firm_id = firm_id
    user.update_db()
    return user


# DELETE BIND FIRM USER
def unbind_firm_user(firm_id: int, user_id: int) -> User:
    user: User = User.query.filter_by(id=user_id, firm_id=firm_id, client_id=g.client_id).first()
    user.firm_id = None
    user.update_db()
    return user


# GET USER IDS BY FIRM ID
def get_user_ids_by_firm_id(firm_id: int) -> List[int]:
    users: List[User] = User.query.filter_by(firm_id=firm_id, client_id=g.client_id).all()
    user_ids: List[int] = []
    for user in users:
        user_ids.append(user.id)
    return user_ids
