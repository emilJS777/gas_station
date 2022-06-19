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
from ..Permission import permission_service_db
from ..RolePermission import role_permission_service_db
from .auth_helper import send_ticket_code_to_email
from flask import g


def login(user_name, password):
    # FIND THE USER BY NAME AND CHECK IF THE PASSWORD
    # IS INCORRECT OR THE USER IS NOT FOUND
    # RETURN RESPONSE UNAUTHORIZED
    user = user_service_db.get_by_name(name=user_name) or user_service_db.get_by_email_address(user_name)
    if not user or not check_password_hash(user.password_hash, password):
        return response(False, {'msg': 'invalid User name and/or password'}, 200)

    # ID USER IS CASHIER SET DATA
    if user.cash_box_id and user.cashier:
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

    permission_list: List[dict] = []
    for permission_id in role_permission_service_db.get_permission_ids_by_role_id(role_id=g.role_id):
        permission: permission_service_db.Permission = permission_service_db.get_by_id(permission_id=permission_id)
        permission_list.append({'id': permission.id, 'name': permission.name, 'title': permission.title})

    role = role_service_db.get_role_by_id(g.role_id)

    return response(True, {'id': user.id,
                           'email_address': user.email_address,
                           'name': user.name,
                           'first_name': user.first_name,
                           'last_name': user.last_name,
                           'cash_box_id': user.cash_box_id,
                           'cashier': user.cashier,
                           'permissions': permission_list,
                           'role': role.name}, 200)


# RESSET PASSWORD
def resset_password(ticket_code: str, new_password: str) -> dict:
    user = user_service_db.get_by_ticket(ticket_code)

    if not user:
        return response(False, {'msg': 'ticket not found'}, 200)

    user_service_db.update_password(user.id, new_password)
    return response(True, {'msg': 'password successfully updated'}, 200)


# REQUEST RESSET PASSWORD
def request_resset_password(email_address: str) -> dict:
    user = user_service_db.get_by_email_address(email_address)
    if not user:
        return response(False, {'msg': 'email address not found'}, 200)

    ticket = user_service_db.set_user_ticket(user.id)
    send_ticket_code_to_email(
        email_address=email_address,
        ticket_code=ticket,
        message="use this password reset code"
    )
    return response(True, {'msg': f'password change ticket code sent by email {email_address}'}, 200)
