from src import db
from datetime import datetime

#
# /SetData?Id=d19&data={"flowpast":3882.6,"flowsarqac":3882.6,"dppastaci":8.0,"dpdrac":8.0,"flowhanac":0.00,"flowmax":0.0,"flowproc":0,"presspastaci":1311.6,
#                       "onoff":1065353216,"selfonoff":0,"kgorcakic":38.0000,"pressgorcakic":0.1856,"flowauto":0.0,"signal":26,
#                       "today":400.12,"yesterday":0.00,"dpgorcakic":0.0021}

class DeviceInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_key = db.Column(db.String(120), nullable=False)
    last_update = db.Column(db.DateTime, default=datetime.utcnow())

    # flow_auto = db.Column(db.Numeric(8, 1))
    # dp_pastaci = db.Column(db.Numeric(8, 1))
    # dp_drac = db.Column(db.Numeric(8, 1))
    # dp_gorcakic = db.Column(db.Numeric(8, 4))
    #
    # flow_past = db.Column(db.Numeric(8, 1))
    # flow_sarqac = db.Column(db.Numeric(8, 1))
    # flow_hanac = db.Column(db.Numeric(8, 2))
    # signal = db.Column(db.Numeric(8, 0))
    #
    # k_gorcakic = db.Column(db.Numeric(8, 4))
    # self_on_off = db.Column(db.Numeric(8, 0))
    # flow_max = db.Column(db.Numeric(8, 1))
    # flow_proc = db.Column(db.Integer)
    # onoff = db.Column(db.Numeric(10, 0))
    #
    # press_pastaci = db.Column(db.Numeric(8, 1))
    # press_gorcakic = db.Column(db.Numeric(8, 4))
    # today = db.Column(db.Numeric(8, 2))
    # yesterday = db.Column(db.Numeric(8, 2))
    # monthly = db.Column(db.Numeric(8, 4))

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
