from . import StationDataRepository
from src.Station import DeviceStationRepository
from src._response import response
from typing import List


# CREATE
def create(station_key: str, weight: float, pressure: float, temperature: float, price: float) -> dict:
    station: DeviceStationRepository.DeviceStation = DeviceStationRepository.get_by_key(station_key)
    if not station:
        return response(False, {'msg': 'device by this key not found'}, 404)

    StationDataRepository.create(
        station_key=station_key,
        weight=weight,
        pressure=pressure,
        temperature=temperature,
        price=price,
        client_id=station.client_id,
        cash_box_id=station.cash_box_id
    )
    return response(True, {'msg': 'station data successfully created'}, 200)


# GET BY ID
def get_by_id(station_data_id: int) -> dict:
    station_data: StationDataRepository.StationData = StationDataRepository.get_by_id(
        station_data_id
    )

    if not station_data:
        return response(False, {'msg': 'device station data not found'}, 404)

    return response(True, {'id': station_data.id,
                           'weight': station_data.weight,
                           'pressure': station_data.pressure,
                           'temperature': station_data.temperature,
                           'price': station_data.price,
                           'creation_date': station_data.creation_date,
                           'client_id': station_data.client_id,
                           'cash_box_id': station_data.cash_box_id}, 200)


# GET ALL IDS
def get_all_ids() -> dict:
    station_data_ids: List[int] = StationDataRepository.get_all_ids()
    return response(True, station_data_ids, 200)
