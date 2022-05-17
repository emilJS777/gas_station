from sqlalchemy import func

from src import db
from datetime import datetime


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))
    price = db.Column(db.Numeric(8, 2), nullable=False)
    creation_date = db.Column(db.Date(), default=func.now())

    client_id = db.Column(db.Integer, nullable=False)
    cash_box_id = db.Column(db.Integer)
    creator_id = db.Column(db.Integer, nullable=False)

    # CONSTRUCTOR
    def __init__(self, name: str, description: str, price: float, cash_box_id: int, client_id: int, creator_id: int):
        self.name = name
        self.description = description
        self.price = price
        self.cash_box_id = cash_box_id
        self.creator_id = creator_id
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
