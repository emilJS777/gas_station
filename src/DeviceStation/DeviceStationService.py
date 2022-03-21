from . import DeviceStationRepository
from src.Client import client_service_db
from src._response import response
from typing import List
from src.CashBox import CashBoxServiceDb


# CREATE
def create(key: id, name: str, description: str, cash_box_id: int, client_id: int) -> dict:
    # GET BY KEY IF VERIFY RETURN CONFLICT
    if DeviceStationRepository.get_by_key(key):
        return response(False, {'msg': 'device by this key exist'}, 409)

    # GET CLIENT AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not client_service_db.get_by_id(client_id):
        return response(False, {'msg': 'client not found'}, 404)

    # GET CASH BOX AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not CashBoxServiceDb.get_by_id(cash_box_id):
        return response(False, {'msg': 'cash box not found'}, 404)

    DeviceStationRepository.create(
        key=key,
        name=name,
        description=description,
        cash_box_id=cash_box_id,
        client_id=client_id
    )
    return response(True, {'msg': 'device successfully created'}, 200)


# UPDATE
def update(device_id: int, key: str, name: str, description: str, cash_box_id: int) -> dict:
    # GET BY ID IF NOT FOUND RETURN NOT FOUND
    if not DeviceStationRepository.get_by_id(device_id):
        return response(False, {'msg': 'device not found'}, 404)

    # GET CASH BOX AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not CashBoxServiceDb.get_by_id(cash_box_id):
        return response(False, {'msg': 'cash box not found'}, 404)

    # IF DEVICE BY THIS KEY EXIST RETURN CONFLICT
    if DeviceStationRepository.get_by_key_exclude_id(device_id=device_id, key=key):
        return response(False, {'msg': 'device by this key exist'}, 409)

    DeviceStationRepository.update(
        device_id=device_id,
        key=key,
        name=name,
        description=description,
        cash_box_id=cash_box_id
    )
    return response(True, {'msg': 'device successfully updated'}, 200)


# DELETE
def delete(device_id: int) -> dict:
    # GET BY ID IF NOT FOUND RETURN NOT FOUND
    if not DeviceStationRepository.get_by_id(device_id):
        return response(False, {'msg': 'device not found'}, 404)

    DeviceStationRepository.delete(device_id)
    return response(True, {'msg': 'device successfully deleted'}, 200)


# GET BY ID
def get_by_id(device_id: int) -> dict:
    device: DeviceStationRepository.DeviceStation = DeviceStationRepository.get_by_id(device_id)
    if not device:
        return response(False, {'msg': 'device not found'}, 404)

    return response(True, {'id': device.id,
                           'key': device.key,
                           'name': device.name,
                           'description': device.description,
                           'last_update': device.last_update,
                           'cash_box_id': device.cash_box_id}, 200)


# GET ALL IDS
def get_all_ids() -> dict:
    device_ids: List[int] = DeviceStationRepository.get_all_ids()
    return response(True, device_ids, 200)
