from .UserImageModel import UserImage


def create_user_image(user_id: int, image_path: str) -> UserImage:
    user_image: UserImage = UserImage()
    user_image.user_id = user_id
    user_image.image_path = image_path
    user_image.save_db()
    return user_image


def get_by_user_id(user_id: int) -> UserImage:
    user_image: UserImage = UserImage.query.filter_by(user_id=user_id).first()
    return user_image


# def update_user_image(user_id: int, image_path: str) -> UserImage:
#     user_image: UserImage = UserImage.query.filter_by(user_id=user_id).first()
#     user_image.image_path = image_path
#     user_image.update_db()
#     return user_image


def delete_user_image(user_id: int) -> UserImage:
    user_image: UserImage = UserImage.query.filter_by(user_id=user_id).first()
    user_image.delete_db()
    return user_image

