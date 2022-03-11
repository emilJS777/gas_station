from src import app
from . import device_info_controller


# UPDATE DEVICE INFO
app.add_url_rule("/api/device_info", view_func=device_info_controller.update_device_info, methods=["GET"])

# GET DEVICE INFO
app.add_url_rule("/api/device_info/<string:device_key>", view_func=device_info_controller.get_device_info, methods=["GET"])
