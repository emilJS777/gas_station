from . import device_set_service_db
from src._response import response


def update(device_set_body: dict) -> dict:
    if not device_set_service_db.get_device_set_by_key(device_key=device_set_body['device_key']):
        return response(False, {'msg': 'Device set not found'}, 404)

    device_set_service_db.update(device_set_body)
    return response(True, {'msg': 'Device set successfully updated'}, 200)


def get_device_set(device_key: str) -> dict:
    device_set: device_set_service_db.DeviceSet = device_set_service_db.get_device_set_by_key(device_key)
    if not device_set:
        return response(False, {'msg': 'Device set not found'}, 404)

    return response(True, {'device_key': device_set.device_key,
                           'last_update': device_set.last_update,

                           'flow_hanac_set': device_set.flow_hanac_set,
                           'press_gorcakic_set': device_set.press_gorcakic_set,
                           'k_gorcakic_set': device_set.k_gorcakic_set,
                           'dp_gorcakic_set': device_set.dp_gorcakic_set,
                           'flow_max_set': device_set.flow_max_set,
                           'flow_proc_set': device_set.flow_proc_set}, 200)


