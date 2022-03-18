from src import db
from datetime import datetime


class DeviceSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_key = db.Column(db.String(120), nullable=False)
    last_update = db.Column(db.DateTime, default=datetime.utcnow())

    flow_hanac_set = db.Column(db.Numeric(8, 2))
    press_gorcakic_set = db.Column(db.Numeric(8, 2))
    k_gorcakic_set = db.Column(db.Numeric(8, 2))
    dp_gorcakic_set = db.Column(db.Numeric(8, 2))
    flow_max_set = db.Column(db.Numeric(8, 2))
    flow_proc_set = db.Column(db.Numeric(8, 2))

    # CONSTRUCTOR
    def __init__(self, device_key: str):
        self.device_key = device_key

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
