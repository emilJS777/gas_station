from .role_model import Role
from flask import g
from typing import List


# CREATE ROLE
def create_role(name) -> Role:
    role: Role = Role(name)
    role.save_db()
    return role


# UPDATE ROLE
def update_role(role_id, name) -> Role:
    role: Role = Role.query.filter_by(id=role_id).first()
    role.name = name
    role.update_db()
    return role


# GET ROLE BY ID
def get_role_by_id(role_id: int) -> Role:
    role: Role = Role.query.filter_by(id=role_id).first()
    return role


# GET ROLE BY NAME
def get_role_by_name(name: str) -> Role:
    role: Role = Role.query.filter_by(name=name).first()
    return role


# GET ROLES
def get_roles() -> List:
    roles: List[Role] = Role.query.all()
    roles_list: List[dict] = []
    for role in roles:
        roles_list.append({'id': role.id, 'name': role.name})
    return roles_list


# DELETE ROLE
def delete_role(role_id) -> Role:
    role = Role.query.filter_by(id=role_id).first()
    role.delete_db()
    return role
