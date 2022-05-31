from datetime import datetime

from sqlalchemy.orm import relationship

from src import db


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=True)
    creator_id = db.Column(db.Integer)
    client_id = db.Column(db.Integer)

    permissions = relationship("Permission", secondary="role_permission", backref=db.backref('role'))

    # CONSTRUCTOR
    def __init__(self, name: str):
        self.name = name

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
