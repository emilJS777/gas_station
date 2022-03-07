from functools import wraps
from src._response import response
from . import permission_service_db
from .permission_service_db import Permission
from src.role import role_service_db
from src.role_permission import role_permission_service_db
from src.user_role import user_role_service_db
from flask import g
from typing import List


# CHECK PERMISSION
def check_permission(allowed_permission: str):
    def decoration(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            for role_id in user_role_service_db.get_role_ids_by_user_id(user_id=g.user_id):

                for permission_id in role_permission_service_db.get_permission_ids_by_role_id(role_id=role_id):

                    permission: Permission = permission_service_db.get_by_id(permission_id=permission_id)

                    if allowed_permission == permission.name:
                        return f(*args, **kwargs)

            return response(False, {'msg': 'forbidden'}, 403)
        return decorated_function
    return decoration
