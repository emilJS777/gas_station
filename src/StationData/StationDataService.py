from . import StationDataRepository
from src.CashBoxUser import CashBoxUserRepository
from src.Station import DeviceStationRepository
from src._response import response
from typing import List
from . import StationDataSocket
from flask_socketio import send, emit


# CREATE
def create(station_key: str, weight: float, pressure: float, temperature: float, price: float) -> dict:
    station: DeviceStationRepository.Station = DeviceStationRepository.get_by_key(station_key)
    if not station:
        return response(False, {'msg': 'device by this key not found'}, 404)

    # SEND SOCKET STATION DATA
    StationDataSocket.send_data({'station_id': station.id, 'weight': weight, 'pressure': pressure, 'temperature': temperature, 'price': price})

    cashier_id: int = CashBoxUserRepository.get_by_cash_box_id_exclude_client(
        cash_box_id=station.cash_box_id
    ).user_id

    StationDataRepository.create(
        station_key=station_key,
        weight=weight,
        pressure=pressure,
        temperature=temperature,
        price=price,
        client_id=station.client_id,
        cash_box_id=station.cash_box_id,
        cashier_id=cashier_id
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
                           'cash_box_id': station_data.cash_box_id,
                           'cashier_id': station_data.cashier_id}, 200)


# GET ALL IDS
def get_all_ids(date) -> dict:
    station_data_ids: List[int] = StationDataRepository.get_all_ids(date)
    return response(True, station_data_ids, 200)


# GET ALL IDS BY CASH BOX ID
def get_all_ids_by_cash_box_id(cash_box_id: int, date) -> dict:
    station_data_ids: List[int] = StationDataRepository.get_all_ids_by_cash_box_id(
        cash_box_id=cash_box_id,
        date=date
    )
    return response(True, station_data_ids, 200)
