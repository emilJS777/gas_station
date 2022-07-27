from src.config import mail
from flask_mail import Message
from src import app
from flask import g


class DeviceErrorSender:

    @staticmethod
    def send(email_address: str or None, error_code: int):
        if email_address:
            msg = Message('Hello', sender=app.config['MAIL_USERNAME'], recipients=[email_address])
            msg.body = f"device error by code {error_code}"
            mail.send(msg)
            print(email_address)


