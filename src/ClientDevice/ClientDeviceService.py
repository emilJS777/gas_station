from . import ClientDeviceRepository
from src._response import response
from src.Client import client_service_db
from src.Device import device_service_db


def create_bind(client_id: int, device_id: int) -> dict:
    if ClientDeviceRepository.get_by_client_id_device_id(client_id, device_id):
        return response(False, {'msg': 'linked exist'}, 409)

    if not client_service_db.get_by_id(client_id):
        return response(False, {'msg': 'client not found'}, 404)

    if not device_service_db.get_device_by_id(device_id):
        return response(False, {'msg': 'device not found'}, 404)

    ClientDeviceRepository.create_bind(client_id, device_id)
    return response(True, {'msg': 'client device successfully linked'}, 200)


def delete_bind(client_id: int, device_id: int) -> dict:
    if not ClientDeviceRepository.get_by_client_id_device_id(client_id, device_id):
        return response(False, {'msg': 'linked not found'}, 404)

    ClientDeviceRepository.delete_bind(client_id, device_id)
    return response(True, {'msg': 'bind successfully deleted'}, 200)


def get_devices_by_client_id(client_id: int) -> dict:
    if not client_service_db.get_by_id(client_id):
        return response(False, {'msg': 'client not found'}, 404)

    device_list = []
    for device_id in ClientDeviceRepository.get_device_ids_by_client_id(client_id):
        device = device_service_db.get_device_by_id(device_id)
        device_list.append({'id': device.id,
                            'key': device.key,
                            'name': device.name,
                            'description': device.description,
                            'parent_key': device.parent_key,
                            'error_after_minutes': device.error_after_minutes,
                            'last_update': device.last_update})

        return response(True, device_list, 200)
