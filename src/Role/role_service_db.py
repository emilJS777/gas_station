from .role_model import Role
from flask import g
from typing import List


# CREATE ROLE
def create_role(name) -> Role:
    role: Role = Role(name)
    role.creator_id = g.user_id
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


# EXCLUDE ID GET BY NAME
def get_role_by_name_exclude_id(name: str, role_id: int) -> Role:
    role: Role = Role.query.filter(Role.name == name, Role.id != role_id).first()
    return role


# GET ROLES
def get_roles() -> List:
    roles: List[Role] = Role.query.filter_by(creator_id=g.user_id).all()
    return roles


# DELETE ROLE
def delete_role(role_id) -> Role:
    role = Role.query.filter_by(id=role_id).first()
    role.delete_db()
    return role
