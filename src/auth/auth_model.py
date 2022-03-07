from datetime import timedelta
from src import db, app
from flask_jwt_extended import create_access_token, create_refresh_token


class Auth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    access_token = db.Column(db.String(400), unique=True, nullable=False)
    refresh_token = db.Column(db.String(400), unique=True, nullable=False)

    # CONSTRUCTOR
    def __init__(self, user_id):
        self.user_id = user_id

    # SAVE DB SELF
    def save_db(self):
        db.session.add(self)
        db.session.commit()

    # DELETE DB
    def delete_db(self):
        db.session.delete(self)
        db.session.commit()

    # UPDATE DATABASE
    @staticmethod
    def update_db():
        db.session.commit()

    # GENERATE ACCESS TOKENS METHOD
    def generate_access_token(self):
        # GET EXPIRES FOR ACCESS
        # CREATE ACCESS TOKEN
        access_time = timedelta(minutes=app.config["JWT_ACCESS_EXP"])
        self.access_token = create_access_token(identity=self.user_id,
                                                expires_delta=access_time)

    # GENERATE REFRESH TOKEN
    def generate_refresh_token(self):
        # GET EXPIRES FOR REFRESH
        # CREATE REFRESH TOKEN
        refresh_time = timedelta(minutes=app.config["JWT_REFRESH_EXP"])
        self.refresh_token = create_refresh_token(identity=self.user_id, expires_delta=refresh_time)
