from flask_mail import Message
from src import app, mail


# EMAIL SENDER
def send_ticket_code_to_email(email_address: str, ticket_code: str, message: str):
    msg = Message('Hello', sender=app.config['MAIL_USERNAME'], recipients=[email_address])
    msg.html = f"<h3><span style='font-size=12px;'>{message}</span> " \
               f"<span style='color=blue;'>{str(ticket_code)}</span></h3>"
    mail.send(msg)
