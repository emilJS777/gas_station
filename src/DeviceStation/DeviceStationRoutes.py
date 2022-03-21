from src import app
from . import DeviceStationController


# CREATE
app.add_url_rule("/api/device_station", view_func=DeviceStationController.create_device_station, methods=["POST"])

# UPDATE
app.add_url_rule("/api/device_station/<int:device_id>", view_func=DeviceStationController.update_device_station, methods=["PUT"])

# DELETE
app.add_url_rule("/api/device_station/<int:device_id>", view_func=DeviceStationController.delete_device_station, methods=["DELETE"])

# GET BY ID
app.add_url_rule("/api/device_station/<int:device_id>", view_func=DeviceStationController.device_station_get_by_id, methods=["GET"])

# GET ALL IDS
app.add_url_rule("/api/device_station", view_func=DeviceStationController.device_station_get_all_ids, methods=["GET"])
