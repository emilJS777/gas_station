from . import device_service_db
from src.DeviceInfo import device_info_service_db
from src.DeviceSet import device_set_service_db
from src.Client import client_service_db
from src.CashBox import CashBoxServiceDb
from src._response import response
from typing import List


# CREATE DEVICE
def create_device(key: str, name: str, description: str, error_after_minutes: int, client_id: int) -> dict:
    # GET CLIENT AND CASH BOX IF NOT FOUND RETURN NOT FOUND
    if not client_service_db.get_by_id(client_id=client_id):
        return response(False, {'msg': 'client and/or cash box not found'}, 404)

    if device_service_db.get_device_by_key(key=key):
        return response(False, {'msg': 'Device by this key exist'}, 409)

    # CREATE DEVICE AND DEVICE INFO IF DEVICE INFO BY THIS KEY NOT FOUND
    device = device_service_db.create_device(
        key=key,
        name=name,
        description=description,
        error_after_minutes=error_after_minutes,
        client_id=client_id
    )
    device_info_service_db.create(device_key=device.key)
    device_set_service_db.create(device_key=device.key)
    return response(True, {'id': device.id,
                           'key': device.key,
                           'name': device.name,
                           'client_id': device.client_id}, 200)


# UPDATE DEVICE
def update_device(device_id: int, key: str, name: str, description: str, error_after_minutes: int, parent_key: str) -> dict:
    old_key: str = device_service_db.get_device_by_id(device_id=device_id).key
    if not old_key:
        return response(False, {'msg': 'Device not found'}, 404)

    if device_service_db.get_by_key_exclude_id(device_id=device_id, key=key):
        return response(False, {'msg': 'Device by this key exist'}, 409)

    device = device_service_db.update_device(device_id=device_id, key=key, name=name,
                                             description=description, error_after_minutes=error_after_minutes,
                                             parent_key=parent_key)
    # UPDATE DEVICE INFO AND SET KEY HERE
    device_set_service_db.update_device_key(device_key_old=old_key, device_key_new=device.key)
    device_info_service_db.update_device_key(device_key_old=old_key, device_key_new=device.key)

    return response(True, {'id': device.id, 'key': device.key, 'name': device.name,
                           'description': device.description, 'last_update': device.last_update}, 200)


# DELETE DEVICE
def delete_device(device_id) -> dict:
    if not device_service_db.get_device_by_id(device_id=device_id):
        return response(False, {'msg': 'Device not found'}, 404)

    device = device_service_db.delete_device(device_id=device_id)
    device_info_service_db.delete(device_key=device.key)
    device_set_service_db.delete(device_key=device.key)
    return response(True, {'msg': 'Device successfully deleted'}, 200)


# GET DEVICE IDS
def get_device_ids() -> dict:
    device_ids: List[int] = device_service_db.get_device_ids()
    return response(True, device_ids, 200)


# GET DEVICE BY ID
def get_device_by_id(device_id: int) -> dict:
    device: device_service_db.Device = device_service_db.get_device_by_id(device_id=device_id)
    if not device:
        return response(False, {'msg': 'Device not found'}, 404)

    return response(True, {'id': device.id, 'key': device.key, 'name': device.name,
                           'description': device.description, 'client_id': device.client_id,
                           'parent_key': device.parent_key, 'last_update': device.last_update}, 200)
