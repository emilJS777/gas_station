from . import client_user_service_db
from src.User import user_service_db
from src.Client import client_service_db
from src._response import response
from flask import g


# GET USER IDS BY CLIENT ID
def get_user_ids_by_client_id(client_id):
    # GET ALL USERS WHICH CREATE USER
    user_ids = client_user_service_db.get_user_ids_by_client_id_creator_id(client_id=client_id, creator_id=g.user_id)
    return response(True, user_ids, 200)


# BIND CLIENT USER
def bind_client_user(client_id, user_id):
    #  IF ONE OF THEM DOES NOT EXIST RETURN NOT FOUND
    if not client_service_db.get_by_id_creator_id(client_id=client_id, creator_id=g.user_id) \
            or not user_service_db.get_by_id_creator_id(user_id=user_id, creator_id=g.user_id):
        return response(False, {'msg': 'Client or/and User not found'}, 404)

    # IF THE USER HAS SUCH CLIENT ID RETURN ANSWER ABOUT THE EXISTENCE OF THIS RECORD
    if client_user_service_db.get_by_user_id_client_id(user_id=user_id, client_id=client_id):
        return response(False, {'msg': 'this Client has such User'}, 409)

    #  ELSE BIND USER CLIENT ID
    client_user_service_db.create_bind(client_id=client_id, user_id=user_id)
    return response(True, {'msg': 'Client User successfully linked'}, 200)


# UNBIND CLIENT USER
def unbind_client_user(client_id, user_id):
    #  IF ONE OF THEM DOES NOT EXIST RETURN NOT FOUND
    if not client_service_db.get_by_id_creator_id(client_id=client_id, creator_id=g.user_id) \
            or not user_service_db.get_by_id_creator_id(user_id=user_id, creator_id=g.user_id):
        return response(False, {'msg': 'Client or/and User not found'}, 404)

    # IF THE USER DOESN'T HAVE SUCH CLIENT ID, RETURN AN ANSWER ABOUT THE ABSENCE OF THIS RECORD
    if not client_user_service_db.get_by_user_id_client_id(user_id=user_id, client_id=client_id):
        return response(False, {'msg': 'the Client does not have such a User'}, 409)

    # GET USER BY ID AND REMOVE BIND ON CLIENT
    client_user_service_db.delete_bind(client_id=client_id, user_id=user_id)
    return response(True, {'msg': 'Client User link successfully deleted'}, 200)
