from . import permission_service_db
from src.Role import role_service_db
from src.RolePermission import role_permission_service_db
from src.UserRole import user_role_service_db
from src._response import response
from flask import g
from typing import List


# # CREATE NEW PERMISSION SERVICE
# def permission_create(permission_name):
#     # IF FIND THIS PERMISSION NAME RETURN RESPONSE CONFLICT
#     if permission_service_db.get_by_name(permission_name):
#         return response(False, {'msg': 'Permission name is taken'}, 409)
#
#     # ELSE PERMISSION BY THIS NAME SAVE
#     permission_service_db.create(permission_name)
#     return response(True, {'msg': 'new Permission successfully created'}, 200)
#
#
# # GET PERMISSION BY ID
# def permission_get_by_id(permission_id):
#     # GET PERMISSION BY ID END VERIFY DOES IT EXIST. IF NO RETURN NOT FOUND
#     Permission = permission_service_db.get_by_id(permission_id)
#     if not Permission:
#         return response(False, {'msg': 'Permission by this id not found'}, 404)
#
#     # ELSE RETURN THIS PERMISSION AND STATUS OK
#     return response(True, {'id': Permission.id, 'name': Permission.name}, 200)


# # GET ALL IDS PERMISSION
# def permission_get_all_ids():
#     # GET AND RETURN ALL PERMISSION IDS BY USER ID
#     permission_ids = []
#     for role_id in user_role_service_db.get_role_ids_by_user_id(user_id=g.user_id):
#         for permission_id in role_permission_service_db.get_permission_ids_by_role_id(role_id=role_id):
#             permission_ids.append(permission_id)
#
#     return response(True, permission_ids, 200)


# GET ALL PERMISSION
def permission_get_all(user_id):
    # GET AND RETURN ALL PERMISSION IDS BY USER ID
    permission_list: List[dict] = []
    for role_id in user_role_service_db.get_role_ids_by_user_id(user_id=user_id):
        for permission_id in role_permission_service_db.get_permission_ids_by_role_id(role_id=role_id):
            permission: permission_service_db.Permission = permission_service_db.get_by_id(permission_id=permission_id)
            permission_list.append({'id': permission.id, 'name': permission.name})

    return response(True, permission_list, 200)


# # UPDATE PERMISSION
# def permission_update(permission_id, permission_name):
#     # GET PERMISSION BY ID AND VERIFY DOES IT EXIST IF NO RETURN NOT FOUND
#     if not permission_service_db.get_by_id(permission_id):
#         return response(False, {'msg': 'Permission by this id not found'}, 404)
#
#     # ELSE CHANGE AND UPDATE DB
#     # AND RETURN RESPONSE OK
#     permission_service_db.update(permission_id, permission_name)
#     return response(True, {'msg': 'Permission successfully update'}, 200)
#
#
# # DELETE PERMISSION BY ID
# def permission_delete(permission_id):
#     # GET PERMISSION BY ID AND VERIFY DIES EXIST IF NO RETURN NOT FOUND
#     if not permission_service_db.get_by_id(permission_id):
#         return response(False, {"msg": "Permission by this id not found"}, 404)
#
#     # ELSE REMOVE THIS PERMISSION AND ROLE PERMISSION LINKS FROM DB
#     role_permission_service_db.delete_all_by_permission_id(permission_id)
#     permission_service_db.delete(permission_id)
#     return response(True, {'msg': "this Permission successfully deleted"}, 200)

