from src import app
from . import firm_controller

# GET ALL FIRM
app.add_url_rule("/api/firm", view_func=firm_controller.firm_get, methods=["GET"])

# GET FIRM BY ID
app.add_url_rule("/api/firm/<int:firm_id>", view_func=firm_controller.firm_get_by_id, methods=["GET"])

# POST FIRM
app.add_url_rule("/api/firm", view_func=firm_controller.firm_post, methods=["POST"])

# PUT FIRM
app.add_url_rule("/api/firm/<int:firm_id>", view_func=firm_controller.firm_update, methods=["PUT"])

# DELETE FIRM
app.add_url_rule("/api/firm/<int:firm_id>", view_func=firm_controller.firm_delete, methods=["DELETE"])
