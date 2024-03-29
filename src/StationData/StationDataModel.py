from src import db
from datetime import datetime
from datetime import date
from sqlalchemy.sql import func


class StationData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_key = db.Column(db.String(120), nullable=False)
    creation_date = db.Column(db.Date(), default=func.now())

    weight = db.Column(db.Numeric(8, 2), nullable=True)
    pressure = db.Column(db.Numeric(8, 2), nullable=True)
    temperature = db.Column(db.Numeric(8, 2), nullable=True)
    price = db.Column(db.Numeric(8, 2), nullable=True)

    cash_box_id = db.Column(db.Integer, nullable=False)
    cashier_id = db.Column(db.Integer, nullable=True)
    client_id = db.Column(db.Integer, nullable=False)

    # CONSTRUCTOR
    def __init__(self, station_key: str, weight: float, pressure: float, temperature: float, price: float,
                 client_id: int, cash_box_id: int, cashier_id: int):
        self.station_key = station_key

        self.weight = weight
        self.pressure = pressure
        self.temperature = temperature
        self.price = price

        self.client_id = client_id
        self.cash_box_id = cash_box_id
        self.cashier_id = cashier_id

    # SAVE DB SELF
    def save_db(self):
        db.session.add(self)
        db.session.commit()

    # DELETE DB
    def delete_db(self):
        db.session.delete(self)
        db.session.commit()

    # UPDATE DATABASE
    @staticmethod
    def update_db():
        db.session.commit()
