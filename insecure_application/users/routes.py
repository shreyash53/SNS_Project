
from flask import redirect, render_template, request, session, Blueprint
from utilities.common_functions import check_session_exists
from utilities.constants import *
from .controller import authenticate, add_user, update_user, forgot_password, reset_password
from blog.controller import get_all_blogs
import os

blueprint = Blueprint("User", __name__, url_prefix="/user")

@blueprint.route('/', methods=GET)
def get_user_dashboard():
    if check_session_exists():
        blogs = get_all_blogs()
        user_ = session['name']
        return render_template('user-dashboard.html', blogs=blogs, user_ = user_.get())
    return redirect('login.html')

@blueprint.route('/signup', methods = POST)
def signup():
    form = request.form
    
    return add_user(form)
    
    
@blueprint.route('/login', methods = POST)
def login():
    form = request.form
    return authenticate(form)
    
    
@blueprint.route('/forgot-password', methods=POST)
def forgot_pass():
    form = request.form
    return forgot_password(form)

@blueprint.route('/reset-password/<user_id>', methods=POST)
def reset_pass(user_id):
    form = request.form
    return reset_password(form, user_id)

@blueprint.route('/update', methods=POST)
def update_user_profile():
    if check_session_exists():
        body = request.form
        print("LOG:", body['email'])
        return update_user(body)
        
        
    return render_template('login.html')

@blueprint.route('/update-image', methods=POST)
def update_user_image():
    if check_session_exists():
        user = session["name"].user
        file = request.files[user]
        # print()
        with open(os.path.join("static/images", user), "wb+") as f:
            file.save(f)
        return render_template('user-profile.html', user=session['name'])
        # return "1234"
        
        
    return render_template('login.html')

@blueprint.route('/update-password', methods=POST)
def update_user_password():
    if session and 'name' in session and session['name']:
        user_ = session["name"]
        body = request.form
        if user_.pword == body['old-password']:
            #change password
            print("changing password")
            return update_user({"user_id": user_.user_id, "pword": body["new-password"]})
            # return "password changed"
        else:
            return render_template('user-profile.html', )
        
        
        
    return render_template('login.html')