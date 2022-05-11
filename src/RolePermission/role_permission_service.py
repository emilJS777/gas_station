from . import role_permission_service_db
from src.UserRole import user_role_service_db
from src.Role import role_service_db
from src.Permission import permission_service_db
from src._response import response
from flask import g


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
    if user_role_service_db.get_by_user_id_role_id(user_id=g.user_id, role_id=role_id):
        return response(False, {'msg': 'you cant change your resolution'}, 403)

    # GET BY ROLE ID AND PERMISSION ID AND VERFY IF NOT FOUND RETURN NOT FOUND
    if not role_permission_service_db.get_by_role_id_permission_id(role_id, permission_id):
        return response(False, {'msg': 'bind not found'}, 404)

    # ELSE DELETE BIND AND RETURN OK
    role_permission_service_db.delete_bind(role_id=role_id, permission_id=permission_id)
    return response(True, {'msg': 'bind successfully deleted'}, 200)


# GET PERMISSIONS BY ROLE ID
def get_permissions_by_role_id(role_id):
    permissions = []
    for permission_id in role_permission_service_db.get_permission_ids_by_role_id(role_id=role_id):
        permission = permission_service_db.get_by_id(permission_id)
        permissions.append({'id': permission.id, 'name': permission.name, 'title': permission.title})

    return response(True, permissions, 200)
