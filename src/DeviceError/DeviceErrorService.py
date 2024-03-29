from datetime import datetime, timedelta
from typing import List
from . import DeviceErrorServiceDb
from src.Device import device_service_db
from src._response import response
import json
from src.EmailSender.DeviceErrorSender import DeviceErrorSender
from src.User import user_service_db


# GET ALL DEVICE ERROR LIST
def get_all() -> dict:
    devices_error_list: List[dict] = DeviceErrorServiceDb.get_all()
    return response(True, devices_error_list, 200)


def check_device_null_error(device_key, req_params):
    req_params = json.loads(req_params)
    error = True

    device = device_service_db.get_device_by_key(device_key)

    # GET REQUEST QUERY KEYS AND VERIFY IF NOT NULL ERROR IS FALSE
    for key in req_params:
        if float(req_params.get(key)) > float(0):
            error = False

            # IF ERROR EXIST BY THIS DEVICE KEY, DELETE HIM FROM DB
            if DeviceErrorServiceDb.get_by_key(device_key):
                DeviceErrorServiceDb.delete(device_key)

            # EXIT FROM THIS CYCLE
            break

    # IF ERROR IS TRUE AND NOT DEVICE ERROR ON DB BY THIS KEY CREATE HIM
    if error and not DeviceErrorServiceDb.get_by_key(device_key):
        DeviceErrorServiceDb.create(device_key=device_key, device_id=device.id, error_type=0)

    # ELSE IF ERROR IS TRUE GET DEVICE ERROR FROM DB
    elif error:
        device_error: DeviceErrorServiceDb.DeviceError = DeviceErrorServiceDb.get_by_key(device_key)

        # IF NOT DEVICE ERROR CONFIRMED AND DEVICE ERROR CREATION DATE < THIS DATE + CREATED
        # MINUTES UPDATE THIS ERROR CONFIRMED TRUE
        if not device_error.confirmed and datetime.utcnow() > device_error.creation_date + \
                timedelta(minutes=device_service_db.get_device_by_key(device_key).error_after_minutes):

            DeviceErrorServiceDb.update(
                device_key=device_key,
                error_type=0,
                confirmed=True,
            )
            users = user_service_db.get_all_by_client_id(device.client_id)
            for user in users:
                DeviceErrorSender().send(email_address=user.email_address, device_key=device_key, error_code=0)
