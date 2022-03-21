from .DeviceStationDataModel import DeviceStationData
from typing import List
from flask import g


# CREATE
def create(device_station_key: str, weight: float, pressure: float, temperature: float, price: float,
           client_id: int, cash_box_id: int) \
        -> DeviceStationData:
    device_station_data: DeviceStationData = DeviceStationData(
        device_station_key=device_station_key,
        weight=weight,
        pressure=pressure,
        temperature=temperature,
        price=price,
        client_id=client_id,
        cash_box_id=cash_box_id
    )
    device_station_data.save_db()
    return device_station_data


# GET BY ID
def get_by_id(device_station_data_id: int) -> DeviceStationData:
    if g.client_id:
        device_station_data: DeviceStationData = DeviceStationData.query.filter_by(id=device_station_data_id,
                                                                                   client_id=g.client_id).first()
    else:
        device_station_data: DeviceStationData = DeviceStationData.query.filter_by(id=device_station_data_id).first()

    return device_station_data


# GET ALL IDS
def get_all_ids() -> List[int]:
    if g.client_id:
        device_stations_data: List[DeviceStationData] = DeviceStationData.query.filter_by(client_id=g.client_id).all()
    else:
        device_stations_data: List[DeviceStationData] = DeviceStationData.query.all()

    device_station_data_ids: List[int] = []
    for device_station_data in device_stations_data:
        device_station_data_ids.append(device_station_data.id)

    return device_station_data_ids
