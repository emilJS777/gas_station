from src import app
from . import auth_controller

# LOGIN ROUTE
app.add_url_rule("/api/login", view_func=auth_controller.login, methods=["POST"])

# REFRESH TOKEN ROUTE
app.add_url_rule("/api/refresh", view_func=auth_controller.refresh_token, methods=["PUT"])

# GET PROFILE
app.add_url_rule("/api/profile", view_func=auth_controller.get_profile, methods=["GET"])

# UPDATE PASSWORD
app.add_url_rule("/api/resset_password", view_func=auth_controller.resset_password, methods=["PUT"])

# UPDATE PASSWORD REQUEST
app.add_url_rule("/api/resset_password", view_func=auth_controller.request_resset_password, methods=["POST"])
