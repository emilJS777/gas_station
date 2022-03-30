from .DeviceErrorModel import DeviceError


# CREATE
def create(device_key: str, error_type: int) -> DeviceError:
    device_error: DeviceError = DeviceError(device_key=device_key, error_type=error_type)
    device_error.save_db()
    return device_error


# UPDATE
def update(device_key: str, confirmed: bool) -> DeviceError:
    device_error: DeviceError = DeviceError.query.filter_by(device_key=device_key).first()
    device_error.confirmed = confirmed
    device_error.update_db()
    return device_error


# DELETE
def delete(device_key: str) -> DeviceError:
    device_error: DeviceError = DeviceError.query.filter_by(device_key=device_key).first()
    device_error.delete_db()
    return device_error


# GET BY KEY
def get_by_key(device_key: str) -> DeviceError:
    device_error: DeviceError = DeviceError.query.filter_by(device_key=device_key).first()
    return device_error
