
from flask import Blueprint, redirect, render_template, session
from utilities.common_functions import check_session_exists
from utilities.constants import *

ADMIN_USER_TYPE = 1

blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@blueprint.route('/', methods=GET)
def get_admin_dashboard():
    if check_session_exists() and session["name"].user_type == ADMIN_USER_TYPE:
        return render_template('admin-dashboard.html', user_ = session['name'].get())
    return redirect('/login')