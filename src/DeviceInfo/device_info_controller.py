import json

from . import device_info_service
from flask import request
from src.DeviceError import DeviceErrorService


def update_device_info() -> dict:
    data = json.loads(request.args["data"])
    res: dict = device_info_service.update(device_key=request.args["Id"], device_info_body=data)
    DeviceErrorService.check_device_null_error(request.args["Id"], request.args["data"])
    return res


def get_device_info(device_key: str) -> dict:
    res = device_info_service.get_device_info(device_key)
    return res
