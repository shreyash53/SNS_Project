from flask import Flask, request, jsonify, make_response, render_template, redirect, session
import logging
from utilities.common_functions import check_session_exists
from users.controller import get_dashboard
from utilities.constants import GET
# import jwt
from users.routes import blueprint as user_blueprint
from config import db, session_obj
from blog.routes import blueprint as blog_blueprint
from admin.routes import blueprint as admin_blueprint

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

@app.route('/', methods=GET)
def provide_index():
    return render_template('index.html')

@app.route('/login', methods=GET)
def provide_login():
    if check_session_exists():
        user_ = session['name']
        return get_dashboard(user_)
        
    return render_template('login.html')

@app.route('/logout', methods=GET)
def logout():
    session['name'] = None
    return render_template('login.html', msg='Successfully Logged out...')


app.register_blueprint(user_blueprint)
app.register_blueprint(blog_blueprint)
app.register_blueprint(admin_blueprint)
