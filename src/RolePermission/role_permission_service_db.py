from .role_permission_model import RolePermission
from typing import List


# CREATE BIND
def create_bind(role_id: int, permission_id: int) -> RolePermission:
    role_permission: RolePermission = RolePermission(role_id=role_id, permission_id=permission_id)
    role_permission.save_db()
    return role_permission


# DELETE BIND
def delete_bind(role_id: int, permission_id: int) -> RolePermission:
    role_permission: RolePermission = RolePermission.query.filter_by(role_id=role_id, permission_id=permission_id).first()
    role_permission.delete_db()
    return role_permission


# GET PERMISSION IDS BY ROLE ID
def get_permission_ids_by_role_id(role_id: int) -> List[int]:
    role_permission_list: List[RolePermission] = RolePermission.query.filter_by(role_id=role_id).all()
    permission_ids: List[int] = []
    for role_permission in role_permission_list:
        permission_ids.append(role_permission.permission_id)
    return permission_ids


# GET BY ROLE ID PERMISSION ID
def get_by_role_id_permission_id(role_id: int, permission_id: int) -> RolePermission:
    role_permission: RolePermission = RolePermission.query.filter_by(role_id=role_id, permission_id=permission_id).first()
    return role_permission
