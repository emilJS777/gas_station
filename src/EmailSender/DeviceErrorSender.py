from src.config import mail
from flask_mail import Message
from src import app
from flask import g
import threading
import smtplib, ssl


class DeviceErrorSender:

    @staticmethod
    def send(email_address: str or None, device_key: str, error_code: int):
        if email_address:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(app.config['MAIL_SERVER'], app.config['MAIL_PORT'], context=context) as server:
                server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
                server.sendmail(app.config['MAIL_USERNAME'], [email_address], f"<h1>Device by key {device_key} error {error_code}</h1>")


