from . import device_info_service_db
from src._response import response
from threading import Thread


# UPDATE
def update(device_info_body: dict) -> dict:
    if not device_info_service_db.get_device_info_by_key(device_key=device_info_body['device_key']):
        return response(False, {'msg': 'Device info not found'}, 404)

    device_info_service_db.update(device_info_body)
    return response(True, {'msg': 'Device info successfully updated'}, 200)


# GET DEVICE INFO
def get_device_info(device_key: str) -> dict:
    device_info: device_info_service_db.DeviceInfo = device_info_service_db.get_device_info_by_key(device_key)
    if not device_info:
        return response(False, {'msg': 'Device info not found'}, 404)

    return response(True, {'device_key': device_info.device_key,
                           'last_update': device_info.last_update,

                           'flow_auto': device_info.flow_auto,
                           'dp_pastaci': device_info.dp_pastaci,
                           'dp_drac': device_info.dp_drac,
                           'dp_gorcakic': device_info.dp_gorcakic,
                           'flow_past': device_info.flow_past,
                           'flow_sarqac': device_info.flow_sarqac,
                           'flow_hanac': device_info.flow_hanac,
                           'k_gorcakic': device_info.k_gorcakic,
                           'self_on_off': device_info.self_on_off,
                           'flow_max': device_info.flow_max,
                           'flow_proc': device_info.flow_proc,
                           'press_pastaci': device_info.press_pastaci,
                           'press_gorcakic': device_info.press_gorcakic,
                           'today': device_info.today,
                           'monthly': device_info.monthly}, 200)
