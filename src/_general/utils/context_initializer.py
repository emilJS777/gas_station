from src import logger
from src.Permission import permission_service_db
from src.Role import role_service_db
from src.User import user_service_db
from src.RolePermission import role_permission_service_db
from src.UserRole import user_role_service_db
from flask import g
import time
from typing import List
from src.DeviceInfo.device_info_model import DeviceInfo
from src.DeviceError import DeviceErrorServiceDb
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from src.Client import client_service_db
from src.ClientUser import client_user_service_db

from sqlalchemy import text, select
from src import app


# DEVICE ERROR TIMER
class DeviceErrorThread:
    # SELECTS
    get_devices = "SELECT `key`, `error_after_minutes` FROM `device`"
    get_device_info = "SELECT last_update FROM device_info WHERE device_key = %s"
    get_device_error = "SELECT error_type, confirmed FROM device_error WHERE device_key = %s"
    # CHECK EXIST
    exist_device_error = "SELECT EXISTS(SELECT * FROM device_error WHERE device_key = %s)"
    # CREATE
    create_device_error = "INSERT INTO device_error (device_key, last_update_info, creation_date, error_type, confirmed) VALUES (%s, %s, %s, %s, %s)"
    # UPDATE
    update_device_error = "UPDATE device_error SET `creation_date` = %s, `error_type` = 1, `confirmed` = 1 WHERE device_key = %s"

    def __init__(self):

        while True:
            db = create_engine(app.config["SQLALCHEMY_DATABASE_URI"], echo=False)
            con = db.connect()

            for device in con.execute(self.get_devices):
                device_key: str = device.key

                for device_info in con.execute(self.get_device_info, (device_key, )):

                    if datetime.utcnow() > device_info.last_update + timedelta(minutes=device.error_after_minutes):

                        for row in con.execute(self.exist_device_error, (device_key, )):

                            if not row[0]:
                                con.execute(self.create_device_error, (device_key, device_info.last_update, datetime.utcnow(), 1, True))
                                print("error", device_key, 'saved')

                            else:
                                for device_error in con.execute(self.get_device_error, (device_key, )):
                                    if device_error.error_type == 0:
                                        con.execute(self.update_device_error, (datetime.utcnow(), device_key, ))



            con.close()
            time.sleep(10)


# INITIALIZER
class Initializer:
    permissions: List = [{'name': 'client_get', 'title': 'ստանալ հաճախորդներ'}, {'name': 'client_edit', 'title': 'խմբագրել հաճախորդներին'},
                         {'name': 'user_get', 'title': 'ստանալ օգտվողներին'}, {'name': 'user_edit', 'title': 'խմբագրել օգտվողներին'},
                         # {'name': 'firm_get', 'title': 'get Firm'}, {'name': 'firm_edit', 'title': 'redactor Firm'},
                         {'name': 'role_get', 'title': 'ստանալ դերեր'}, {'name': 'role_edit', 'title': 'խմբագրել դերերը'},
                         {'name': 'device_get', 'title': 'ստանալ սարքեր'}, {'name': 'device_edit', 'title': 'խմբագրել սարքերը'},
                         {'name': 'cash_box_get', 'title': 'ստանալ դրամարկղերը'}, {'name': 'cash_box_edit', 'title': 'խմբագրել դրամարկղերը'},
                         {'name': 'station_get', 'title': 'ստանալ կայանի սարքեր'}, {'name': 'station_edit', 'title': 'խմբագրել կայանի սարքերը'},
                         {'name': 'expense_get', 'title': 'ստանալ ծախսերը'}, {'name': 'expense_edit', 'title': 'խմբագրել ծախսերը'},
                         {'name': 'cash_box_data_get', 'title': 'ստանալ դրամարկղի տվյալները'}, {'name': 'cash_box_data_edit', 'title': 'խմբագրել դրամարկղի տվյալները'}]
    role: str = "admin"

    def __init__(self):
        self.init_permission()
        self.init_role()
        self.init_role_permission()
        client: client_service_db.Client = self.init_client()
        self.init_user(client=client)

    def init_permission(self):
        for permission in self.permissions:
            if not permission_service_db.get_by_name(permission_name=permission['name']):
                permission_service_db.create(permission_name=permission['name'], permission_title=permission['title'])
                logger.info(f"permission {permission['title']} created")

    def init_role(self):
        if not role_service_db.get_role_by_name(name=self.role):
            role_service_db.create_role(name=self.role)
            logger.info(f"Role by name {self.role} created")

    def init_role_permission(self):
        role_db: role_service_db.Role = role_service_db.get_role_by_name(name=self.role)
        permission_ids = []

        for permission in self.permissions:
            permission_db: permission_service_db.Permission = permission_service_db.get_by_name(permission_name=permission['name'])
            permission_ids.append(permission_db.id)
            if not role_permission_service_db.get_by_role_id_permission_id(role_id=role_db.id, permission_id=permission_db.id):
                role_permission_service_db.create_bind(role_id=role_db.id, permission_ids=permission_ids)
                logger.info(f"Role {role_db.name} and permission {permission_db.name} bind")

    def init_client(self):
        if not client_service_db.get_first():
            return client_service_db.create(
                client_name="admin",
                client_description="admin",
                creator_id=None
            )
        return client_service_db.get_first()

    def init_user(self, client):
        if not user_service_db.get_first_by_creator_id(creator_id=None):
            user: user_service_db.User = user_service_db.create_ticket(client_id=client.id, first_name="Admin", last_name="Admin")
            logger.info(f"first admin ticket {user.ticket}")

            user_role_service_db.create_bind(user_id=user.id, role_id=role_service_db.get_role_by_name(name=self.role).id)







