from . import auth_service, auth_middleware
from flask import request
from flask_jwt_extended import jwt_required


def login():
    req = request.get_json()
    res = auth_service.login(user_name=req['user_name'], password=req['password'])
    return res


@jwt_required(refresh=True)
def refresh_token():
    res = auth_service.refresh_token()
    return res


@auth_middleware.check_authorize
def get_profile() -> dict:
    res: dict = auth_service.get_profile()
    return res
