from src import app
from . import firm_user_controller

# GET USER IDS BY FIRM ID
app.add_url_rule("/api/firm-user/<int:firm_id>",
                 view_func=firm_user_controller.get_user_ids_by_firm_id, methods=["GET"])

# BIND FIRM USER
app.add_url_rule("/api/firm-user", view_func=firm_user_controller.bind_firm_user, methods=["POST"])

# UNBIND FIRM USER
app.add_url_rule("/api/firm-user", view_func=firm_user_controller.unbind_firm_user, methods=["DELETE"])
