from .auth_model import Auth


# UPDATE PAIR TOKENS
def update_pair_tokens(user_id):
    # GET AUTHORIZATION BY USER ID OR CREATE A NEW TOKEN PAIR
    auth = Auth.query.filter_by(user_id=user_id).first() or Auth(user_id=user_id)
    auth.generate_access_token()
    auth.generate_refresh_token()
    auth.update_db() or auth.save_db()
    return auth


# GET AUTH BY USER ID
def get_by_user_id(user_id):
    # GET AUTH BY USER ID
    auth = Auth.query.filter_by(user_id=user_id).first()
    return auth
