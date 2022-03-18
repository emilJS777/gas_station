from src import app
from . import CashBoxController


# CREATE
app.add_url_rule("/api/cash_box", view_func=CashBoxController.create, methods=["POST"])

# UPDATE
app.add_url_rule("/api/cash_box/<int:cash_box_id>", view_func=CashBoxController.update, methods=["PUT"])

# DELETE
app.add_url_rule("/api/cash_box/<int:cash_box_id>", view_func=CashBoxController.create, methods=["DELETE"])

# GET BY ID
app.add_url_rule("/api/cash_box/<int:cash_box_id>", view_func=CashBoxController.get_by_id, methods=["GET"])

# GET ALL IDS
app.add_url_rule("/api/cash_box", view_func=CashBoxController.get_all_ids, methods=["GET"])
