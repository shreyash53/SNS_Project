from flask import Flask, request, jsonify, make_response, render_template, redirect, send_file, session
from users.routes import blueprint as user_blueprint
from utilities.constants import GET
from config import db, session_obj
import logging
import os
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
    if session and 'name' in session and session['name']:
        user_ = session['name']
        if user_.user_type == 1:
            return render_template('admin-dashboard.html') 
        elif user_.user_type == 2:
            return render_template('user-dashboard.html') 
        
    return render_template('login.html')

@app.route('/user-profile', methods=GET)
def provide_profile():
    if session and 'name' in session and session['name']:
        user_ = session['name']
        return render_template('user-profile.html', user=user_) 
        
    return render_template('login.html')

@app.route('/profile_picture', methods=GET)
def provide_profile():
    if session and 'name' in session and session['name']:
        user_ = session['name']
        body = request.get_json()
        path = os.path.join('static/images', body["picture_name"])
        return send_file(path)
        
    return render_template('login.html')



app.register_blueprint(user_blueprint)
