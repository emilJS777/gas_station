from src import app
from . import StationDataController


# CREATE
app.add_url_rule("/api/station_data_set",
                 view_func=StationDataController.create_station_data,
                 methods=["GET"])

# GET BY ID
app.add_url_rule("/api/station_data/<int:device_station_data_id>",
                 view_func=StationDataController.station_data_get_by_id,
                 methods=["GET"])

# GET ALL IDS
app.add_url_rule("/api/station_data",
                 view_func=StationDataController.station_data_get_all_ids,
                 methods=["GET"])
