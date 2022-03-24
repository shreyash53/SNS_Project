
from flask import render_template, request, session, Blueprint
from utilities.constants import *
from .controller import authenticate, add_user, update_user

blueprint = Blueprint("User", __name__, url_prefix="/user")


@blueprint.route('/signup', methods = POST)
def signup():
    form = request.form
    
    return add_user(form)
    
    
@blueprint.route('/login', methods = POST)
def login():
    form = request.form
    return authenticate(form)
    

@blueprint.route('/update', methods=POST)
def update_user_profile():
    if session and 'name' in session and session['name']:
        body = request.form
        return update_user(body)
        
        
    return render_template('login.html')