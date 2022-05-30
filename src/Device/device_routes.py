from src import app
from . import device_controller


# GET DEVICE BY ID
app.add_url_rule("/api/device/<int:device_id>", view_func=device_controller.get_device_by_id, methods=["GET"])

# GET DEVICE IDS
app.add_url_rule("/api/device", view_func=device_controller.get_devices, methods=["GET"])

# CREATE DEVICE
app.add_url_rule("/api/device", view_func=device_controller.create_device, methods=["POST"])

# UPDATE DEVICE
app.add_url_rule("/api/device/<int:device_id>", view_func=device_controller.update_device, methods=["PUT"])

# DELETE DEVICE
app.add_url_rule("/api/device/<int:device_id>", view_func=device_controller.delete_device, methods=["DELETE"])
