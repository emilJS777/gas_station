from src.User import user_service_db
from src.UserRole import user_role_service_db
from src.Role import role_service_db
from . import auth_service_db
from flask_bcrypt import check_password_hash
from flask import request, g
from src._response import response
from flask_jwt_extended import get_jwt_identity
from src.CashBoxUser import CashBoxUserRepository
from typing import List
from src.CashBoxUser import CashBoxUserRepository


def login(user_name, password):
    # FIND THE USER BY NAME AND CHECK IF THE PASSWORD
    # IS INCORRECT OR THE USER IS NOT FOUND
    # RETURN RESPONSE UNAUTHORIZED
    user = user_service_db.get_by_name(name=user_name)
    if not user or not check_password_hash(user.password_hash, password):
        return response(False, {'msg': 'invalid User name and/or password'}, 401)

    # ID USER IS CASHIER SET DATA
    if user.cash_box_id:
        cash_box_user = CashBoxUserRepository.get_by_cash_box_id(cash_box_id=user.cash_box_id, client_id=user.client_id)

        if cash_box_user.user_id == user.id or not cash_box_user.user_id or cash_box_user.next_user_id == user.id:
            CashBoxUserRepository.update(cash_box_id=user.cash_box_id, user_id=user.id)
        else:
            return response(False, {'msg': 'this is not your shift'}, 403)

    # UPDATE AUTH PAIR TOKENS AND RETURN
    new_auth = auth_service_db.update_pair_tokens(user_id=user.id)
    return response(True, {'access_token': new_auth.access_token, "refresh_token": new_auth.refresh_token}, 200)


def refresh_token():
    # GET AUTH BY USER ID AND CHECK
    # FOR COMPLIANCE WITH THE REFRESH TOKEN
    auth = auth_service_db.get_by_user_id(user_id=get_jwt_identity())
    if auth.refresh_token == request.headers['authorization'].split(' ')[1]:

        # UPON MATCHING, A NEW PAIR OF TOKENS IS GENERATED AND RESPOND
        new_auth = auth_service_db.update_pair_tokens(user_id=get_jwt_identity())
        return response(True, {'access_token': new_auth.access_token, 'refresh_token': new_auth.refresh_token}, 200)

    # IF DO NOT MATCH RETURN WITHOUT SUCCESS
    return response(False, {'msg': 'invalid refresh token'}, 401)


def get_profile() -> dict:
    user: user_service_db.User = user_service_db.get_by_id(user_id=g.user_id)

    role_ids: List[int] = user_role_service_db.get_role_ids_by_user_id(user_id=g.user_id)
    roles: List[dict] = []

    for role_id in role_ids:
        role = role_service_db.get_role_by_id(role_id)
        roles.append({'name': role.name})

    return response(True, {'name': user.name, 'first_name': user.first_name, 'last_name': user.last_name, 'roles': roles}, 200)
