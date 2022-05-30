from src.User.user_model import User
from src._general.parents import get_page_items


def delete_bind(client_id, user_id):
    # GET USER AND DELETE BIND CLIENT
    user = User.query.filter_by(id=user_id, client_id=client_id).first()
    user.client_id = None
    user.update_db()


# def get_users_by_client(client_id: int, page: int, per_page: int):
#     # GET ALL USERS WHICH CREATE USER IN A CYCLE TO ID AND RETURN
#     arr_user_list = []
#     for user in User.query.filter_by(client_id=client_id).paginate(page=page, per_page=per_page):
#         arr_user_list.append({
#             'id': user.id,
#             'name': user.name,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'ticket': user.ticket,
#             'cash_box_id': user.cash_box_id,
#             'cashier': user.cashier,
#             'creation_date': user.creation_date
#         })
#     return arr_user_list


def get_by_user_id_client_id(user_id, client_id):
    # GET AND RETURN USER BY USER ID AND CLIENT ID
    user = User.query.filter_by(id=user_id, client_id=client_id).first()
    return user


def create_bind(client_id, user_id):
    # CREATE BIND BY CLIENT ID AND USER ID WHERE
    user = User.query.filter_by(id=user_id).first()
    user.client_id = client_id
    user.update_db()
