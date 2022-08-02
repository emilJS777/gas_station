from sqlalchemy import func

from src import db
from datetime import datetime
from sqlalchemy.orm import relationship


class DeviceError(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_key = db.Column(db.String(120), unique=True)
    # creation_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    last_update_info = db.Column(db.DateTime(timezone=True), nullable=True)
    error_type = db.Column(db.Integer, nullable=False)
    confirmed = db.Column(db.Boolean, default=False)

    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    device = relationship("Device")

    # CONSTRUCTOR
    def __init__(self, device_key: str, error_type: int, confirmed: bool):
        self.device_key = device_key
        self.error_type = error_type
        self.confirmed = confirmed

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
