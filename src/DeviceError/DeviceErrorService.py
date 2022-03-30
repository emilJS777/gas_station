from datetime import datetime, timedelta
from typing import List
from . import DeviceErrorServiceDb


def check_device_null_error(req_params):
    error = True

    # GET REQUEST QUERY KEYS AND VERIFY IF NOT NULL ERROR IS FALSE
    for key in req_params:
        if not key == "device_key" and float(req_params.get(key)) > float(0):
            error = False

            # IF ERROR EXIST BY THIS DEVICE KEY, DELETE HIM FROM DB
            if DeviceErrorServiceDb.get_by_key(req_params.get("device_key")):
                DeviceErrorServiceDb.delete(req_params.get("device_key"))

            # EXIT FROM THIS CYCLE
            break

    # IF ERROR IS TRUE AND NOT DEVICE ERROR ON DB BY THIS KEY CREATE HIM
    if error and not DeviceErrorServiceDb.get_by_key(req_params.get("device_key")):
        DeviceErrorServiceDb.create(device_key=req_params.get("device_key"), error_type=0)

    # ELSE IF ERROR IS TRUE GET DEVICE ERROR FROM DB
    elif error:
        device_error: DeviceErrorServiceDb.DeviceError = DeviceErrorServiceDb.get_by_key(req_params.get("device_key"))

        # IF NOT DEVICE ERROR CONFIRMED AND DEVICE ERROR CREATION DATE < THIS DATE + CREATED
        # MINUTES UPDATE THIS ERROR CONFIRMED TRUE
        if not device_error.confirmed and datetime.utcnow() > device_error.creation_date + timedelta(minutes=2):
            DeviceErrorServiceDb.update(
                device_key=req_params.get("device_key"),
                confirmed=True
            )
