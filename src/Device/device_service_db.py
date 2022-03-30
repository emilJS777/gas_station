from . device_model import Device
from flask import g
from typing import List
from datetime import datetime


def create_device(key: str, name: str, description: str, error_after_minutes: int, client_id: int) -> Device:
    device: Device = Device(
        key=key,
        name=name,
        error_after_minutes=error_after_minutes,
        client_id=client_id,
        description=description
    )
    device.save_db()
    return device


def update_device(device_id: int, key: str, name: str, description: str, error_after_minutes: int, parent_key: str) -> Device:
    device: Device = Device.query.filter_by(id=device_id).first()
    device.key = key
    device.name = name
    device.error_after_minutes = error_after_minutes
    device.description = description
    device.parent_key = parent_key
    device.last_update = datetime.utcnow()
    device.update_db()
    return device


def delete_device(device_id: int):
    device: Device = Device.query.filter_by(id=device_id).first()
    device.delete_db()
    return device


def get_device_by_id(device_id: int) -> Device:
    device: Device = Device.query.filter_by(id=device_id, client_id=g.client_id).first() \
        if g.client_id else \
        Device.query.filter_by(id=device_id).first()
    return device


def get_device_by_key(key: str) -> Device:
    device: Device = Device.query.filter_by(key=key).first()
    return device


def get_by_key_exclude_id(device_id, key):
    device = Device.query.filter(Device.id != device_id, Device.key == key).first()
    return device


def get_device_ids():
    devices: List[Device] = Device.query.filter_by(client_id=g.client_id).all()\
        if g.client_id else \
        Device.query.all()
    devices_ids: List[int] = []

    for device in devices:
        devices_ids.append(device.id)

    return devices_ids
