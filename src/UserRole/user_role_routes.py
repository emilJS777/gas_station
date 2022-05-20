from src import app
from . import user_role_controller


# CREATE BIND
app.add_url_rule("/api/user_role", view_func=user_role_controller.user_role_bind, methods=["POST"])

# DELETE BIND
app.add_url_rule("/api/user_role", view_func=user_role_controller.user_role_unbind, methods=["DELETE"])

# GET USER IDS BY ROLE ID
app.add_url_rule("/api/roles_by_user/<int:user_id>", view_func=user_role_controller.get_roles_by_user_id, methods=["GET"])
