from src import app
from . import client_user_controller

# # GET USER IDS BY CLIENT ID
# app.add_url_rule("/api/client_user",
#                  view_func=client_user_controller.get_users_by_client_id, methods=["GET"])

# BIND CLIENT USER
app.add_url_rule("/api/client_user", view_func=client_user_controller.bind_client_user, methods=["POST"])

# UNBIND CLIENT USER
app.add_url_rule("/api/client_user", view_func=client_user_controller.unbind_client_user, methods=["DELETE"])
