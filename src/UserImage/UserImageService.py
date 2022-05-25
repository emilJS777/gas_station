import base64
import os
from src import app
from . import UserImageServiceDb
from src._response import response


def create_user_image(user_id: int, image) -> dict:
    user_image: UserImageServiceDb.UserImage = UserImageServiceDb.get_by_user_id(user_id)

    if user_image:
        os.remove(app.config["IMAGE_UPLOADS"] + '/' + user_image.image_path)
        UserImageServiceDb.delete_user_image(user_id)

    filename = str(user_id) + image.filename
    image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

    UserImageServiceDb.create_user_image(user_id, filename)
    return response(True, {'msg': 'image successfully created'}, 200)


def delete_user_image(user_id: int):
    user_image: UserImageServiceDb.UserImage = UserImageServiceDb.get_by_user_id(user_id)

    if user_image:
        return response(False, {'msg': 'image not found'}, 404)

    os.remove(app.config["IMAGE_UPLOADS"] + '/' + user_image.image_path)
    UserImageServiceDb.delete_user_image(user_id)
    return response(True, {'msg': 'image successfully deleted'}, 200)


def get_user_image(user_id: int):
    user_image: UserImageServiceDb.UserImage = UserImageServiceDb.get_by_user_id(user_id)
    if not user_image:
        return response(False, {'msg': 'image not found'}, 404)

    # CONVERT TO BASE64 AND SEND RESPONSE
    with open(os.path.join(app.config["IMAGE_UPLOADS"], user_image.image_path), 'rb') as binary_file:
        base64_encoded_data = base64.b64encode(binary_file.read())

        return response(True, {'b64': str(base64_encoded_data.decode('utf-8')),
                               'format': user_image.image_path.split('.')[-1]}, 200)
