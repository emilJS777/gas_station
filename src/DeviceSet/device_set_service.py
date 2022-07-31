from . import device_set_service_db
from src._response import response
from flask import make_response, jsonify
from datetime import datetime


def update(device_set_body: dict) -> dict:
    if not device_set_service_db.get_device_set_by_key(device_key=device_set_body['device_key']):
        return response(False, {'msg': 'Device set not found'}, 404)

    device_set_service_db.update(device_set_body)
    return response(True, {'msg': 'Device set successfully updated'}, 200)


def get_device_set(device_key: str):
    device_set: device_set_service_db.DeviceSet = device_set_service_db.get_device_set_by_key(device_key)
    if not device_set:
        return response(False, {'msg': 'Device set not found'}, 404)

    return make_response(jsonify({'id': device_set.device_key,
                                  'date': datetime.strftime(device_set.last_update, "%m/%d/%Y %H:%M:%S"),
                                  'masterFlowAuto': device_set.master_flow_auto,
                                  'fowAuto': device_set.flow_auto_set,
                                  'flowhanac': device_set.flow_hanac_set,
                                  'pressgorcakic': device_set.press_gorcakic_set,
                                  'kgorcakic': device_set.k_gorcakic_set,
                                  'dpgorcakic': float(device_set.dp_gorcakic_set),
                                  'flowmax': device_set.flow_max_set,
                                  'flowproc': device_set.flow_proc_set,
                                  'flowAutoOnOff': device_set.flow_auto_on_off,
                                  # 'masterFlowAuto': device_set.master_flow_auto
                                 }), 200)
    # return response(True, {'id': device_set.device_key,
    #                        'date': device_set.last_update,
    #
    #                        'flowhanac': device_set.flow_hanac_set,
    #                        'pressgorcakic': device_set.press_gorcakic_set,
    #                        'kgorcakic': device_set.k_gorcakic_set,
    #                        'dpgorcakic': device_set.dp_gorcakic_set,
    #                        'flowmax': device_set.flow_max_set,
    #                        'flowproc': device_set.flow_proc_set,
    #                        'onoff': device_set.onoff,
    #                        'flowAutoOnOff': device_set.flow_auto_on_off,
    #                        'masterFlowAuto': device_set.master_flow_auto}, 200)


