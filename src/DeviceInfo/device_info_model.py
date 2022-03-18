from src import db
from datetime import datetime


class DeviceInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_key = db.Column(db.String(120), nullable=False)
    last_update = db.Column(db.DateTime, default=datetime.utcnow())

    flow_auto = db.Column(db.Numeric(8, 2))
    dp_pastaci = db.Column(db.Numeric(8, 2))
    dp_drac = db.Column(db.Numeric(8, 2))
    dp_gorcakic = db.Column(db.Numeric(8, 2))
    flow_past = db.Column(db.Numeric(8, 2))
    flow_sarqac = db.Column(db.Numeric(8, 2))
    flow_hanac = db.Column(db.Numeric(8, 2))

    k_gorcakic = db.Column(db.Numeric(8, 2))
    self_on_off = db.Column(db.Numeric(8, 2))
    flow_max = db.Column(db.Numeric(8, 2))
    flow_proc = db.Column(db.Numeric(8, 2))
    press_pastaci = db.Column(db.Numeric(8, 2))
    press_gorcakic = db.Column(db.Numeric(8, 2))
    today = db.Column(db.Numeric(8, 2))
    monthly = db.Column(db.Numeric(8, 2))

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
