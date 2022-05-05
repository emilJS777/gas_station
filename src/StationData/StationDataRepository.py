from .StationDataModel import StationData
from typing import List
from flask import g


# CREATE
def create(station_key: str, weight: float, pressure: float, temperature: float, price: float,
           client_id: int, cash_box_id: int, cashier_id: int) \
        -> StationData:
    station_data: StationData = StationData(
        station_key=station_key,
        weight=weight,
        pressure=pressure,
        temperature=temperature,
        price=price,
        client_id=client_id,
        cash_box_id=cash_box_id,
        cashier_id=cashier_id
    )
    station_data.save_db()
    return station_data


# GET BY ID
def get_by_id(station_data_id: int) -> StationData:
    if g.cash_box_id:
        station_data: StationData = StationData.query.filter_by(id=station_data_id, cash_box_id=g.cash_box_id,
                                                                cashier_id=g.user_id).first()
    elif g.client_id:
        station_data: StationData = StationData.query.filter_by(id=station_data_id, client_id=g.client_id).first()
    else:
        station_data: StationData = StationData.query.filter_by(id=station_data_id).first()

    return station_data


# GET ALL IDS
def get_all_ids(date) -> List[int]:
    if g.cash_box_id:
        stations_data: List[StationData] = StationData.query.filter_by(cash_box_id=g.cash_box_id,
                                                                       creation_date=date,
                                                                       cashier_id=g.user_id).all()
    elif g.client_id:
        stations_data: List[StationData] = StationData.query.filter_by(client_id=g.client_id, creation_date=date).all()
    else:
        stations_data: List[StationData] = StationData.query.all()

    station_data_ids: List[int] = []
    for station_data in stations_data:
        station_data_ids.append(station_data.id)

    return station_data_ids


# GET ALL IDS BY CASH BOX ID
def get_all_ids_by_cash_box_id(cash_box_id: int) -> List[int]:
    if g.client_id:
        stations_data: List[StationData] = StationData.query.filter_by(cash_box_id=cash_box_id,
                                                                       client_id=g.client_id).all()
    else:
        stations_data: List[StationData] = StationData.query.filter_by(cash_box_id=cash_box_id).all()

    station_data_ids: List[int] = []
    for station_data in stations_data:
        station_data_ids.append(station_data.id)

    return station_data_ids
