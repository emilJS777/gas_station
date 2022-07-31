from sqlalchemy import func

from src import db
from datetime import datetime

#
# /SetData?Id=d19&data={"flowpast":3882.6,"flowsarqac":3882.6,"dppastaci":8.0,"dpdrac":8.0,"flowhanac":0.00,"flowmax":0.0,"flowproc":0,"presspastaci":1311.6,
#                       "onoff":1065353216,"selfonoff":0,"kgorcakic":38.0000,"pressgorcakic":0.1856,"flowauto":0.0,"signal":26,
#                       "today":400.12,"yesterday":0.00,"dpgorcakic":0.0021}


# {"id":"d3","flowhanac":0,"flowmax":null,"flowproc":null,"dpgorcakic":0.0021,"kgorcakic":8.06,
#  "flowauto":0,"pressgorcakic":0.1856,"onoff":true,
#  "flowAutoOnoff":null,"masterFlowAuto":null,"date":"12/04/2022 11:31:42"}

class DeviceSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_key = db.Column(db.String(120), nullable=False)
    # last_update = db.Column(db.DateTime(timezone=True), default=datetime.utcnow())

    flow_auto_set = db.Column(db.Numeric(8, 0))
    flow_hanac_set = db.Column(db.Numeric(8, 0))
    press_gorcakic_set = db.Column(db.Numeric(8, 4))
    k_gorcakic_set = db.Column(db.Numeric(8, 2))
    dp_gorcakic_set = db.Column(db.Numeric(8, 4))
    flow_max_set = db.Column(db.Numeric(8, 1))
    flow_proc_set = db.Column(db.Numeric(8, 0))

    # onoff = db.Column(db.Boolean)
    flow_auto_on_off = db.Column(db.Numeric(8, 4))
    master_flow_auto = db.Column(db.Numeric(8, 4))

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
