from .ClientDeviceModel import ClientDevice
from src.Client.client_model import Client
from src.Device.device_model import Device


def create_bind(client_id: int, device_ids: list):

    client = Client.query.filter_by(id=client_id).first()
    devices = Device.query.filter(Device.id.in_(device_ids)).all()
    client.devices = devices
    client.update_db()
    # client_device: ClientDevice = ClientDevice()
    # client_device.client_id = client_id
    # client_device.device_id = device_id
    # client_device.save_db()
    # return client_device


def delete_bind(client_id: int, device_id: int):
    client_device: ClientDevice = ClientDevice.query.filter_by(client_id=client_id, device_id=device_id).first()
    client_device.delete_db()
    return client_device


def get_by_client_id_device_id(client_id: int, device_id: int):
    client_device: ClientDevice = ClientDevice.query.filter_by(client_id=client_id, device_id=device_id).first()
    return client_device


# def get_device_ids_by_client_id(client_id: int):
#     device_ids = []
#     for client_device in ClientDevice.query.filter_by(client_id=client_id).all():
#         device_ids.append(client_device.device_id)
#
#     return device_ids


def delete_all_by_client_id(client_id):
    client_device: list[ClientDevice] = ClientDevice.query.filter_by(client_id=client_id).all()

    for c_d in client_device:
        c_d.delete_db()


def delete_all_by_device_id(device_id):
    client_device: list[ClientDevice] = ClientDevice.query.filter_by(device_id=device_id).all()

    for c_d in client_device:
        c_d.delete_db()
