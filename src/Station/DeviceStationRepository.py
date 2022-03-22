from .DeviceStationModel import DeviceStation
from typing import List
from datetime import datetime
from flask import g


# CREATE
def create(key: str, name: str, description: str, cash_box_id: int, client_id: int) -> DeviceStation:
    device: DeviceStation = DeviceStation(
        key=key,
        name=name,
        description=description,
        cash_box_id=cash_box_id,
        client_id=client_id
    )
    device.save_db()
    return device


# UPDATE
def update(device_id: int, key: str, name: str, description: str, cash_box_id: int) -> DeviceStation:
    device: DeviceStation = DeviceStation.query.filter_by(id=device_id).first()
    device.key = key
    device.name = name
    device.description = description
    device.cash_box_id = cash_box_id
    device.last_update = datetime.utcnow()
    device.update_db()
    return device


# DELETE
def delete(device_id: int) -> DeviceStation:
    device: DeviceStation = DeviceStation.query.filter_by(id=device_id).first()
    device.delete_db()
    return device


# GET BY ID
def get_by_id(device_id: int) -> DeviceStation:
    if g.cash_box_id:
        device: DeviceStation = DeviceStation.query.filter_by(id=device_id, cash_box_id=g.cash_box_id).first()
    elif g.client_id:
        device: DeviceStation = DeviceStation.query.filter_by(id=device_id, client_id=g.client_id).first()
    else:
        device: DeviceStation = DeviceStation.query.filter_by(id=device_id).first()

    return device


# GET BY KEY
def get_by_key(key: str) -> DeviceStation:
    device: DeviceStation = DeviceStation.query.filter_by(key=key).first()
    return device


# GET BY KEY EXCLUDE ID
def get_by_key_exclude_id(device_id: int, key: str) -> DeviceStation:
    device: DeviceStation = DeviceStation.query.filter(DeviceStation.key == key, DeviceStation.id != device_id).first()
    return device


# GET ALL IDS
def get_all_ids() -> List[int]:
    if g.cash_box_id:
        devices: List[DeviceStation] = DeviceStation.query.filter_by(cash_box_id=g.cash_box_id).all()
    elif g.client_id:
        devices: List[DeviceStation] = DeviceStation.query.filter_by(client_id=g.client_id).all()
    else:
        devices: List[DeviceStation] = DeviceStation.query.all()

    device_ids: List[int] = []

    for device in devices:
        device_ids.append(device.id)

    return device_ids


# GET ALL IDS BY CASH BOX ID
def get_all_ids_by_cash_box_id(cash_box_id: int) -> List[int]:
    devices: List[DeviceStation] = DeviceStation.query.filter_by(cash_box_id=cash_box_id).all()
    device_ids: List[int] = []

    for device in devices:
        device_ids.append(device.id)

    return device_ids

