from .ClientDeviceModel import ClientDevice


def create_bind(client_id: int, device_id: int):
    client_device: ClientDevice = ClientDevice()
    client_device.client_id = client_id
    client_device.device_id = device_id
    client_device.save_db()
    return client_device


def delete_bind(client_id: int, device_id: int):
    client_device: ClientDevice = ClientDevice.query.filter_by(client_id=client_id, device_id=device_id).first()
    client_device.delete_db()
    return client_device


def get_by_client_id_device_id(client_id: int, device_id: int):
    client_device: ClientDevice = ClientDevice.query.filter_by(client_id=client_id, device_id=device_id).first()
    return client_device


def get_device_ids_by_client_id(client_id: int):
    device_ids = []
    for client_device in ClientDevice.query.filter_by(client_id=client_id).all():
        device_ids.append(client_device.device_id)

    return device_ids


