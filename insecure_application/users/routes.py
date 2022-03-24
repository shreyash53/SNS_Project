
from flask import redirect, render_template, request, session, Blueprint
from utilities.common_functions import check_session_exists
from utilities.constants import *
from .controller import authenticate, add_user
from blog.controller import get_all_blogs

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
    