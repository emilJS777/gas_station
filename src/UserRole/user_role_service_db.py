from .user_role_model import UserRole
from typing import List


def create_bind(user_id: int, role_id: int) -> UserRole:
    user_role: UserRole = UserRole(user_id=user_id, role_id=role_id)
    user_role.save_db()
    return user_role


def delete_bind(user_id: int, role_id: int) -> UserRole:
    user_role: UserRole = UserRole.query.filter_by(user_id=user_id, role_id=role_id).first()
    user_role.delete_db()
    return user_role


def get_role_ids_by_user_id(user_id: int):
    user_roles: List[UserRole] = UserRole.query.filter_by(user_id=user_id).all()
    role_ids: List[int] = []
    for user_role in user_roles:
        role_ids.append(user_role.role_id)

    return role_ids


def get_by_user_id_role_id(user_id: int, role_id: int) -> UserRole:
    user_role: UserRole = UserRole.query.filter_by(user_id=user_id, role_id=role_id).first()
    return user_role
