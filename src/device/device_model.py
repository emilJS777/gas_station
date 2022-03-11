from src import db
from datetime import datetime


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(120), nullable=True)
    last_update = db.Column(db.DateTime, default=datetime.utcnow())
    client_id = db.Column(db.Integer, nullable=False)
    parent_key = db.Column(db.String(120))

    # CONSTRUCTOR
    def __init__(self, key: str, name: str, description: str, client_id: int):
        self.key = key
        self.name = name
        self.description = description
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
