from src import app
from . import UserImageController


app.add_url_rule("/api/user_image", view_func=UserImageController.create_user_image, methods=["POST"])

app.add_url_rule("/api/user_image", view_func=UserImageController.delete_user_image, methods=["DELETE"])

app.add_url_rule("/api/user_image/<int:user_id>", view_func=UserImageController.get_user_image, methods=["GET"])
