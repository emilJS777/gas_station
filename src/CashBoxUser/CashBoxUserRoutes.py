from src import app
from . import CashBoxUserController


app.add_url_rule("/api/cash_box_user/<int:cash_box_id>", view_func=CashBoxUserController.get_by_cash_box_id, methods=["GET"])
