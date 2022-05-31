from .role_permission_model import RolePermission
from typing import List
from src.Role.role_model import Role
from src.Permission.permission_model import Permission


# CREATE BIND
def create_bind(role_id: int, permission_ids: list):
    role: Role = Role.query.filter_by(id=role_id).first()
    permissions = Permission.query.filter(Permission.id.in_(permission_ids)).all()
    role.permissions = permissions
    role.update_db()


# # DELETE BIND
# def delete_bind(role_id: int, permission_id: int) -> RolePermission:
#     role_permission: RolePermission = RolePermission.query.filter_by(role_id=role_id, permission_id=permission_id).first()
#     role_permission.delete_db()
#     return role_permission


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


# DELETE ALL BY ROLE ID
def delete_all_by_role_id(role_id):
    role_permission: List[RolePermission] = RolePermission.query.filter_by(role_id=role_id).all()

    for r_p in role_permission:
        r_p.delete_db()
