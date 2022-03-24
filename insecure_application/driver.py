from flask import Flask, request, jsonify, make_response, render_template, redirect, session
import logging
from utilities.constants import GET
# import jwt
from users.routes import blueprint as user_blueprint
from config import db, session_obj
app = Flask(__name__)

app.config['SECRET_KEY'] = '10101010101010'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "sqlalchemy"
app.config["SESSION_SQLALCHEMY"] = db

db.init_app(app)

session_obj.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=GET)
def provide_index():
    return render_template('index.html')

@app.route('/login', methods=GET)
def provide_login():
    if session and session['name']:
        user_ = session['name']
        if user_.user_type == 1:
            return render_template('admin-dashboard.html') 
        elif user_.user_type == 2:
            return render_template('user-dashboard.html') 
        
    return render_template('login.html')

app.register_blueprint(user_blueprint)
