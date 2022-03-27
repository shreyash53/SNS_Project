
from flask import session
from config import mail
from flask_mail import Message
from utilities.constants import SENDER_EMAIL

def check_session_exists():
    return session and 'name' in session and session['name']

def email_service(user_email, email_title, user_id):
    try:
        msg = Message(email_title, sender = SENDER_EMAIL, recipients = [user_email])
        msg.body = "Hello, Reset your account using this url: " + 'http://localhost:5000' + '/user/pass_reset' + '/%d'%(user_id)
        mail.send(msg)
    except:
        print('mail failed to send')