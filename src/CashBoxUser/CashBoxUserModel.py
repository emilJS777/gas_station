from src import db
from datetime import datetime


class CashBoxUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cash_box_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=True)

    last_update = db.Column(db.DateTime, default=datetime.utcnow())
    client_id = db.Column(db.Integer, nullable=False)

    # CONSTRUCTOR
    def __init__(self, cash_box_id: int, client_id: int):
        self.cash_box_id = cash_box_id
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
