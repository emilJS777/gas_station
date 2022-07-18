from .DeviceErrorModel import DeviceError
from typing import List
from datetime import datetime


# CREATE
def create(device_key: str, error_type: int, confirmed=False) -> DeviceError:
    device_error: DeviceError = DeviceError(device_key=device_key, error_type=error_type, confirmed=confirmed)
    device_error.last_update_info = datetime.utcnow()
    device_error.save_db()
    return device_error


# UPDATE
def update(device_key: str, error_type: int, confirmed: bool) -> DeviceError:
    device_error: DeviceError = DeviceError.query.filter_by(device_key=device_key).first()
    device_error.error_type = error_type
    device_error.confirmed = confirmed
    device_error.last_update_info = datetime.utcnow()
    device_error.update_db()
    return device_error


# DELETE
def delete(device_key: str) -> DeviceError:
    device_error: DeviceError = DeviceError.query.filter_by(device_key=device_key).first()
    device_error.delete_db()
    return device_error


# GET BY KEY
def get_by_key(device_key: str) -> DeviceError:
    device_error: DeviceError = DeviceError.query.filter_by(device_key=device_key).first()
    return device_error


# GET ALL
def get_all() -> List[dict]:
    devices_error: List[DeviceError] = DeviceError.query.filter_by(confirmed=True).all()

    devices_error_list: List[dict] = []
    for device_error in devices_error:
        devices_error_list.append({'id': device_error.id, 'device_key': device_error.device_key,
                                   'creation_date': device_error.creation_date, 'error_type': device_error.error_type,
                                   'last_update_info': device_error.last_update_info})

    return devices_error_list
