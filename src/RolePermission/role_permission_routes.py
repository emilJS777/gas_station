from src import app
from . import role_permission_controller


# CREATE BIND
app.add_url_rule("/api/role_permission", view_func=role_permission_controller.create_bind, methods=["POST"])

# DELETE BIND
app.add_url_rule("/api/role_permission", view_func=role_permission_controller.delete_bind, methods=["DELETE"])

# GET PERMISSION IDS BY ROLE ID
app.add_url_rule("/api/permissions_by_role/<int:role_id>", view_func=role_permission_controller.get_permission_ids_by_role_id, methods=["GET"])
