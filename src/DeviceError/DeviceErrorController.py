from . import DeviceErrorService


def get_all_device_error() -> dict:
    res: dict = DeviceErrorService.get_all()
    return res
