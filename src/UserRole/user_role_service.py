from . import user_role_service_db
from src.User import user_service_db
from src.Role import role_service_db
from src._response import response
from typing import List
from flask import g


def create_bind(user_id: int, role_id: int):
    if not user_service_db.get_by_id(user_id=user_id) or not role_service_db.get_role_by_id(role_id=role_id):
        return response(False, {'msg': 'User or Role not found'}, 404)

    user_role_service_db.create_bind(user_id=user_id, role_id=role_id)
    return response(True, {'msg': 'User Role successfully bind'}, 200)


def delete_bind(user_id: int, role_id: int):
    if g.user_id == user_id:
        return response(False, {'msg': 'you cant change your role'}, 403)

    if not user_role_service_db.get_by_user_id_role_id(user_id=user_id, role_id=role_id):
        return response(False, {'msg': 'User or Role not found'}, 404)

    user_role_service_db.delete_bind(user_id=user_id, role_id=role_id)
    return response(True, {'msg': 'User Role bind successfully deleted'}, 200)


def get_roles_by_user_id(user_id: int):
    role_list: List[dict] = []

    for role_id in user_role_service_db.get_role_ids_by_user_id(user_id=user_id):
        role: role_service_db.Role = role_service_db.get_role_by_id(role_id)
        role_list.append({'id': role.id, 'name': role.name})

    return response(True, role_list, 200)
