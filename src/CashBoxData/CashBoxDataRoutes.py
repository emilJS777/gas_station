from src import app
from . import CashBoxDataController


app.add_url_rule("/api/cash_box_data",
                 view_func=CashBoxDataController.create_cash_box_data,
                 methods=["POST"])

app.add_url_rule("/api/cash_box_data",
                 view_func=CashBoxDataController.get_by_date,
                 methods=["GET"])
