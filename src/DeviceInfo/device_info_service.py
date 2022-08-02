from . import device_info_service_db
from src._response import response
from threading import Thread
import json


# UPDATE
def update(device_key: str, device_info_body) -> dict:
    if not device_info_service_db.get_device_info_by_key(device_key=device_key):
        return response(False, {'msg': 'Device info not found'}, 200)

    device_info_service_db.update(device_key, device_info_body)
    return response(True, {'msg': 'Device info successfully updated'}, 200)


# GET DEVICE INFO
def get_device_info(device_key: str) -> dict:
    device_info: device_info_service_db.DeviceInfo = device_info_service_db.get_device_info_by_key(device_key)
    if not device_info:
        return response(False, {'msg': 'Device info not found'}, 200)

    return response(True, {'id': device_info.device_key,
                           'last_update': device_info.last_update,
                           'flowauto': device_info.flow_auto,
                           'dp_pastaci': device_info.dp_pastaci,
                           'dp_drac': device_info.dp_drac,
                           'dpgorcakic': device_info.dp_gorcakic,
                           'flow_past': device_info.flow_past,
                           'flow_sarqac': device_info.flow_sarqac,
                           'flowhanac': device_info.flow_hanac,
                           'kgorcakic': device_info.k_gorcakic,
                           'self_on_off': device_info.self_on_off,
                           'flowmax': device_info.flow_max,
                           'flowproc': device_info.flow_proc,
                           'press_pastaci': device_info.press_pastaci,
                           'pressgorcakic': device_info.press_gorcakic,
                           'today': device_info.today,
                           'yesterday': device_info.yesterday,
                           'signal': device_info.signal,
                           'onoff': device_info.onoff,
                           'monthly': device_info.monthly
                           }, 200)
#