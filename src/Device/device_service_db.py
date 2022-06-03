from . device_model import Device
from flask import g
from typing import List
from datetime import datetime
from src.Client import client_service_db
from src._general.parents import get_page_items
from src.Client.client_model import Client
from sqlalchemy import or_, and_


def create_device(key: str, name: str, description: str, error_after_minutes: int,
                  parent_ids, client_id: int,
                  client_ids: list) -> Device:
    device: Device = Device(
        key=key,
        name=name,
        error_after_minutes=error_after_minutes,
        client_id=client_id,
        description=description
    )
    clients = Client.query.filter(Client.id.in_(client_ids)).all()
    self_client = Client.query.filter_by(id=g.client_id).first()
    clients.append(self_client)

    device.clients = clients

    devices = Device.query.filter(Device.id.in_(parent_ids)).all()
    device.parent_devices = devices
    device.save_db()
    return device


def update_device(device_id: int, key: str, name: str, description: str, error_after_minutes: int, parent_ids,
                  client_ids: list[int]) -> Device:
    device: Device = Device.query.filter_by(id=device_id).first()
    device.key = key
    device.name = name
    device.error_after_minutes = error_after_minutes
    device.description = description
    device.last_update = datetime.utcnow()

    clients = Client.query.filter(Client.id.in_(client_ids)).all()
    clients.append(Client.query.filter_by(id=g.client_id).first())
    device.clients = clients

    devices = Device.query.filter(Device.id.in_(parent_ids)).all()
    device.parent_devices = devices

    device.update_db()
    return device


def delete_device(device_id: int):
    device: Device = Device.query.filter_by(id=device_id).first()
    device.delete_db()
    return device


def get_device_by_id(device_id: int) -> Device:
    device: Device = Device.query.join(Device.clients).filter(Client.id.in_([g.client_id]), Device.id==device_id).first()
    return device


def get_device_by_key(key: str) -> Device:
    device: Device = Device.query.filter_by(key=key).first()
    return device


def get_by_key_exclude_id(device_id, key):
    device = Device.query.filter(Device.id != device_id, Device.key == key).first()
    return device


def get_devices(page: int, per_page: int, client_id: int):
    # if client_id > 0:
    #     devices = Device.query.join(Device.clients).filter(Client.id.in_([g.client_id, ])) \
    #         .paginate(page=page, per_page=per_page)
    # else:
    devices = Device.query.join(Device.clients).filter(Client.id.in_([g.client_id]))\
            .paginate(page=page, per_page=per_page)

    return get_page_items(devices)

