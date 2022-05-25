from . import UserImageService
from flask import request, g
from src.Auth import auth_middleware


@auth_middleware.check_authorize
def create_user_image() -> dict:
    res: dict = UserImageService.create_user_image(user_id=g.user_id, image=request.files["image"])
    return res


@auth_middleware.check_authorize
def delete_user_image() -> dict:
    res: dict = UserImageService.delete_user_image(user_id=g.user_id)
    return res


@auth_middleware.check_authorize
def get_user_image(user_id: int) -> dict:
    res: dict = UserImageService.get_user_image(user_id=user_id)
    return res
