from src import db


class Firm(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(30), nullable=False)
    activity_address = db.Column(db.String(100), nullable=False)
    client_id = db.Column(db.Integer, nullable=False)

    # CONSTRUCTOR
    def __init__(self, title: str, activity_address: str, client_id: int):
        self.title = title
        self.activity_address = activity_address
        self.client_id = client_id

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
