from sqlalchemy import func
from src import db


class CashBoxData(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    salary = db.Column(db.Numeric(8, 2))
    car_gas = db.Column(db.Integer)
    payment_gas = db.Column(db.Integer)

    payment_electricity = db.Column(db.Integer)
    harka = db.Column(db.Integer)

    r = db.Column(db.Integer)
    s = db.Column(db.Integer)

    cash_box_id = db.Column(db.Integer, nullable=False)
    # cashier_id = db.Column(db.Integer, nullable=False)
    client_id = db.Column(db.Integer, nullable=False)
    creation_date = db.Column(db.Date(), default=func.now())

    # CONSTRUCTOR
    def __init__(self, client_id: int):
        self.client_id = client_id

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
