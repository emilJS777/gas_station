from . import role_service_db
from src._response import response
from src.RolePermission import role_permission_service_db
from src.UserRole import user_role_service_db
from src._general.parents import get_array_items


# CREATE ROLE
def create_role(name: str, permission_ids: list):
    # GET ROLE BY THIS NAME AND VERIFY IF EXIST RETURN NOT FOUND
    if role_service_db.get_role_by_name(name=name):
        return response(False, {'msg': 'Role by this name exist'}, 200)

    # ELSE CREATE NEW ROLE AND RETURN OK
    role = role_service_db.create_role(name=name)
    role_permission_service_db.create_bind(role_id=role.id, permission_ids=permission_ids)
    return response(True, {'id': role.id, 'name': role.name}, 200)


# UPDATE ROLE
def update_role(role_id, name, permission_ids: list):
    # GET ROLE BY THIS NAME AND VERIFY IF EXIST RETURN NOT FOUND
    if role_service_db.get_role_by_name_exclude_id(name=name, role_id=role_id):
        return response(False, {'msg': 'Role by this name exist'}, 200)

    # ELSE UPDATE ROLE AND RETURN OK
    role = role_service_db.update_role(role_id=role_id, name=name)
    role_permission_service_db.create_bind(role_id=role.id, permission_ids=permission_ids)
    return response(True, {'msg': 'role successfully updated'}, 200)


# GET ROLE BY ID
def get_role_by_id(role_id: int):
    # GET ROLE AND VERIFY IF NOT FOUND RETURN NOT FOUND
    role: role_service_db.Role = role_service_db.get_role_by_id(role_id=role_id)
    if not role:
        return response(False, {'msg': 'Role not found'}, 200)

    # ELSE RETURN ROLE FIELDS AND OK
    return response(True, {'id': role.id, 'name': role.name}, 200)


# GET ROLES
def get_roles():
    roles = role_service_db.get_roles()
    roles_list: list[dict] = []

    for role in roles:
        users: list = user_role_service_db.get_user_ids_by_role_id(role.id)
        roles_list.append({'id': role.id, 'name': role.name, 'users': len(users), 'permissions': get_array_items(role.permissions)})

    return response(True, roles_list, 200)


# DELETE ROLE
def delete_role(role_id):
    # GET ROLE BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not role_service_db.get_role_by_id(role_id=role_id):
        return response(False, {'msg': 'Role by this id not found'}, 200)

    role_permission_service_db.delete_all_by_role_id(role_id)

    # ELSE DELETE ROLE AND RETURN OK
    role_service_db.delete_role(role_id=role_id)
    return response(True, {'msg': 'Role successfully deleted'}, 200)
