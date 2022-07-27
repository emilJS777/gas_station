from . import auth_service, auth_middleware
from flask import request
from flask_jwt_extended import jwt_required
from src.Client import client_middleware
from flask_expects_json import expects_json
from .auth_validator import resset_password_schema, request_resset_password_schema
from src.EmailSender.DeviceErrorSender import DeviceErrorSender


def login():
    req = request.get_json()
    res = auth_service.login(user_name=req['user_name'], password=req['password'])
    DeviceErrorSender().send()
    return res


@expects_json(resset_password_schema)
def resset_password() -> dict:
    req = request.get_json()
    res = auth_service.resset_password(ticket_code=req['ticket_code'], new_password=req['new_password'])
    return res


@expects_json(request_resset_password_schema)
def request_resset_password() -> dict:
    req = request.get_json()
    res = auth_service.request_resset_password(req['email_address'])
    return res


@jwt_required(refresh=True)
def refresh_token():
    res = auth_service.refresh_token()
    return res


@auth_middleware.check_authorize
@client_middleware.check_client(required=True)
def get_profile() -> dict:
    res: dict = auth_service.get_profile()
    return res
