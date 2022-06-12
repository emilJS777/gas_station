# from src.Firm import firm_service_db
from . import client_service_db
from src._response import response
from flask import g
from src.ClientDevice import ClientDeviceRepository


# CREATE NEW CLIENT
def client_create(client_name, client_description):
    # IF FIND THIS CLIENT NAME RETURN RESPONSE CONFLICT
    if client_service_db.get_by_name(client_name=client_name):
        return response(False, {'msg': 'Client name is taken'}, 200)

    # ELSE CLIENT BY THIS NAME SAVE
    new_client = client_service_db.create(client_name=client_name,
                                          client_description=client_description,
                                          creator_id=g.user_id,
                                          parent_id=g.client_id
                                          )
    return response(True, {'msg': 'new Client by id {} successfully created'.format(new_client.id)}, 200)


# CLIENT GET BY ID
def client_get_by_id(client_id):
    # GET CLIENT BY ID END VERIFY USER DOES IT EXIST. IF NO RETURN NOT FOUND
    client = client_service_db.get_by_id(client_id=client_id)
    if not client:
        return response(False, {'msg': 'Client by this id not found'}, 200)

    # ELSE RETURN THIS CLIENT AND STATUS OK
    return response(True, {'id': client.id, 'name': client.name, 'description': client.description, 'creation_date': client.creation_date}, 200)


# GET ALL CLIENT
def client_get_all(page: int, per_page: int):
    # GET ALL CLIENT IDS BY CREATOR ID
    client_list = client_service_db.get_all(
        page=page,
        per_page=per_page
    )
    return response(True, client_list, 200)


# UPDATE CLIENT
def client_update(client_id, client_name, client_description):
    # GET CLIENT BY ID AND VERIFY DOES IT EXIST. IF NO RETURN NOT FOUND
    if not client_service_db.get_by_id_creator_id(client_id=client_id, creator_id=g.user_id):
        return response(False, {'msg': 'Client by this id not found'}, 200)

    # IF CLIENT BY THIS NAME EXIST RETURN CONFLICT
    if client_service_db.get_by_name_exclude_id(client_id=client_id, name=client_name):
        return response(False, {'msg': 'Client by this name exist'}, 200)

    # ELSE CHANGE AND UPDATE DB, AND RETURN RESPONSE OK
    client_service_db.update(client_id=client_id, client_name=client_name, client_description=client_description)
    return response(True, {'msg': 'Client successfully update'}, 200)


# DELETE CLIENT BY ID
def client_delete(client_id):
    # GET CLIENT BY ID AND VERIFY DIES EXIST. IF NO RETURN NOT FOUND
    if not client_service_db.get_by_id(client_id=client_id):
        return response(False, {"msg": "Client by this id not found"}, 200)

    ClientDeviceRepository.delete_all_by_client_id(client_id)
    # REMOVE THIS CLIENT FROM DB
    client_service_db.delete(client_id=client_id)
    return response(True, {'msg': "this Client successfully deleted"}, 200)



