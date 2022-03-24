
from flask import render_template, request, session, Blueprint
from utilities.constants import *
from .controller import authenticate

blueprint = Blueprint("User", __name__, url_prefix="/user")


@blueprint.route('/signup', methods = POST)
def signup():
    try:
        body = request.form
        username = body['user']
        password = body['pword']
        user_type = body['user_type']
        print(username, password, user_type)
        # record= database(user_name=username, password=password, user_type=user_type)
        
        return {"message":"Added new user"}
    except:
        return {"message":"There was an issue adding the user"}
    
    
@blueprint.route('/login', methods = POST)
def login():
    form = request.form
    user = form['user']
    passw = form['pword']
    status = authenticate(user, passw)
    if status == 1:
        return render_template('admin-dashboard.html')
    elif status == 2:
        return render_template('user-dashboard.html')
    return render_template('login.html')