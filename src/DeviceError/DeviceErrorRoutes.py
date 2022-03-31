from src import app
from . import DeviceErrorController


app.add_url_rule("/api/device_error", view_func=DeviceErrorController.get_all_device_error, methods=["GET"])
