from . import device_info_service
from flask import request


def update_device_info() -> dict:
    res = device_info_service.update(device_info_body=request.args)
    return res


def get_device_info(device_key: str) -> dict:
    res = device_info_service.get_device_info(device_key)
    return res
