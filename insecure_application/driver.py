from crypt import methods
from flask import Flask, request, jsonify, make_response, render_template, redirect, session, send_file
import logging
from utilities.common_functions import check_session_exists
from users.controller import get_dashboard
from utilities.constants import GET, POST
# import jwt
from users.routes import blueprint as user_blueprint
from utilities.constants import GET
from config import db, session_obj, GMAIL_PASSWORD, GMAIL_ID
import logging
import os
from blog.routes import blueprint as blog_blueprint
from admin.routes import blueprint as admin_blueprint
from users import model as user_model

from flask_mail import Mail,  Message

app = Flask(__name__)

app.config['SECRET_KEY'] = '10101010101010'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_SQLALCHEMY"] = db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

session_obj.init_app(app)

with app.app_context():
    db.create_all()

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = GMAIL_ID,
    MAIL_PASSWORD = GMAIL_PASSWORD
)

mail = Mail(app)

@app.route('/send-mail/', methods=GET)
def send_mail():
    msg = mail.send_message(
        'Password Recovery',
        sender='sartthakrawatt@gmail.com',
        recipients=['srtkrwt@gmail.com'],
        body="Click on the link to change the password..."
    )
    return 'Mail sent'

@app.route('/', methods=GET)
def provide_index():
    return render_template('index.html')

@app.route('/login', methods=GET)
def provide_login():
    if check_session_exists():
        user_ = session['name']
        return get_dashboard(user_)
        
    return render_template('login.html')

@app.route('/user-profile', methods=GET)
def provide_profile():
    if session and 'name' in session and session['name']:
        # user_ = session['name']
        user_ = db.session.query(user_model.Users).get(session['name'].user_id)
        # print(user_.user)
        user_type = user_.user_type
        if user_type == 1:
            return redirect('/admin/')
        elif user_type == 2:
            return render_template('user-profile.html', user=user_) 
        
    return render_template('login.html')

@app.route('/profile_picture', methods=POST)
def provide_profile_picture():
    if True:# or session and 'name' in session and session['name']:
        # user_ = session['name']
        body = request.get_json()
        path = os.path.join('static/images', body["picture_name"])
        return send_file(path)
        
    return render_template('login.html')

@app.route('/logout', methods=GET)
def logout():
    session['name'] = None
    return render_template('login.html', msg='Successfully Logged out...')


app.register_blueprint(user_blueprint)
app.register_blueprint(blog_blueprint)
app.register_blueprint(admin_blueprint)
