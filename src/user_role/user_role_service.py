from . import user_role_service_db
from src.user import user_service_db
from src.role import role_service_db
from src._response import response
from typing import List


def create_bind(user_id: int, role_id: int):
    if not user_service_db.get_by_id(user_id=user_id) or not role_service_db.get_role_by_id(role_id=role_id):
        return response(False, {'msg': 'user or role not found'}, 404)

    user_role_service_db.create_bind(user_id=user_id, role_id=role_id)
    return response(True, {'msg': 'user role successfully bind'}, 200)


def delete_bind(user_id: int, role_id: int):
    if not user_role_service_db.get_by_user_id_role_id(user_id=user_id, role_id=role_id):
        return response(False, {'msg': 'user or role not found'}, 404)

    user_role_service_db.delete_bind(user_id=user_id, role_id=role_id)
    return response(True, {'msg': 'user role bind successfully deleted'}, 200)


def get_role_ids_by_user_id(user_id: int):
    role_ids: List[int] = user_role_service_db.get_role_ids_by_user_id(user_id=user_id)
    return response(True, role_ids, 200)
