from src.ClientUser import client_user_service_db
from src.CashBox import CashBoxServiceDb
from . import user_service_db
from src._response import response
from src.Role import role_service_db
from src.UserRole import user_role_service_db
from flask import g


# CREATE NEW USER
def create_user(ticket: str, user_name: str, password: str):
    # IF TICKET NOT FOUND RETURN NOT FOUND
    if not user_service_db.get_by_ticket(ticket=ticket):
        return response(False, {'msg': 'ticket not found'}, 200)

    # # IF EMAIL EXIST RETURN CONFLICT
    # if user_service_db.get_by_email_address(email_address):
    #     return response(False, {'email address exist'}, 200)

    # IF FIND THIS USERNAME RETURN RESPONSE CONFLICT
    if user_service_db.get_by_name(name=user_name):
        return response(False, {'msg': 'User name is taken'}, 200)

    # ELSE USER BY THIS NAME SAVE
    new_user = user_service_db.create(
        ticket=ticket,
        name=user_name,
        password=password,
    )
    return response(True, {'msg': 'new User by id {} successfully created'.format(new_user.id)}, 200)


# CREATE USER TICKET
def create_user_ticket(creator_id, client_id, first_name: str, last_name: str, cash_box_id: int, cashier: bool):
    # GET CASH BOX BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if cash_box_id and not CashBoxServiceDb.get_by_id(cash_box_id):
        return response(False, {'msg': 'cash box not found'}, 200)

    # CREATE USER AND VERIFY IF CREATOR TIED TO CLIENT means to bind the new User too
    user = user_service_db.create_ticket(creator_id=creator_id,
                                         first_name=first_name,
                                         last_name=last_name,
                                         cash_box_id=cash_box_id,
                                         cashier=cashier)

    # IF CLIENT ID EXIST BIND NEW USER AND CLIENT ID
    if client_id:
        client_user_service_db.create_bind(client_id=client_id, user_id=user.id)

    return response(True, {'id': user.id, 'ticket': user.ticket}, 200)


# USER GET BY ID
def user_get_by_id(user_id):
    # ELSE IF CLIENT ID EXIST RETURN ALL USERS BY CLIENT ID
    user = user_service_db.get_by_id(user_id=user_id)

    # # ELSE RETURN ALL USERS BY CREATOR ID
    # else:
    #     User = user_service_db.get_by_id_creator_id(user_id=user_id, creator_id=g.user_id)

    # IF USER NOT FOUND RETURN NOT FOUND
    if not user:
        return response(False, {'msg': 'User by this id not found'}, 200)

    # ELSE RETURN THIS USER AND STATUS OK
    return response(True, {'id': user.id,
                           'name': user.name,
                           'first_name': user.first_name,
                           'last_name': user.last_name,
                           'cash_box_id': user.cash_box_id,
                           'cashier': user.cashier,
                           'ticket': user.ticket,
                           'creation_date': user.creation_date}, 200)


# GET ALL USER
def user_get_all(page: int, per_page: int, client_id: int):
    users: dict = user_service_db.get_all(page=page, per_page=per_page, client_id=client_id)
    for user, index in enumerate(users['items']):
        print(user, index)
        users['items'][index]['roles'] = []
        for role_id in user_role_service_db.get_role_ids_by_user_id(user.id):
            users['items'][index].roles.append(role_service_db.get_role_by_id(role_id).name)

    return response(True, users, 200)


# UPDATE USER
def user_update(user_id: int, first_name: str, last_name: str, cash_box_id: int, cashier: bool):
    # GET CASH BOX BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if cash_box_id and not CashBoxServiceDb.get_by_id(cash_box_id):
        return response(False, {'msg': 'cash box not found'}, 200)

    # GET USER BY ID AND VERIFY DOES IT EXIST. IF NO RETURN NOT FOUND
    user = user_service_db.get_by_id(user_id=user_id)
    if not user:
        return response(False, {'msg': 'User by this id not found'}, 200)

    # ELSE CHANGE AND UPDATE DB AND RETURN RESPONSE OK
    user_service_db.update(user_id=user_id,
                           first_name=first_name,
                           last_name=last_name,
                           cash_box_id=cash_box_id,
                           cashier=cashier)
    return response(True, {'msg': 'User successfully update'}, 200)


# DELETE USER BY ID CLIENT ID
def user_delete(user_id):
    # IF CLIENT EXIST FIND USER BY ID AND THIS CLIENT ID
    # GET AND VERIFY IF CLiENT AND USER BY ID NOT FOUND RETURN NOT FOUND
    if not user_service_db.get_by_id(user_id=user_id):
        return response(False, {'msg': 'User not found'}, 200)

    # REMOVE THIS USER FROM DB AND THIS USER AND PERMISSION BIND
    user_service_db.delete(user_id=user_id)
    return response(True, {'msg': "this User successfully deleted"}, 200)
