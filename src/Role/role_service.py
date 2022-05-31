from . import role_service_db
from src._response import response
from src.RolePermission import role_permission_service_db

# CREATE ROLE
def create_role(name: str):
    # GET ROLE BY THIS NAME AND VERIFY IF EXIST RETURN NOT FOUND
    if role_service_db.get_role_by_name(name=name):
        return response(False, {'msg': 'Role by this name exist'}, 409)

    # ELSE CREATE NEW ROLE AND RETURN OK
    role = role_service_db.create_role(name=name)
    return response(True, {'id': role.id, 'name': role.name}, 200)


# UPDATE ROLE
def update_role(role_id, name):
    # GET ROLE BY THIS NAME AND VERIFY IF EXIST RETURN NOT FOUND
    if role_service_db.get_role_by_name(name=name):
        return response(False, {'msg': 'Role by this name exist'}, 409)

    # ELSE UPDATE ROLE AND RETURN OK
    role = role_service_db.update_role(role_id=role_id, name=name)
    return response(True, {'msg': 'role successfully updated'}, 200)


# GET ROLE BY ID
def get_role_by_id(role_id: int):
    # GET ROLE AND VERIFY IF NOT FOUND RETURN NOT FOUND
    role: role_service_db.Role = role_service_db.get_role_by_id(role_id=role_id)
    if not role:
        return response(False, {'msg': 'Role not found'}, 404)

    # ELSE RETURN ROLE FIELDS AND OK
    return response(True, {'id': role.id, 'name': role.name}, 200)


# GET ROLES
def get_roles():
    roles = role_service_db.get_roles()
    return response(True, roles, 200)


# DELETE ROLE
def delete_role(role_id):
    # GET ROLE BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not role_service_db.get_role_by_id(role_id=role_id):
        return response(False, {'msg': 'Role by this id not found'}, 404)

    role_permission_service_db.delete_all_by_role_id(role_id)

    # ELSE DELETE ROLE AND RETURN OK
    role_service_db.delete_role(role_id=role_id)
    return response(True, {'msg': 'Role successfully deleted'}, 200)
