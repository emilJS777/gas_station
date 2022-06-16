from . import device_set_service
from flask import request
from src.Auth import auth_middleware


@auth_middleware.check_authorize
def update_device_set() -> dict:
    res = device_set_service.update(device_set_body=request.args)
    return res


def get_device_set(device_key: str) -> dict:
    res = device_set_service.get_device_set(device_key)
    return res