# class Initializer:
#     permissions = [{'name': 'client_get', 'title': 'get clients'}, {'name': 'client_edit', 'title': 'redactor Client'},
#                    {'name': 'user_get', 'title': 'get User'}, {'name': 'user_edit', 'title': 'redactor User'},
#                    {'name': 'firm_get', 'title': 'get Firm'}, {'name': 'firm_edit', 'title': 'redactor Firm'},
#                    {'name': 'role_edit'}]
#
#     first_role = ["admin"]
#
#     def __init__(self):
#         user_ticket = self.first_ticket_initializer()
#         for Permission in self.permissions:
#             init_permission = self.permission_initializer(Permission=Permission)
#             self.ticket_permission_initializer(ticket=user_ticket, Permission=init_permission)
#
#     # PERMISSIONS INITIALIZER
#     @staticmethod
#     def permission_initializer(Permission):
#         permission_from_db = permission_service_db.get_by_name(permission_name=Permission['name'])
#
#         if not permission_from_db:
#             return permission_service_db.create(permission_name=Permission['name'],
#                                                 permission_title=Permission['title'])
#
#         if not permission_from_db.title == Permission['title']:
#             return permission_service_db.update(permission_id=permission_from_db.id,
#                                                 permission_name=permission_from_db.name,
#                                                 permission_title=Permission['title'])
#         return permission_from_db
#
#     # FIRST TICKET INITIALIZER
#     @staticmethod
#     def first_ticket_initializer():
#         ticket = user_service_db.get_first_by_creator_id(creator_id=None)
#         if not ticket:
#             new_ticket = user_service_db.create_ticket(creator_id=None)
#             logger.info(f"first ticket {Fore.RED + new_ticket.ticket + Fore.RESET}")
#             return new_ticket
#
#         else:
#             return ticket
#
#     # TICKET AND PERMISSION INITIALIZER
#     @staticmethod
#     def ticket_permission_initializer(ticket, Permission):
#         if not user_permission_service_db.get_by_user_id_permission_id(user_id=ticket.id, permission_id=Permission.id):
#             user_permission_service_db.create_bind(user_id=ticket.id, permission_id=Permission.id)
#             logger.info(f"User or ticket by id {ticket.id} and Permission by name {Permission.name} bind!")


# v.0.1
# class Initializer:
#     Role = {"name": "super_admin"}
#     permissions = ["create_client", "get_client_by_id", "get_clients", "update_client", "delete_client",
#                    "get_user_ids_by_client_id", "bind_client_user", "unbind_client_user",
#                    "create_firm", "get_firm_by_id", "get_firms", "update_firm", "delete_firm",
#                    "get_user_ids_by_firm_id", "bind_firm_user", "unbind_firm_user",
#                    # "create_permission", "update_permission", "delete_permission",
#                    "create_role", "get_role_by_id", "get_roles", "update_role", "delete_role",
#                    "get_permission_ids_by_role_id", "bind_role_permission", "unbind_role_permission",
#                    "create_user", "create_user_ticket", "get_user_by_id", "get_users", "update_user", "delete_user",
#                    "get_role_ids_by_user_id", "bind_user_role", "unbind_user_role",
#                    "create_employee", "update_employee", "delete_employee", "get_employee_by_id", "get_employees"]
#
#     def __init__(self):
#         # CHECK OR CREATE FIRST ROLE
#         Role = self.init_first_role(role_name=self.Role["name"])
#
#         # CHECK OR CREATE PERMISSIONS AND CHECK OR BIND ROLE PERMISSION
#         for permission_name in self.permissions:
#             Permission = self.init_permission(permission_name=permission_name)
#             self.init_role_permission(role_id=Role.id, permission_id=Permission.id)
#
#         # CHECK OR CREATE FIRST ADMIN
#         User = self.init_first_admin()
#
#         # CHECK OR CREATE BIND USER ROLE
#         self.init_user_role(user_id=User.id, role_id=Role.id)
#
#     @staticmethod
#     def init_first_admin():
#         # CHECK OR CREATE FIRST ADMIN
#         User = user_service_db.create_ticket(creator_id=None)
#         logger.info(f"first ticket {Fore.BLUE + User.ticket + Fore.RESET} created")
#         return User
#
#     @staticmethod
#     def init_first_role(role_name):
#         # CHECK OR CREATE FIRST ROLE
#         Role = role_service_db.get_by_name(name=role_name) or \
#                role_service_db.create(name=role_name, creator_id=None)
#         logger.info(f"first Role {Role.name} created")
#         return Role
#
#     @staticmethod
#     def init_user_role(user_id, role_id):
#         # CHECK OR CREATE USER ROLE BIND
#         UserRole = user_role_service_db.get_by_user_id_role_id(user_id=user_id, role_id=role_id) or \
#                     user_role_service_db.create_bind(user_id=user_id, role_id=role_id)
#         return UserRole
#
#     @staticmethod
#     def init_permission(permission_name):
#         # CHECK OR CREATE PERMISSION
#         Permission = permission_service_db.get_by_name(permission_name=permission_name) or \
#                      permission_service_db.create(permission_name=permission_name)
#         logger.info(f"Permission {Permission.name} created")
#         return Permission
#
#     @staticmethod
#     def init_role_permission(role_id, permission_id):
#         # CHECK OR CREATE ROLE PERMISSION BIND
#         RolePermission = role_permission_service_db.get_by_role_id_permission_id(role_id=role_id, permission_id=permission_id) or \
#                           role_permission_service_db.create_bind(role_id=role_id, permission_id=permission_id)
#         return RolePermission
