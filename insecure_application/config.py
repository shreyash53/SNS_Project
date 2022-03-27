
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_mail import Mail

db = SQLAlchemy()
session_obj = Session()
mail = Mail()