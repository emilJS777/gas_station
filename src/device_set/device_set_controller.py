from . import device_set_service
from flask import request


def update_device_set() -> dict:
    res = device_set_service.update(device_set_body=request.args)
    return res


def get_device_set(device_key: str) -> dict:
    res = device_set_service.get_device_set(device_key)
    return res
