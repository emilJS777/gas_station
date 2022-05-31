from src import app
from . import ClientDeviceController

# BIND CLIENT DEVICE
app.add_url_rule("/api/client_device", view_func=ClientDeviceController.client_device_bind, methods=["POST"])

# BIND CLIENT DEVICE
app.add_url_rule("/api/client_device", view_func=ClientDeviceController.client_device_unbind, methods=["DELETE"])

# # GET  DEVICES BY CLIENT ID
# app.add_url_rule("/api/client_device", view_func=ClientDeviceController.get_devices_by_client_id, methods=["GET"])
