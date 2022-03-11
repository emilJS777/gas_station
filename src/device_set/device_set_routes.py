from src import app
from . import device_set_controller


# UPDATE DEVICE SET
app.add_url_rule("/api/device_set", view_func=device_set_controller.update_device_set, methods=["GET"])

# GET DEVICE SET
app.add_url_rule("/api/device_set/<string:device_key>", view_func=device_set_controller.get_device_set, methods=["GET"])
