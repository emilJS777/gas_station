from datetime import datetime
from src import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(18), nullable=True)
    password_hash = db.Column(db.String(200), nullable=True)
    first_name = db.Column(db.String(15), nullable=True)
    last_name = db.Column(db.String(15), nullable=True)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
    ticket = db.Column(db.String(50), nullable=True, unique=True)
    email_address = db.Column(db.String(80), nullable=True, unique=True)

    # NOT REQUIRE FIELDS
    creator_id = db.Column(db.Integer)
    client_id = db.Column(db.Integer)
    cash_box_id = db.Column(db.Integer)
    cashier = db.Column(db.Boolean)

    # CONSTRUCTOR
    def __init__(self, ticket):
        self.ticket = ticket

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
