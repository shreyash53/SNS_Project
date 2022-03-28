
from flask import session
from config import mail
from flask_mail import Message
from utilities.constants import SENDER_EMAIL

def check_session_exists():
    return session and 'name' in session and session['name']

def email_service(user_email, email_title, user_id):
    try:
        # msg = Message(email_title, sender = SENDER_EMAIL, recipients = [user_email])
        # msg.body = "Hello, Reset your account using this url: " + 'http://localhost:5000' + '/user/pass_reset' + '/%d'%(user_id)
        # mail.send(msg)
        print("Sending mail...")
        msg = mail.send_message(
            'Password Recovery',
            sender='sartthakrawatt@gmail.com',
            recipients=[user_email],
            body="Click on the link to change the password..."
        )
    except Exception as e:
        print('mail failed to send', e)