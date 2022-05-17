from src import app
from . import ExpenseController


# CREATE
app.add_url_rule("/api/expense",
                 view_func=ExpenseController.create_expense,
                 methods=["POST"])

# GET BY ID
app.add_url_rule("/api/expense/<int:expense_id>",
                 view_func=ExpenseController.get_by_id_expense,
                 methods=["GET"])

# GET ALL
app.add_url_rule("/api/expense",
                 view_func=ExpenseController.get_all_expense,
                 methods=["GET"])
