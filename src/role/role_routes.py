from src import app
from . import role_controller

# CREATE ROLE
app.add_url_rule("/api/role", view_func=role_controller.create_role, methods=["POST"])

# GET ALL ROLES
app.add_url_rule("/api/role", view_func=role_controller.get_roles, methods=["GET"])

# GET ROLE BY ID
app.add_url_rule("/api/role/<int:role_id>", view_func=role_controller.get_role_by_id, methods=["GET"])

# UPDATE ROLE
app.add_url_rule("/api/role/<int:role_id>", view_func=role_controller.update_role, methods=["PUT"])

# DELETE ROLE
app.add_url_rule("/api/role/<int:role_id>", view_func=role_controller.delete_role, methods=["DELETE"])
