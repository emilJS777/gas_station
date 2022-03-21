from src import app
from . import DeviceStationDataController


# CREATE
app.add_url_rule("/api/device_station_data_set",
                 view_func=DeviceStationDataController.create_device_station_data,
                 methods=["GET"])

# GET BY ID
app.add_url_rule("/api/device_station_data/<int:device_station_data_id>",
                 view_func=DeviceStationDataController.device_station_data_get_by_id,
                 methods=["GET"])

# GET ALL IDS
app.add_url_rule("/api/device_station_data",
                 view_func=DeviceStationDataController.device_station_data_get_all_ids,
                 methods=["GET"])
