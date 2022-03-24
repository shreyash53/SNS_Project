from flask import Flask, request, jsonify, make_response, render_template, redirect, session
import logging
# import jwt
from onboarding import create_tables
from flask_session import Session
from users.routes import blueprint as user_blueprint

app = Flask(__name__)

app.config['SECRET_KEY'] = '10101010101010'
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.register_blueprint(user_blueprint)

create_tables()