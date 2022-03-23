from src import db
from datetime import datetime


class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    last_update = db.Column(db.DateTime, default=datetime.utcnow())

    cash_box_id = db.Column(db.Integer, nullable=False)
    client_id = db.Column(db.Integer, nullable=False)

    # CONSTRUCTOR
    def __init__(self, key: str, name: str, description: str, cash_box_id: int, client_id: int):
        self.key = key
        self.name = name
        self.description = description
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
