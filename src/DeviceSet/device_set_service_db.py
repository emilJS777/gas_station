from .device_set_model import DeviceSet
from datetime import datetime


def create(device_key: str) -> DeviceSet:
    device_set: DeviceSet = DeviceSet(device_key=device_key)
    device_set.save_db()
    return device_set


def update(device_set_body: dict) -> dict:
    device_set: DeviceSet = DeviceSet.query.filter_by(device_key=device_set_body['device_key']).first()
    print(device_set_body['press_gorcakic_set'])
    device_set.flow_auto_set = device_set_body['flow_auto_set']
    device_set.flow_hanac_set = device_set_body['flow_hanac_set']
    device_set.press_gorcakic_set = device_set_body['press_gorcakic_set']
    device_set.k_gorcakic_set = device_set_body['k_gorcakic_set']
    device_set.dp_gorcakic_set = device_set_body['dp_gorcakic_set']
    device_set.flow_max_set = device_set_body['flow_max_set']
    device_set.flow_proc_set = device_set_body['flow_proc_set']
    device_set.onoff = device_set_body['onoff'] == 'true'
    device_set.flow_auto_on_off = device_set_body['flow_auto_on_off']
    device_set.master_flow_auto = device_set_body['master_flow_auto']

    device_set.last_update = datetime.utcnow()
    device_set.update_db()
    return device_set


def update_device_key(device_key_old: str, device_key_new: str) -> DeviceSet:
    device_set: DeviceSet = DeviceSet.query.filter_by(device_key=device_key_old).first()
    device_set.device_key = device_key_new
    device_set.update_db()
    return device_set


def get_device_set_by_key(device_key: str) -> DeviceSet:
    device_set: DeviceSet = DeviceSet.query.filter_by(device_key=device_key).first()
    return device_set


def delete(device_key: str) -> DeviceSet:
    device_set: DeviceSet = DeviceSet.query.filter_by(device_key=device_key).first()
    device_set.delete_db()
    return device_set


