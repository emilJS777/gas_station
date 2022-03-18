from .device_info_model import DeviceInfo
from datetime import datetime


def create(device_key: str) -> DeviceInfo:
    device_info: DeviceInfo = DeviceInfo(device_key=device_key)
    device_info.save_db()
    return device_info


def update(device_info_body: dict) -> DeviceInfo:
    device_info: DeviceInfo = DeviceInfo.query.filter_by(device_key=device_info_body['device_key']).first()
    device_info.flow_auto = device_info_body['flow_auto']
    device_info.dp_pastaci = device_info_body['dp_pastaci']
    device_info.dp_drac = device_info_body['dp_pastaci']
    device_info.dp_gorcakic = device_info_body['dp_gorcakic']

    device_info.flow_past = device_info_body['flow_past']
    device_info.flow_sarqac = device_info_body['flow_sarqac']
    device_info.flow_hanac = device_info_body['flow_hanac']
    device_info.k_gorcakic = device_info_body['k_gorcakic']

    device_info.self_on_off = device_info_body['self_on_off']
    device_info.flow_max = device_info_body['flow_max']
    device_info.flow_proc = device_info_body['flow_proc']
    device_info.press_pastaci = device_info_body['press_pastaci']

    device_info.press_gorcakic = device_info_body['press_gorcakic']
    device_info.today = device_info_body['today']
    device_info.monthly = device_info_body['monthly']

    device_info.last_update = datetime.utcnow()
    device_info.update_db()
    return device_info


def update_device_key(device_key_old: str, device_key_new: str) -> DeviceInfo:
    device_info: DeviceInfo = DeviceInfo.query.filter_by(device_key=device_key_old).first()
    device_info.device_key = device_key_new
    device_info.update_db()
    return device_info


def delete(device_key: str) -> DeviceInfo:
    device_info: DeviceInfo = DeviceInfo.query.filter_by(device_key=device_key).first()
    device_info.delete_db()
    return device_info


def get_device_info_by_key(device_key: str) -> DeviceInfo:
    device_info: DeviceInfo = DeviceInfo.query.filter_by(device_key=device_key).first()
    return device_info



