from src import app
from . import CashBoxUserController


app.add_url_rule("/api/cash_box_user/<int:cash_box_id>",
                 view_func=CashBoxUserController.get_by_cash_box_id,
                 methods=["GET"])

app.add_url_rule("/api/cash_box_user/users_by_cash_box_id/<int:cash_box_id>",
                 view_func=CashBoxUserController.get_users_by_cash_box_id,
                 methods=["GET"])

app.add_url_rule("/api/cash_box_user/request_change/<int:user_id>",
                 view_func=CashBoxUserController.request_change_cash_box_user,
                 methods=["PUT"])
