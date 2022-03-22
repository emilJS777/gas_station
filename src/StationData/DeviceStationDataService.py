from . import DeviceStationDataRepository
from src.Station import DeviceStationRepository
from src._response import response
from typing import List


# CREATE
def create(device_station_key: str, weight: float, pressure: float, temperature: float, price: float) -> dict:
    device_station: DeviceStationRepository.DeviceStation = DeviceStationRepository.get_by_key(device_station_key)
    if not device_station:
        return response(False, {'msg': 'device by this key not found'}, 404)

    DeviceStationDataRepository.create(
        device_station_key=device_station_key,
        weight=weight,
        pressure=pressure,
        temperature=temperature,
        price=price,
        client_id=device_station.client_id,
        cash_box_id=device_station.cash_box_id
    )
    return response(True, {'msg': 'device station data successfully created'}, 200)


# GET BY ID
def get_by_id(device_station_data_id: int) -> dict:
    device_station_data: DeviceStationDataRepository.DeviceStationData = DeviceStationDataRepository.get_by_id(
        device_station_data_id
    )

    if not device_station_data:
        return response(False, {'msg': 'device station data not found'}, 404)

    return response(True, {'id': device_station_data.id,
                           'weight': device_station_data.weight,
                           'pressure': device_station_data.pressure,
                           'temperature': device_station_data.temperature,
                           'price': device_station_data.price,
                           'creation_date': device_station_data.creation_date,
                           'client_id': device_station_data.client_id,
                           'cash_box_id': device_station_data.cash_box_id}, 200)


# GET ALL IDS
def get_all_ids() -> dict:
    device_station_data_ids: List[int] = DeviceStationDataRepository.get_all_ids()
    return response(True, device_station_data_ids, 200)
