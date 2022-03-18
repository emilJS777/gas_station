from . import role_permission_service_db
from src.Role import role_service_db
from src.Permission import permission_service_db
from src._response import response


# CREATE BIND
def create_bind(role_id: int, permission_id: int):
    # GET ROLE AND PERMISSION BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not role_service_db.get_role_by_id(role_id=role_id) or not permission_service_db.get_by_id(permission_id=permission_id):
        return response(False, {'msg': 'Role or Permission not found'}, 404)

    # ELSE CREATE NEW ROLE PERMISSION BIND AND RETURN OK
    role_permission_service_db.create_bind(role_id=role_id, permission_id=permission_id)
    return response(True, {'msg': 'bind successfully created'}, 200)


# DELETE BIND
def delete_bind(role_id: int, permission_id: id):
    # GET BY ROLE ID AND PERMISSION ID AND VERFY IF NOT FOUND RETURN NOT FOUND
    if not role_permission_service_db.get_by_role_id_permission_id(role_id, permission_id):
        return response(False, {'msg': 'bind not found'}, 404)

    # ELSE DELETE BIND AND RETURN OK
    role_permission_service_db.delete_bind(role_id=role_id, permission_id=permission_id)
    return response(True, {'msg': 'bind successfully deleted'}, 200)


# GET PERMISSION IDS BY ROLE ID
def get_permission_ids_by_role_id(role_id):
    permission_ids = role_permission_service_db.get_permission_ids_by_role_id(role_id=role_id)
    return response(True, permission_ids, 200)
