from .device_info_model import DeviceInfo
from datetime import datetime


def create(device_key: str) -> DeviceInfo:
    device_info: DeviceInfo = DeviceInfo(device_key=device_key)
    device_info.save_db()
    return device_info


def update(device_key, device_info_body) -> DeviceInfo:

    device_info: DeviceInfo = DeviceInfo.query.filter_by(device_key=device_key).first()
    device_info.flow_auto = device_info_body['flowauto']
    device_info.dp_pastaci = device_info_body['dppastaci']
    device_info.dp_drac = device_info_body['dppastaci']
    device_info.dp_gorcakic = device_info_body['dpgorcakic']

    device_info.flow_past = device_info_body['flowpast']
    device_info.flow_sarqac = device_info_body['flowsarqac']
    device_info.flow_hanac = device_info_body['flowhanac']
    device_info.k_gorcakic = device_info_body['kgorcakic']
    device_info.signal = device_info_body['signal']

    device_info.self_on_off = device_info_body['selfonoff']
    device_info.flow_max = device_info_body['flowmax']
    device_info.flow_proc = device_info_body['flowproc']
    device_info.press_pastaci = device_info_body['presspastaci']
    device_info.onoff = device_info_body['onoff']

    device_info.press_gorcakic = device_info_body['pressgorcakic']
    device_info.today = device_info_body['today']
    device_info.yesterday = device_info_body['yesterday']
    # device_info.monthly = device_info_body['monthly']

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



