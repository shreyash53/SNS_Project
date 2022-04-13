
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_mail import Mail

db = SQLAlchemy()
session_obj = Session()

GMAIL_ID="example@gmail.com"
GMAIL_PASSWORD="example"
mail = Mail()
